"""Generated message classes for cloudfunctions version v1.

Manages lightweight user-provided functions executed in response to events.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'cloudfunctions'


class CallFunctionRequest(_messages.Message):
  """Request for the `CallFunction` method.

  Fields:
    data: Input to be passed to the function.
  """

  data = _messages.StringField(1)


class CallFunctionResponse(_messages.Message):
  """Response of `CallFunction` method.

  Fields:
    error: Either system or user-function generated error. Set if execution
      was not successful.
    executionId: Execution id of function invocation.
    result: Result populated for successful execution of synchronous function.
      Will not be populated if function does not return a result through
      context.
  """

  error = _messages.StringField(1)
  executionId = _messages.StringField(2)
  result = _messages.StringField(3)


class CloudFunction(_messages.Message):
  """Describes a Cloud Function that contains user computation executed in
  response to an event. It encapsulate function and triggers configurations.

  Enums:
    StatusValueValuesEnum: Output only. Status of the function deployment.

  Messages:
    LabelsValue: Labels associated with this Cloud Function.

  Fields:
    availableMemoryMb: The amount of memory in MB available for a function.
      Defaults to 256MB.
    description: User-provided description of a function.
    entryPoint: The name of the function (as defined in source code) that will
      be executed. Defaults to the resource name suffix, if not specified. For
      backward compatibility, if function with given name is not found, then
      the system will try to use function named "function". For Node.js this
      is name of a function exported by the module specified in
      `source_location`.
    eventTrigger: A source that fires events in response to a condition in
      another service.
    httpsTrigger: An HTTPS endpoint type of source that can be triggered via
      URL.
    labels: Labels associated with this Cloud Function.
    name: A user-defined name of the function. Function names must be unique
      globally and match pattern `projects/*/locations/*/functions/*`
    serviceAccountEmail: Output only. The email of the function's service
      account.
    sourceArchiveUrl: The Google Cloud Storage URL, starting with gs://,
      pointing to the zip archive which contains the function.
    sourceRepository: **Beta Feature**  The source repository where a function
      is hosted.
    sourceUploadUrl: The Google Cloud Storage signed URL used for source
      uploading, generated by google.cloud.functions.v1.GenerateUploadUrl
    status: Output only. Status of the function deployment.
    timeout: The function execution timeout. Execution is considered failed
      and can be terminated if the function is not completed at the end of the
      timeout period. Defaults to 60 seconds.
    updateTime: Output only. The last update timestamp of a Cloud Function.
    versionId: Output only. The version identifier of the Cloud Function. Each
      deployment attempt results in a new version of a function being created.
  """

  class StatusValueValuesEnum(_messages.Enum):
    """Output only. Status of the function deployment.

    Values:
      CLOUD_FUNCTION_STATUS_UNSPECIFIED: Not specified. Invalid state.
      ACTIVE: Function has been succesfully deployed and is serving.
      OFFLINE: Function deployment failed and the function isn\u2019t serving.
      DEPLOY_IN_PROGRESS: Function is being created or updated.
      DELETE_IN_PROGRESS: Function is being deleted.
      UNKNOWN: Function deployment failed and the function serving state is
        undefined. The function should be updated or deleted to move it out of
        this state.
    """
    CLOUD_FUNCTION_STATUS_UNSPECIFIED = 0
    ACTIVE = 1
    OFFLINE = 2
    DEPLOY_IN_PROGRESS = 3
    DELETE_IN_PROGRESS = 4
    UNKNOWN = 5

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """Labels associated with this Cloud Function.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  availableMemoryMb = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  description = _messages.StringField(2)
  entryPoint = _messages.StringField(3)
  eventTrigger = _messages.MessageField('EventTrigger', 4)
  httpsTrigger = _messages.MessageField('HttpsTrigger', 5)
  labels = _messages.MessageField('LabelsValue', 6)
  name = _messages.StringField(7)
  serviceAccountEmail = _messages.StringField(8)
  sourceArchiveUrl = _messages.StringField(9)
  sourceRepository = _messages.MessageField('SourceRepository', 10)
  sourceUploadUrl = _messages.StringField(11)
  status = _messages.EnumField('StatusValueValuesEnum', 12)
  timeout = _messages.StringField(13)
  updateTime = _messages.StringField(14)
  versionId = _messages.IntegerField(15)


