# BankingDirectDebit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | A unique ID of the account adhering to the standards for ID permanence. | 
**authorised_entity** | [**BankingAuthorisedEntity**](BankingAuthorisedEntity.md) |  | 
**last_debit_date_time** | **str** | The date and time of the last debit executed under this authorisation | [optional] 
**last_debit_amount** | **str** | The amount of the last debit executed under this authorisation | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_direct_debit import BankingDirectDebit

# TODO update the JSON string below
json = "{}"
# create an instance of BankingDirectDebit from a JSON string
banking_direct_debit_instance = BankingDirectDebit.from_json(json)
# print the JSON string representation of the object
print BankingDirectDebit.to_json()

# convert the object into a dict
banking_direct_debit_dict = banking_direct_debit_instance.to_dict()
# create an instance of BankingDirectDebit from a dict
banking_direct_debit_form_dict = banking_direct_debit.from_dict(banking_direct_debit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


