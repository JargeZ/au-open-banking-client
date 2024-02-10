# BankingScheduledPaymentV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_payment_id** | **str** | A unique ID of the scheduled payment adhering to the standards for ID permanence | 
**nickname** | **str** | The short display name of the scheduled payment as provided by the customer if provided. Where a customer has not provided a nickname, a display name derived by the bank for the scheduled payment should be provided that is consistent with existing digital banking channels | [optional] 
**payer_reference** | **str** | The reference for the transaction that will be used by the originating institution for the purposes of constructing a statement narrative on the payer’s account. Empty string if no data provided | 
**payee_reference** | **str** | The reference for the transaction, if applicable, that will be provided by the originating institution for all payments in the payment set. Empty string if no data provided | [optional] 
**status** | **str** | Indicates whether the schedule is currently active. The value SKIP is equivalent to ACTIVE except that the customer has requested the next normal occurrence to be skipped. | 
**var_from** | [**BankingScheduledPaymentFrom**](BankingScheduledPaymentFrom.md) |  | 
**payment_set** | [**List[BankingScheduledPaymentSetV2]**](BankingScheduledPaymentSetV2.md) |  | 
**recurrence** | [**BankingScheduledPaymentRecurrence**](BankingScheduledPaymentRecurrence.md) |  | 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_v2 import BankingScheduledPaymentV2

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentV2 from a JSON string
banking_scheduled_payment_v2_instance = BankingScheduledPaymentV2.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentV2.to_json()

# convert the object into a dict
banking_scheduled_payment_v2_dict = banking_scheduled_payment_v2_instance.to_dict()
# create an instance of BankingScheduledPaymentV2 from a dict
banking_scheduled_payment_v2_form_dict = banking_scheduled_payment_v2.from_dict(banking_scheduled_payment_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


