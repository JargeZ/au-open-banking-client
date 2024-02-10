# coding: utf-8

"""
    CDR Banking API

    Consumer Data Standards APIs created by the Data Standards Body (DSB), with the Data Standards Chair as the decision maker to meet the needs of the Consumer Data Right

    The version of the OpenAPI document: 1.29.0
    Contact: contact@consumerdatastandards.gov.au
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from au_open_banking_spec.models.banking_biller_payee import BankingBillerPayee
from au_open_banking_spec.models.banking_digital_wallet_payee import BankingDigitalWalletPayee
from au_open_banking_spec.models.banking_domestic_payee import BankingDomesticPayee
from au_open_banking_spec.models.banking_international_payee import BankingInternationalPayee
from typing import Optional, Set
from typing_extensions import Self

class BankingScheduledPaymentToV2(BaseModel):
    """
    Object containing details of the destination of the payment. Used to specify a variety of payment destination types
    """ # noqa: E501
    to_u_type: StrictStr = Field(description="The type of object provided that specifies the destination of the funds for the payment.", alias="toUType")
    account_id: Optional[StrictStr] = Field(default=None, description="Present if toUType is set to accountId. Indicates that the payment is to another account that is accessible under the current consent", alias="accountId")
    payee_id: Optional[StrictStr] = Field(default=None, description="Present if toUType is set to payeeId. Indicates that the payment is to registered payee that can be accessed using the payee end point. If the Bank Payees scope has not been consented to then a payeeId should not be provided and the full payee details should be provided instead", alias="payeeId")
    nickname: Optional[StrictStr] = Field(default=None, description="The short display name of the payee as provided by the customer unless toUType is set to payeeId. Where a customer has not provided a nickname, a display name derived by the bank for payee should be provided that is consistent with existing digital banking channels")
    payee_reference: Optional[StrictStr] = Field(default=None, description="The reference for the transaction, if applicable, that will be provided by the originating institution for the specific payment. If not empty, it overrides the value provided at the BankingScheduledPayment level.", alias="payeeReference")
    digital_wallet: Optional[BankingDigitalWalletPayee] = Field(default=None, alias="digitalWallet")
    domestic: Optional[BankingDomesticPayee] = None
    biller: Optional[BankingBillerPayee] = None
    international: Optional[BankingInternationalPayee] = None
    __properties: ClassVar[List[str]] = ["toUType", "accountId", "payeeId", "nickname", "payeeReference", "digitalWallet", "domestic", "biller", "international"]

    @field_validator('to_u_type')
    def to_u_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['accountId', 'biller', 'digitalWallet', 'domestic', 'international', 'payeeId']):
            raise ValueError("must be one of enum values ('accountId', 'biller', 'digitalWallet', 'domestic', 'international', 'payeeId')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BankingScheduledPaymentToV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of digital_wallet
        if self.digital_wallet:
            _dict['digitalWallet'] = self.digital_wallet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domestic
        if self.domestic:
            _dict['domestic'] = self.domestic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of biller
        if self.biller:
            _dict['biller'] = self.biller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of international
        if self.international:
            _dict['international'] = self.international.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankingScheduledPaymentToV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "toUType": obj.get("toUType"),
            "accountId": obj.get("accountId"),
            "payeeId": obj.get("payeeId"),
            "nickname": obj.get("nickname"),
            "payeeReference": obj.get("payeeReference"),
            "digitalWallet": BankingDigitalWalletPayee.from_dict(obj["digitalWallet"]) if obj.get("digitalWallet") is not None else None,
            "domestic": BankingDomesticPayee.from_dict(obj["domestic"]) if obj.get("domestic") is not None else None,
            "biller": BankingBillerPayee.from_dict(obj["biller"]) if obj.get("biller") is not None else None,
            "international": BankingInternationalPayee.from_dict(obj["international"]) if obj.get("international") is not None else None
        })
        return _obj


