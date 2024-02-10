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
from au_open_banking_spec.models.banking_balance_purse import BankingBalancePurse
from typing import Optional, Set
from typing_extensions import Self

class BankingBalance(BaseModel):
    """
    BankingBalance
    """ # noqa: E501
    account_id: StrictStr = Field(description="A unique ID of the account adhering to the standards for ID permanence", alias="accountId")
    current_balance: StrictStr = Field(description="The balance of the account at this time. Should align to the balance available via other channels such as Internet Banking. Assumed to be negative if the customer has money owing", alias="currentBalance")
    available_balance: StrictStr = Field(description="Balance representing the amount of funds available for transfer. Assumed to be zero or positive", alias="availableBalance")
    credit_limit: Optional[StrictStr] = Field(default=None, description="Object representing the maximum amount of credit that is available for this account. Assumed to be zero if absent", alias="creditLimit")
    amortised_limit: Optional[StrictStr] = Field(default=None, description="Object representing the available limit amortised according to payment schedule. Assumed to be zero if absent", alias="amortisedLimit")
    currency: Optional[StrictStr] = Field(default=None, description="The currency for the balance amounts. If absent assumed to be AUD")
    purses: Optional[List[BankingBalancePurse]] = Field(default=None, description="Optional array of balances for the account in other currencies. Included to support accounts that support multi-currency purses such as Travel Cards")
    __properties: ClassVar[List[str]] = ["accountId", "currentBalance", "availableBalance", "creditLimit", "amortisedLimit", "currency", "purses"]

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
        """Create an instance of BankingBalance from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in purses (list)
        _items = []
        if self.purses:
            for _item in self.purses:
                if _item:
                    _items.append(_item.to_dict())
            _dict['purses'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankingBalance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accountId": obj.get("accountId"),
            "currentBalance": obj.get("currentBalance"),
            "availableBalance": obj.get("availableBalance"),
            "creditLimit": obj.get("creditLimit"),
            "amortisedLimit": obj.get("amortisedLimit"),
            "currency": obj.get("currency"),
            "purses": [BankingBalancePurse.from_dict(_item) for _item in obj["purses"]] if obj.get("purses") is not None else None
        })
        return _obj


