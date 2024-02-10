# BankingScheduledPaymentInterval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interval** | **str** | An interval for the payment. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)  (excludes recurrence syntax) with components less than a day in length ignored. This duration defines the period between payments starting with nextPaymentDate | 
**day_in_interval** | **str** | Uses an interval to define the ordinal day within the interval defined by the interval field on which the payment occurs. If the resulting duration is 0 days in length or larger than the number of days in the interval then the payment will occur on the last day of the interval. A duration of 1 day indicates the first day of the interval. If absent the assumed value is P1D. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) with components less than a day in length ignored. The first day of a week is considered to be Monday. | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_interval import BankingScheduledPaymentInterval

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentInterval from a JSON string
banking_scheduled_payment_interval_instance = BankingScheduledPaymentInterval.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentInterval.to_json()

# convert the object into a dict
banking_scheduled_payment_interval_dict = banking_scheduled_payment_interval_instance.to_dict()
# create an instance of BankingScheduledPaymentInterval from a dict
banking_scheduled_payment_interval_form_dict = banking_scheduled_payment_interval.from_dict(banking_scheduled_payment_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


