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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BankingTransactionDetailAllOfExtendedDataX2p101Payload(BaseModel):
    """
    BankingTransactionDetailAllOfExtendedDataX2p101Payload
    """ # noqa: E501
    extended_description: Optional[StrictStr] = Field(default=None, description="An extended string description. Required if the extensionUType field is `x2p101Payload`", alias="extendedDescription")
    end_to_end_id: Optional[StrictStr] = Field(default=None, description="An end to end ID for the payment created at initiation", alias="endToEndId")
    purpose_code: Optional[StrictStr] = Field(default=None, description="Purpose of the payment.  Format is defined by NPP standards for the x2p1.01 overlay service", alias="purposeCode")
    __properties: ClassVar[List[str]] = ["extendedDescription", "endToEndId", "purposeCode"]

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
        """Create an instance of BankingTransactionDetailAllOfExtendedDataX2p101Payload from a JSON string"""
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
        """Create an instance of BankingTransactionDetailAllOfExtendedDataX2p101Payload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extendedDescription": obj.get("extendedDescription"),
            "endToEndId": obj.get("endToEndId"),
            "purposeCode": obj.get("purposeCode")
        })
        return _obj


