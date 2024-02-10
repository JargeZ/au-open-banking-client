# BankingScheduledPaymentRecurrenceOnceOff

Indicates that the payment is a once off payment on a specific future date. Mandatory if recurrenceUType is set to onceOff

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_date** | **str** | The scheduled date for the once off payment | 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_recurrence_once_off import BankingScheduledPaymentRecurrenceOnceOff

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentRecurrenceOnceOff from a JSON string
banking_scheduled_payment_recurrence_once_off_instance = BankingScheduledPaymentRecurrenceOnceOff.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentRecurrenceOnceOff.to_json()

# convert the object into a dict
banking_scheduled_payment_recurrence_once_off_dict = banking_scheduled_payment_recurrence_once_off_instance.to_dict()
# create an instance of BankingScheduledPaymentRecurrenceOnceOff from a dict
banking_scheduled_payment_recurrence_once_off_form_dict = banking_scheduled_payment_recurrence_once_off.from_dict(banking_scheduled_payment_recurrence_once_off_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


