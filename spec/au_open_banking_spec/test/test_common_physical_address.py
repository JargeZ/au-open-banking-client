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

from au_open_banking_spec.models.common_physical_address import CommonPhysicalAddress

class TestCommonPhysicalAddress(unittest.TestCase):
    """CommonPhysicalAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommonPhysicalAddress:
        """Test CommonPhysicalAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommonPhysicalAddress`
        """
        model = CommonPhysicalAddress()
        if include_optional:
            return CommonPhysicalAddress(
                address_u_type = 'paf',
                simple = au_open_banking_spec.models.common_simple_address.CommonSimpleAddress(
                    mailing_name = '', 
                    address_line1 = '', 
                    address_line2 = '', 
                    address_line3 = '', 
                    postcode = '', 
                    city = '', 
                    state = '', 
                    country = 'AUS', ),
                paf = au_open_banking_spec.models.common_paf_address.CommonPAFAddress(
                    dpid = '', 
                    thoroughfare_number1 = 56, 
                    thoroughfare_number1_suffix = '', 
                    thoroughfare_number2 = 56, 
                    thoroughfare_number2_suffix = '', 
                    flat_unit_type = '', 
                    flat_unit_number = '', 
                    floor_level_type = '', 
                    floor_level_number = '', 
                    lot_number = '', 
                    building_name1 = '', 
                    building_name2 = '', 
                    street_name = '', 
                    street_type = '', 
                    street_suffix = '', 
                    postal_delivery_type = '', 
                    postal_delivery_number = 56, 
                    postal_delivery_number_prefix = '', 
                    postal_delivery_number_suffix = '', 
                    locality_name = '', 
                    postcode = '', 
                    state = '', )
            )
        else:
            return CommonPhysicalAddress(
                address_u_type = 'paf',
        )
        """

    def testCommonPhysicalAddress(self):
        """Test CommonPhysicalAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()