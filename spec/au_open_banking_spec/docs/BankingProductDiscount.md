# BankingProductDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the discount | 
**discount_type** | **str** | The type of discount. See the next section for an overview of valid values and their meaning | 
**amount** | **str** | Dollar value of the discount. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory. | [optional] 
**balance_rate** | **str** | A discount rate calculated based on a proportion of the balance. Note that the currency of the fee discount is expected to be the same as the currency of the fee itself. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory. Unless noted in additionalInfo, assumes the application and calculation frequency are the same as the corresponding fee | [optional] 
**transaction_rate** | **str** | A discount rate calculated based on a proportion of a transaction. Note that the currency of the fee discount is expected to be the same as the currency of the fee itself. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory | [optional] 
**accrued_rate** | **str** | A discount rate calculated based on a proportion of the calculated interest accrued on the account. Note that the currency of the fee discount is expected to be the same as the currency of the fee itself. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory. Unless noted in additionalInfo, assumes the application and calculation frequency are the same as the corresponding fee | [optional] 
**fee_rate** | **str** | A discount rate calculated based on a proportion of the fee to which this discount is attached. Note that the currency of the fee discount is expected to be the same as the currency of the fee itself. One of amount, balanceRate, transactionRate, accruedRate and feeRate is mandatory. Unless noted in additionalInfo, assumes the application and calculation frequency are the same as the corresponding fee | [optional] 
**additional_value** | **str** | Generic field containing additional information relevant to the [discountType](#tocSproductdiscounttypedoc) specified. Whether mandatory or not is dependent on the value of [discountType](#tocSproductdiscounttypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the discount | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this discount | [optional] 
**eligibility** | [**List[BankingProductDiscountEligibility]**](BankingProductDiscountEligibility.md) | Eligibility constraints that apply to this discount. Mandatory if &#x60;&#x60;discountType&#x60;&#x60; is &#x60;&#x60;ELIGIBILITY_ONLY&#x60;&#x60;. | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_discount import BankingProductDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductDiscount from a JSON string
banking_product_discount_instance = BankingProductDiscount.from_json(json)
# print the JSON string representation of the object
print BankingProductDiscount.to_json()

# convert the object into a dict
banking_product_discount_dict = banking_product_discount_instance.to_dict()
# create an instance of BankingProductDiscount from a dict
banking_product_discount_form_dict = banking_product_discount.from_dict(banking_product_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


