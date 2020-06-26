# openlattice-rundeck.StorageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_storage_keys_path_delete**](StorageApi.md#api26_storage_keys_path_delete) | **DELETE** /api/26/storage/keys/{path} | Deletes the file if it exists and returns 204 response.


# **api26_storage_keys_path_delete**
> api26_storage_keys_path_delete(path)

Deletes the file if it exists and returns 204 response.

### Example

```python
from __future__ import print_function
import time
import openlattice-rundeck
from openlattice-rundeck.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openlattice-rundeck.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openlattice-rundeck.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openlattice-rundeck.StorageApi(api_client)
    path = None # object | Key path

    try:
        # Deletes the file if it exists and returns 204 response.
        api_instance.api26_storage_keys_path_delete(path)
    except ApiException as e:
        print("Exception when calling StorageApi->api26_storage_keys_path_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | [**object**](.md)| Key path | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success ! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