class CloudfunctionsOperationsGetRequest(_messages.Message):
  """A CloudfunctionsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class CloudfunctionsOperationsListRequest(_messages.Message):
  """A CloudfunctionsOperationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The name of the operation's parent resource.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class CloudfunctionsProjectsLocationsFunctionsCallRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsFunctionsCallRequest object.

  Fields:
    callFunctionRequest: A CallFunctionRequest resource to be passed as the
      request body.
    name: The name of the function to be called.
  """

  callFunctionRequest = _messages.MessageField('CallFunctionRequest', 1)
  name = _messages.StringField(2, required=True)


class CloudfunctionsProjectsLocationsFunctionsCreateRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsFunctionsCreateRequest object.

  Fields:
    cloudFunction: A CloudFunction resource to be passed as the request body.
    location: The project and location in which the function should be
      created, specified in the format `projects/*/locations/*`
  """

  cloudFunction = _messages.MessageField('CloudFunction', 1)
  location = _messages.StringField(2, required=True)


class CloudfunctionsProjectsLocationsFunctionsDeleteRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsFunctionsDeleteRequest object.

  Fields:
    name: The name of the function which should be deleted.
  """

  name = _messages.StringField(1, required=True)


class CloudfunctionsProjectsLocationsFunctionsGenerateDownloadUrlRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsFunctionsGenerateDownloadUrlRequest
  object.

  Fields:
    generateDownloadUrlRequest: A GenerateDownloadUrlRequest resource to be
      passed as the request body.
    name: The name of function for which source code Google Cloud Storage
      signed URL should be generated.
  """

  generateDownloadUrlRequest = _messages.MessageField('GenerateDownloadUrlRequest', 1)
  name = _messages.StringField(2, required=True)


class CloudfunctionsProjectsLocationsFunctionsGenerateUploadUrlRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsFunctionsGenerateUploadUrlRequest
  object.

  Fields:
    generateUploadUrlRequest: A GenerateUploadUrlRequest resource to be passed
      as the request body.
    parent: The project and location in which the Google Cloud Storage signed
      URL should be generated, specified in the format
      `projects/*/locations/*`.
  """

  generateUploadUrlRequest = _messages.MessageField('GenerateUploadUrlRequest', 1)
  parent = _messages.StringField(2, required=True)


class CloudfunctionsProjectsLocationsFunctionsGetRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsFunctionsGetRequest object.

  Fields:
    name: The name of the function which details should be obtained.
  """

  name = _messages.StringField(1, required=True)


class CloudfunctionsProjectsLocationsFunctionsListRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsFunctionsListRequest object.

  Fields:
    pageSize: Maximum number of functions to return per call.
    pageToken: The value returned by the last `ListFunctionsResponse`;
      indicates that this is a continuation of a prior `ListFunctions` call,
      and that the system should return the next page of data.
    parent: The project and location from which the function should be listed,
      specified in the format `projects/*/locations/*` If you want to list
      functions in all locations, use "-" in place of a location.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class CloudfunctionsProjectsLocationsFunctionsPatchRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsFunctionsPatchRequest object.

  Fields:
    cloudFunction: A CloudFunction resource to be passed as the request body.
    name: A user-defined name of the function. Function names must be unique
      globally and match pattern `projects/*/locations/*/functions/*`
    updateMask: Required list of fields to be updated in this request.
  """

  cloudFunction = _messages.MessageField('CloudFunction', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class CloudfunctionsProjectsLocationsListRequest(_messages.Message):
  """A CloudfunctionsProjectsLocationsListRequest object.

  Fields:
    filter: The standard list filter.
    name: The resource that owns the locations collection, if applicable.
    pageSize: The standard list page size.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class EventTrigger(_messages.Message):
  """Describes EventTrigger, used to request events be sent from another
  service.

  Fields:
    eventType: Required. The type of event to observe. For example:
      `providers/cloud.storage/eventTypes/object.change` and
      `providers/cloud.pubsub/eventTypes/topic.publish`.  Event types match
      pattern `providers/*/eventTypes/*.*`. The pattern contains:  1.
      namespace: For example, `cloud.storage` and
      `google.firebase.analytics`. 2. resource type: The type of resource on
      which event occurs. For    example, the Google Cloud Storage API
      includes the type `object`. 3. action: The action that generates the
      event. For example, action for    a Google Cloud Storage Object is
      'change'. These parts are lower case.
    failurePolicy: Specifies policy for failed executions.
    resource: Required. The resource(s) from which to observe events, for
      example, `projects/_/buckets/myBucket`.  Not all syntactically correct
      values are accepted by all services. For example:  1. The authorization
      model must support it. Google Cloud Functions    only allows
      EventTriggers to be deployed that observe resources in the    same
      project as the `CloudFunction`. 2. The resource type must match the
      pattern expected for an    `event_type`. For example, an `EventTrigger`
      that has an    `event_type` of "google.pubsub.topic.publish" should have
      a resource    that matches Google Cloud Pub/Sub topics.  Additionally,
      some services may support short names when creating an `EventTrigger`.
      These will always be returned in the normalized "long" format.  See each
      *service's* documentation for supported formats.
    service: The hostname of the service that should be observed.  If no
      string is provided, the default service implementing the API will be
      used. For example, `storage.googleapis.com` is the default for all event
      types in the `google.storage` namespace.
  """

  eventType = _messages.StringField(1)
  failurePolicy = _messages.MessageField('FailurePolicy', 2)
  resource = _messages.StringField(3)
  service = _messages.StringField(4)


