# ResponseBankingDirectDebitAuthorisationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ResponseBankingDirectDebitAuthorisationListData**](ResponseBankingDirectDebitAuthorisationListData.md) |  | 
**links** | [**LinksPaginated**](LinksPaginated.md) |  | 
**meta** | [**MetaPaginated**](MetaPaginated.md) |  | 

## Example

```python
from au_open_banking_spec.models.response_banking_direct_debit_authorisation_list import ResponseBankingDirectDebitAuthorisationList

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingDirectDebitAuthorisationList from a JSON string
response_banking_direct_debit_authorisation_list_instance = ResponseBankingDirectDebitAuthorisationList.from_json(json)
# print the JSON string representation of the object
print ResponseBankingDirectDebitAuthorisationList.to_json()

# convert the object into a dict
response_banking_direct_debit_authorisation_list_dict = response_banking_direct_debit_authorisation_list_instance.to_dict()
# create an instance of ResponseBankingDirectDebitAuthorisationList from a dict
response_banking_direct_debit_authorisation_list_form_dict = response_banking_direct_debit_authorisation_list.from_dict(response_banking_direct_debit_authorisation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


