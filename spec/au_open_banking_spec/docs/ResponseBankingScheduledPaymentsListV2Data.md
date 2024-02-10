# ResponseBankingScheduledPaymentsListV2Data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_payments** | [**List[BankingScheduledPaymentV2]**](BankingScheduledPaymentV2.md) | The list of scheduled payments to return | 

## Example

```python
from au_open_banking_spec.models.response_banking_scheduled_payments_list_v2_data import ResponseBankingScheduledPaymentsListV2Data

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBankingScheduledPaymentsListV2Data from a JSON string
response_banking_scheduled_payments_list_v2_data_instance = ResponseBankingScheduledPaymentsListV2Data.from_json(json)
# print the JSON string representation of the object
print ResponseBankingScheduledPaymentsListV2Data.to_json()

# convert the object into a dict
response_banking_scheduled_payments_list_v2_data_dict = response_banking_scheduled_payments_list_v2_data_instance.to_dict()
# create an instance of ResponseBankingScheduledPaymentsListV2Data from a dict
response_banking_scheduled_payments_list_v2_data_form_dict = response_banking_scheduled_payments_list_v2_data.from_dict(response_banking_scheduled_payments_list_v2_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


