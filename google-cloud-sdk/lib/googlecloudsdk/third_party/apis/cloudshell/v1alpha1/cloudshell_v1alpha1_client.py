"""Generated client library for cloudshell version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudshell.v1alpha1 import cloudshell_v1alpha1_messages as messages


class CloudshellV1alpha1(base_api.BaseApiClient):
  """Generated client library for service cloudshell version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://cloudshell.googleapis.com/'
  MTLS_BASE_URL = 'https://cloudshell.mtls.googleapis.com/'

  _PACKAGE = 'cloudshell'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CloudshellV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudshell handle."""
    url = url or self.BASE_URL
    super(CloudshellV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.users_environments_publicKeys = self.UsersEnvironmentsPublicKeysService(self)
    self.users_environments = self.UsersEnvironmentsService(self)
    self.users = self.UsersService(self)

  class UsersEnvironmentsPublicKeysService(base_api.BaseApiService):
    """Service class for the users_environments_publicKeys resource."""

    _NAME = 'users_environments_publicKeys'

    def __init__(self, client):
      super(CloudshellV1alpha1.UsersEnvironmentsPublicKeysService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Adds a public SSH key to an environment, allowing clients with the.
corresponding private key to connect to that environment via SSH. If a key
with the same format and content already exists, this will return the
existing key.

      Args:
        request: (CloudshellUsersEnvironmentsPublicKeysCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PublicKey) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/users/{usersId}/environments/{environmentsId}/publicKeys',
        http_method='POST',
        method_id='cloudshell.users.environments.publicKeys.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1alpha1/{+parent}/publicKeys',
        request_field='createPublicKeyRequest',
        request_type_name='CloudshellUsersEnvironmentsPublicKeysCreateRequest',
        response_type_name='PublicKey',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Removes a public SSH key from an environment. Clients will no longer be.
able to connect to the environment using the corresponding private key.

      Args:
        request: (CloudshellUsersEnvironmentsPublicKeysDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/users/{usersId}/environments/{environmentsId}/publicKeys/{publicKeysId}',
        http_method='DELETE',
        method_id='cloudshell.users.environments.publicKeys.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CloudshellUsersEnvironmentsPublicKeysDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

  class UsersEnvironmentsService(base_api.BaseApiService):
    """Service class for the users_environments resource."""

    _NAME = 'users_environments'

    def __init__(self, client):
      super(CloudshellV1alpha1.UsersEnvironmentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Authorize(self, request, global_params=None):
      r"""Sends OAuth credentials to a running environment on behalf of a user. When.
this completes, the environment will be authorized to run various Google
Cloud command line tools without requiring the user to manually
authenticate.

      Args:
        request: (CloudshellUsersEnvironmentsAuthorizeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Authorize')
      return self._RunMethod(
          config, request, global_params=global_params)

    Authorize.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/users/{usersId}/environments/{environmentsId}:authorize',
        http_method='POST',
        method_id='cloudshell.users.environments.authorize',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}:authorize',
        request_field='authorizeEnvironmentRequest',
        request_type_name='CloudshellUsersEnvironmentsAuthorizeRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets an environment. Returns NOT_FOUND if the environment does not exist.

      Args:
        request: (CloudshellUsersEnvironmentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Environment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/users/{usersId}/environments/{environmentsId}',
        http_method='GET',
        method_id='cloudshell.users.environments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CloudshellUsersEnvironmentsGetRequest',
        response_type_name='Environment',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates an existing environment.

      Args:
        request: (CloudshellUsersEnvironmentsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Environment) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/users/{usersId}/environments/{environmentsId}',
        http_method='PATCH',
        method_id='cloudshell.users.environments.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='environment',
        request_type_name='CloudshellUsersEnvironmentsPatchRequest',
        response_type_name='Environment',
        supports_download=False,
    )

    def Start(self, request, global_params=None):
      r"""Starts an existing environment, allowing clients to connect to it. The.
returned operation will contain an instance of StartEnvironmentMetadata in
its metadata field. Users can wait for the environment to start by polling
this operation via GetOperation. Once the environment has finished starting
and is ready to accept connections, the operation will contain a
StartEnvironmentResponse in its response field.

      Args:
        request: (CloudshellUsersEnvironmentsStartRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Start')
      return self._RunMethod(
          config, request, global_params=global_params)

    Start.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/users/{usersId}/environments/{environmentsId}:start',
        http_method='POST',
        method_id='cloudshell.users.environments.start',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}:start',
        request_field='startEnvironmentRequest',
        request_type_name='CloudshellUsersEnvironmentsStartRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class UsersService(base_api.BaseApiService):
    """Service class for the users resource."""

    _NAME = 'users'

    def __init__(self, client):
      super(CloudshellV1alpha1.UsersService, self).__init__(client)
      self._upload_configs = {
          }
