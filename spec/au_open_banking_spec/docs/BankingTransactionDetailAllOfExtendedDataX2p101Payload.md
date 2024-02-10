# BankingTransactionDetailAllOfExtendedDataX2p101Payload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extended_description** | **str** | An extended string description. Required if the extensionUType field is &#x60;x2p101Payload&#x60; | [optional] 
**end_to_end_id** | **str** | An end to end ID for the payment created at initiation | [optional] 
**purpose_code** | **str** | Purpose of the payment.  Format is defined by NPP standards for the x2p1.01 overlay service | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_transaction_detail_all_of_extended_data_x2p101_payload import BankingTransactionDetailAllOfExtendedDataX2p101Payload

# TODO update the JSON string below
json = "{}"
# create an instance of BankingTransactionDetailAllOfExtendedDataX2p101Payload from a JSON string
banking_transaction_detail_all_of_extended_data_x2p101_payload_instance = BankingTransactionDetailAllOfExtendedDataX2p101Payload.from_json(json)
# print the JSON string representation of the object
print BankingTransactionDetailAllOfExtendedDataX2p101Payload.to_json()

# convert the object into a dict
banking_transaction_detail_all_of_extended_data_x2p101_payload_dict = banking_transaction_detail_all_of_extended_data_x2p101_payload_instance.to_dict()
# create an instance of BankingTransactionDetailAllOfExtendedDataX2p101Payload from a dict
banking_transaction_detail_all_of_extended_data_x2p101_payload_form_dict = banking_transaction_detail_all_of_extended_data_x2p101_payload.from_dict(banking_transaction_detail_all_of_extended_data_x2p101_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


