# BankingAccountDetailV3AllOfFeaturesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_type** | **str** | The type of feature described | 
**additional_value** | **str** | Generic field containing additional information relevant to the [featureType](#tocSproductfeaturetypedoc) specified. Whether mandatory or not is dependent on the value of the [featureType.](#tocSproductfeaturetypedoc) | [optional] 
**additional_info** | **str** | Display text providing more information on the feature. Mandatory if the [feature type](#tocSproductfeaturetypedoc) is set to OTHER | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on this feature | [optional] 
**is_activated** | **bool** | True if the feature is already activated and false if the feature is available for activation. Defaults to true if absent. (note this is an additional field appended to the feature object defined in the Product Reference payload) | [optional] [default to True]

## Example

```python
from au_open_banking_spec.models.banking_account_detail_v3_all_of_features_inner import BankingAccountDetailV3AllOfFeaturesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BankingAccountDetailV3AllOfFeaturesInner from a JSON string
banking_account_detail_v3_all_of_features_inner_instance = BankingAccountDetailV3AllOfFeaturesInner.from_json(json)
# print the JSON string representation of the object
print BankingAccountDetailV3AllOfFeaturesInner.to_json()

# convert the object into a dict
banking_account_detail_v3_all_of_features_inner_dict = banking_account_detail_v3_all_of_features_inner_instance.to_dict()
# create an instance of BankingAccountDetailV3AllOfFeaturesInner from a dict
banking_account_detail_v3_all_of_features_inner_form_dict = banking_account_detail_v3_all_of_features_inner.from_dict(banking_account_detail_v3_all_of_features_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


