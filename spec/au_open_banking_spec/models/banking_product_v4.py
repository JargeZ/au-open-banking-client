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

from pydantic import BaseModel, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from au_open_banking_spec.models.banking_product_additional_information_v2 import BankingProductAdditionalInformationV2
from au_open_banking_spec.models.banking_product_category import BankingProductCategory
from au_open_banking_spec.models.banking_product_v4_card_art import BankingProductV4CardArt
from typing import Optional, Set
from typing_extensions import Self

class BankingProductV4(BaseModel):
    """
    BankingProductV4
    """ # noqa: E501
    product_id: StrictStr = Field(description="A data holder specific unique identifier for this product. This identifier must be unique to a product but does not otherwise need to adhere to ID permanence guidelines.", alias="productId")
    effective_from: Optional[StrictStr] = Field(default=None, description="The date and time from which this product is effective (ie. is available for origination).  Used to enable the articulation of products to the regime before they are available for customers to originate", alias="effectiveFrom")
    effective_to: Optional[StrictStr] = Field(default=None, description="The date and time at which this product will be retired and will no longer be offered.  Used to enable the managed deprecation of products", alias="effectiveTo")
    last_updated: StrictStr = Field(description="The last date and time that the information for this product was changed (or the creation date for the product if it has never been altered)", alias="lastUpdated")
    product_category: BankingProductCategory = Field(alias="productCategory")
    name: StrictStr = Field(description="The display name of the product")
    description: StrictStr = Field(description="A description of the product")
    brand: StrictStr = Field(description="A label of the brand for the product. Able to be used for filtering. For data holders with single brands this value is still required")
    brand_name: Optional[StrictStr] = Field(default=None, description="An optional display name of the brand", alias="brandName")
    application_uri: Optional[StrictStr] = Field(default=None, description="A link to an application web page where this product can be applied for.", alias="applicationUri")
    is_tailored: StrictBool = Field(description="Indicates whether the product is specifically tailored to a circumstance.  In this case fees and prices are significantly negotiated depending on context. While all products are open to a degree of tailoring this flag indicates that tailoring is expected and thus that the provision of specific fees and rates is not applicable", alias="isTailored")
    additional_information: Optional[BankingProductAdditionalInformationV2] = Field(default=None, alias="additionalInformation")
    card_art: Optional[List[BankingProductV4CardArt]] = Field(default=None, description="An array of card art images", alias="cardArt")
    __properties: ClassVar[List[str]] = ["productId", "effectiveFrom", "effectiveTo", "lastUpdated", "productCategory", "name", "description", "brand", "brandName", "applicationUri", "isTailored", "additionalInformation", "cardArt"]

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
        """Create an instance of BankingProductV4 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of additional_information
        if self.additional_information:
            _dict['additionalInformation'] = self.additional_information.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in card_art (list)
        _items = []
        if self.card_art:
            for _item in self.card_art:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cardArt'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankingProductV4 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "productId": obj.get("productId"),
            "effectiveFrom": obj.get("effectiveFrom"),
            "effectiveTo": obj.get("effectiveTo"),
            "lastUpdated": obj.get("lastUpdated"),
            "productCategory": obj.get("productCategory"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "brand": obj.get("brand"),
            "brandName": obj.get("brandName"),
            "applicationUri": obj.get("applicationUri"),
            "isTailored": obj.get("isTailored"),
            "additionalInformation": BankingProductAdditionalInformationV2.from_dict(obj["additionalInformation"]) if obj.get("additionalInformation") is not None else None,
            "cardArt": [BankingProductV4CardArt.from_dict(_item) for _item in obj["cardArt"]] if obj.get("cardArt") is not None else None
        })
        return _obj


