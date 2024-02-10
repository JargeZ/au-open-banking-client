# ResponseBankingTransactionListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transactions** | [**List[BankingTransaction]**](BankingTransaction.md) |  | 

## Example

```python
from au_open_banking_spec.models.response_banking_transaction_list_data import ResponseBankingTransactionListData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingTransactionListData from a JSON string
response_banking_transaction_list_data_instance = ResponseBankingTransactionListData.from_json(json)
# print the JSON string representation of the object
print ResponseBankingTransactionListData.to_json()

# convert the object into a dict
response_banking_transaction_list_data_dict = response_banking_transaction_list_data_instance.to_dict()
# create an instance of ResponseBankingTransactionListData from a dict
response_banking_transaction_list_data_form_dict = response_banking_transaction_list_data.from_dict(response_banking_transaction_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


