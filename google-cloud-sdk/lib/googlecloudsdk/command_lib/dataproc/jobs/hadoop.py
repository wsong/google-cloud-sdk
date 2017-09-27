# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base class for Hadoop Job."""

import argparse

from apitools.base.py import encoding

from googlecloudsdk.api_lib.dataproc import exceptions
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.command_lib.dataproc.jobs import base as job_base
from googlecloudsdk.core import log


class HadoopBase(job_base.JobBase):
  """Common functionality between release tracks."""

  @staticmethod
  def Args(parser):
    """Parses command-line arguments specific to submitting Hadoop jobs."""
    parser.add_argument(
        '--jars',
        type=arg_parsers.ArgList(),
        metavar='JAR',
        default=[],
        help=('Comma separated list of jar files to be provided to the MR and '
              'driver classpaths.'))
    parser.add_argument(
        '--files',
        type=arg_parsers.ArgList(),
        metavar='FILE',
        default=[],
        help='Comma separated list of files to be provided to the job.')
    parser.add_argument(
        '--archives',
        type=arg_parsers.ArgList(),
        metavar='ARCHIVE',
        default=[],
        help=('Comma separated list of archives to be provided to the job. '
              'must be one of the following file formats: .zip, .tar, .tar.gz, '
              'or .tgz.'))
    parser.add_argument(
        'job_args',
        nargs=argparse.REMAINDER,
        help='The arguments to pass to the driver.')
    parser.add_argument(
        '--properties',
        type=arg_parsers.ArgDict(),
        metavar='PROPERTY=VALUE',
        help='A list of key value pairs to configure Hadoop.')
    parser.add_argument(
        '--driver-log-levels',
        type=arg_parsers.ArgDict(),
        metavar='PACKAGE=LEVEL',
        help=('A list of package to log4j log level pairs to configure driver '
              'logging. For example: root=FATAL,com.example=INFO'))

  @staticmethod
  def GetFilesByType(args):
    """Returns a dict of files by their type (jars, archives, etc.)."""
    # TODO(b/36050338): Move arg manipulation elsewhere.
    # TODO(b/36051982): Remove with GA flags 2017-04-01 (b/33298024).
    if not args.main_class and not args.main_jar:
      raise exceptions.ArgumentError('Must either specify --class or JAR.')
    if args.main_class and args.main_jar:
      log.warn(
          'You must specify exactly one of --jar and --class. '
          'This will be strictly enforced in April 2017. '
          "Use 'gcloud beta dataproc jobs submit hadoop' to see new behavior.")
      log.info('Passing main jar as an additional jar.')
      args.jars.append(args.main_jar)
      args.main_jar = None

    return {
        'main_jar': args.main_jar,
        'jars': args.jars,
        'archives': args.archives,
        'files': args.files}

  @staticmethod
  def ConfigureJob(messages, job, files_by_type, logging_config, args):
    """Populates the hadoopJob member of the given job."""
    hadoop_job = messages.HadoopJob(
        args=args.job_args or [],
        archiveUris=files_by_type['archives'],
        fileUris=files_by_type['files'],
        jarFileUris=files_by_type['jars'],
        mainClass=args.main_class,
        mainJarFileUri=files_by_type['main_jar'],
        loggingConfig=logging_config)

    if args.properties:
      hadoop_job.properties = encoding.DictToMessage(
          args.properties, messages.HadoopJob.PropertiesValue)

    job.hadoopJob = hadoop_job
