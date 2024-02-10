# MetaPaginatedTransactionAllOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_query_param_unsupported** | **bool** | **true** if *\&quot;text\&quot;* query parameter is not supported | [optional] [default to False]

## Example

```python
from au_open_banking_spec.models.meta_paginated_transaction_all_of import MetaPaginatedTransactionAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of MetaPaginatedTransactionAllOf from a JSON string
meta_paginated_transaction_all_of_instance = MetaPaginatedTransactionAllOf.from_json(json)
# print the JSON string representation of the object
print MetaPaginatedTransactionAllOf.to_json()

# convert the object into a dict
meta_paginated_transaction_all_of_dict = meta_paginated_transaction_all_of_instance.to_dict()
# create an instance of MetaPaginatedTransactionAllOf from a dict
meta_paginated_transaction_all_of_form_dict = meta_paginated_transaction_all_of.from_dict(meta_paginated_transaction_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


