# ResponseBankingAccountByIdV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankingAccountDetailV3**](BankingAccountDetailV3.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | **object** |  | [optional] 

## Example

```python
from au_open_banking_spec.models.response_banking_account_by_id_v3 import ResponseBankingAccountByIdV3

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingAccountByIdV3 from a JSON string
response_banking_account_by_id_v3_instance = ResponseBankingAccountByIdV3.from_json(json)
# print the JSON string representation of the object
print ResponseBankingAccountByIdV3.to_json()

# convert the object into a dict
response_banking_account_by_id_v3_dict = response_banking_account_by_id_v3_instance.to_dict()
# create an instance of ResponseBankingAccountByIdV3 from a dict
response_banking_account_by_id_v3_form_dict = response_banking_account_by_id_v3.from_dict(response_banking_account_by_id_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


