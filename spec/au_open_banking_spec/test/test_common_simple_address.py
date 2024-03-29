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

from au_open_banking_spec.models.common_simple_address import CommonSimpleAddress

class TestCommonSimpleAddress(unittest.TestCase):
    """CommonSimpleAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonSimpleAddress:
        """Test CommonSimpleAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonSimpleAddress`
        """
        model = CommonSimpleAddress()
        if include_optional:
            return CommonSimpleAddress(
                mailing_name = '',
                address_line1 = '',
                address_line2 = '',
                address_line3 = '',
                postcode = '',
                city = '',
                state = '',
                country = 'AUS'
            )
        else:
            return CommonSimpleAddress(
                address_line1 = '',
                city = '',
                state = '',
        )
        """

    def testCommonSimpleAddress(self):
        """Test CommonSimpleAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
