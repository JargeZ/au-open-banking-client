# BankingTransactionDetailAllOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extended_data** | [**BankingTransactionDetailAllOfExtendedData**](BankingTransactionDetailAllOfExtendedData.md) |  | 

## Example

```python
from au_open_banking_spec.models.banking_transaction_detail_all_of import BankingTransactionDetailAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of BankingTransactionDetailAllOf from a JSON string
banking_transaction_detail_all_of_instance = BankingTransactionDetailAllOf.from_json(json)
# print the JSON string representation of the object
print BankingTransactionDetailAllOf.to_json()

# convert the object into a dict
banking_transaction_detail_all_of_dict = banking_transaction_detail_all_of_instance.to_dict()
# create an instance of BankingTransactionDetailAllOf from a dict
banking_transaction_detail_all_of_form_dict = banking_transaction_detail_all_of.from_dict(banking_transaction_detail_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


