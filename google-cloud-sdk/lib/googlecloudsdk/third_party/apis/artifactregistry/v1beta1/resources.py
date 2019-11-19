# -*- coding: utf-8 -*- #
# Copyright 2015 Google LLC. All Rights Reserved.
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
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://artifactregistry.googleapis.com/v1beta1/'
DOCS_URL = 'https://cloud.google.com/artifact-registry'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  PROJECTS = (
      'projects',
      'projects/{projectsId}',
      {},
      [u'projectsId'],
      True
  )
  PROJECTS_LOCATIONS = (
      'projects.locations',
      'projects/{projectsId}/locations/{locationsId}',
      {},
      [u'projectsId', u'locationsId'],
      True
  )
  PROJECTS_LOCATIONS_OPERATIONS = (
      'projects.locations.operations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/operations/'
              '{operationsId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_REPOSITORIES = (
      'projects.locations.repositories',
      'projects/{projectsId}/locations/{locationsId}/repositories/'
      '{repositoriesId}',
      {},
      [u'projectsId', u'locationsId', u'repositoriesId'],
      True
  )
  PROJECTS_LOCATIONS_REPOSITORIES_FILES = (
      'projects.locations.repositories.files',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/repositories/'
              '{repositoriesId}/files/{filesId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_REPOSITORIES_PACKAGES = (
      'projects.locations.repositories.packages',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/repositories/'
              '{repositoriesId}/packages/{packagesId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_REPOSITORIES_PACKAGES_TAGS = (
      'projects.locations.repositories.packages.tags',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/repositories/'
              '{repositoriesId}/packages/{packagesId}/tags/{tagsId}',
      },
      [u'name'],
      True
  )
  PROJECTS_LOCATIONS_REPOSITORIES_PACKAGES_VERSIONS = (
      'projects.locations.repositories.packages.versions',
      '{+name}',
      {
          '':
              'projects/{projectsId}/locations/{locationsId}/repositories/'
              '{repositoriesId}/packages/{packagesId}/versions/{versionsId}',
      },
      [u'name'],
      True
  )
  PROJECTS_REPOSITORIES = (
      'projects.repositories',
      'projects/{projectsId}/repositories/{repositoriesId}',
      {},
      [u'projectsId', u'repositoriesId'],
      True
  )
  PROJECTS_REPOSITORIES_LOCATIONS = (
      'projects.repositories.locations',
      '{+name}',
      {
          '':
              'projects/{projectsId}/repositories/{repositoriesId}/locations/'
              '{locationsId}',
      },
      [u'name'],
      True
  )

  def __init__(self, collection_name, path, flat_paths, params,
               enable_uri_parsing):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
    self.enable_uri_parsing = enable_uri_parsing