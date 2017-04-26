# Copyright 2017 Google Inc. All Rights Reserved.
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
"""Common utilities for the Cloud Datapol API."""

from googlecloudsdk.api_lib.cloudresourcemanager import projects_api
from googlecloudsdk.api_lib.util import apis
from googlecloudsdk.api_lib.util import exceptions
from googlecloudsdk.command_lib.projects import util as projects_util
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources

_DATAPOL_API_NAME = 'datapol'
_DATAPOL_API_VERSION = 'v1alpha1'

# Organization Id place holder for projects that do not belong to any
# organizations.
_ORG_ID_PLACE_HOLDER = '_NO_ORGS_'


def GetMessagesModule():
  return apis.GetMessagesModule(_DATAPOL_API_NAME, _DATAPOL_API_VERSION)


def GetClientInstance():
  return apis.GetClientInstance(_DATAPOL_API_NAME, _DATAPOL_API_VERSION)


def GetProjectName():
  """Gets name of the current project."""
  return properties.VALUES.core.project.Get(required=True)


def GetOrganizationId():
  """Gets id of current organization."""
  proj = projects_api.Get(projects_util.ParseProject(GetProjectName()))
  return (proj.parent.id if proj.parent and proj.parent.type == 'organization'
          else _ORG_ID_PLACE_HOLDER)


def GetTaxonomyResource(taxonomy_name):
  """Gets the taxonomy resource from a taxonomy name."""
  return resources.REGISTRY.Create(
      'datapol.orgs.policyTaxonomies',
      orgsId=GetOrganizationId(),
      policyTaxonomiesId=taxonomy_name).RelativeName()


def ErrorWrapper(err, resource_name):
  """Wraps http errors to handle resources names with more than 4 '/'s.

  Args:
    err: An apitools.base.py.exceptions.HttpError.
    resource_name: The requested resource name.

  Returns:
    A googlecloudsdk.api_lib.util.exceptions.HttpException.
  """
  exc = exceptions.HttpException(err)
  if exc.payload.status_code == 404:
    # status_code specific error message
    exc.error_format = ('{{api_name}}: {resource_name} not found.').format(
        resource_name=resource_name)
  else:
    # override default error message
    exc.error_format = ('Unknown error. Status code {status_code}.')
  return exc
