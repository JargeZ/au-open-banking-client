# BankingScheduledPaymentRecurrenceEventBased

Indicates that the schedule of payments is defined according to an external event that cannot be predetermined. Mandatory if recurrenceUType is set to eventBased

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the event and conditions that will result in the payment. Expected to be formatted for display to a customer | 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_recurrence_event_based import BankingScheduledPaymentRecurrenceEventBased

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentRecurrenceEventBased from a JSON string
banking_scheduled_payment_recurrence_event_based_instance = BankingScheduledPaymentRecurrenceEventBased.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentRecurrenceEventBased.to_json()

# convert the object into a dict
banking_scheduled_payment_recurrence_event_based_dict = banking_scheduled_payment_recurrence_event_based_instance.to_dict()
# create an instance of BankingScheduledPaymentRecurrenceEventBased from a dict
banking_scheduled_payment_recurrence_event_based_form_dict = banking_scheduled_payment_recurrence_event_based.from_dict(banking_scheduled_payment_recurrence_event_based_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


