# BankingBalancePurse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | The balance available for this additional currency purse | 
**currency** | **str** | The currency for the purse | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_balance_purse import BankingBalancePurse

# TODO update the JSON string below
json = "{}"
# create an instance of BankingBalancePurse from a JSON string
banking_balance_purse_instance = BankingBalancePurse.from_json(json)
# print the JSON string representation of the object
print BankingBalancePurse.to_json()

# convert the object into a dict
banking_balance_purse_dict = banking_balance_purse_instance.to_dict()
# create an instance of BankingBalancePurse from a dict
banking_balance_purse_form_dict = banking_balance_purse.from_dict(banking_balance_purse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


