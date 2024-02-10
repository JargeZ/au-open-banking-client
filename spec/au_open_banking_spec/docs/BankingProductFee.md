# BankingProductFee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the fee | 
**fee_type** | **str** | The type of fee | 
**amount** | **str** | The amount charged for the fee. One of amount, balanceRate, transactionRate and accruedRate is mandatory unless the *feeType* \&quot;VARIABLE\&quot; is supplied | [optional] 
**balance_rate** | **str** | A fee rate calculated based on a proportion of the balance. One of amount, balanceRate, transactionRate and accruedRate is mandatory unless the *feeType* \&quot;VARIABLE\&quot; is supplied. | [optional] 
**transaction_rate** | **str** | A fee rate calculated based on a proportion of a transaction. One of amount, balanceRate, transactionRate and accruedRate is mandatory unless the *feeType* \&quot;VARIABLE\&quot; is supplied | [optional] 
**accrued_rate** | **str** | A fee rate calculated based on a proportion of the calculated interest accrued on the account. One of amount, balanceRate, transactionRate and accruedRate is mandatory unless the *feeType* \&quot;VARIABLE\&quot; is supplied | [optional] 
**accrual_frequency** | **str** | The indicative frequency with which the fee is calculated on the account. Only applies if balanceRate or accruedRate is also present. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 
**currency** | **str** | The currency the fee will be charged in. Assumes AUD if absent | [optional] 
**additional_value** | **str** | Generic field containing additional information relevant to the [feeType](#tocSproductfeetypedoc) specified. Whether mandatory or not is dependent on the value of [feeType](#tocSproductfeetypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the fee | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this fee | [optional] 
**discounts** | [**List[BankingProductDiscount]**](BankingProductDiscount.md) | An optional list of discounts to this fee that may be available | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_fee import BankingProductFee

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductFee from a JSON string
banking_product_fee_instance = BankingProductFee.from_json(json)
# print the JSON string representation of the object
print BankingProductFee.to_json()

# convert the object into a dict
banking_product_fee_dict = banking_product_fee_instance.to_dict()
# create an instance of BankingProductFee from a dict
banking_product_fee_form_dict = banking_product_fee.from_dict(banking_product_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


