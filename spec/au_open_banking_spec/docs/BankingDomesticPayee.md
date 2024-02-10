# BankingDomesticPayee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_account_u_type** | **str** | Type of account object included. Valid values are: **account** A standard Australian account defined by BSB/Account Number. **card** A credit or charge card to pay to (note that PANs are masked). **payId** A PayID recognised by NPP | 
**account** | [**BankingDomesticPayeeAccount**](BankingDomesticPayeeAccount.md) |  | [optional] 
**card** | [**BankingDomesticPayeeCard**](BankingDomesticPayeeCard.md) |  | [optional] 
**pay_id** | [**BankingDomesticPayeePayId**](BankingDomesticPayeePayId.md) |  | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_domestic_payee import BankingDomesticPayee

# TODO update the JSON string below
json = "{}"
# create an instance of BankingDomesticPayee from a JSON string
banking_domestic_payee_instance = BankingDomesticPayee.from_json(json)
# print the JSON string representation of the object
print BankingDomesticPayee.to_json()

# convert the object into a dict
banking_domestic_payee_dict = banking_domestic_payee_instance.to_dict()
# create an instance of BankingDomesticPayee from a dict
banking_domestic_payee_form_dict = banking_domestic_payee.from_dict(banking_domestic_payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


