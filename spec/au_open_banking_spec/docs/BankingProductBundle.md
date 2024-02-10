# BankingProductBundle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the bundle | 
**description** | **str** | Description of the bundle | 
**additional_info** | **str** | Display text providing more information on the bundle | [optional] 
**additional_info_uri** | **str** | Link to a web page with more information on the bundle criteria and benefits | [optional] 
**product_ids** | **List[str]** | Array of product IDs for products included in the bundle that are available via the product end points.  Note that this array is not intended to represent a comprehensive model of the products included in the bundle and some products available for the bundle may not be available via the product reference end points | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_bundle import BankingProductBundle

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductBundle from a JSON string
banking_product_bundle_instance = BankingProductBundle.from_json(json)
# print the JSON string representation of the object
print BankingProductBundle.to_json()

# convert the object into a dict
banking_product_bundle_dict = banking_product_bundle_instance.to_dict()
# create an instance of BankingProductBundle from a dict
banking_product_bundle_form_dict = banking_product_bundle.from_dict(banking_product_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


