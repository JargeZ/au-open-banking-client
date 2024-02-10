# coding: utf-8

"""
    CDR Banking API

    Consumer Data Standards APIs created by the Data Standards Body (DSB), with the Data Standards Chair as the decision maker to meet the needs of the Consumer Data Right

    The version of the OpenAPI document: 1.29.0
    Contact: contact@consumerdatastandards.gov.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from au_open_banking_spec.models.response_banking_product_list_v2 import ResponseBankingProductListV2

class TestResponseBankingProductListV2(unittest.TestCase):
    """ResponseBankingProductListV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseBankingProductListV2:
        """Test ResponseBankingProductListV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseBankingProductListV2`
        """
        model = ResponseBankingProductListV2()
        if include_optional:
            return ResponseBankingProductListV2(
                data = {"products":[{"additionalInformation":{"eligibilityUri":"eligibilityUri","additionalFeesAndPricingUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalTermsUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"bundleUri":"bundleUri","feesAndPricingUri":"feesAndPricingUri","additionalBundleUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalEligibilityUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalOverviewUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"termsUri":"termsUri","overviewUri":"overviewUri"},"brandName":"brandName","productId":"productId","description":"description","effectiveTo":"effectiveTo","cardArt":[{"imageUri":"imageUri","title":"title"},{"imageUri":"imageUri","title":"title"}],"lastUpdated":"lastUpdated","isTailored":true,"name":"name","applicationUri":"applicationUri","effectiveFrom":"effectiveFrom","brand":"brand"},{"additionalInformation":{"eligibilityUri":"eligibilityUri","additionalFeesAndPricingUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalTermsUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"bundleUri":"bundleUri","feesAndPricingUri":"feesAndPricingUri","additionalBundleUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalEligibilityUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalOverviewUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"termsUri":"termsUri","overviewUri":"overviewUri"},"brandName":"brandName","productId":"productId","description":"description","effectiveTo":"effectiveTo","cardArt":[{"imageUri":"imageUri","title":"title"},{"imageUri":"imageUri","title":"title"}],"lastUpdated":"lastUpdated","isTailored":true,"name":"name","applicationUri":"applicationUri","effectiveFrom":"effectiveFrom","brand":"brand"}]},
                links = {"next":"next","last":"last","prev":"prev","self":"self","first":"first"},
                meta = {"totalRecords":0,"totalPages":6}
            )
        else:
            return ResponseBankingProductListV2(
                data = {"products":[{"additionalInformation":{"eligibilityUri":"eligibilityUri","additionalFeesAndPricingUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalTermsUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"bundleUri":"bundleUri","feesAndPricingUri":"feesAndPricingUri","additionalBundleUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalEligibilityUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalOverviewUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"termsUri":"termsUri","overviewUri":"overviewUri"},"brandName":"brandName","productId":"productId","description":"description","effectiveTo":"effectiveTo","cardArt":[{"imageUri":"imageUri","title":"title"},{"imageUri":"imageUri","title":"title"}],"lastUpdated":"lastUpdated","isTailored":true,"name":"name","applicationUri":"applicationUri","effectiveFrom":"effectiveFrom","brand":"brand"},{"additionalInformation":{"eligibilityUri":"eligibilityUri","additionalFeesAndPricingUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalTermsUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"bundleUri":"bundleUri","feesAndPricingUri":"feesAndPricingUri","additionalBundleUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalEligibilityUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"additionalOverviewUris":[{"additionalInfoUri":"additionalInfoUri","description":"description"},{"additionalInfoUri":"additionalInfoUri","description":"description"}],"termsUri":"termsUri","overviewUri":"overviewUri"},"brandName":"brandName","productId":"productId","description":"description","effectiveTo":"effectiveTo","cardArt":[{"imageUri":"imageUri","title":"title"},{"imageUri":"imageUri","title":"title"}],"lastUpdated":"lastUpdated","isTailored":true,"name":"name","applicationUri":"applicationUri","effectiveFrom":"effectiveFrom","brand":"brand"}]},
                links = {"next":"next","last":"last","prev":"prev","self":"self","first":"first"},
                meta = {"totalRecords":0,"totalPages":6},
        )
        """

    def testResponseBankingProductListV2(self):
        """Test ResponseBankingProductListV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
