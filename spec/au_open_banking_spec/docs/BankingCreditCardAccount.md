# BankingCreditCardAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_payment_amount** | **str** | The minimum payment amount due for the next card payment | 
**payment_due_amount** | **str** | The amount due for the next card payment | 
**payment_currency** | **str** | If absent assumes AUD | [optional] 
**payment_due_date** | **str** | Date that the next payment for the card is due | 

## Example

```python
from au_open_banking_spec.models.banking_credit_card_account import BankingCreditCardAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankingCreditCardAccount from a JSON string
banking_credit_card_account_instance = BankingCreditCardAccount.from_json(json)
# print the JSON string representation of the object
print BankingCreditCardAccount.to_json()

# convert the object into a dict
banking_credit_card_account_dict = banking_credit_card_account_instance.to_dict()
# create an instance of BankingCreditCardAccount from a dict
banking_credit_card_account_form_dict = banking_credit_card_account.from_dict(banking_credit_card_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


