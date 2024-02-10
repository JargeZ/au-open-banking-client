# BankingProductRateCondition

Defines a condition for the applicability of a tiered rate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_info** | **str** | Display text providing more information on the condition | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this condition | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_rate_condition import BankingProductRateCondition

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductRateCondition from a JSON string
banking_product_rate_condition_instance = BankingProductRateCondition.from_json(json)
# print the JSON string representation of the object
print BankingProductRateCondition.to_json()

# convert the object into a dict
banking_product_rate_condition_dict = banking_product_rate_condition_instance.to_dict()
# create an instance of BankingProductRateCondition from a dict
banking_product_rate_condition_form_dict = banking_product_rate_condition.from_dict(banking_product_rate_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


