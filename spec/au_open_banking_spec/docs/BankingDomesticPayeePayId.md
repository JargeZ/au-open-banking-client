# BankingDomesticPayeePayId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name assigned to the PayID by the owner of the PayID | [optional] 
**identifier** | **str** | The identifier of the PayID (dependent on type) | 
**type** | **str** | The type of the PayID | 

## Example

```python
from au_open_banking_spec.models.banking_domestic_payee_pay_id import BankingDomesticPayeePayId

# TODO update the JSON string below
json = "{}"
# create an instance of BankingDomesticPayeePayId from a JSON string
banking_domestic_payee_pay_id_instance = BankingDomesticPayeePayId.from_json(json)
# print the JSON string representation of the object
print BankingDomesticPayeePayId.to_json()

# convert the object into a dict
banking_domestic_payee_pay_id_dict = banking_domestic_payee_pay_id_instance.to_dict()
# create an instance of BankingDomesticPayeePayId from a dict
banking_domestic_payee_pay_id_form_dict = banking_domestic_payee_pay_id.from_dict(banking_domestic_payee_pay_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


