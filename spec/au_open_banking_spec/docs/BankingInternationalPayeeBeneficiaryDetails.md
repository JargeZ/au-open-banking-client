# BankingInternationalPayeeBeneficiaryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the beneficiary | [optional] 
**country** | **str** | Country where the beneficiary resides. A valid [ISO 3166 Alpha-3](https://www.iso.org/iso-3166-country-codes.html) country code | 
**message** | **str** | Response message for the payment | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_international_payee_beneficiary_details import BankingInternationalPayeeBeneficiaryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BankingInternationalPayeeBeneficiaryDetails from a JSON string
banking_international_payee_beneficiary_details_instance = BankingInternationalPayeeBeneficiaryDetails.from_json(json)
# print the JSON string representation of the object
print BankingInternationalPayeeBeneficiaryDetails.to_json()

# convert the object into a dict
banking_international_payee_beneficiary_details_dict = banking_international_payee_beneficiary_details_instance.to_dict()
# create an instance of BankingInternationalPayeeBeneficiaryDetails from a dict
banking_international_payee_beneficiary_details_form_dict = banking_international_payee_beneficiary_details.from_dict(banking_international_payee_beneficiary_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


