# openlattice-rundeck.FileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_execution_id_output_get**](FileApi.md#api26_execution_id_output_get) | **GET** /api/26/execution/{id}/output | List input files for an execution


# **api26_execution_id_output_get**
> api26_execution_id_output_get(id, offset=offset, maxlines=maxlines)

List input files for an execution

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
    api_instance = openlattice-rundeck.FileApi(api_client)
    id = 'id_example' # str | 
offset = 'offset_example' # str |  (optional)
maxlines = None # object |  (optional)

    try:
        # List input files for an execution
        api_instance.api26_execution_id_output_get(id, offset=offset, maxlines=maxlines)
    except ApiException as e:
        print("Exception when calling FileApi->api26_execution_id_output_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **offset** | **str**|  | [optional] 
 **maxlines** | [**object**](.md)|  | [optional] 

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
**200** | List of execution input files |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

