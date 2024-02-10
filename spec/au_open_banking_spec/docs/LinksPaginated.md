# LinksPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Fully qualified link that generated the current response document | 
**first** | **str** | URI to the first page of this set. Mandatory if this response is not the first page | [optional] 
**prev** | **str** | URI to the previous page of this set. Mandatory if this response is not the first page | [optional] 
**next** | **str** | URI to the next page of this set. Mandatory if this response is not the last page | [optional] 
**last** | **str** | URI to the last page of this set. Mandatory if this response is not the last page | [optional] 

## Example

```python
from au_open_banking_spec.models.links_paginated import LinksPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of LinksPaginated from a JSON string
links_paginated_instance = LinksPaginated.from_json(json)
# print the JSON string representation of the object
print LinksPaginated.to_json()

# convert the object into a dict
links_paginated_dict = links_paginated_instance.to_dict()
# create an instance of LinksPaginated from a dict
links_paginated_form_dict = links_paginated.from_dict(links_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


