# RequestAccountIdsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_ids** | **List[str]** |  | 

## Example

```python
from au_open_banking_spec.models.request_account_ids_data import RequestAccountIdsData

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAccountIdsData from a JSON string
request_account_ids_data_instance = RequestAccountIdsData.from_json(json)
# print the JSON string representation of the object
print RequestAccountIdsData.to_json()

# convert the object into a dict
request_account_ids_data_dict = request_account_ids_data_instance.to_dict()
# create an instance of RequestAccountIdsData from a dict
request_account_ids_data_form_dict = request_account_ids_data.from_dict(request_account_ids_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


