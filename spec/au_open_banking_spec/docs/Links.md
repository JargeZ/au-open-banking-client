# Links


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Fully qualified link that generated the current response document | 

## Example

```python
from au_open_banking_spec.models.links import Links

# TODO update the JSON string below
json = "{}"
# create an instance of Links from a JSON string
links_instance = Links.from_json(json)
# print the JSON string representation of the object
print Links.to_json()

# convert the object into a dict
links_dict = links_instance.to_dict()
# create an instance of Links from a dict
links_form_dict = links.from_dict(links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


