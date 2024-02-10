# ResponseErrorListV2Errors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the error encountered. Where the error is specific to the respondent, an application-specific error code, expressed as a string value. If the error is application-specific, the URN code that the specific error extends must be provided in the meta object. Otherwise, the value is the error code URN. | 
**title** | **str** | A short, human-readable summary of the problem that MUST NOT change from occurrence to occurrence of the problem represented by the error code. | 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | 
**meta** | [**MetaError**](MetaError.md) |  | [optional] 

## Example

```python
from au_open_banking_spec.models.response_error_list_v2_errors import ResponseErrorListV2Errors

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseErrorListV2Errors from a JSON string
response_error_list_v2_errors_instance = ResponseErrorListV2Errors.from_json(json)
# print the JSON string representation of the object
print ResponseErrorListV2Errors.to_json()

# convert the object into a dict
response_error_list_v2_errors_dict = response_error_list_v2_errors_instance.to_dict()
# create an instance of ResponseErrorListV2Errors from a dict
response_error_list_v2_errors_form_dict = response_error_list_v2_errors.from_dict(response_error_list_v2_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


