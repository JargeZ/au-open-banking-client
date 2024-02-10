# BankingScheduledPaymentRecurrenceIntervalSchedule

Indicates that the schedule of payments is defined by a series of intervals. Mandatory if recurrenceUType is set to intervalSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**final_payment_date** | **str** | The limit date after which no more payments should be made using this schedule. If both finalPaymentDate and paymentsRemaining are present then payments will stop according to the most constraining value. If neither field is present the payments will continue indefinitely | [optional] 
**payments_remaining** | **int** | Indicates the number of payments remaining in the schedule. If both finalPaymentDate and paymentsRemaining are present then payments will stop according to the most constraining value, If neither field is present the payments will continue indefinitely | [optional] 
**non_business_day_treatment** | **str** | Enumerated field giving the treatment where a scheduled payment date is not a business day. If absent assumed to be ON.&lt;br/&gt;**AFTER** - If a scheduled payment date is a non-business day the payment will be made on the first business day after the scheduled payment date.&lt;br/&gt;**BEFORE** - If a scheduled payment date is a non-business day the payment will be made on the first business day before the scheduled payment date.&lt;br/&gt;**ON** - If a scheduled payment date is a non-business day the payment will be made on that day regardless.&lt;br/&gt;**ONLY** - Payments only occur on business days. If a scheduled payment date is a non-business day the payment will be ignored | [optional] [default to 'ON']
**intervals** | [**List[BankingScheduledPaymentInterval]**](BankingScheduledPaymentInterval.md) | An array of interval objects defining the payment schedule.  Each entry in the array is additive, in that it adds payments to the overall payment schedule.  If multiple intervals result in a payment on the same day then only one payment will be made. Must have at least one entry | 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_recurrence_interval_schedule import BankingScheduledPaymentRecurrenceIntervalSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentRecurrenceIntervalSchedule from a JSON string
banking_scheduled_payment_recurrence_interval_schedule_instance = BankingScheduledPaymentRecurrenceIntervalSchedule.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentRecurrenceIntervalSchedule.to_json()

# convert the object into a dict
banking_scheduled_payment_recurrence_interval_schedule_dict = banking_scheduled_payment_recurrence_interval_schedule_instance.to_dict()
# create an instance of BankingScheduledPaymentRecurrenceIntervalSchedule from a dict
banking_scheduled_payment_recurrence_interval_schedule_form_dict = banking_scheduled_payment_recurrence_interval_schedule.from_dict(banking_scheduled_payment_recurrence_interval_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


