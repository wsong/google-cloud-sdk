"""Generated client library for language version v1beta2."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.language.v1beta2 import language_v1beta2_messages as messages


class LanguageV1beta2(base_api.BaseApiClient):
  """Generated client library for service language version v1beta2."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://language.googleapis.com/'
  MTLS_BASE_URL = ''

  _PACKAGE = 'language'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-language', 'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta2'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'LanguageV1beta2'
  _URL_VERSION = 'v1beta2'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new language handle."""
    url = url or self.BASE_URL
    super(LanguageV1beta2, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.documents = self.DocumentsService(self)

  class DocumentsService(base_api.BaseApiService):
    """Service class for the documents resource."""

    _NAME = 'documents'

    def __init__(self, client):
      super(LanguageV1beta2.DocumentsService, self).__init__(client)
      self._upload_configs = {
          }

    def AnalyzeEntities(self, request, global_params=None):
      r"""Finds named entities (currently proper names and common nouns) in the text.
along with entity types, salience, mentions for each entity, and
other properties.

      Args:
        request: (AnalyzeEntitiesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeEntitiesResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeEntities')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeEntities.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='language.documents.analyzeEntities',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1beta2/documents:analyzeEntities',
        request_field='<request>',
        request_type_name='AnalyzeEntitiesRequest',
        response_type_name='AnalyzeEntitiesResponse',
        supports_download=False,
    )

    def AnalyzeEntitySentiment(self, request, global_params=None):
      r"""Finds entities, similar to AnalyzeEntities in the text and analyzes.
sentiment associated with each entity and its mentions.

      Args:
        request: (AnalyzeEntitySentimentRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeEntitySentimentResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeEntitySentiment')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeEntitySentiment.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='language.documents.analyzeEntitySentiment',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1beta2/documents:analyzeEntitySentiment',
        request_field='<request>',
        request_type_name='AnalyzeEntitySentimentRequest',
        response_type_name='AnalyzeEntitySentimentResponse',
        supports_download=False,
    )

    def AnalyzeSentiment(self, request, global_params=None):
      r"""Analyzes the sentiment of the provided text.

      Args:
        request: (AnalyzeSentimentRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeSentimentResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeSentiment')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeSentiment.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='language.documents.analyzeSentiment',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1beta2/documents:analyzeSentiment',
        request_field='<request>',
        request_type_name='AnalyzeSentimentRequest',
        response_type_name='AnalyzeSentimentResponse',
        supports_download=False,
    )

    def AnalyzeSyntax(self, request, global_params=None):
      r"""Analyzes the syntax of the text and provides sentence boundaries and.
tokenization along with part of speech tags, dependency trees, and other
properties.

      Args:
        request: (AnalyzeSyntaxRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnalyzeSyntaxResponse) The response message.
      """
      config = self.GetMethodConfig('AnalyzeSyntax')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnalyzeSyntax.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='language.documents.analyzeSyntax',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1beta2/documents:analyzeSyntax',
        request_field='<request>',
        request_type_name='AnalyzeSyntaxRequest',
        response_type_name='AnalyzeSyntaxResponse',
        supports_download=False,
    )

    def AnnotateText(self, request, global_params=None):
      r"""A convenience method that provides all syntax, sentiment, entity, and.
classification features in one call.

      Args:
        request: (AnnotateTextRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AnnotateTextResponse) The response message.
      """
      config = self.GetMethodConfig('AnnotateText')
      return self._RunMethod(
          config, request, global_params=global_params)

    AnnotateText.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='language.documents.annotateText',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1beta2/documents:annotateText',
        request_field='<request>',
        request_type_name='AnnotateTextRequest',
        response_type_name='AnnotateTextResponse',
        supports_download=False,
    )

    def ClassifyText(self, request, global_params=None):
      r"""Classifies a document into categories.

      Args:
        request: (ClassifyTextRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ClassifyTextResponse) The response message.
      """
      config = self.GetMethodConfig('ClassifyText')
      return self._RunMethod(
          config, request, global_params=global_params)

    ClassifyText.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='language.documents.classifyText',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1beta2/documents:classifyText',
        request_field='<request>',
        request_type_name='ClassifyTextRequest',
        response_type_name='ClassifyTextResponse',
        supports_download=False,
    )
