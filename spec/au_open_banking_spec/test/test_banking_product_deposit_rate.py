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

from au_open_banking_spec.models.banking_product_deposit_rate import BankingProductDepositRate

class TestBankingProductDepositRate(unittest.TestCase):
    """BankingProductDepositRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankingProductDepositRate:
        """Test BankingProductDepositRate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankingProductDepositRate`
        """
        model = BankingProductDepositRate()
        if include_optional:
            return BankingProductDepositRate(
                deposit_rate_type = 'BONUS',
                rate = '',
                calculation_frequency = '',
                application_frequency = '',
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
            return BankingProductDepositRate(
                deposit_rate_type = 'BONUS',
                rate = '',
        )
        """

    def testBankingProductDepositRate(self):
        """Test BankingProductDepositRate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
