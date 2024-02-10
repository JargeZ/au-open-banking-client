# BankingDigitalWalletPayee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The display name of the wallet as given by the customer, else a default value defined by the data holder | 
**identifier** | **str** | The identifier of the digital wallet (dependent on type) | 
**type** | **str** | The type of the digital wallet identifier | 
**provider** | **str** | The provider of the digital wallet | 

## Example

```python
from au_open_banking_spec.models.banking_digital_wallet_payee import BankingDigitalWalletPayee

# TODO update the JSON string below
json = "{}"
# create an instance of BankingDigitalWalletPayee from a JSON string
banking_digital_wallet_payee_instance = BankingDigitalWalletPayee.from_json(json)
# print the JSON string representation of the object
print BankingDigitalWalletPayee.to_json()

# convert the object into a dict
banking_digital_wallet_payee_dict = banking_digital_wallet_payee_instance.to_dict()
# create an instance of BankingDigitalWalletPayee from a dict
banking_digital_wallet_payee_form_dict = banking_digital_wallet_payee.from_dict(banking_digital_wallet_payee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


