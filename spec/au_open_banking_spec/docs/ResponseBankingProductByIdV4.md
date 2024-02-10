# ResponseBankingProductByIdV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankingProductDetailV4**](BankingProductDetailV4.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | **object** |  | [optional] 

## Example

```python
from au_open_banking_spec.models.response_banking_product_by_id_v4 import ResponseBankingProductByIdV4

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingProductByIdV4 from a JSON string
response_banking_product_by_id_v4_instance = ResponseBankingProductByIdV4.from_json(json)
# print the JSON string representation of the object
print ResponseBankingProductByIdV4.to_json()

# convert the object into a dict
response_banking_product_by_id_v4_dict = response_banking_product_by_id_v4_instance.to_dict()
# create an instance of ResponseBankingProductByIdV4 from a dict
response_banking_product_by_id_v4_form_dict = response_banking_product_by_id_v4.from_dict(response_banking_product_by_id_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


