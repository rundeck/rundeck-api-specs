# openlattice-rundeck.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api26_project_project_motd_md_delete**](ProjectApi.md#api26_project_project_motd_md_delete) | **DELETE** /api/26/project/{project}/motd.md | Delete project motd.md


# **api26_project_project_motd_md_delete**
> api26_project_project_motd_md_delete(project)

Delete project motd.md

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
    api_instance = openlattice-rundeck.ProjectApi(api_client)
    project = 'project_example' # str | Name of the project to import jobs into.

    try:
        # Delete project motd.md
        api_instance.api26_project_project_motd_md_delete(project)
    except ApiException as e:
        print("Exception when calling ProjectApi->api26_project_project_motd_md_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Name of the project to import jobs into. | 

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

