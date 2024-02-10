# BankingProductAdditionalInformationV2

Object that contains links to additional information on specific topics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overview_uri** | **str** | General overview of the product. Mandatory if &#x60;additionalOverviewUris&#x60; includes one or more supporting documents. | [optional] 
**terms_uri** | **str** | Terms and conditions for the product. Mandatory if &#x60;additionalTermsUris&#x60; includes one or more supporting documents. | [optional] 
**eligibility_uri** | **str** | Eligibility rules and criteria for the product. Mandatory if &#x60;additionalEligibilityUris&#x60; includes one or more supporting documents. | [optional] 
**fees_and_pricing_uri** | **str** | Description of fees, pricing, discounts, exemptions and bonuses for the product. Mandatory if &#x60;additionalFeesAndPricingUris&#x60; includes one or more supporting documents. | [optional] 
**bundle_uri** | **str** | Description of a bundle that this product can be part of. Mandatory if &#x60;additionalBundleUris&#x60; includes one or more supporting documents. | [optional] 
**additional_overview_uris** | [**List[BankingProductAdditionalInformationV2AdditionalInformationUris]**](BankingProductAdditionalInformationV2AdditionalInformationUris.md) | An array of additional general overviews for the product or features of the product, if applicable. To be treated as secondary documents to the &#x60;overviewUri&#x60;. Only to be used if there is a primary &#x60;overviewUri&#x60;. | [optional] 
**additional_terms_uris** | [**List[BankingProductAdditionalInformationV2AdditionalInformationUris]**](BankingProductAdditionalInformationV2AdditionalInformationUris.md) | An array of additional terms and conditions for the product, if applicable. To be treated as secondary documents to the &#x60;termsUri&#x60;. Only to be used if there is a primary &#x60;termsUri&#x60;. | [optional] 
**additional_eligibility_uris** | [**List[BankingProductAdditionalInformationV2AdditionalInformationUris]**](BankingProductAdditionalInformationV2AdditionalInformationUris.md) | An array of additional eligibility rules and criteria for the product, if applicable. To be treated as secondary documents to the &#x60;eligibilityUri&#x60;. Only to be used if there is a primary &#x60;eligibilityUri&#x60;. | [optional] 
**additional_fees_and_pricing_uris** | [**List[BankingProductAdditionalInformationV2AdditionalInformationUris]**](BankingProductAdditionalInformationV2AdditionalInformationUris.md) | An array of additional fees, pricing, discounts, exemptions and bonuses for the product, if applicable. To be treated as secondary documents to the &#x60;feesAndPricingUri&#x60;. Only to be used if there is a primary &#x60;feesAndPricingUri&#x60;. | [optional] 
**additional_bundle_uris** | [**List[BankingProductAdditionalInformationV2AdditionalInformationUris]**](BankingProductAdditionalInformationV2AdditionalInformationUris.md) | An array of additional bundles for the product, if applicable. To be treated as secondary documents to the &#x60;bundleUri&#x60;. Only to be used if there is a primary &#x60;bundleUri&#x60;. | [optional] 

## Example

```python
from au_open_banking_spec.models.banking_product_additional_information_v2 import BankingProductAdditionalInformationV2

# TODO update the JSON string below
json = "{}"
# create an instance of BankingProductAdditionalInformationV2 from a JSON string
banking_product_additional_information_v2_instance = BankingProductAdditionalInformationV2.from_json(json)
# print the JSON string representation of the object
print BankingProductAdditionalInformationV2.to_json()

# convert the object into a dict
banking_product_additional_information_v2_dict = banking_product_additional_information_v2_instance.to_dict()
# create an instance of BankingProductAdditionalInformationV2 from a dict
banking_product_additional_information_v2_form_dict = banking_product_additional_information_v2.from_dict(banking_product_additional_information_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


