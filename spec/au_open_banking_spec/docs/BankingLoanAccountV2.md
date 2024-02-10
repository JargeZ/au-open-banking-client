# BankingLoanAccountV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_start_date** | **str** | Optional original start date for the loan | [optional] 
**original_loan_amount** | **str** | Optional original loan value | [optional] 
**original_loan_currency** | **str** | If absent assumes AUD | [optional] 
**loan_end_date** | **str** | Date that the loan is due to be repaid in full | [optional] 
**next_instalment_date** | **str** | Next date that an instalment is required | [optional] 
**min_instalment_amount** | **str** | Minimum amount of next instalment | [optional] 
**min_instalment_currency** | **str** | If absent assumes AUD | [optional] 
**max_redraw** | **str** | Maximum amount of funds that can be redrawn. If not present redraw is not available even if the feature exists for the account | [optional] 
**max_redraw_currency** | **str** | If absent assumes AUD | [optional] 
**min_redraw** | **str** | Minimum redraw amount | [optional] 
**min_redraw_currency** | **str** | If absent assumes AUD | [optional] 
**offset_account_enabled** | **bool** | Set to true if one or more offset accounts are configured for this loan account | [optional] 
**offset_account_ids** | **List[str]** | The accountIDs of the configured offset accounts attached to this loan. Only offset accounts that can be accessed under the current authorisation should be included. It is expected behaviour that offsetAccountEnabled is set to true but the offsetAccountIds field is absent or empty. This represents a situation where an offset account exists but details can not be accessed under the current authorisation | [optional] 
**repayment_type** | **str** | Options in place for repayments. If absent defaults to PRINCIPAL_AND_INTEREST | [optional] [default to 'PRINCIPAL_AND_INTEREST']
**repayment_frequency** | **str** | The expected or required repayment frequency. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_loan_account_v2 import BankingLoanAccountV2

# TODO update the JSON string below
json = "{}"
# create an instance of BankingLoanAccountV2 from a JSON string
banking_loan_account_v2_instance = BankingLoanAccountV2.from_json(json)
# print the JSON string representation of the object
print BankingLoanAccountV2.to_json()

# convert the object into a dict
banking_loan_account_v2_dict = banking_loan_account_v2_instance.to_dict()
# create an instance of BankingLoanAccountV2 from a dict
banking_loan_account_v2_form_dict = banking_loan_account_v2.from_dict(banking_loan_account_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


