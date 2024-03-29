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

from au_open_banking_spec.models.banking_account_v2 import BankingAccountV2

class TestBankingAccountV2(unittest.TestCase):
    """BankingAccountV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BankingAccountV2:
        """Test BankingAccountV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BankingAccountV2`
        """
        model = BankingAccountV2()
        if include_optional:
            return BankingAccountV2(
                account_id = '',
                creation_date = '',
                display_name = '',
                nickname = '',
                open_status = 'OPEN',
                is_owned = True,
                account_ownership = 'UNKNOWN',
                masked_number = '',
                product_category = 'BUSINESS_LOANS',
                product_name = ''
            )
        else:
            return BankingAccountV2(
                account_id = '',
                display_name = '',
                account_ownership = 'UNKNOWN',
                masked_number = '',
                product_category = 'BUSINESS_LOANS',
                product_name = '',
        )
        """

    def testBankingAccountV2(self):
        """Test BankingAccountV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
