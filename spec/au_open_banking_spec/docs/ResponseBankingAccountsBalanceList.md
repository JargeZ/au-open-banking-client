# ResponseBankingAccountsBalanceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseBankingAccountsBalanceListData**](ResponseBankingAccountsBalanceListData.md) |  | 
**links** | [**LinksPaginated**](LinksPaginated.md) |  | 
**meta** | [**MetaPaginated**](MetaPaginated.md) |  | 

## Example

```python
from au_open_banking_spec.models.response_banking_accounts_balance_list import ResponseBankingAccountsBalanceList

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingAccountsBalanceList from a JSON string
response_banking_accounts_balance_list_instance = ResponseBankingAccountsBalanceList.from_json(json)
# print the JSON string representation of the object
print ResponseBankingAccountsBalanceList.to_json()

# convert the object into a dict
response_banking_accounts_balance_list_dict = response_banking_accounts_balance_list_instance.to_dict()
# create an instance of ResponseBankingAccountsBalanceList from a dict
response_banking_accounts_balance_list_form_dict = response_banking_accounts_balance_list.from_dict(response_banking_accounts_balance_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


