# CommonPhysicalAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_u_type** | **str** | The type of address object present | 
**simple** | [**CommonSimpleAddress**](CommonSimpleAddress.md) |  | [optional] 
**paf** | [**CommonPAFAddress**](CommonPAFAddress.md) |  | [optional] 

## Example

```python
from au_open_banking_spec.models.common_physical_address import CommonPhysicalAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPhysicalAddress from a JSON string
common_physical_address_instance = CommonPhysicalAddress.from_json(json)
# print the JSON string representation of the object
print CommonPhysicalAddress.to_json()

# convert the object into a dict
common_physical_address_dict = common_physical_address_instance.to_dict()
# create an instance of CommonPhysicalAddress from a dict
common_physical_address_form_dict = common_physical_address.from_dict(common_physical_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


