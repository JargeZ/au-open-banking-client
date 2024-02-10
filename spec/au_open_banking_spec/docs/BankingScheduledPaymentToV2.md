# BankingScheduledPaymentToV2

Object containing details of the destination of the payment. Used to specify a variety of payment destination types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_u_type** | **str** | The type of object provided that specifies the destination of the funds for the payment. | 
**account_id** | **str** | Present if toUType is set to accountId. Indicates that the payment is to another account that is accessible under the current consent | [optional] 
**payee_id** | **str** | Present if toUType is set to payeeId. Indicates that the payment is to registered payee that can be accessed using the payee end point. If the Bank Payees scope has not been consented to then a payeeId should not be provided and the full payee details should be provided instead | [optional] 
**nickname** | **str** | The short display name of the payee as provided by the customer unless toUType is set to payeeId. Where a customer has not provided a nickname, a display name derived by the bank for payee should be provided that is consistent with existing digital banking channels | [optional] 
**payee_reference** | **str** | The reference for the transaction, if applicable, that will be provided by the originating institution for the specific payment. If not empty, it overrides the value provided at the BankingScheduledPayment level. | [optional] 
**digital_wallet** | [**BankingDigitalWalletPayee**](BankingDigitalWalletPayee.md) |  | [optional] 
**domestic** | [**BankingDomesticPayee**](BankingDomesticPayee.md) |  | [optional] 
**biller** | [**BankingBillerPayee**](BankingBillerPayee.md) |  | [optional] 
**international** | [**BankingInternationalPayee**](BankingInternationalPayee.md) |  | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_scheduled_payment_to_v2 import BankingScheduledPaymentToV2

# TODO update the JSON string below
json = "{}"
# create an instance of BankingScheduledPaymentToV2 from a JSON string
banking_scheduled_payment_to_v2_instance = BankingScheduledPaymentToV2.from_json(json)
# print the JSON string representation of the object
print BankingScheduledPaymentToV2.to_json()

# convert the object into a dict
banking_scheduled_payment_to_v2_dict = banking_scheduled_payment_to_v2_instance.to_dict()
# create an instance of BankingScheduledPaymentToV2 from a dict
banking_scheduled_payment_to_v2_form_dict = banking_scheduled_payment_to_v2.from_dict(banking_scheduled_payment_to_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


