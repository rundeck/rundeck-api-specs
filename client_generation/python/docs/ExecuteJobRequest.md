# ExecuteJobRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arg_string** | **str** | Argument string to pass to the job, of the form &#x60;-opt value -opt2 value ...&#x60; | [optional] 
**loglevel** | **str** | Loglevel to use | [optional] 
**as_user** | **str** | A username identifying the user who ran the job. Requires &#x60;runAs&#x60; permission. | [optional] 
**filter** | **str** | A node filter string. | [optional] 
**run_at_time** | **str** | Specify a time to run the job (*API v18* or later). &#x60;ISO-8601&#x60; format with optional milliseconds. | [optional] 
**options** | **object** | Option value for option named &#x60;OPTNAME&#x60;. If specified the &#x60;argString&#x60; value is ignored (*API v18* or later). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


