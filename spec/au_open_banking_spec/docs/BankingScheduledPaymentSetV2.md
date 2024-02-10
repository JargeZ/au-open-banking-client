# BankingScheduledPaymentSetV2

The set of payment amounts and destination accounts for this payment accommodating multi-part payments. A single entry indicates a simple payment with one destination account. Must have at least one entry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to** | [**BankingScheduledPaymentToV2**](BankingScheduledPaymentToV2.md) |  | 
**is_amount_calculated** | **bool** | Flag indicating whether the amount of the payment is calculated based on the context of the event. For instance a payment to reduce the balance of a credit card to zero. If absent then false is assumed | [optional] 
**amount** | **str** | The amount of the next payment if known. Mandatory unless the isAmountCalculated field is set to true. Must be zero or positive if present | [optional] 
**currency** | **str** | The currency for the payment. AUD assumed if not present | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_set_v2 import BankingScheduledPaymentSetV2

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentSetV2 from a JSON string
banking_scheduled_payment_set_v2_instance = BankingScheduledPaymentSetV2.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentSetV2.to_json()

# convert the object into a dict
banking_scheduled_payment_set_v2_dict = banking_scheduled_payment_set_v2_instance.to_dict()
# create an instance of BankingScheduledPaymentSetV2 from a dict
banking_scheduled_payment_set_v2_form_dict = banking_scheduled_payment_set_v2.from_dict(banking_scheduled_payment_set_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


