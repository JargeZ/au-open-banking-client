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

from au_open_banking_spec.models.banking_product_lending_rate_v2 import BankingProductLendingRateV2

class TestBankingProductLendingRateV2(unittest.TestCase):
    """BankingProductLendingRateV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankingProductLendingRateV2:
        """Test BankingProductLendingRateV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankingProductLendingRateV2`
        """
        model = BankingProductLendingRateV2()
        if include_optional:
            return BankingProductLendingRateV2(
                lending_rate_type = 'BUNDLE_DISCOUNT_FIXED',
                rate = '',
                comparison_rate = '',
                calculation_frequency = '',
                application_frequency = '',
                interest_payment_due = 'IN_ADVANCE',
                repayment_type = 'INTEREST_ONLY',
                loan_purpose = 'INVESTMENT',
                tiers = [
                    au_open_banking_spec.models.banking_product_rate_tier_v3.BankingProductRateTierV3(
                        name = '', 
                        unit_of_measure = 'DAY', 
                        minimum_value = 1.337, 
                        maximum_value = 1.337, 
                        rate_application_method = 'PER_TIER', 
                        applicability_conditions = au_open_banking_spec.models.banking_product_rate_condition.BankingProductRateCondition(
                            additional_info = '', 
                            additional_info_uri = '', ), 
                        additional_info = '', 
                        additional_info_uri = '', )
                    ],
                additional_value = '',
                additional_info = '',
                additional_info_uri = ''
            )
        else:
            return BankingProductLendingRateV2(
                lending_rate_type = 'BUNDLE_DISCOUNT_FIXED',
                rate = '',
        )
        """

    def testBankingProductLendingRateV2(self):
        """Test BankingProductLendingRateV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()