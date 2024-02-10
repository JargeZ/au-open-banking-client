# ResponseBankingPayeeByIdV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BankingPayeeDetailV2**](BankingPayeeDetailV2.md) |  | 
**links** | [**Links**](Links.md) |  | 
**meta** | **object** |  | [optional] 

## Example

```python
from au_open_banking_spec.models.response_banking_payee_by_id_v2 import ResponseBankingPayeeByIdV2

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingPayeeByIdV2 from a JSON string
response_banking_payee_by_id_v2_instance = ResponseBankingPayeeByIdV2.from_json(json)
# print the JSON string representation of the object
print ResponseBankingPayeeByIdV2.to_json()

# convert the object into a dict
response_banking_payee_by_id_v2_dict = response_banking_payee_by_id_v2_instance.to_dict()
# create an instance of ResponseBankingPayeeByIdV2 from a dict
response_banking_payee_by_id_v2_form_dict = response_banking_payee_by_id_v2.from_dict(response_banking_payee_by_id_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


