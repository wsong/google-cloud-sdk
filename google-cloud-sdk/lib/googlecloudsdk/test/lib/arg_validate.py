# Copyright 2015 Google Inc. All Rights Reserved.

"""A shared library to validate 'gcloud test' CLI argument values."""

import re
import sys

from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import exceptions


class InvalidArgException(exceptions.InvalidArgumentException):
  """InvalidArgException is for malformed gcloud test argument values.

  It provides a wrapper around Calliope's InvalidArgumentException that
  conveniently converts internal arg names with underscores into the external
  arg names with hyphens.
  """

  def __init__(self, param_name, message):
    super(InvalidArgException, self).__init__(ExternalArgNameFrom(param_name),
                                              message)


def ValidateArgFromFile(arg_internal_name, arg_value):
  """Do checks/mutations on arg values parsed from YAML which need validation.

  Any arg not appearing in the _ARG_VALIDATORS dictionary is assumed to be a
  simple string to be validated by the default _ValidateString() function.

  Mutations of the args are done in limited cases to improve ease-of-use.
  This includes:
  1) The YAML parser automatically converts attribute values into numeric types
  where possible. The os-version-ids for Android devices happen to be integers,
  but the Testing service expects them to be strings, so we automatically
  convert them to strings so users don't have to quote each one.
  2) The include: keyword, plus all test args that normally expect lists (e.g.
  device-ids, os-version-ids, locales, orientations...), will also accept a
  single value which is not specified using YAML list notation (e.g not enclosed
  in []). Such single values are automatically converted into a list containing
  one element.

  Args:
    arg_internal_name: the internal form of the arg name.
    arg_value: the argument's value as parsed from the yaml file.

  Returns:
    The validated argument value.

  Raises:
    InvalidArgException: If the arg value is missing or is not valid.
  """
  if arg_value is None:
    raise InvalidArgException(arg_internal_name, 'no argument value found.')
  if arg_internal_name in _ARG_VALIDATORS:
    return _ARG_VALIDATORS[arg_internal_name](arg_internal_name, arg_value)
  return _ValidateString(arg_internal_name, arg_value)


# Constants shared between arg-file validation and CLI flag validation.
POSITIVE_INT_PARSER = arg_parsers.BoundedInt(1, sys.maxint)
NONNEGATIVE_INT_PARSER = arg_parsers.BoundedInt(0, sys.maxint)
TIMEOUT_PARSER = arg_parsers.Duration(lower_bound='1m', upper_bound='6h')
ORIENTATION_LIST = ['portrait', 'landscape']


def ValidateStringList(arg_internal_name, arg_value):
  """Validates an arg whose value should be a list of strings.

  Args:
    arg_internal_name: the internal form of the arg name.
    arg_value: the argument's value parsed from yaml file.

  Returns:
    The validated argument value.

  Raises:
    InvalidArgException: the argument's value is not valid.
  """
  if isinstance(arg_value, basestring):  # convert single str to a str list
    return [arg_value]
  if isinstance(arg_value, int):  # convert single int to a str list
    return [str(arg_value)]
  if isinstance(arg_value, list):
    return [_ValidateString(arg_internal_name, value) for value in arg_value]
  raise InvalidArgException(arg_internal_name, arg_value)


def _ValidateString(arg_internal_name, arg_value):
  """Validates an arg whose value should be a simple string."""
  if isinstance(arg_value, basestring):
    return arg_value
  if isinstance(arg_value, int):  # convert int->str if str is really expected
    return str(arg_value)
  raise InvalidArgException(arg_internal_name, arg_value)


def _ValidateBool(arg_internal_name, arg_value):
  """Validates an argument which should have a boolean value."""
  # Note: the python yaml parser automatically does string->bool conversion for
  # true/True/TRUE/false/False/FALSE and also for variations of on/off/yes/no.
  if isinstance(arg_value, bool):
    return arg_value
  raise InvalidArgException(arg_internal_name, arg_value)


def _ValidateDuration(arg_internal_name, arg_value):
  """Validates an argument which should have a Duration value."""
  try:
    if isinstance(arg_value, basestring):
      return TIMEOUT_PARSER(arg_value)
    elif isinstance(arg_value, int):
      return TIMEOUT_PARSER(str(arg_value))
  except arg_parsers.ArgumentTypeError as e:
    raise InvalidArgException(arg_internal_name, e.message)
  raise InvalidArgException(arg_internal_name, arg_value)


def _ValidateInteger(arg_internal_name, arg_value):
  """Validates an argument which should have any integer value."""
  if isinstance(arg_value, int):
    return arg_value
  raise InvalidArgException(arg_internal_name, arg_value)


def _ValidatePositiveInteger(arg_internal_name, arg_value):
  """Validates an argument which should be an integer > 0."""
  try:
    if isinstance(arg_value, int):
      return POSITIVE_INT_PARSER(str(arg_value))
  except arg_parsers.ArgumentTypeError as e:
    raise InvalidArgException(arg_internal_name, e.message)
  raise InvalidArgException(arg_internal_name, arg_value)


