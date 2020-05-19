"""Generated client library for recommender version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.recommender.v1 import recommender_v1_messages as messages


class RecommenderV1(base_api.BaseApiClient):
  """Generated client library for service recommender version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://recommender.googleapis.com/'
  MTLS_BASE_URL = 'https://recommender.mtls.googleapis.com/'

  _PACKAGE = 'recommender'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'RecommenderV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new recommender handle."""
    url = url or self.BASE_URL
    super(RecommenderV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_insightTypes_insights = self.ProjectsLocationsInsightTypesInsightsService(self)
    self.projects_locations_insightTypes = self.ProjectsLocationsInsightTypesService(self)
    self.projects_locations_recommenders_recommendations = self.ProjectsLocationsRecommendersRecommendationsService(self)
    self.projects_locations_recommenders = self.ProjectsLocationsRecommendersService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsInsightTypesInsightsService(base_api.BaseApiService):
    """Service class for the projects_locations_insightTypes_insights resource."""

    _NAME = 'projects_locations_insightTypes_insights'

    def __init__(self, client):
      super(RecommenderV1.ProjectsLocationsInsightTypesInsightsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the requested insight. Requires the recommender.*.get IAM permission.
for the specified insight type.

      Args:
        request: (RecommenderProjectsLocationsInsightTypesInsightsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1Insight) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/insightTypes/{insightTypesId}/insights/{insightsId}',
        http_method='GET',
        method_id='recommender.projects.locations.insightTypes.insights.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='RecommenderProjectsLocationsInsightTypesInsightsGetRequest',
        response_type_name='GoogleCloudRecommenderV1Insight',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists insights for a Cloud project. Requires the recommender.*.list IAM.
permission for the specified insight type.

      Args:
        request: (RecommenderProjectsLocationsInsightTypesInsightsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1ListInsightsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/insightTypes/{insightTypesId}/insights',
        http_method='GET',
        method_id='recommender.projects.locations.insightTypes.insights.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/insights',
        request_field='',
        request_type_name='RecommenderProjectsLocationsInsightTypesInsightsListRequest',
        response_type_name='GoogleCloudRecommenderV1ListInsightsResponse',
        supports_download=False,
    )

    def MarkAccepted(self, request, global_params=None):
      r"""Marks the Insight State as Accepted. Users can use this method to.
indicate to the Recommender API that they have applied some action based
on the insight. This stops the insight content from being updated.

MarkInsightAccepted can be applied to insights in ACTIVE state. Requires
the recommender.*.update IAM permission for the specified insight.

      Args:
        request: (RecommenderProjectsLocationsInsightTypesInsightsMarkAcceptedRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1Insight) The response message.
      """
      config = self.GetMethodConfig('MarkAccepted')
      return self._RunMethod(
          config, request, global_params=global_params)

    MarkAccepted.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/insightTypes/{insightTypesId}/insights/{insightsId}:markAccepted',
        http_method='POST',
        method_id='recommender.projects.locations.insightTypes.insights.markAccepted',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:markAccepted',
        request_field='googleCloudRecommenderV1MarkInsightAcceptedRequest',
        request_type_name='RecommenderProjectsLocationsInsightTypesInsightsMarkAcceptedRequest',
        response_type_name='GoogleCloudRecommenderV1Insight',
        supports_download=False,
    )

  class ProjectsLocationsInsightTypesService(base_api.BaseApiService):
    """Service class for the projects_locations_insightTypes resource."""

    _NAME = 'projects_locations_insightTypes'

    def __init__(self, client):
      super(RecommenderV1.ProjectsLocationsInsightTypesService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsRecommendersRecommendationsService(base_api.BaseApiService):
    """Service class for the projects_locations_recommenders_recommendations resource."""

    _NAME = 'projects_locations_recommenders_recommendations'

    def __init__(self, client):
      super(RecommenderV1.ProjectsLocationsRecommendersRecommendationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the requested recommendation. Requires the recommender.*.get.
IAM permission for the specified recommender.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1Recommendation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations/{recommendationsId}',
        http_method='GET',
        method_id='recommender.projects.locations.recommenders.recommendations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='RecommenderProjectsLocationsRecommendersRecommendationsGetRequest',
        response_type_name='GoogleCloudRecommenderV1Recommendation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists recommendations for a Cloud project. Requires the recommender.*.list.
IAM permission for the specified recommender.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1ListRecommendationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations',
        http_method='GET',
        method_id='recommender.projects.locations.recommenders.recommendations.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/recommendations',
        request_field='',
        request_type_name='RecommenderProjectsLocationsRecommendersRecommendationsListRequest',
        response_type_name='GoogleCloudRecommenderV1ListRecommendationsResponse',
        supports_download=False,
    )

    def MarkClaimed(self, request, global_params=None):
      r"""Marks the Recommendation State as Claimed. Users can use this method to.
indicate to the Recommender API that they are starting to apply the
recommendation themselves. This stops the recommendation content from being
updated. Associated insights are frozen and placed in the ACCEPTED state.

MarkRecommendationClaimed can be applied to recommendations in CLAIMED,
SUCCEEDED, FAILED, or ACTIVE state.

Requires the recommender.*.update IAM permission for the specified
recommender.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsMarkClaimedRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1Recommendation) The response message.
      """
      config = self.GetMethodConfig('MarkClaimed')
      return self._RunMethod(
          config, request, global_params=global_params)

    MarkClaimed.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations/{recommendationsId}:markClaimed',
        http_method='POST',
        method_id='recommender.projects.locations.recommenders.recommendations.markClaimed',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:markClaimed',
        request_field='googleCloudRecommenderV1MarkRecommendationClaimedRequest',
        request_type_name='RecommenderProjectsLocationsRecommendersRecommendationsMarkClaimedRequest',
        response_type_name='GoogleCloudRecommenderV1Recommendation',
        supports_download=False,
    )

    def MarkFailed(self, request, global_params=None):
      r"""Marks the Recommendation State as Failed. Users can use this method to.
indicate to the Recommender API that they have applied the recommendation
themselves, and the operation failed. This stops the recommendation content
from being updated. Associated insights are frozen and placed in the
ACCEPTED state.

MarkRecommendationFailed can be applied to recommendations in ACTIVE,
CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified
recommender.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsMarkFailedRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1Recommendation) The response message.
      """
      config = self.GetMethodConfig('MarkFailed')
      return self._RunMethod(
          config, request, global_params=global_params)

    MarkFailed.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations/{recommendationsId}:markFailed',
        http_method='POST',
        method_id='recommender.projects.locations.recommenders.recommendations.markFailed',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:markFailed',
        request_field='googleCloudRecommenderV1MarkRecommendationFailedRequest',
        request_type_name='RecommenderProjectsLocationsRecommendersRecommendationsMarkFailedRequest',
        response_type_name='GoogleCloudRecommenderV1Recommendation',
        supports_download=False,
    )

    def MarkSucceeded(self, request, global_params=None):
      r"""Marks the Recommendation State as Succeeded. Users can use this method to.
indicate to the Recommender API that they have applied the recommendation
themselves, and the operation was successful. This stops the recommendation
content from being updated. Associated insights are frozen and placed in
the ACCEPTED state.

MarkRecommendationSucceeded can be applied to recommendations in ACTIVE,
CLAIMED, SUCCEEDED, or FAILED state.

Requires the recommender.*.update IAM permission for the specified
recommender.

      Args:
        request: (RecommenderProjectsLocationsRecommendersRecommendationsMarkSucceededRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (GoogleCloudRecommenderV1Recommendation) The response message.
      """
      config = self.GetMethodConfig('MarkSucceeded')
      return self._RunMethod(
          config, request, global_params=global_params)

    MarkSucceeded.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/projects/{projectsId}/locations/{locationsId}/recommenders/{recommendersId}/recommendations/{recommendationsId}:markSucceeded',
        http_method='POST',
        method_id='recommender.projects.locations.recommenders.recommendations.markSucceeded',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:markSucceeded',
        request_field='googleCloudRecommenderV1MarkRecommendationSucceededRequest',
        request_type_name='RecommenderProjectsLocationsRecommendersRecommendationsMarkSucceededRequest',
        response_type_name='GoogleCloudRecommenderV1Recommendation',
        supports_download=False,
    )

  class ProjectsLocationsRecommendersService(base_api.BaseApiService):
    """Service class for the projects_locations_recommenders resource."""

    _NAME = 'projects_locations_recommenders'

    def __init__(self, client):
      super(RecommenderV1.ProjectsLocationsRecommendersService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(RecommenderV1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(RecommenderV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
