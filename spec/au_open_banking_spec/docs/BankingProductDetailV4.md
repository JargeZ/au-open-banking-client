# BankingProductDetailV4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** | A data holder specific unique identifier for this product. This identifier must be unique to a product but does not otherwise need to adhere to ID permanence guidelines. | 
**effective_from** | **str** | The date and time from which this product is effective (ie. is available for origination).  Used to enable the articulation of products to the regime before they are available for customers to originate | [optional] 
**effective_to** | **str** | The date and time at which this product will be retired and will no longer be offered.  Used to enable the managed deprecation of products | [optional] 
**last_updated** | **str** | The last date and time that the information for this product was changed (or the creation date for the product if it has never been altered) | 
**product_category** | [**BankingProductCategory**](BankingProductCategory.md) |  | 
**name** | **str** | The display name of the product | 
**description** | **str** | A description of the product | 
**brand** | **str** | A label of the brand for the product. Able to be used for filtering. For data holders with single brands this value is still required | 
**brand_name** | **str** | An optional display name of the brand | [optional] 
**application_uri** | **str** | A link to an application web page where this product can be applied for. | [optional] 
**is_tailored** | **bool** | Indicates whether the product is specifically tailored to a circumstance.  In this case fees and prices are significantly negotiated depending on context. While all products are open to a degree of tailoring this flag indicates that tailoring is expected and thus that the provision of specific fees and rates is not applicable | 
**additional_information** | [**BankingProductAdditionalInformationV2**](BankingProductAdditionalInformationV2.md) |  | [optional] 
**card_art** | [**List[BankingProductV4CardArt]**](BankingProductV4CardArt.md) | An array of card art images | [optional] 
**bundles** | [**List[BankingProductBundle]**](BankingProductBundle.md) | An array of bundles that this product participates in.  Each bundle is described by free form information but also by a list of product IDs of the other products that are included in the bundle.  It is assumed that the current product is included in the bundle also | [optional] 
**features** | [**List[BankingProductFeatureV2]**](BankingProductFeatureV2.md) | Array of features available for the product | [optional] 
**constraints** | [**List[BankingProductConstraint]**](BankingProductConstraint.md) | Constraints on the application for or operation of the product such as minimum balances or limit thresholds | [optional] 
**eligibility** | [**List[BankingProductEligibility]**](BankingProductEligibility.md) | Eligibility criteria for the product | [optional] 
**fees** | [**List[BankingProductFee]**](BankingProductFee.md) | Fees applicable for the product | [optional] 
**deposit_rates** | [**List[BankingProductDepositRate]**](BankingProductDepositRate.md) | Interest rates available for deposits | [optional] 
**lending_rates** | [**List[BankingProductLendingRateV2]**](BankingProductLendingRateV2.md) | Interest rates charged against lending balances | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_detail_v4 import BankingProductDetailV4

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductDetailV4 from a JSON string
banking_product_detail_v4_instance = BankingProductDetailV4.from_json(json)
# print the JSON string representation of the object
print BankingProductDetailV4.to_json()

# convert the object into a dict
banking_product_detail_v4_dict = banking_product_detail_v4_instance.to_dict()
# create an instance of BankingProductDetailV4 from a dict
banking_product_detail_v4_form_dict = banking_product_detail_v4.from_dict(banking_product_detail_v4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