def _ValidateNonNegativeInteger(arg_internal_name, arg_value):
  """Validates an argument which should be an integer >= 0."""
  try:
    if isinstance(arg_value, int):
      return NONNEGATIVE_INT_PARSER(str(arg_value))
  except arg_parsers.ArgumentTypeError as e:
    raise InvalidArgException(arg_internal_name, e.message)
  raise InvalidArgException(arg_internal_name, arg_value)


def _ValidateOrientationList(arg_internal_name, arg_value):
  """Validates that 'orientations' only contains 'portrait' and 'landscape'."""
  arg_value = ValidateStringList(arg_internal_name, arg_value)
  for orientation in arg_value:
    if orientation not in ORIENTATION_LIST:
      raise InvalidArgException(arg_internal_name, orientation)
  if len(arg_value) != len(set(arg_value)):
    raise InvalidArgException(arg_internal_name,
                              'orientations may not be repeated.')
  return arg_value


def _ValidateObbFileList(arg_internal_name, arg_value):
  """Validates that 'obb-files' contains at most 2 entries."""
  arg_value = ValidateStringList(arg_internal_name, arg_value)
  if len(arg_value) > 2:
    raise InvalidArgException(arg_internal_name,
                              'At most two OBB files may be specified.')
  return arg_value


# Map of internal arg names to their appropriate validation functions.
# Any arg not appearing in this map is assumed to be a simple string.
_ARG_VALIDATORS = {
    'async': _ValidateBool,
    'auto_google_login': _ValidateBool,
    'timeout': _ValidateDuration,
    'device_ids': ValidateStringList,
    'os_version_ids': ValidateStringList,
    'locales': ValidateStringList,
    'orientations': _ValidateOrientationList,
    'obb_files': _ValidateObbFileList,
    'event_count': _ValidatePositiveInteger,
    'event_delay': _ValidateNonNegativeInteger,
    'random_seed': _ValidateInteger,
    'max_steps': _ValidateNonNegativeInteger,
    'max_depth': _ValidatePositiveInteger,
}


def InternalArgNameFrom(arg_external_name):
  """Converts a user-visible arg name into its corresponding internal name."""
  return arg_external_name.replace('-', '_')


def ExternalArgNameFrom(arg_internal_name):
  """Converts an internal arg name into its corresponding user-visible name."""
  return arg_internal_name.replace('_', '-')


# Validation methods below this point are meant to be used on args regardless
# of whether they came from the command-line or an arg-file, while the methods
# above here are only for arg-file args, which bypass the standard validations
# performed by the argparse package (which only works with CLI args).

def ValidateArgsForTestType(
    args, test_type, type_rules, shared_rules, all_test_args_set):
  """Raise errors if required args are missing or invalid args are present.

  Args:
    args: an argparse.Namespace object which contains attributes for all the
      arguments that were provided to the command invocation (i.e. command
      group and command arguments combined).
    test_type: string containing the type of test to run.
    type_rules: a nested dictionary defining the required and optional args
      per type of test, plus any default values.
    shared_rules: a nested dictionary defining the required and optional args
      shared among all test types, plus any default values.
    all_test_args_set: a set of strings for every gcloud-test argument to use
      for validation.

  Raises:
    InvalidArgException: If an arg doesn't pair with the test type.
    RequiredArgumentException: If a required arg for the test type is missing.
  """
  required_args = type_rules[test_type]['required'] + shared_rules['required']
  optional_args = type_rules[test_type]['optional'] + shared_rules['optional']
  allowable_args_for_type = required_args + optional_args

  # Raise an error if an optional test arg is not allowed with this test_type.
  for arg in all_test_args_set:
    if getattr(args, arg, None) is not None:  # Ignore args equal to None
      if arg not in allowable_args_for_type:
        raise InvalidArgException(
            arg, "may not be used with test type '{0}'.".format(test_type))
  # Raise an error if a required test arg is missing or equal to None.
  for arg in required_args:
    if getattr(args, arg, None) is None:
      raise exceptions.RequiredArgumentException(
          '{0}'.format(ExternalArgNameFrom(arg)),
          "must be specified with test type '{0}'.".format(test_type))


def ValidateResultsBucket(args):
  """Do some basic sanity checks on the format of the results-bucket arg."""
  if args.results_bucket is None:
    return
  # TODO(user): use the resources module here once it understands gs:// links
  if args.results_bucket.startswith('gs://'):
    args.results_bucket = args.results_bucket[5:]
  args.results_bucket = args.results_bucket.rstrip('/')
  if '/' in args.results_bucket:
    raise exceptions.InvalidArgumentException(
        'results-bucket', 'Results bucket name is not valid')


_OBB_FILE_REGEX = re.compile(
    r'(.*[\\/:])?(main|patch)\.\d+(\.[a-zA-Z]\w*)+\.obb$')


def ValidateObbFileNames(obb_files):
  """Confirm that any OBB file names follow the required Android pattern."""
  for obb_file in (obb_files or []):
    if not _OBB_FILE_REGEX.match(obb_file):
      raise InvalidArgException(
          'obb_files',
          '[{0}] is not a valid OBB file name, which must have the format: '
          '(main|patch).<versionCode>.<package.name>.obb'.format(obb_file))
