# BankingProductFeatureV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_type** | **str** | The type of feature described | 
**additional_value** | **str** | Generic field containing additional information relevant to the [featureType](#tocSproductfeaturetypedoc) specified. Whether mandatory or not is dependent on the value of the [featureType.](#tocSproductfeaturetypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the feature. Mandatory if the [feature type](#tocSproductfeaturetypedoc) is set to OTHER | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this feature | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_feature_v2 import BankingProductFeatureV2

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductFeatureV2 from a JSON string
banking_product_feature_v2_instance = BankingProductFeatureV2.from_json(json)
# print the JSON string representation of the object
print BankingProductFeatureV2.to_json()

# convert the object into a dict
banking_product_feature_v2_dict = banking_product_feature_v2_instance.to_dict()
# create an instance of BankingProductFeatureV2 from a dict
banking_product_feature_v2_form_dict = banking_product_feature_v2.from_dict(banking_product_feature_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


