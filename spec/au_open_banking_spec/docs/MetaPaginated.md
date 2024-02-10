# MetaPaginated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_records** | **int** | The total number of records in the full set. See [pagination](#pagination). | 
**total_pages** | **int** | The total number of pages in the full set. See [pagination](#pagination). | 

## Example

```python
from au_open_banking_spec.models.meta_paginated import MetaPaginated

# TODO update the JSON string below
json = "{}"
# create an instance of MetaPaginated from a JSON string
meta_paginated_instance = MetaPaginated.from_json(json)
# print the JSON string representation of the object
print MetaPaginated.to_json()

# convert the object into a dict
meta_paginated_dict = meta_paginated_instance.to_dict()
# create an instance of MetaPaginated from a dict
meta_paginated_form_dict = meta_paginated.from_dict(meta_paginated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


