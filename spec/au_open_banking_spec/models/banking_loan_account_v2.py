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

from pydantic import BaseModel, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BankingLoanAccountV2(BaseModel):
    """
    BankingLoanAccountV2
    """ # noqa: E501
    original_start_date: Optional[StrictStr] = Field(default=None, description="Optional original start date for the loan", alias="originalStartDate")
    original_loan_amount: Optional[StrictStr] = Field(default=None, description="Optional original loan value", alias="originalLoanAmount")
    original_loan_currency: Optional[StrictStr] = Field(default=None, description="If absent assumes AUD", alias="originalLoanCurrency")
    loan_end_date: Optional[StrictStr] = Field(default=None, description="Date that the loan is due to be repaid in full", alias="loanEndDate")
    next_instalment_date: Optional[StrictStr] = Field(default=None, description="Next date that an instalment is required", alias="nextInstalmentDate")
    min_instalment_amount: Optional[StrictStr] = Field(default=None, description="Minimum amount of next instalment", alias="minInstalmentAmount")
    min_instalment_currency: Optional[StrictStr] = Field(default=None, description="If absent assumes AUD", alias="minInstalmentCurrency")
    max_redraw: Optional[StrictStr] = Field(default=None, description="Maximum amount of funds that can be redrawn. If not present redraw is not available even if the feature exists for the account", alias="maxRedraw")
    max_redraw_currency: Optional[StrictStr] = Field(default=None, description="If absent assumes AUD", alias="maxRedrawCurrency")
    min_redraw: Optional[StrictStr] = Field(default=None, description="Minimum redraw amount", alias="minRedraw")
    min_redraw_currency: Optional[StrictStr] = Field(default=None, description="If absent assumes AUD", alias="minRedrawCurrency")
    offset_account_enabled: Optional[StrictBool] = Field(default=None, description="Set to true if one or more offset accounts are configured for this loan account", alias="offsetAccountEnabled")
    offset_account_ids: Optional[List[StrictStr]] = Field(default=None, description="The accountIDs of the configured offset accounts attached to this loan. Only offset accounts that can be accessed under the current authorisation should be included. It is expected behaviour that offsetAccountEnabled is set to true but the offsetAccountIds field is absent or empty. This represents a situation where an offset account exists but details can not be accessed under the current authorisation", alias="offsetAccountIds")
    repayment_type: Optional[StrictStr] = Field(default='PRINCIPAL_AND_INTEREST', description="Options in place for repayments. If absent defaults to PRINCIPAL_AND_INTEREST", alias="repaymentType")
    repayment_frequency: Optional[StrictStr] = Field(default=None, description="The expected or required repayment frequency. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)", alias="repaymentFrequency")
    __properties: ClassVar[List[str]] = ["originalStartDate", "originalLoanAmount", "originalLoanCurrency", "loanEndDate", "nextInstalmentDate", "minInstalmentAmount", "minInstalmentCurrency", "maxRedraw", "maxRedrawCurrency", "minRedraw", "minRedrawCurrency", "offsetAccountEnabled", "offsetAccountIds", "repaymentType", "repaymentFrequency"]

    @field_validator('repayment_type')
    def repayment_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INTEREST_ONLY', 'PRINCIPAL_AND_INTEREST']):
            raise ValueError("must be one of enum values ('INTEREST_ONLY', 'PRINCIPAL_AND_INTEREST')")
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
        """Create an instance of BankingLoanAccountV2 from a JSON string"""
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
        """Create an instance of BankingLoanAccountV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "originalStartDate": obj.get("originalStartDate"),
            "originalLoanAmount": obj.get("originalLoanAmount"),
            "originalLoanCurrency": obj.get("originalLoanCurrency"),
            "loanEndDate": obj.get("loanEndDate"),
            "nextInstalmentDate": obj.get("nextInstalmentDate"),
            "minInstalmentAmount": obj.get("minInstalmentAmount"),
            "minInstalmentCurrency": obj.get("minInstalmentCurrency"),
            "maxRedraw": obj.get("maxRedraw"),
            "maxRedrawCurrency": obj.get("maxRedrawCurrency"),
            "minRedraw": obj.get("minRedraw"),
            "minRedrawCurrency": obj.get("minRedrawCurrency"),
            "offsetAccountEnabled": obj.get("offsetAccountEnabled"),
            "offsetAccountIds": obj.get("offsetAccountIds"),
            "repaymentType": obj.get("repaymentType") if obj.get("repaymentType") is not None else 'PRINCIPAL_AND_INTEREST',
            "repaymentFrequency": obj.get("repaymentFrequency")
        })
        return _obj


