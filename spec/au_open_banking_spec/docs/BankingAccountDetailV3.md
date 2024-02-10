# BankingAccountDetailV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | A unique ID of the account adhering to the standards for ID permanence | 
**creation_date** | **str** | Date that the account was created (if known) | [optional] 
**display_name** | **str** | The display name of the account as defined by the bank. This should not incorporate account numbers or PANs. If it does the values should be masked according to the rules of the MaskedAccountString common type. | 
**nickname** | **str** | A customer supplied nick name for the account | [optional] 
**open_status** | **str** | Open or closed status for the account. If not present then OPEN is assumed | [optional] [default to 'OPEN']
**is_owned** | **bool** | Flag indicating that the customer associated with the authorisation is an owner of the account. Does not indicate sole ownership, however. If not present then &#39;true&#39; is assumed | [optional] [default to True]
**account_ownership** | **str** | Value indicating the number of customers that have ownership of the account, according to the data holder&#39;s definition of account ownership. Does not indicate that all account owners are eligible consumers | 
**masked_number** | **str** | A masked version of the account. Whether BSB/Account Number, Credit Card PAN or another number | 
**product_category** | [**BankingProductCategory**](BankingProductCategory.md) |  | 
**product_name** | **str** | The unique identifier of the account as defined by the data holder (akin to model number for the account) | 
**bsb** | **str** | The unmasked BSB for the account. Is expected to be formatted as digits only with leading zeros included and no punctuation or spaces | [optional] 
**account_number** | **str** | The unmasked account number for the account. Should not be supplied if the account number is a PAN requiring PCI compliance. Is expected to be formatted as digits only with leading zeros included and no punctuation or spaces | [optional] 
**bundle_name** | **str** | Optional field to indicate if this account is part of a bundle that is providing additional benefit to the customer | [optional] 
**specific_account_u_type** | **str** | The type of structure to present account specific fields. | [optional] 
**term_deposit** | [**List[BankingTermDepositAccount]**](BankingTermDepositAccount.md) |  | [optional] 
**credit_card** | [**BankingCreditCardAccount**](BankingCreditCardAccount.md) |  | [optional] 
**loan** | [**BankingLoanAccountV2**](BankingLoanAccountV2.md) |  | [optional] 
**deposit_rate** | **str** | current rate to calculate interest earned being applied to deposit balances as it stands at the time of the API call | [optional] 
**lending_rate** | **str** | The current rate to calculate interest payable being applied to lending balances as it stands at the time of the API call | [optional] 
**deposit_rates** | [**List[BankingProductDepositRate]**](BankingProductDepositRate.md) | Fully described deposit rates for this account based on the equivalent structure in Product Reference | [optional] 
**lending_rates** | [**List[BankingProductLendingRateV2]**](BankingProductLendingRateV2.md) | Fully described lending rates for this account based on the equivalent structure in Product Reference | [optional] 
**features** | [**List[BankingAccountDetailV3AllOfFeaturesInner]**](BankingAccountDetailV3AllOfFeaturesInner.md) | Array of features of the account based on the equivalent structure in Product Reference with the following additional field | [optional] 
**fees** | [**List[BankingProductFee]**](BankingProductFee.md) | Fees and charges applicable to the account based on the equivalent structure in Product Reference | [optional] 
**addresses** | [**List[CommonPhysicalAddress]**](CommonPhysicalAddress.md) | The addresses for the account to be used for correspondence | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_account_detail_v3 import BankingAccountDetailV3

# TODO update the JSON string below
json = "{}"
# create an instance of BankingAccountDetailV3 from a JSON string
banking_account_detail_v3_instance = BankingAccountDetailV3.from_json(json)
# print the JSON string representation of the object
print BankingAccountDetailV3.to_json()

# convert the object into a dict
banking_account_detail_v3_dict = banking_account_detail_v3_instance.to_dict()
# create an instance of BankingAccountDetailV3 from a dict
banking_account_detail_v3_form_dict = banking_account_detail_v3.from_dict(banking_account_detail_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


