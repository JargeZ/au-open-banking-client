# BankingTransactionDetailAllOfExtendedData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer** | **str** | Label of the originating payer. Mandatory for inbound payment | [optional] 
**payee** | **str** | Label of the target PayID.  Mandatory for an outbound payment. The name assigned to the BSB/Account Number or PayID (by the owner of the PayID) | [optional] 
**extension_u_type** | **str** | Optional extended data specific to transactions originated via NPP | [optional] 
**x2p101_payload** | [**BankingTransactionDetailAllOfExtendedDataX2p101Payload**](BankingTransactionDetailAllOfExtendedDataX2p101Payload.md) |  | [optional] 
**service** | **str** | Identifier of the applicable overlay service. Valid values are: X2P1.01 | 

## Example

```python
from au_open_banking_spec.models.banking_transaction_detail_all_of_extended_data import BankingTransactionDetailAllOfExtendedData

# TODO update the JSON string below
json = "{}"
# create an instance of BankingTransactionDetailAllOfExtendedData from a JSON string
banking_transaction_detail_all_of_extended_data_instance = BankingTransactionDetailAllOfExtendedData.from_json(json)
# print the JSON string representation of the object
print BankingTransactionDetailAllOfExtendedData.to_json()

# convert the object into a dict
banking_transaction_detail_all_of_extended_data_dict = banking_transaction_detail_all_of_extended_data_instance.to_dict()
# create an instance of BankingTransactionDetailAllOfExtendedData from a dict
banking_transaction_detail_all_of_extended_data_form_dict = banking_transaction_detail_all_of_extended_data.from_dict(banking_transaction_detail_all_of_extended_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