class FailurePolicy(_messages.Message):
  """Describes the policy in case of function's execution failure. If empty,
  then defaults to ignoring failures (i.e. not retrying them).

  Fields:
    retry: If specified, then the function will be retried in case of a
      failure.
  """

  retry = _messages.MessageField('Retry', 1)


class GenerateDownloadUrlRequest(_messages.Message):
  """Request of `GenerateDownloadUrl` method.

  Fields:
    versionId: The optional version of function. If not set, default, current
      version is used.
  """

  versionId = _messages.IntegerField(1, variant=_messages.Variant.UINT64)


class GenerateDownloadUrlResponse(_messages.Message):
  """Response of `GenerateDownloadUrl` method.

  Fields:
    downloadUrl: The generated Google Cloud Storage signed URL that should be
      used for function source code download.
  """

  downloadUrl = _messages.StringField(1)


class GenerateUploadUrlRequest(_messages.Message):
  """Request of `GenerateSourceUploadUrl` method."""


class GenerateUploadUrlResponse(_messages.Message):
  """Response of `GenerateSourceUploadUrl` method.

  Fields:
    uploadUrl: The generated Google Cloud Storage signed URL that should be
      used for a function source code upload. The uploaded file should be a
      zip archive which contains a function.
  """

  uploadUrl = _messages.StringField(1)


class HttpsTrigger(_messages.Message):
  """Describes HttpsTrigger, could be used to connect web hooks to function.

  Fields:
    url: Output only. The deployed url for the function.
  """

  url = _messages.StringField(1)


