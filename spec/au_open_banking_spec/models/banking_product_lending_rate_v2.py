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
from au_open_banking_spec.models.banking_product_rate_tier_v3 import BankingProductRateTierV3
from typing import Optional, Set
from typing_extensions import Self

class BankingProductLendingRateV2(BaseModel):
    """
    BankingProductLendingRateV2
    """ # noqa: E501
    lending_rate_type: StrictStr = Field(description="The type of rate (fixed, variable, etc). See the next section for an overview of valid values and their meaning", alias="lendingRateType")
    rate: StrictStr = Field(description="The rate to be applied")
    comparison_rate: Optional[StrictStr] = Field(default=None, description="A comparison rate equivalent for this rate", alias="comparisonRate")
    calculation_frequency: Optional[StrictStr] = Field(default=None, description="The period after which the rate is applied to the balance to calculate the amount due for the period. Calculation of the amount is often daily (as balances may change) but accumulated until the total amount is 'applied' to the account (see applicationFrequency). Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)", alias="calculationFrequency")
    application_frequency: Optional[StrictStr] = Field(default=None, description="The period after which the calculated amount(s) (see calculationFrequency) are 'applied' (i.e. debited or credited) to the account. Formatted according to [ISO 8601 Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) (excludes recurrence syntax)", alias="applicationFrequency")
    interest_payment_due: Optional[StrictStr] = Field(default=None, description="When loan payments are due to be paid within each period. The investment benefit of earlier payments affect the rate that can be offered", alias="interestPaymentDue")
    repayment_type: Optional[StrictStr] = Field(default=None, description="Options in place for repayments. If absent, the lending rate is applicable to all repayment types", alias="repaymentType")
    loan_purpose: Optional[StrictStr] = Field(default=None, description="The reason for taking out the loan. If absent, the lending rate is applicable to all loan purposes", alias="loanPurpose")
    tiers: Optional[List[BankingProductRateTierV3]] = Field(default=None, description="Rate tiers applicable for this rate")
    additional_value: Optional[StrictStr] = Field(default=None, description="Generic field containing additional information relevant to the [lendingRateType](#tocSproductlendingratetypedoc) specified. Whether mandatory or not is dependent on the value of [lendingRateType](#tocSproductlendingratetypedoc)", alias="additionalValue")
    additional_info: Optional[StrictStr] = Field(default=None, description="Display text providing more information on the rate.", alias="additionalInfo")
    additional_info_uri: Optional[StrictStr] = Field(default=None, description="Link to a web page with more information on this rate", alias="additionalInfoUri")
    __properties: ClassVar[List[str]] = ["lendingRateType", "rate", "comparisonRate", "calculationFrequency", "applicationFrequency", "interestPaymentDue", "repaymentType", "loanPurpose", "tiers", "additionalValue", "additionalInfo", "additionalInfoUri"]

    @field_validator('lending_rate_type')
    def lending_rate_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['BUNDLE_DISCOUNT_FIXED', 'BUNDLE_DISCOUNT_VARIABLE', 'CASH_ADVANCE', 'DISCOUNT', 'FIXED', 'FLOATING', 'INTRODUCTORY', 'MARKET_LINKED', 'PENALTY', 'PURCHASE', 'VARIABLE']):
            raise ValueError("must be one of enum values ('BUNDLE_DISCOUNT_FIXED', 'BUNDLE_DISCOUNT_VARIABLE', 'CASH_ADVANCE', 'DISCOUNT', 'FIXED', 'FLOATING', 'INTRODUCTORY', 'MARKET_LINKED', 'PENALTY', 'PURCHASE', 'VARIABLE')")
        return value

    @field_validator('interest_payment_due')
    def interest_payment_due_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['IN_ADVANCE', 'IN_ARREARS']):
            raise ValueError("must be one of enum values ('IN_ADVANCE', 'IN_ARREARS')")
        return value

    @field_validator('repayment_type')
    def repayment_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INTEREST_ONLY', 'PRINCIPAL_AND_INTEREST']):
            raise ValueError("must be one of enum values ('INTEREST_ONLY', 'PRINCIPAL_AND_INTEREST')")
        return value

    @field_validator('loan_purpose')
    def loan_purpose_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INVESTMENT', 'OWNER_OCCUPIED']):
            raise ValueError("must be one of enum values ('INVESTMENT', 'OWNER_OCCUPIED')")
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
        """Create an instance of BankingProductLendingRateV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tiers (list)
        _items = []
        if self.tiers:
            for _item in self.tiers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tiers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankingProductLendingRateV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lendingRateType": obj.get("lendingRateType"),
            "rate": obj.get("rate"),
            "comparisonRate": obj.get("comparisonRate"),
            "calculationFrequency": obj.get("calculationFrequency"),
            "applicationFrequency": obj.get("applicationFrequency"),
            "interestPaymentDue": obj.get("interestPaymentDue"),
            "repaymentType": obj.get("repaymentType"),
            "loanPurpose": obj.get("loanPurpose"),
            "tiers": [BankingProductRateTierV3.from_dict(_item) for _item in obj["tiers"]] if obj.get("tiers") is not None else None,
            "additionalValue": obj.get("additionalValue"),
            "additionalInfo": obj.get("additionalInfo"),
            "additionalInfoUri": obj.get("additionalInfoUri")
        })
        return _obj

