# RequestAccountIds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RequestAccountIdsData**](RequestAccountIdsData.md) |  | 
**meta** | **object** |  | [optional] 

## Example

```python
from au_open_banking_spec.models.request_account_ids import RequestAccountIds

# TODO update the JSON string below
json = "{}"
# create an instance of RequestAccountIds from a JSON string
request_account_ids_instance = RequestAccountIds.from_json(json)
# print the JSON string representation of the object
print RequestAccountIds.to_json()

# convert the object into a dict
request_account_ids_dict = request_account_ids_instance.to_dict()
# create an instance of RequestAccountIds from a dict
request_account_ids_form_dict = request_account_ids.from_dict(request_account_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


