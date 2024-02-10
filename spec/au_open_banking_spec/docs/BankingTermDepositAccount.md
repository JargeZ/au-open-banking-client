# BankingTermDepositAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lodgement_date** | **str** | The lodgement date of the original deposit | 
**maturity_date** | **str** | Maturity date for the term deposit | 
**maturity_amount** | **str** | Amount to be paid upon maturity. If absent it implies the amount to paid is variable and cannot currently be calculated | [optional] 
**maturity_currency** | **str** | If absent assumes AUD | [optional] 
**maturity_instructions** | **str** | Current instructions on action to be taken at maturity. This includes default actions that may be specified in the terms and conditions for the product e.g. roll-over to the same term and frequency of interest payments | 

## Example

```python
from au_open_banking_spec.models.banking_term_deposit_account import BankingTermDepositAccount

# TODO update the JSON string below
json = "{}"
# create an instance of BankingTermDepositAccount from a JSON string
banking_term_deposit_account_instance = BankingTermDepositAccount.from_json(json)
# print the JSON string representation of the object
print BankingTermDepositAccount.to_json()

# convert the object into a dict
banking_term_deposit_account_dict = banking_term_deposit_account_instance.to_dict()
# create an instance of BankingTermDepositAccount from a dict
banking_term_deposit_account_form_dict = banking_term_deposit_account.from_dict(banking_term_deposit_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


