# BankingDomesticPayeeCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Name of the account to pay to | 

## Example

```python
from au_open_banking_spec.models.banking_domestic_payee_card import BankingDomesticPayeeCard

# TODO update the JSON string below
json = "{}"
# create an instance of BankingDomesticPayeeCard from a JSON string
banking_domestic_payee_card_instance = BankingDomesticPayeeCard.from_json(json)
# print the JSON string representation of the object
print BankingDomesticPayeeCard.to_json()

# convert the object into a dict
banking_domestic_payee_card_dict = banking_domestic_payee_card_instance.to_dict()
# create an instance of BankingDomesticPayeeCard from a dict
banking_domestic_payee_card_form_dict = banking_domestic_payee_card.from_dict(banking_domestic_payee_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


