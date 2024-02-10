# ResponseBankingDirectDebitAuthorisationListData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direct_debit_authorisations** | [**List[BankingDirectDebit]**](BankingDirectDebit.md) | The list of authorisations returned | 

## Example

```python
from au_open_banking_spec.models.response_banking_direct_debit_authorisation_list_data import ResponseBankingDirectDebitAuthorisationListData

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingDirectDebitAuthorisationListData from a JSON string
response_banking_direct_debit_authorisation_list_data_instance = ResponseBankingDirectDebitAuthorisationListData.from_json(json)
# print the JSON string representation of the object
print ResponseBankingDirectDebitAuthorisationListData.to_json()

# convert the object into a dict
response_banking_direct_debit_authorisation_list_data_dict = response_banking_direct_debit_authorisation_list_data_instance.to_dict()
# create an instance of ResponseBankingDirectDebitAuthorisationListData from a dict
response_banking_direct_debit_authorisation_list_data_form_dict = response_banking_direct_debit_authorisation_list_data.from_dict(response_banking_direct_debit_authorisation_list_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


