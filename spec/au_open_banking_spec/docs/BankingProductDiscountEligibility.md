# BankingProductDiscountEligibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_eligibility_type** | **str** | The type of the specific eligibility constraint for a discount | 
**additional_value** | **str** | Generic field containing additional information relevant to the [discountEligibilityType](#tocSproductdiscounteligibilitydoc) specified. Whether mandatory or not is dependent on the value of [discountEligibilityType](#tocSproductdiscounteligibilitydoc) | [optional] 
**additional_info** | **str** | Display text providing more information on this eligibility constraint. Whether mandatory or not is dependent on the value of [discountEligibilityType](#tocSproductdiscounteligibilitydoc) | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this eligibility constraint | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_discount_eligibility import BankingProductDiscountEligibility

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductDiscountEligibility from a JSON string
banking_product_discount_eligibility_instance = BankingProductDiscountEligibility.from_json(json)
# print the JSON string representation of the object
print BankingProductDiscountEligibility.to_json()

# convert the object into a dict
banking_product_discount_eligibility_dict = banking_product_discount_eligibility_instance.to_dict()
# create an instance of BankingProductDiscountEligibility from a dict
banking_product_discount_eligibility_form_dict = banking_product_discount_eligibility.from_dict(banking_product_discount_eligibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


