# BankingProductEligibility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility_type** | **str** | The type of eligibility criteria described.  See the next section for an overview of valid values and their meaning | 
**additional_value** | **str** | Generic field containing additional information relevant to the [eligibilityType](#tocSproducteligibilitytypedoc) specified. Whether mandatory or not is dependent on the value of [eligibilityType](#tocSproducteligibilitytypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the [eligibility](#tocSproducteligibilitytypedoc) criteria. Mandatory if the field is set to OTHER | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this eligibility criteria | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_eligibility import BankingProductEligibility

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductEligibility from a JSON string
banking_product_eligibility_instance = BankingProductEligibility.from_json(json)
# print the JSON string representation of the object
print BankingProductEligibility.to_json()

# convert the object into a dict
banking_product_eligibility_dict = banking_product_eligibility_instance.to_dict()
# create an instance of BankingProductEligibility from a dict
banking_product_eligibility_form_dict = banking_product_eligibility.from_dict(banking_product_eligibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


