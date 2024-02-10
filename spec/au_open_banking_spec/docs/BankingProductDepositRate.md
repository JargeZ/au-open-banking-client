# BankingProductDepositRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deposit_rate_type** | **str** | The type of rate (base, bonus, etc). See the next section for an overview of valid values and their meaning | 
**rate** | **str** | The rate to be applied | 
**calculation_frequency** | **str** | The period after which the rate is applied to the balance to calculate the amount due for the period. Calculation of the amount is often daily (as balances may change) but accumulated until the total amount is &#39;applied&#39; to the account (see applicationFrequency). Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 
**application_frequency** | **str** | The period after which the calculated amount(s) (see calculationFrequency) are &#39;applied&#39; (i.e. debited or credited) to the account. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax) | [optional] 
**tiers** | [**List[BankingProductRateTierV3]**](BankingProductRateTierV3.md) | Rate tiers applicable for this rate | [optional] 
**additional_value** | **str** | Generic field containing additional information relevant to the [depositRateType](#tocSproductdepositratetypedoc) specified. Whether mandatory or not is dependent on the value of [depositRateType](#tocSproductdepositratetypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the rate | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this rate | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_deposit_rate import BankingProductDepositRate

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductDepositRate from a JSON string
banking_product_deposit_rate_instance = BankingProductDepositRate.from_json(json)
# print the JSON string representation of the object
print BankingProductDepositRate.to_json()

# convert the object into a dict
banking_product_deposit_rate_dict = banking_product_deposit_rate_instance.to_dict()
# create an instance of BankingProductDepositRate from a dict
banking_product_deposit_rate_form_dict = banking_product_deposit_rate.from_dict(banking_product_deposit_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


