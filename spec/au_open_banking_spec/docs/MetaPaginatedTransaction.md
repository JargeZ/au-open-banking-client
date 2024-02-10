# MetaPaginatedTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_records** | **int** | The total number of records in the full set. See [pagination](#pagination). | 
**total_pages** | **int** | The total number of pages in the full set. See [pagination](#pagination). | 
**is_query_param_unsupported** | **bool** | **true** if *\&quot;text\&quot;* query parameter is not supported | [optional] [default to False]

## Example

```python
from au_open_banking_spec.models.meta_paginated_transaction import MetaPaginatedTransaction

# TODO update the JSON string below
json = "{}"
# create an instance of MetaPaginatedTransaction from a JSON string
meta_paginated_transaction_instance = MetaPaginatedTransaction.from_json(json)
# print the JSON string representation of the object
print MetaPaginatedTransaction.to_json()

# convert the object into a dict
meta_paginated_transaction_dict = meta_paginated_transaction_instance.to_dict()
# create an instance of MetaPaginatedTransaction from a dict
meta_paginated_transaction_form_dict = meta_paginated_transaction.from_dict(meta_paginated_transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


