# CommonPAFAddress

Australian address formatted according to the file format defined by the [PAF file format](https://auspost.com.au/content/dam/auspost_corp/media/documents/australia-post-data-guide.pdf)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dpid** | **str** | Unique identifier for an address as defined by Australia Post.  Also known as Delivery Point Identifier | [optional] 
**thoroughfare_number1** | **int** | Thoroughfare number for a property (first number in a property ranged address) | [optional] 
**thoroughfare_number1_suffix** | **str** | Suffix for the thoroughfare number. Only relevant is thoroughfareNumber1 is populated | [optional] 
**thoroughfare_number2** | **int** | Second thoroughfare number (only used if the property has a ranged address eg 23-25) | [optional] 
**thoroughfare_number2_suffix** | **str** | Suffix for the second thoroughfare number. Only relevant is thoroughfareNumber2 is populated | [optional] 
**flat_unit_type** | **str** | Type of flat or unit for the address | [optional] 
**flat_unit_number** | **str** | Unit number (including suffix, if applicable) | [optional] 
**floor_level_type** | **str** | Type of floor or level for the address | [optional] 
**floor_level_number** | **str** | Floor or level number (including alpha characters) | [optional] 
**lot_number** | **str** | Allotment number for the address | [optional] 
**building_name1** | **str** | Building/Property name 1 | [optional] 
**building_name2** | **str** | Building/Property name 2 | [optional] 
**street_name** | **str** | The name of the street | [optional] 
**street_type** | **str** | The street type. Valid enumeration defined by Australia Post PAF code file | [optional] 
**street_suffix** | **str** | The street type suffix. Valid enumeration defined by Australia Post PAF code file | [optional] 
**postal_delivery_type** | **str** | Postal delivery type. (eg. PO BOX). Valid enumeration defined by Australia Post PAF code file | [optional] 
**postal_delivery_number** | **int** | Postal delivery number if the address is a postal delivery type | [optional] 
**postal_delivery_number_prefix** | **str** | Postal delivery number prefix related to the postal delivery number | [optional] 
**postal_delivery_number_suffix** | **str** | Postal delivery number suffix related to the postal delivery number | [optional] 
**locality_name** | **str** | Full name of locality | 
**postcode** | **str** | Postcode for the locality | 
**state** | **str** | State in which the address belongs. Valid enumeration defined by Australia Post PAF code file [State Type Abbreviation](https://auspost.com.au/content/dam/auspost_corp/media/documents/australia-post-data-guide.pdf). NSW, QLD, VIC, NT, WA, SA, TAS, ACT, AAT | 

## Example

```python
from au_open_banking_spec.models.common_paf_address import CommonPAFAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CommonPAFAddress from a JSON string
common_paf_address_instance = CommonPAFAddress.from_json(json)
# print the JSON string representation of the object
print CommonPAFAddress.to_json()

# convert the object into a dict
common_paf_address_dict = common_paf_address_instance.to_dict()
# create an instance of CommonPAFAddress from a dict
common_paf_address_form_dict = common_paf_address.from_dict(common_paf_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


