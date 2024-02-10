# BankingAuthorisedEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the authorised entity derived from previously executed direct debits | [optional] 
**financial_institution** | **str** | Name of the financial institution through which the direct debit will be executed. Is required unless the payment is made via a credit card scheme | [optional] 
**abn** | **str** | Australian Business Number for the authorised entity | [optional] 
**acn** | **str** | Australian Company Number for the authorised entity | [optional] 
**arbn** | **str** | Australian Registered Body Number for the authorised entity | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_authorised_entity import BankingAuthorisedEntity

# TODO update the JSON string below
json = "{}"
# create an instance of BankingAuthorisedEntity from a JSON string
banking_authorised_entity_instance = BankingAuthorisedEntity.from_json(json)
# print the JSON string representation of the object
print BankingAuthorisedEntity.to_json()

# convert the object into a dict
banking_authorised_entity_dict = banking_authorised_entity_instance.to_dict()
# create an instance of BankingAuthorisedEntity from a dict
banking_authorised_entity_form_dict = banking_authorised_entity.from_dict(banking_authorised_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


