# BankingPayeeDetailV2AllOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_u_type** | **str** | Type of object included that describes the payee in detail | 
**biller** | [**BankingBillerPayee**](BankingBillerPayee.md) |  | [optional] 
**domestic** | [**BankingDomesticPayee**](BankingDomesticPayee.md) |  | [optional] 
**digital_wallet** | [**BankingDigitalWalletPayee**](BankingDigitalWalletPayee.md) |  | [optional] 
**international** | [**BankingInternationalPayee**](BankingInternationalPayee.md) |  | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_payee_detail_v2_all_of import BankingPayeeDetailV2AllOf

# TODO update the JSON string below
json = "{}"
# create an instance of BankingPayeeDetailV2AllOf from a JSON string
banking_payee_detail_v2_all_of_instance = BankingPayeeDetailV2AllOf.from_json(json)
# print the JSON string representation of the object
print BankingPayeeDetailV2AllOf.to_json()

# convert the object into a dict
banking_payee_detail_v2_all_of_dict = banking_payee_detail_v2_all_of_instance.to_dict()
# create an instance of BankingPayeeDetailV2AllOf from a dict
banking_payee_detail_v2_all_of_form_dict = banking_payee_detail_v2_all_of.from_dict(banking_payee_detail_v2_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


