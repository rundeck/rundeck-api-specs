# openlattice-rundeck.AclApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_system_acl_policy_name_delete**](AclApi.md#api26_system_acl_policy_name_delete) | **DELETE** /api/26/system/acl/{policyName} | Delete policy


# **api26_system_acl_policy_name_delete**
> api26_system_acl_policy_name_delete(policy_name)

Delete policy

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
    api_instance = openlattice-rundeck.AclApi(api_client)
    policy_name = 'policy_name_example' # str | Policy file name

    try:
        # Delete policy
        api_instance.api26_system_acl_policy_name_delete(policy_name)
    except ApiException as e:
        print("Exception when calling AclApi->api26_system_acl_policy_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_name** | **str**| Policy file name | 

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

