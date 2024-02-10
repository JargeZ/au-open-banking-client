# CommonSimpleAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailing_name** | **str** | Name of the individual or business formatted for inclusion in an address used for physical mail | [optional] 
**address_line1** | **str** | First line of the standard address object | 
**address_line2** | **str** | Second line of the standard address object | [optional] 
**address_line3** | **str** | Third line of the standard address object | [optional] 
**postcode** | **str** | Mandatory for Australian addresses | [optional] 
**city** | **str** | Name of the city or locality | 
**state** | **str** | Free text if the country is not Australia. If country is Australia then must be one of the values defined by the [State Type Abbreviation](https://auspost.com.au/content/dam/auspost_corp/media/documents/australia-post-data-guide.pdf) in the PAF file format. NSW, QLD, VIC, NT, WA, SA, TAS, ACT, AAT | 
**country** | **str** | A valid [ISO 3166 Alpha-3](https://www.iso.org/iso-3166-country-codes.html) country code. Australia (AUS) is assumed if country is not present. | [optional] [default to 'AUS']

## Example

```python
from au_open_banking_spec.models.common_simple_address import CommonSimpleAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSimpleAddress from a JSON string
common_simple_address_instance = CommonSimpleAddress.from_json(json)
# print the JSON string representation of the object
print CommonSimpleAddress.to_json()

# convert the object into a dict
common_simple_address_dict = common_simple_address_instance.to_dict()
# create an instance of CommonSimpleAddress from a dict
common_simple_address_form_dict = common_simple_address.from_dict(common_simple_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


