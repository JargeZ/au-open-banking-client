# ResponseBankingAccountsBalanceById


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankingBalance**](BankingBalance.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | **object** |  | [optional] 

## Example

```python
from au_open_banking_spec.models.response_banking_accounts_balance_by_id import ResponseBankingAccountsBalanceById

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingAccountsBalanceById from a JSON string
response_banking_accounts_balance_by_id_instance = ResponseBankingAccountsBalanceById.from_json(json)
# print the JSON string representation of the object
print ResponseBankingAccountsBalanceById.to_json()

# convert the object into a dict
response_banking_accounts_balance_by_id_dict = response_banking_accounts_balance_by_id_instance.to_dict()
# create an instance of ResponseBankingAccountsBalanceById from a dict
response_banking_accounts_balance_by_id_form_dict = response_banking_accounts_balance_by_id.from_dict(response_banking_accounts_balance_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


