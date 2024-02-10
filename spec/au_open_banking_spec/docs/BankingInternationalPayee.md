# BankingInternationalPayee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beneficiary_details** | [**BankingInternationalPayeeBeneficiaryDetails**](BankingInternationalPayeeBeneficiaryDetails.md) |  | 
**bank_details** | [**BankingInternationalPayeeBankDetails**](BankingInternationalPayeeBankDetails.md) |  | 

## Example

```python
from au_open_banking_spec.models.banking_international_payee import BankingInternationalPayee

# TODO update the JSON string below
json = "{}"
# create an instance of BankingInternationalPayee from a JSON string
banking_international_payee_instance = BankingInternationalPayee.from_json(json)
# print the JSON string representation of the object
print BankingInternationalPayee.to_json()

# convert the object into a dict
banking_international_payee_dict = banking_international_payee_instance.to_dict()
# create an instance of BankingInternationalPayee from a dict
banking_international_payee_form_dict = banking_international_payee.from_dict(banking_international_payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