class ListFunctionsResponse(_messages.Message):
  """Response for the `ListFunctions` method.

  Fields:
    functions: The functions that match the request.
    nextPageToken: If not empty, indicates that there may be more functions
      that match the request; this value should be passed in a new
      google.cloud.functions.v1.ListFunctionsRequest to get more functions.
  """

  functions = _messages.MessageField('CloudFunction', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListLocationsResponse(_messages.Message):
  """The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class ListOperationsResponse(_messages.Message):
  """The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Location(_messages.Message):
  """A resource that represents Google Cloud Platform location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    """Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Operation(_messages.Message):
  """This resource represents a long-running operation that is the result of a
  network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation.
      It typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal response of the operation in case of success.
      If the original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation.  It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata.  Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should have the format of `operations/some/unique/name`.
    response: The normal response of the operation in case of success.  If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`.  If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource.  For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name.  For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    """Service-specific metadata associated with the operation.  It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata.  Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    """The normal response of the operation in case of success.  If the
    original method returns no data on success, such as `Delete`, the response
    is `google.protobuf.Empty`.  If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource.  For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name.  For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationMetadataV1(_messages.Message):
  """Metadata describing an Operation

  Enums:
    TypeValueValuesEnum: Type of operation.

  Messages:
    RequestValue: The original request that started the operation.

  Fields:
    request: The original request that started the operation.
    target: Target of the operation - for example
      projects/project-1/locations/region-1/functions/function-1
    type: Type of operation.
    updateTime: The last update timestamp of the operation.
    versionId: Version id of the function created or updated by an API call.
      This field is only pupulated for Create and Update operations.
  """

  class TypeValueValuesEnum(_messages.Enum):
    """Type of operation.

    Values:
      OPERATION_UNSPECIFIED: Unknown operation type.
      CREATE_FUNCTION: Triggered by CreateFunction call
      UPDATE_FUNCTION: Triggered by UpdateFunction call
      DELETE_FUNCTION: Triggered by DeleteFunction call.
    """
    OPERATION_UNSPECIFIED = 0
    CREATE_FUNCTION = 1
    UPDATE_FUNCTION = 2
    DELETE_FUNCTION = 3

  @encoding.MapUnrecognizedFields('additionalProperties')
  class RequestValue(_messages.Message):
    """The original request that started the operation.

    Messages:
      AdditionalProperty: An additional property for a RequestValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a RequestValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  request = _messages.MessageField('RequestValue', 1)
  target = _messages.StringField(2)
  type = _messages.EnumField('TypeValueValuesEnum', 3)
  updateTime = _messages.StringField(4)
  versionId = _messages.IntegerField(5)


class OperationMetadataV1Beta2(_messages.Message):
  """Metadata describing an Operation

  Enums:
    TypeValueValuesEnum: Type of operation.

  Messages:
    RequestValue: The original request that started the operation.

  Fields:
    request: The original request that started the operation.
    target: Target of the operation - for example
      projects/project-1/locations/region-1/functions/function-1
    type: Type of operation.
    updateTime: The last update timestamp of the operation.
    versionId: Version id of the function created or updated by an API call.
      This field is only pupulated for Create and Update operations.
  """

  class TypeValueValuesEnum(_messages.Enum):
    """Type of operation.

    Values:
      OPERATION_UNSPECIFIED: Unknown operation type.
      CREATE_FUNCTION: Triggered by CreateFunction call
      UPDATE_FUNCTION: Triggered by UpdateFunction call
      DELETE_FUNCTION: Triggered by DeleteFunction call.
    """
    OPERATION_UNSPECIFIED = 0
    CREATE_FUNCTION = 1
    UPDATE_FUNCTION = 2
    DELETE_FUNCTION = 3

  @encoding.MapUnrecognizedFields('additionalProperties')
  class RequestValue(_messages.Message):
    """The original request that started the operation.

    Messages:
      AdditionalProperty: An additional property for a RequestValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a RequestValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  request = _messages.MessageField('RequestValue', 1)
  target = _messages.StringField(2)
  type = _messages.EnumField('TypeValueValuesEnum', 3)
  updateTime = _messages.StringField(4)
  versionId = _messages.IntegerField(5)


class Retry(_messages.Message):
  """Describes the retry policy in case of function's execution failure. A
  function execution will be retried on any failure. A failed execution will
  be retried up to 7 days with an exponential backoff (capped at 10 seconds).
  Retried execution is charged as any other execution.
  """



class SourceRepository(_messages.Message):
  """Describes SourceRepository, used to represent parameters related to
  source repository where a function is hosted.

  Fields:
    deployedUrl: Output only. The URL pointing to the hosted repository where
      the function were defined at the time of deployment. It always points to
      a specific commit in the format described above.
    url: The URL pointing to the hosted repository where the function is
      defined. There are supported Cloud Source Repository URLs in the
      following formats:  To refer to a specific commit: `https://source.devel
      opers.google.com/projects/*/repos/*/revisions/*/paths/*` To refer to a
      moveable alias (branch):
      `https://source.developers.google.com/projects/*/repos/*/moveable-
      aliases/*/paths/*` In particular, to refer to HEAD use `master` moveable
      alias. To refer to a specific fixed alias (tag):
      `https://source.developers.google.com/projects/*/repos/*/fixed-
      aliases/*/paths/*`  You may omit `paths/*` if you want to use the main
      directory.
  """

  deployedUrl = _messages.StringField(1)
  url = _messages.StringField(2)


class StandardQueryParameters(_messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = _messages.StringField(4)
  callback = _messages.StringField(5)
  fields = _messages.StringField(6)
  key = _messages.StringField(7)
  oauth_token = _messages.StringField(8)
  pp = _messages.BooleanField(9, default=True)
  prettyPrint = _messages.BooleanField(10, default=True)
  quotaUser = _messages.StringField(11)
  trace = _messages.StringField(12)
  uploadType = _messages.StringField(13)
  upload_protocol = _messages.StringField(14)


class Status(_messages.Message):
  """The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). The error model is designed to be:
  - Simple to use and understand for most users - Flexible enough to meet
  unexpected needs  # Overview  The `Status` message contains three pieces of
  data: error code, error message, and error details. The error code should be
  an enum value of google.rpc.Code, but it may accept additional error codes
  if needed.  The error message should be a developer-facing English message
  that helps developers *understand* and *resolve* the error. If a localized
  user-facing error message is needed, put the localized message in the error
  details or localize it in the client. The optional error details may contain
  arbitrary information about the error. There is a predefined set of error
  detail types in the package `google.rpc` that can be used for common error
  conditions.  # Language mapping  The `Status` message is the logical
  representation of the error model, but it is not necessarily the actual wire
  format. When the `Status` message is exposed in different client libraries
  and different wire protocols, it can be mapped differently. For example, it
  will likely be mapped to some exceptions in Java, but more likely mapped to
  some error codes in C.  # Other uses  The error model and the `Status`
  message can be used in a variety of environments, either with or without
  APIs, to provide a consistent developer experience across different
  environments.  Example uses of this error model include:  - Partial errors.
  If a service needs to return partial errors to the client,     it may embed
  the `Status` in the normal response to indicate the partial     errors.  -
  Workflow errors. A typical workflow has multiple steps. Each step may
  have a `Status` message for error reporting.  - Batch operations. If a
  client uses batch request and batch response, the     `Status` message
  should be used directly inside batch response, one for     each error sub-
  response.  - Asynchronous operations. If an API call embeds asynchronous
  operation     results in its response, the status of those operations should
  be     represented directly using the `Status` message.  - Logging. If some
  API errors are stored in logs, the message `Status` could     be used
  directly after any stripping needed for security/privacy reasons.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
