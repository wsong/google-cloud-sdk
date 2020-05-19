"""Generated client library for discovery version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.discovery.v1 import discovery_v1_messages as messages


class DiscoveryV1(base_api.BaseApiClient):
  """Generated client library for service discovery version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://www.googleapis.com/discovery/v1/'
  MTLS_BASE_URL = ''

  _PACKAGE = 'discovery'
  _SCOPES = ['https://www.googleapis.com/auth/userinfo.email']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'DiscoveryV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new discovery handle."""
    url = url or self.BASE_URL
    super(DiscoveryV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.apis = self.ApisService(self)

  class ApisService(base_api.BaseApiService):
    """Service class for the apis resource."""

    _NAME = 'apis'

    def __init__(self, client):
      super(DiscoveryV1.ApisService, self).__init__(client)
      self._upload_configs = {
          }

    def GetRest(self, request, global_params=None):
      r"""Retrieve the description of a particular version of an api.

      Args:
        request: (DiscoveryApisGetRestRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (RestDescription) The response message.
      """
      config = self.GetMethodConfig('GetRest')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetRest.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='discovery.apis.getRest',
        ordered_params=['api', 'version'],
        path_params=['api', 'version'],
        query_params=[],
        relative_path='apis/{api}/{version}/rest',
        request_field='',
        request_type_name='DiscoveryApisGetRestRequest',
        response_type_name='RestDescription',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Retrieve the list of APIs supported at this endpoint.

      Args:
        request: (DiscoveryApisListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (DirectoryList) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='discovery.apis.list',
        ordered_params=[],
        path_params=[],
        query_params=['label', 'name', 'preferred'],
        relative_path='apis',
        request_field='',
        request_type_name='DiscoveryApisListRequest',
        response_type_name='DirectoryList',
        supports_download=False,
    )
