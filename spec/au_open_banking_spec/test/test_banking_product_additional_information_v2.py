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

from au_open_banking_spec.models.banking_product_additional_information_v2 import BankingProductAdditionalInformationV2

class TestBankingProductAdditionalInformationV2(unittest.TestCase):
    """BankingProductAdditionalInformationV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankingProductAdditionalInformationV2:
        """Test BankingProductAdditionalInformationV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankingProductAdditionalInformationV2`
        """
        model = BankingProductAdditionalInformationV2()
        if include_optional:
            return BankingProductAdditionalInformationV2(
                overview_uri = '',
                terms_uri = '',
                eligibility_uri = '',
                fees_and_pricing_uri = '',
                bundle_uri = '',
                additional_overview_uris = [
                    {"additionalInfoUri":"additionalInfoUri","description":"description"}
                    ],
                additional_terms_uris = [
                    {"additionalInfoUri":"additionalInfoUri","description":"description"}
                    ],
                additional_eligibility_uris = [
                    {"additionalInfoUri":"additionalInfoUri","description":"description"}
                    ],
                additional_fees_and_pricing_uris = [
                    {"additionalInfoUri":"additionalInfoUri","description":"description"}
                    ],
                additional_bundle_uris = [
                    {"additionalInfoUri":"additionalInfoUri","description":"description"}
                    ]
            )
        else:
            return BankingProductAdditionalInformationV2(
        )
        """

    def testBankingProductAdditionalInformationV2(self):
        """Test BankingProductAdditionalInformationV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
