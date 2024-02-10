# BankingProductConstraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_type** | **str** | The type of constraint described.  See the next section for an overview of valid values and their meaning | 
**additional_value** | **str** | Generic field containing additional information relevant to the [constraintType](#tocSproductconstrainttypedoc) specified.  Whether mandatory or not is dependent on the value of [constraintType](#tocSproductconstrainttypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information the constraint | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on the constraint | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_constraint import BankingProductConstraint

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductConstraint from a JSON string
banking_product_constraint_instance = BankingProductConstraint.from_json(json)
# print the JSON string representation of the object
print BankingProductConstraint.to_json()

# convert the object into a dict
banking_product_constraint_dict = banking_product_constraint_instance.to_dict()
# create an instance of BankingProductConstraint from a dict
banking_product_constraint_form_dict = banking_product_constraint.from_dict(banking_product_constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


