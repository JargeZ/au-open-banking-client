# ResponseBankingTransactionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseBankingTransactionListData**](ResponseBankingTransactionListData.md) |  | 
**links** | [**LinksPaginated**](LinksPaginated.md) |  | 
**meta** | [**MetaPaginatedTransaction**](MetaPaginatedTransaction.md) |  | 

## Example

```python
from au_open_banking_spec.models.response_banking_transaction_list import ResponseBankingTransactionList

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingTransactionList from a JSON string
response_banking_transaction_list_instance = ResponseBankingTransactionList.from_json(json)
# print the JSON string representation of the object
print ResponseBankingTransactionList.to_json()

# convert the object into a dict
response_banking_transaction_list_dict = response_banking_transaction_list_instance.to_dict()
# create an instance of ResponseBankingTransactionList from a dict
response_banking_transaction_list_form_dict = response_banking_transaction_list.from_dict(response_banking_transaction_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


