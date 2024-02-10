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

from au_open_banking_spec.models.response_banking_direct_debit_authorisation_list import ResponseBankingDirectDebitAuthorisationList

class TestResponseBankingDirectDebitAuthorisationList(unittest.TestCase):
    """ResponseBankingDirectDebitAuthorisationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseBankingDirectDebitAuthorisationList:
        """Test ResponseBankingDirectDebitAuthorisationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseBankingDirectDebitAuthorisationList`
        """
        model = ResponseBankingDirectDebitAuthorisationList()
        if include_optional:
            return ResponseBankingDirectDebitAuthorisationList(
                data = {"directDebitAuthorisations":[{"lastDebitAmount":"lastDebitAmount","accountId":"accountId","lastDebitDateTime":"lastDebitDateTime","authorisedEntity":{"arbn":"arbn","description":"description","financialInstitution":"financialInstitution","abn":"abn","acn":"acn"}},{"lastDebitAmount":"lastDebitAmount","accountId":"accountId","lastDebitDateTime":"lastDebitDateTime","authorisedEntity":{"arbn":"arbn","description":"description","financialInstitution":"financialInstitution","abn":"abn","acn":"acn"}}]},
                links = {"next":"next","last":"last","prev":"prev","self":"self","first":"first"},
                meta = {"totalRecords":0,"totalPages":6}
            )
        else:
            return ResponseBankingDirectDebitAuthorisationList(
                data = {"directDebitAuthorisations":[{"lastDebitAmount":"lastDebitAmount","accountId":"accountId","lastDebitDateTime":"lastDebitDateTime","authorisedEntity":{"arbn":"arbn","description":"description","financialInstitution":"financialInstitution","abn":"abn","acn":"acn"}},{"lastDebitAmount":"lastDebitAmount","accountId":"accountId","lastDebitDateTime":"lastDebitDateTime","authorisedEntity":{"arbn":"arbn","description":"description","financialInstitution":"financialInstitution","abn":"abn","acn":"acn"}}]},
                links = {"next":"next","last":"last","prev":"prev","self":"self","first":"first"},
                meta = {"totalRecords":0,"totalPages":6},
        )
        """

    def testResponseBankingDirectDebitAuthorisationList(self):
        """Test ResponseBankingDirectDebitAuthorisationList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
