# BankingScheduledPaymentRecurrence

Object containing the detail of the schedule for the payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_payment_date** | **str** | The date of the next payment under the recurrence schedule | [optional] 
**recurrence_u_type** | **str** | The type of recurrence used to define the schedule | 
**once_off** | [**BankingScheduledPaymentRecurrenceOnceOff**](BankingScheduledPaymentRecurrenceOnceOff.md) |  | [optional] 
**interval_schedule** | [**BankingScheduledPaymentRecurrenceIntervalSchedule**](BankingScheduledPaymentRecurrenceIntervalSchedule.md) |  | [optional] 
**last_week_day** | [**BankingScheduledPaymentRecurrenceLastWeekday**](BankingScheduledPaymentRecurrenceLastWeekday.md) |  | [optional] 
**event_based** | [**BankingScheduledPaymentRecurrenceEventBased**](BankingScheduledPaymentRecurrenceEventBased.md) |  | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_recurrence import BankingScheduledPaymentRecurrence

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentRecurrence from a JSON string
banking_scheduled_payment_recurrence_instance = BankingScheduledPaymentRecurrence.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentRecurrence.to_json()

# convert the object into a dict
banking_scheduled_payment_recurrence_dict = banking_scheduled_payment_recurrence_instance.to_dict()
# create an instance of BankingScheduledPaymentRecurrence from a dict
banking_scheduled_payment_recurrence_form_dict = banking_scheduled_payment_recurrence.from_dict(banking_scheduled_payment_recurrence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


