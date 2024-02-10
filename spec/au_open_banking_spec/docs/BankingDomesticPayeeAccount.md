# BankingDomesticPayeeAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_name** | **str** | Name of the account to pay to | [optional] 
**bsb** | **str** | BSB of the account to pay to | 
**account_number** | **str** | Number of the account to pay to | 

## Example

```python
from au_open_banking_spec.models.banking_domestic_payee_account import BankingDomesticPayeeAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankingDomesticPayeeAccount from a JSON string
banking_domestic_payee_account_instance = BankingDomesticPayeeAccount.from_json(json)
# print the JSON string representation of the object
print BankingDomesticPayeeAccount.to_json()

# convert the object into a dict
banking_domestic_payee_account_dict = banking_domestic_payee_account_instance.to_dict()
# create an instance of BankingDomesticPayeeAccount from a dict
banking_domestic_payee_account_form_dict = banking_domestic_payee_account.from_dict(banking_domestic_payee_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


