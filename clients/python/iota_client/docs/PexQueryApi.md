# affinidi_tdk_iota_client.PexQueryApi

All URIs are relative to *https://apse1.api.affinidi.io/ais*

| Method                                                              | HTTP request                                                          | Description         |
| ------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------- |
| [**create_pex_query**](PexQueryApi.md#create_pex_query)             | **POST** /v1/configurations/{configurationId}/pex-queries             |
| [**delete_pex_queries**](PexQueryApi.md#delete_pex_queries)         | **POST** /v1/configurations/{configurationId}/delete-queries          | deletes pex queries |
| [**delete_pex_query_by_id**](PexQueryApi.md#delete_pex_query_by_id) | **DELETE** /v1/configurations/{configurationId}/pex-queries/{queryId} |
| [**get_pex_query_by_id**](PexQueryApi.md#get_pex_query_by_id)       | **GET** /v1/configurations/{configurationId}/pex-queries/{queryId}    |
| [**list_pex_queries**](PexQueryApi.md#list_pex_queries)             | **GET** /v1/configurations/{configurationId}/pex-queries              |
| [**save_pex_queries**](PexQueryApi.md#save_pex_queries)             | **POST** /v1/configurations/{configurationId}/save-queries            |
| [**update_pex_query_by_id**](PexQueryApi.md#update_pex_query_by_id) | **PATCH** /v1/configurations/{configurationId}/pex-queries/{queryId}  |

# **create_pex_query**

> PexQueryDto create_pex_query(configuration_id, create_pex_query_input)

### Example

- Api Key Authentication (ProjectTokenAuth):

```python
import time
import os
import affinidi_tdk_iota_client
from affinidi_tdk_iota_client.models.create_pex_query_input import CreatePexQueryInput
from affinidi_tdk_iota_client.models.pex_query_dto import PexQueryDto
from affinidi_tdk_iota_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/ais
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iota_client.Configuration(
    host = "https://apse1.api.affinidi.io/ais"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ProjectTokenAuth
configuration.api_key['ProjectTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ProjectTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iota_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iota_client.PexQueryApi(api_client)
    configuration_id = 'configuration_id_example' # str | iotaConfiguration Id
    create_pex_query_input = affinidi_tdk_iota_client.CreatePexQueryInput() # CreatePexQueryInput | CreatePexQuery

    try:
        api_response = api_instance.create_pex_query(configuration_id, create_pex_query_input)
        print("The response of PexQueryApi->create_pex_query:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PexQueryApi->create_pex_query: %s\n" % e)
```

### Parameters

| Name                       | Type                                              | Description          | Notes |
| -------------------------- | ------------------------------------------------- | -------------------- | ----- |
| **configuration_id**       | **str**                                           | iotaConfiguration Id |
| **create_pex_query_input** | [**CreatePexQueryInput**](CreatePexQueryInput.md) | CreatePexQuery       |

### Return type

[**PexQueryDto**](PexQueryDto.md)

### Authorization

[ProjectTokenAuth](../README.md#ProjectTokenAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description         | Response headers |
| ----------- | ------------------- | ---------------- |
| **201**     | CreatePexQueryOK    | -                |
| **400**     | BadRequestError     | -                |
| **403**     | ForbiddenError      | -                |
| **404**     | NotFoundError       | -                |
| **409**     | ConflictError       | -                |
| **422**     | UnprocessableEntity | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pex_queries**

> delete_pex_queries(configuration_id)

deletes pex queries

deletes pex queries

### Example

- Api Key Authentication (ProjectTokenAuth):

```python
import time
import os
import affinidi_tdk_iota_client
from affinidi_tdk_iota_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/ais
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iota_client.Configuration(
    host = "https://apse1.api.affinidi.io/ais"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ProjectTokenAuth
configuration.api_key['ProjectTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ProjectTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iota_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iota_client.PexQueryApi(api_client)
    configuration_id = 'configuration_id_example' # str | iotaConfiguration Id

    try:
        # deletes pex queries
        api_instance.delete_pex_queries(configuration_id)
    except Exception as e:
        print("Exception when calling PexQueryApi->delete_pex_queries: %s\n" % e)
```

### Parameters

| Name                 | Type    | Description          | Notes |
| -------------------- | ------- | -------------------- | ----- |
| **configuration_id** | **str** | iotaConfiguration Id |

### Return type

void (empty response body)

### Authorization

[ProjectTokenAuth](../README.md#ProjectTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description     | Response headers |
| ----------- | --------------- | ---------------- |
| **200**     |                 | -                |
| **400**     | BadRequestError | -                |
| **403**     | ForbiddenError  | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pex_query_by_id**

> delete_pex_query_by_id(configuration_id, query_id)

### Example

- Api Key Authentication (ProjectTokenAuth):

```python
import time
import os
import affinidi_tdk_iota_client
from affinidi_tdk_iota_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/ais
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iota_client.Configuration(
    host = "https://apse1.api.affinidi.io/ais"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ProjectTokenAuth
configuration.api_key['ProjectTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ProjectTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iota_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iota_client.PexQueryApi(api_client)
    configuration_id = 'configuration_id_example' # str | iotaConfiguration Id
    query_id = 'query_id_example' # str | pex-query Id

    try:
        api_instance.delete_pex_query_by_id(configuration_id, query_id)
    except Exception as e:
        print("Exception when calling PexQueryApi->delete_pex_query_by_id: %s\n" % e)
```

### Parameters

| Name                 | Type    | Description          | Notes |
| -------------------- | ------- | -------------------- | ----- |
| **configuration_id** | **str** | iotaConfiguration Id |
| **query_id**         | **str** | pex-query Id         |

### Return type

void (empty response body)

### Authorization

[ProjectTokenAuth](../README.md#ProjectTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description     | Response headers |
| ----------- | --------------- | ---------------- |
| **204**     | Deleted         | -                |
| **400**     | BadRequestError | -                |
| **403**     | ForbiddenError  | -                |
| **404**     | NotFoundError   | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pex_query_by_id**

> PexQueryDto get_pex_query_by_id(configuration_id, query_id)

### Example

- Api Key Authentication (ProjectTokenAuth):

```python
import time
import os
import affinidi_tdk_iota_client
from affinidi_tdk_iota_client.models.pex_query_dto import PexQueryDto
from affinidi_tdk_iota_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/ais
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iota_client.Configuration(
    host = "https://apse1.api.affinidi.io/ais"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ProjectTokenAuth
configuration.api_key['ProjectTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ProjectTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iota_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iota_client.PexQueryApi(api_client)
    configuration_id = 'configuration_id_example' # str | iotaConfiguration Id
    query_id = 'query_id_example' # str | pex-query Id

    try:
        api_response = api_instance.get_pex_query_by_id(configuration_id, query_id)
        print("The response of PexQueryApi->get_pex_query_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PexQueryApi->get_pex_query_by_id: %s\n" % e)
```

### Parameters

| Name                 | Type    | Description          | Notes |
| -------------------- | ------- | -------------------- | ----- |
| **configuration_id** | **str** | iotaConfiguration Id |
| **query_id**         | **str** | pex-query Id         |

### Return type

[**PexQueryDto**](PexQueryDto.md)

### Authorization

[ProjectTokenAuth](../README.md#ProjectTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description       | Response headers |
| ----------- | ----------------- | ---------------- |
| **200**     | GetPexQueryByIdOK | -                |
| **400**     | BadRequestError   | -                |
| **403**     | ForbiddenError    | -                |
| **404**     | NotFoundError     | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pex_queries**

> ListPexQueriesOK list_pex_queries(configuration_id, limit=limit, exclusive_start_key=exclusive_start_key)

### Example

- Api Key Authentication (ProjectTokenAuth):

```python
import time
import os
import affinidi_tdk_iota_client
from affinidi_tdk_iota_client.models.list_pex_queries_ok import ListPexQueriesOK
from affinidi_tdk_iota_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/ais
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iota_client.Configuration(
    host = "https://apse1.api.affinidi.io/ais"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ProjectTokenAuth
configuration.api_key['ProjectTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ProjectTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iota_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iota_client.PexQueryApi(api_client)
    configuration_id = 'configuration_id_example' # str | iotaConfiguration Id
    limit = 56 # int | Maximum number of records to fetch in a list (optional)
    exclusive_start_key = 'exclusive_start_key_example' # str | The base64url encoded key of the first item that this operation will evaluate (it is not returned). Use the value that was returned in the previous operation. (optional)

    try:
        api_response = api_instance.list_pex_queries(configuration_id, limit=limit, exclusive_start_key=exclusive_start_key)
        print("The response of PexQueryApi->list_pex_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PexQueryApi->list_pex_queries: %s\n" % e)
```

### Parameters

| Name                    | Type    | Description                                                                                                                                                    | Notes      |
| ----------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **configuration_id**    | **str** | iotaConfiguration Id                                                                                                                                           |
| **limit**               | **int** | Maximum number of records to fetch in a list                                                                                                                   | [optional] |
| **exclusive_start_key** | **str** | The base64url encoded key of the first item that this operation will evaluate (it is not returned). Use the value that was returned in the previous operation. | [optional] |

### Return type

[**ListPexQueriesOK**](ListPexQueriesOK.md)

### Authorization

[ProjectTokenAuth](../README.md#ProjectTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description      | Response headers |
| ----------- | ---------------- | ---------------- |
| **200**     | ListPexQueriesOK | -                |
| **400**     | BadRequestError  | -                |
| **403**     | ForbiddenError   | -                |
| **404**     | NotFoundError    | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_pex_queries**

> object save_pex_queries(configuration_id, save_pex_queries_update_input)

saves all pex queries

### Example

- Api Key Authentication (ProjectTokenAuth):

```python
import time
import os
import affinidi_tdk_iota_client
from affinidi_tdk_iota_client.models.save_pex_queries_update_input import SavePexQueriesUpdateInput
from affinidi_tdk_iota_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/ais
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iota_client.Configuration(
    host = "https://apse1.api.affinidi.io/ais"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ProjectTokenAuth
configuration.api_key['ProjectTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ProjectTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iota_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iota_client.PexQueryApi(api_client)
    configuration_id = 'configuration_id_example' # str | iotaConfiguration Id
    save_pex_queries_update_input = affinidi_tdk_iota_client.SavePexQueriesUpdateInput() # SavePexQueriesUpdateInput | SavePexQueriesInput

    try:
        api_response = api_instance.save_pex_queries(configuration_id, save_pex_queries_update_input)
        print("The response of PexQueryApi->save_pex_queries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PexQueryApi->save_pex_queries: %s\n" % e)
```

### Parameters

| Name                              | Type                                                          | Description          | Notes |
| --------------------------------- | ------------------------------------------------------------- | -------------------- | ----- |
| **configuration_id**              | **str**                                                       | iotaConfiguration Id |
| **save_pex_queries_update_input** | [**SavePexQueriesUpdateInput**](SavePexQueriesUpdateInput.md) | SavePexQueriesInput  |

### Return type

**object**

### Authorization

[ProjectTokenAuth](../README.md#ProjectTokenAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description              | Response headers |
| ----------- | ------------------------ | ---------------- |
| **200**     | SavePexQueriesResponseOK | -                |
| **400**     | BadRequestError          | -                |
| **403**     | ForbiddenError           | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pex_query_by_id**

> PexQueryDto update_pex_query_by_id(configuration_id, query_id, update_pex_query_input)

### Example

- Api Key Authentication (ProjectTokenAuth):

```python
import time
import os
import affinidi_tdk_iota_client
from affinidi_tdk_iota_client.models.pex_query_dto import PexQueryDto
from affinidi_tdk_iota_client.models.update_pex_query_input import UpdatePexQueryInput
from affinidi_tdk_iota_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/ais
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iota_client.Configuration(
    host = "https://apse1.api.affinidi.io/ais"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ProjectTokenAuth
configuration.api_key['ProjectTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ProjectTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iota_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iota_client.PexQueryApi(api_client)
    configuration_id = 'configuration_id_example' # str | iotaConfiguration Id
    query_id = 'query_id_example' # str | pex-query Id
    update_pex_query_input = affinidi_tdk_iota_client.UpdatePexQueryInput() # UpdatePexQueryInput | UpdatePexQueryById

    try:
        api_response = api_instance.update_pex_query_by_id(configuration_id, query_id, update_pex_query_input)
        print("The response of PexQueryApi->update_pex_query_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PexQueryApi->update_pex_query_by_id: %s\n" % e)
```

### Parameters

| Name                       | Type                                              | Description          | Notes |
| -------------------------- | ------------------------------------------------- | -------------------- | ----- |
| **configuration_id**       | **str**                                           | iotaConfiguration Id |
| **query_id**               | **str**                                           | pex-query Id         |
| **update_pex_query_input** | [**UpdatePexQueryInput**](UpdatePexQueryInput.md) | UpdatePexQueryById   |

### Return type

[**PexQueryDto**](PexQueryDto.md)

### Authorization

[ProjectTokenAuth](../README.md#ProjectTokenAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description          | Response headers |
| ----------- | -------------------- | ---------------- |
| **200**     | UpdatePexQueryByIdOK | -                |
| **400**     | BadRequestError      | -                |
| **403**     | ForbiddenError       | -                |
| **404**     | NotFoundError        | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
