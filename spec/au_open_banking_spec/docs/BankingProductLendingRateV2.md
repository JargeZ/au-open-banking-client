# BankingProductLendingRateV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lending_rate_type** | **str** | The type of rate (fixed, variable, etc). See the next section for an overview of valid values and their meaning | 
**rate** | **str** | The rate to be applied | 
**comparison_rate** | **str** | A comparison rate equivalent for this rate | [optional] 
**calculation_frequency** | **str** | The period after which the rate is applied to the balance to calculate the amount due for the period. Calculation of the amount is often daily (as balances may change) but accumulated until the total amount is &#39;applied&#39; to the account (see applicationFrequency). Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 
**application_frequency** | **str** | The period after which the calculated amount(s) (see calculationFrequency) are &#39;applied&#39; (i.e. debited or credited) to the account. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 
**interest_payment_due** | **str** | When loan payments are due to be paid within each period. The investment benefit of earlier payments affect the rate that can be offered | [optional] 
**repayment_type** | **str** | Options in place for repayments. If absent, the lending rate is applicable to all repayment types | [optional] 
**loan_purpose** | **str** | The reason for taking out the loan. If absent, the lending rate is applicable to all loan purposes | [optional] 
**tiers** | [**List[BankingProductRateTierV3]**](BankingProductRateTierV3.md) | Rate tiers applicable for this rate | [optional] 
**additional_value** | **str** | Generic field containing additional information relevant to the [lendingRateType](#tocSproductlendingratetypedoc) specified. Whether mandatory or not is dependent on the value of [lendingRateType](#tocSproductlendingratetypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the rate. | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this rate | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_lending_rate_v2 import BankingProductLendingRateV2

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductLendingRateV2 from a JSON string
banking_product_lending_rate_v2_instance = BankingProductLendingRateV2.from_json(json)
# print the JSON string representation of the object
print BankingProductLendingRateV2.to_json()

# convert the object into a dict
banking_product_lending_rate_v2_dict = banking_product_lending_rate_v2_instance.to_dict()
# create an instance of BankingProductLendingRateV2 from a dict
banking_product_lending_rate_v2_form_dict = banking_product_lending_rate_v2.from_dict(banking_product_lending_rate_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


