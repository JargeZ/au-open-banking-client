# BankingPayeeDetailV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** | ID of the payee adhering to the rules of ID permanence | 
**nickname** | **str** | The short display name of the payee as provided by the customer. Where a customer has not provided a nickname, a display name derived by the bank for the payee consistent with existing digital banking channels | 
**description** | **str** | A description of the payee provided by the customer | [optional] 
**type** | **str** | The type of payee.&lt;br/&gt;DOMESTIC means a registered payee for domestic payments including NPP. &lt;br/&gt;INTERNATIONAL means a registered payee for international payments. &lt;br/&gt;BILLER means a registered payee for BPAY. &lt;br/&gt;DIGITAL_WALLET means a registered payee for a bank&#39;s digital wallet | 
**creation_date** | **str** | The date the payee was created by the customer | [optional] 
**payee_u_type** | **str** | Type of object included that describes the payee in detail | 
**biller** | [**BankingBillerPayee**](BankingBillerPayee.md) |  | [optional] 
**domestic** | [**BankingDomesticPayee**](BankingDomesticPayee.md) |  | [optional] 
**digital_wallet** | [**BankingDigitalWalletPayee**](BankingDigitalWalletPayee.md) |  | [optional] 
**international** | [**BankingInternationalPayee**](BankingInternationalPayee.md) |  | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_payee_detail_v2 import BankingPayeeDetailV2

# TODO update the JSON string below
json = "{}"
# create an instance of BankingPayeeDetailV2 from a JSON string
banking_payee_detail_v2_instance = BankingPayeeDetailV2.from_json(json)
# print the JSON string representation of the object
print BankingPayeeDetailV2.to_json()

# convert the object into a dict
banking_payee_detail_v2_dict = banking_payee_detail_v2_instance.to_dict()
# create an instance of BankingPayeeDetailV2 from a dict
banking_payee_detail_v2_form_dict = banking_payee_detail_v2.from_dict(banking_payee_detail_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


