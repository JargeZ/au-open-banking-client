# MetaError

Additional data for customised error codes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urn** | **str** | The CDR error code URN which the application-specific error code extends. Mandatory if the error &#x60;code&#x60; is an application-specific error rather than a standardised error code. | [optional] 

## Example

```python
from au_open_banking_spec.models.meta_error import MetaError

# TODO update the JSON string below
json = "{}"
# create an instance of MetaError from a JSON string
meta_error_instance = MetaError.from_json(json)
# print the JSON string representation of the object
print MetaError.to_json()

# convert the object into a dict
meta_error_dict = meta_error_instance.to_dict()
# create an instance of MetaError from a dict
meta_error_form_dict = meta_error.from_dict(meta_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


