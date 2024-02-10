# BankingProductDetailV4AllOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundles** | [**List[BankingProductBundle]**](BankingProductBundle.md) | An array of bundles that this product participates in.  Each bundle is described by free form information but also by a list of product IDs of the other products that are included in the bundle.  It is assumed that the current product is included in the bundle also | [optional] 
**features** | [**List[BankingProductFeatureV2]**](BankingProductFeatureV2.md) | Array of features available for the product | [optional] 
**constraints** | [**List[BankingProductConstraint]**](BankingProductConstraint.md) | Constraints on the application for or operation of the product such as minimum balances or limit thresholds | [optional] 
**eligibility** | [**List[BankingProductEligibility]**](BankingProductEligibility.md) | Eligibility criteria for the product | [optional] 
**fees** | [**List[BankingProductFee]**](BankingProductFee.md) | Fees applicable for the product | [optional] 
**deposit_rates** | [**List[BankingProductDepositRate]**](BankingProductDepositRate.md) | Interest rates available for deposits | [optional] 
**lending_rates** | [**List[BankingProductLendingRateV2]**](BankingProductLendingRateV2.md) | Interest rates charged against lending balances | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_detail_v4_all_of import BankingProductDetailV4AllOf

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductDetailV4AllOf from a JSON string
banking_product_detail_v4_all_of_instance = BankingProductDetailV4AllOf.from_json(json)
# print the JSON string representation of the object
print BankingProductDetailV4AllOf.to_json()

# convert the object into a dict
banking_product_detail_v4_all_of_dict = banking_product_detail_v4_all_of_instance.to_dict()
# create an instance of BankingProductDetailV4AllOf from a dict
banking_product_detail_v4_all_of_form_dict = banking_product_detail_v4_all_of.from_dict(banking_product_detail_v4_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


