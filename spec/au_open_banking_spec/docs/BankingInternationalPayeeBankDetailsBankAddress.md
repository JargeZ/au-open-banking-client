# BankingInternationalPayeeBankDetailsBankAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the recipient Bank | 
**address** | **str** | Address of the recipient Bank | 

## Example

```python
from au_open_banking_spec.models.banking_international_payee_bank_details_bank_address import BankingInternationalPayeeBankDetailsBankAddress

# TODO update the JSON string below
json = "{}"
# create an instance of BankingInternationalPayeeBankDetailsBankAddress from a JSON string
banking_international_payee_bank_details_bank_address_instance = BankingInternationalPayeeBankDetailsBankAddress.from_json(json)
# print the JSON string representation of the object
print BankingInternationalPayeeBankDetailsBankAddress.to_json()

# convert the object into a dict
banking_international_payee_bank_details_bank_address_dict = banking_international_payee_bank_details_bank_address_instance.to_dict()
# create an instance of BankingInternationalPayeeBankDetailsBankAddress from a dict
banking_international_payee_bank_details_bank_address_form_dict = banking_international_payee_bank_details_bank_address.from_dict(banking_international_payee_bank_details_bank_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


