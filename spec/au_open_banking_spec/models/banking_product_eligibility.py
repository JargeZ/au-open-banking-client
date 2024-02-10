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

class BankingProductEligibility(BaseModel):
    """
    BankingProductEligibility
    """ # noqa: E501
    eligibility_type: StrictStr = Field(description="The type of eligibility criteria described.  See the next section for an overview of valid values and their meaning", alias="eligibilityType")
    additional_value: Optional[StrictStr] = Field(default=None, description="Generic field containing additional information relevant to the [eligibilityType](#tocSproducteligibilitytypedoc) specified. Whether mandatory or not is dependent on the value of [eligibilityType](#tocSproducteligibilitytypedoc)", alias="additionalValue")
    additional_info: Optional[StrictStr] = Field(default=None, description="Display text providing more information on the [eligibility](#tocSproducteligibilitytypedoc) criteria. Mandatory if the field is set to OTHER", alias="additionalInfo")
    additional_info_uri: Optional[StrictStr] = Field(default=None, description="Link to a web page with more information on this eligibility criteria", alias="additionalInfoUri")
    __properties: ClassVar[List[str]] = ["eligibilityType", "additionalValue", "additionalInfo", "additionalInfoUri"]

    @field_validator('eligibility_type')
    def eligibility_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['BUSINESS', 'EMPLOYMENT_STATUS', 'MAX_AGE', 'MIN_AGE', 'MIN_INCOME', 'MIN_TURNOVER', 'NATURAL_PERSON', 'OTHER', 'PENSION_RECIPIENT', 'RESIDENCY_STATUS', 'STAFF', 'STUDENT']):
            raise ValueError("must be one of enum values ('BUSINESS', 'EMPLOYMENT_STATUS', 'MAX_AGE', 'MIN_AGE', 'MIN_INCOME', 'MIN_TURNOVER', 'NATURAL_PERSON', 'OTHER', 'PENSION_RECIPIENT', 'RESIDENCY_STATUS', 'STAFF', 'STUDENT')")
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
        """Create an instance of BankingProductEligibility from a JSON string"""
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
        """Create an instance of BankingProductEligibility from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "eligibilityType": obj.get("eligibilityType"),
            "additionalValue": obj.get("additionalValue"),
            "additionalInfo": obj.get("additionalInfo"),
            "additionalInfoUri": obj.get("additionalInfoUri")
        })
        return _obj


