# BankingProductRateTierV3

Defines the criteria and conditions for which a rate applies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A display name for the tier | 
**unit_of_measure** | **str** | The unit of measure that applies to the minimumValue and maximumValue values e.g. a **DOLLAR** amount. **PERCENT** (in the case of loan-to-value ratio or LVR). Tier term period representing a discrete number of **MONTH**&#39;s or **DAY**&#39;s (in the case of term deposit tiers) | 
**minimum_value** | **float** | The number of unitOfMeasure units that form the lower bound of the tier. The tier should be inclusive of this value | 
**maximum_value** | **float** | The number of unitOfMeasure units that form the upper bound of the tier or band. For a tier with a discrete value (as opposed to a range of values e.g. 1 month) this must be the same as minimumValue. Where this is the same as the minimumValue value of the next-higher tier the referenced tier should be exclusive of this value. For example a term deposit of 2 months falls into the upper tier of the following tiers: (1 – 2 months, 2 – 3 months). If absent the tier&#39;s range has no upper bound. | [optional] 
**rate_application_method** | **str** | The method used to calculate the amount to be applied using one or more tiers. A single rate may be applied to the entire balance or each applicable tier rate is applied to the portion of the balance that falls into that tier (referred to as &#39;bands&#39; or &#39;steps&#39;) | [optional] 
**applicability_conditions** | [**BankingProductRateCondition**](BankingProductRateCondition.md) |  | [optional] 
**additional_info** | **str** | Display text providing more information on the rate tier. | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this rate tier | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_rate_tier_v3 import BankingProductRateTierV3

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductRateTierV3 from a JSON string
banking_product_rate_tier_v3_instance = BankingProductRateTierV3.from_json(json)
# print the JSON string representation of the object
print BankingProductRateTierV3.to_json()

# convert the object into a dict
banking_product_rate_tier_v3_dict = banking_product_rate_tier_v3_instance.to_dict()
# create an instance of BankingProductRateTierV3 from a dict
banking_product_rate_tier_v3_form_dict = banking_product_rate_tier_v3.from_dict(banking_product_rate_tier_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


