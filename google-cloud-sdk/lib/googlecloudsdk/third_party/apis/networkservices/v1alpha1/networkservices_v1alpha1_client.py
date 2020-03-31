"""Generated client library for networkservices version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.networkservices.v1alpha1 import networkservices_v1alpha1_messages as messages


class NetworkservicesV1alpha1(base_api.BaseApiClient):
  """Generated client library for service networkservices version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://networkservices.googleapis.com/'
  MTLS_BASE_URL = u'https://networkservices.mtls.googleapis.com/'

  _PACKAGE = u'networkservices'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = u'google-cloud-sdk'
  _CLIENT_CLASS_NAME = u'NetworkservicesV1alpha1'
  _URL_VERSION = u'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new networkservices handle."""
    url = url or self.BASE_URL
    super(NetworkservicesV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_endpointConfigSelectors = self.ProjectsLocationsEndpointConfigSelectorsService(self)
    self.projects_locations_httpFilters = self.ProjectsLocationsHttpFiltersService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsEndpointConfigSelectorsService(base_api.BaseApiService):
    """Service class for the projects_locations_endpointConfigSelectors resource."""

    _NAME = u'projects_locations_endpointConfigSelectors'

    def __init__(self, client):
      super(NetworkservicesV1alpha1.ProjectsLocationsEndpointConfigSelectorsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new EndpointConfigSelector in a given project and location.

      Args:
        request: (NetworkservicesProjectsLocationsEndpointConfigSelectorsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/endpointConfigSelectors',
        http_method=u'POST',
        method_id=u'networkservices.projects.locations.endpointConfigSelectors.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'endpointConfigSelectorId'],
        relative_path=u'v1alpha1/{+parent}/endpointConfigSelectors',
        request_field=u'endpointConfigSelector',
        request_type_name=u'NetworkservicesProjectsLocationsEndpointConfigSelectorsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single EndpointConfigSelector.

      Args:
        request: (NetworkservicesProjectsLocationsEndpointConfigSelectorsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/endpointConfigSelectors/{endpointConfigSelectorsId}',
        http_method=u'DELETE',
        method_id=u'networkservices.projects.locations.endpointConfigSelectors.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsEndpointConfigSelectorsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single EndpointConfigSelector.

      Args:
        request: (NetworkservicesProjectsLocationsEndpointConfigSelectorsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (EndpointConfigSelector) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/endpointConfigSelectors/{endpointConfigSelectorsId}',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.endpointConfigSelectors.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsEndpointConfigSelectorsGetRequest',
        response_type_name=u'EndpointConfigSelector',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (NetworkservicesProjectsLocationsEndpointConfigSelectorsGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/endpointConfigSelectors/{endpointConfigSelectorsId}:getIamPolicy',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.endpointConfigSelectors.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[u'options_requestedPolicyVersion'],
        relative_path=u'v1alpha1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsEndpointConfigSelectorsGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists EndpointConfigSelectors in a given project and location.

      Args:
        request: (NetworkservicesProjectsLocationsEndpointConfigSelectorsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListEndpointConfigSelectorsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/endpointConfigSelectors',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.endpointConfigSelectors.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/endpointConfigSelectors',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsEndpointConfigSelectorsListRequest',
        response_type_name=u'ListEndpointConfigSelectorsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single EndpointConfigSelector.

      Args:
        request: (NetworkservicesProjectsLocationsEndpointConfigSelectorsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/endpointConfigSelectors/{endpointConfigSelectorsId}',
        http_method=u'PATCH',
        method_id=u'networkservices.projects.locations.endpointConfigSelectors.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'endpointConfigSelector',
        request_type_name=u'NetworkservicesProjectsLocationsEndpointConfigSelectorsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

      Args:
        request: (NetworkservicesProjectsLocationsEndpointConfigSelectorsSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/endpointConfigSelectors/{endpointConfigSelectorsId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'networkservices.projects.locations.endpointConfigSelectors.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'NetworkservicesProjectsLocationsEndpointConfigSelectorsSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (NetworkservicesProjectsLocationsEndpointConfigSelectorsTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/endpointConfigSelectors/{endpointConfigSelectorsId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'networkservices.projects.locations.endpointConfigSelectors.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'NetworkservicesProjectsLocationsEndpointConfigSelectorsTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsHttpFiltersService(base_api.BaseApiService):
    """Service class for the projects_locations_httpFilters resource."""

    _NAME = u'projects_locations_httpFilters'

    def __init__(self, client):
      super(NetworkservicesV1alpha1.ProjectsLocationsHttpFiltersService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new HttpFilter in a given project and location.

      Args:
        request: (NetworkservicesProjectsLocationsHttpFiltersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/httpFilters',
        http_method=u'POST',
        method_id=u'networkservices.projects.locations.httpFilters.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'httpFilterId'],
        relative_path=u'v1alpha1/{+parent}/httpFilters',
        request_field=u'httpFilter',
        request_type_name=u'NetworkservicesProjectsLocationsHttpFiltersCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single HttpFilter.

      Args:
        request: (NetworkservicesProjectsLocationsHttpFiltersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/httpFilters/{httpFiltersId}',
        http_method=u'DELETE',
        method_id=u'networkservices.projects.locations.httpFilters.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsHttpFiltersDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single HttpFilter.

      Args:
        request: (NetworkservicesProjectsLocationsHttpFiltersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (HttpFilter) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/httpFilters/{httpFiltersId}',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.httpFilters.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsHttpFiltersGetRequest',
        response_type_name=u'HttpFilter',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource.
Returns an empty policy if the resource exists and does not have a policy
set.

      Args:
        request: (NetworkservicesProjectsLocationsHttpFiltersGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/httpFilters/{httpFiltersId}:getIamPolicy',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.httpFilters.getIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[u'options_requestedPolicyVersion'],
        relative_path=u'v1alpha1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsHttpFiltersGetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists HttpFilters in a given project and location.

      Args:
        request: (NetworkservicesProjectsLocationsHttpFiltersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListHttpFiltersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/httpFilters',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.httpFilters.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+parent}/httpFilters',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsHttpFiltersListRequest',
        response_type_name=u'ListHttpFiltersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the parameters of a single HttpFilter.

      Args:
        request: (NetworkservicesProjectsLocationsHttpFiltersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/httpFilters/{httpFiltersId}',
        http_method=u'PATCH',
        method_id=u'networkservices.projects.locations.httpFilters.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'httpFilter',
        request_type_name=u'NetworkservicesProjectsLocationsHttpFiltersPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any.
existing policy.

Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

      Args:
        request: (NetworkservicesProjectsLocationsHttpFiltersSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/httpFilters/{httpFiltersId}:setIamPolicy',
        http_method=u'POST',
        method_id=u'networkservices.projects.locations.httpFilters.setIamPolicy',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:setIamPolicy',
        request_field=u'setIamPolicyRequest',
        request_type_name=u'NetworkservicesProjectsLocationsHttpFiltersSetIamPolicyRequest',
        response_type_name=u'Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource.
If the resource does not exist, this will return an empty set of
permissions, not a NOT_FOUND error.

Note: This operation is designed to be used for building permission-aware
UIs and command-line tools, not for authorization checking. This operation
may "fail open" without warning.

      Args:
        request: (NetworkservicesProjectsLocationsHttpFiltersTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/httpFilters/{httpFiltersId}:testIamPermissions',
        http_method=u'POST',
        method_id=u'networkservices.projects.locations.httpFilters.testIamPermissions',
        ordered_params=[u'resource'],
        path_params=[u'resource'],
        query_params=[],
        relative_path=u'v1alpha1/{+resource}:testIamPermissions',
        request_field=u'testIamPermissionsRequest',
        request_type_name=u'NetworkservicesProjectsLocationsHttpFiltersTestIamPermissionsRequest',
        response_type_name=u'TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = u'projects_locations_operations'

    def __init__(self, client):
      super(NetworkservicesV1alpha1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (NetworkservicesProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method=u'POST',
        method_id=u'networkservices.projects.locations.operations.cancel',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}:cancel',
        request_field=u'cancelOperationRequest',
        request_type_name=u'NetworkservicesProjectsLocationsOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (NetworkservicesProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'DELETE',
        method_id=u'networkservices.projects.locations.operations.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsOperationsDeleteRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (NetworkservicesProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.operations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (NetworkservicesProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.operations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+name}/operations',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = u'projects_locations'

    def __init__(self, client):
      super(NetworkservicesV1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (NetworkservicesProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations/{locationsId}',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsGetRequest',
        response_type_name=u'Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (NetworkservicesProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/projects/{projectsId}/locations',
        http_method=u'GET',
        method_id=u'networkservices.projects.locations.list',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'filter', u'pageSize', u'pageToken'],
        relative_path=u'v1alpha1/{+name}/locations',
        request_field='',
        request_type_name=u'NetworkservicesProjectsLocationsListRequest',
        response_type_name=u'ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(NetworkservicesV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
