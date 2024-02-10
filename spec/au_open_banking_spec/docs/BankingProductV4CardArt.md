# BankingProductV4CardArt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Display label for the specific image | [optional] 
**image_uri** | **str** | URI reference to a PNG, JPG or GIF image with proportions defined by ISO 7810 ID-1 and width no greater than 512 pixels. The URI reference may be a link or url-encoded data URI according to **[[RFC2397]](#nref-RFC2397)** | 

## Example

```python
from au_open_banking_spec.models.banking_product_v4_card_art import BankingProductV4CardArt

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductV4CardArt from a JSON string
banking_product_v4_card_art_instance = BankingProductV4CardArt.from_json(json)
# print the JSON string representation of the object
print BankingProductV4CardArt.to_json()

# convert the object into a dict
banking_product_v4_card_art_dict = banking_product_v4_card_art_instance.to_dict()
# create an instance of BankingProductV4CardArt from a dict
banking_product_v4_card_art_form_dict = banking_product_v4_card_art.from_dict(banking_product_v4_card_art_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


