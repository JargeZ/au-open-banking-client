# ResponseBankingAccountListV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseBankingAccountListV2Data**](ResponseBankingAccountListV2Data.md) |  | 
**links** | [**LinksPaginated**](LinksPaginated.md) |  | 
**meta** | [**MetaPaginated**](MetaPaginated.md) |  | 

## Example

```python
from au_open_banking_spec.models.response_banking_account_list_v2 import ResponseBankingAccountListV2

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingAccountListV2 from a JSON string
response_banking_account_list_v2_instance = ResponseBankingAccountListV2.from_json(json)
# print the JSON string representation of the object
print ResponseBankingAccountListV2.to_json()

# convert the object into a dict
response_banking_account_list_v2_dict = response_banking_account_list_v2_instance.to_dict()
# create an instance of ResponseBankingAccountListV2 from a dict
response_banking_account_list_v2_form_dict = response_banking_account_list_v2.from_dict(response_banking_account_list_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


