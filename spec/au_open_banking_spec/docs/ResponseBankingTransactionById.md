# ResponseBankingTransactionById


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankingTransactionDetail**](BankingTransactionDetail.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | **object** |  | [optional] 

## Example

```python
from au_open_banking_spec.models.response_banking_transaction_by_id import ResponseBankingTransactionById

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingTransactionById from a JSON string
response_banking_transaction_by_id_instance = ResponseBankingTransactionById.from_json(json)
# print the JSON string representation of the object
print ResponseBankingTransactionById.to_json()

# convert the object into a dict
response_banking_transaction_by_id_dict = response_banking_transaction_by_id_instance.to_dict()
# create an instance of ResponseBankingTransactionById from a dict
response_banking_transaction_by_id_form_dict = response_banking_transaction_by_id.from_dict(response_banking_transaction_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


