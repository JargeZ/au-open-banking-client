# BankingScheduledPaymentFrom

Object containing details of the source of the payment. Currently only specifies an account ID but provided as an object to facilitate future extensibility and consistency with the to object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account that is the source of funds for the payment | 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_from import BankingScheduledPaymentFrom

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentFrom from a JSON string
banking_scheduled_payment_from_instance = BankingScheduledPaymentFrom.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentFrom.to_json()

# convert the object into a dict
banking_scheduled_payment_from_dict = banking_scheduled_payment_from_instance.to_dict()
# create an instance of BankingScheduledPaymentFrom from a dict
banking_scheduled_payment_from_form_dict = banking_scheduled_payment_from.from_dict(banking_scheduled_payment_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


