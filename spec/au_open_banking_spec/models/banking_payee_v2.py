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
from typing import Optional, Set
from typing_extensions import Self

class BankingPayeeV2(BaseModel):
    """
    BankingPayeeV2
    """ # noqa: E501
    payee_id: StrictStr = Field(description="ID of the payee adhering to the rules of ID permanence", alias="payeeId")
    nickname: StrictStr = Field(description="The short display name of the payee as provided by the customer. Where a customer has not provided a nickname, a display name derived by the bank for the payee consistent with existing digital banking channels")
    description: Optional[StrictStr] = Field(default=None, description="A description of the payee provided by the customer")
    type: StrictStr = Field(description="The type of payee.<br/>DOMESTIC means a registered payee for domestic payments including NPP. <br/>INTERNATIONAL means a registered payee for international payments. <br/>BILLER means a registered payee for BPAY. <br/>DIGITAL_WALLET means a registered payee for a bank's digital wallet")
    creation_date: Optional[StrictStr] = Field(default=None, description="The date the payee was created by the customer", alias="creationDate")
    __properties: ClassVar[List[str]] = ["payeeId", "nickname", "description", "type", "creationDate"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['BILLER', 'DIGITAL_WALLET', 'DOMESTIC', 'INTERNATIONAL']):
            raise ValueError("must be one of enum values ('BILLER', 'DIGITAL_WALLET', 'DOMESTIC', 'INTERNATIONAL')")
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
        """Create an instance of BankingPayeeV2 from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankingPayeeV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "payeeId": obj.get("payeeId"),
            "nickname": obj.get("nickname"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "creationDate": obj.get("creationDate")
        })
        return _obj


