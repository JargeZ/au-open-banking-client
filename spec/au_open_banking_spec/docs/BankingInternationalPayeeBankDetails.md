# BankingInternationalPayeeBankDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | Country of the recipient institution. A valid [ISO 3166 Alpha-3](https://www.iso.org/iso-3166-country-codes.html) country code | 
**account_number** | **str** | Account Targeted for payment | 
**bank_address** | [**BankingInternationalPayeeBankDetailsBankAddress**](BankingInternationalPayeeBankDetailsBankAddress.md) |  | [optional] 
**beneficiary_bank_bic** | **str** | Swift bank code.  Aligns with standard [ISO 9362](https://www.iso.org/standard/60390.html) | [optional] 
**fed_wire_number** | **str** | Number for Fedwire payment (Federal Reserve Wire Network) | [optional] 
**sort_code** | **str** | Sort code used for account identification in some jurisdictions | [optional] 
**chip_number** | **str** | Number for the Clearing House Interbank Payments System | [optional] 
**routing_number** | **str** | International bank routing number | [optional] 
**legal_entity_identifier** | **str** | The legal entity identifier (LEI) for the beneficiary.  Aligns with [ISO 17442](https://www.iso.org/standard/59771.html) | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_international_payee_bank_details import BankingInternationalPayeeBankDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BankingInternationalPayeeBankDetails from a JSON string
banking_international_payee_bank_details_instance = BankingInternationalPayeeBankDetails.from_json(json)
# print the JSON string representation of the object
print BankingInternationalPayeeBankDetails.to_json()

# convert the object into a dict
banking_international_payee_bank_details_dict = banking_international_payee_bank_details_instance.to_dict()
# create an instance of BankingInternationalPayeeBankDetails from a dict
banking_international_payee_bank_details_form_dict = banking_international_payee_bank_details.from_dict(banking_international_payee_bank_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


