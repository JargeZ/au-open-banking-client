# ResponseBankingAccountsBalanceListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balances** | [**List[BankingBalance]**](BankingBalance.md) | The list of balances returned | 

## Example

```python
from au_open_banking_spec.models.response_banking_accounts_balance_list_data import ResponseBankingAccountsBalanceListData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingAccountsBalanceListData from a JSON string
response_banking_accounts_balance_list_data_instance = ResponseBankingAccountsBalanceListData.from_json(json)
# print the JSON string representation of the object
print ResponseBankingAccountsBalanceListData.to_json()

# convert the object into a dict
response_banking_accounts_balance_list_data_dict = response_banking_accounts_balance_list_data_instance.to_dict()
# create an instance of ResponseBankingAccountsBalanceListData from a dict
response_banking_accounts_balance_list_data_form_dict = response_banking_accounts_balance_list_data.from_dict(response_banking_accounts_balance_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


