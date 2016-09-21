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
"""Resource definitions for cloud platform apis."""

import enum


BASE_URL = 'https://bigtableadmin.googleapis.com/v2/'


class Collections(enum.Enum):
  """Collections for all supported apis."""

  OPERATIONS = (
      'operations',
      'operations/{operationsId}',
      [
          'operations/{operationsId}',
      ],
      [u'operationsId'])
  PROJECTS_INSTANCES = (
      'projects.instances',
      'projects/{projectsId}/instances/{instancesId}',
      [
          'projects/{projectsId}/instances/{instancesId}',
      ],
      [u'projectsId', u'instancesId'])
  PROJECTS_INSTANCES_CLUSTERS = (
      'projects.instances.clusters',
      'projects/{projectsId}/instances/{instancesId}/clusters/{clustersId}',
      [
          'projects/{projectsId}/instances/{instancesId}/clusters/'
          '{clustersId}',
      ],
      [u'projectsId', u'instancesId', u'clustersId'])
  PROJECTS_INSTANCES_CLUSTERS_SNAPSHOTS = (
      'projects.instances.clusters.snapshots',
      'projects/{projectsId}/instances/{instancesId}/clusters/{clustersId}/'
      'snapshots/{snapshotsId}',
      [
          'projects/{projectsId}/instances/{instancesId}/clusters/'
          '{clustersId}/snapshots/{snapshotsId}',
      ],
      [u'projectsId', u'instancesId', u'clustersId', u'snapshotsId'])
  PROJECTS_INSTANCES_TABLES = (
      'projects.instances.tables',
      'projects/{projectsId}/instances/{instancesId}/tables/{tablesId}',
      [
          'projects/{projectsId}/instances/{instancesId}/tables/{tablesId}',
      ],
      [u'projectsId', u'instancesId', u'tablesId'])

  def __init__(self, collection_name, path, flat_paths, params):
    self.collection_name = collection_name
    self.path = path
    self.flat_paths = flat_paths
    self.params = params
