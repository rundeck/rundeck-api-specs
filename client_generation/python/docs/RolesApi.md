# openlattice-rundeck.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_user_roles_get**](RolesApi.md#api26_user_roles_get) | **GET** /api/26/user/roles | List the roles of the authenticated user


# **api26_user_roles_get**
> api26_user_roles_get()

List the roles of the authenticated user

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
    api_instance = openlattice-rundeck.RolesApi(api_client)
    
    try:
        # List the roles of the authenticated user
        api_instance.api26_user_roles_get()
    except ApiException as e:
        print("Exception when calling RolesApi->api26_user_roles_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | Expected response to a valid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

