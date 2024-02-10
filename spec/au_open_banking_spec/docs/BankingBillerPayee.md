# BankingBillerPayee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biller_code** | **str** | BPAY Biller Code of the Biller | 
**crn** | **str** | BPAY CRN of the Biller (if available).&lt;br/&gt;Where the CRN contains sensitive information, it should be masked in line with how the Data Holder currently displays account identifiers in their existing online banking channels. If the contents of the CRN match the format of a Credit Card PAN they should be masked according to the rules applicable for MaskedPANString. If the contents are otherwise sensitive, then it should be masked using the rules applicable for the MaskedAccountString common type. | [optional] 
**biller_name** | **str** | Name of the Biller | 

## Example

```python
from au_open_banking_spec.models.banking_biller_payee import BankingBillerPayee

# TODO update the JSON string below
json = "{}"
# create an instance of BankingBillerPayee from a JSON string
banking_biller_payee_instance = BankingBillerPayee.from_json(json)
# print the JSON string representation of the object
print BankingBillerPayee.to_json()

# convert the object into a dict
banking_biller_payee_dict = banking_biller_payee_instance.to_dict()
# create an instance of BankingBillerPayee from a dict
banking_biller_payee_form_dict = banking_biller_payee.from_dict(banking_biller_payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


