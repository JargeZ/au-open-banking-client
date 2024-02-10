# BankingBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | A unique ID of the account adhering to the standards for ID permanence | 
**current_balance** | **str** | The balance of the account at this time. Should align to the balance available via other channels such as Internet Banking. Assumed to be negative if the customer has money owing | 
**available_balance** | **str** | Balance representing the amount of funds available for transfer. Assumed to be zero or positive | 
**credit_limit** | **str** | Object representing the maximum amount of credit that is available for this account. Assumed to be zero if absent | [optional] 
**amortised_limit** | **str** | Object representing the available limit amortised according to payment schedule. Assumed to be zero if absent | [optional] 
**currency** | **str** | The currency for the balance amounts. If absent assumed to be AUD | [optional] 
**purses** | [**List[BankingBalancePurse]**](BankingBalancePurse.md) | Optional array of balances for the account in other currencies. Included to support accounts that support multi-currency purses such as Travel Cards | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_balance import BankingBalance

# TODO update the JSON string below
json = "{}"
# create an instance of BankingBalance from a JSON string
banking_balance_instance = BankingBalance.from_json(json)
# print the JSON string representation of the object
print BankingBalance.to_json()

# convert the object into a dict
banking_balance_dict = banking_balance_instance.to_dict()
# create an instance of BankingBalance from a dict
banking_balance_form_dict = banking_balance.from_dict(banking_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


