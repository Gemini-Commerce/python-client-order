# coding: utf-8

"""
    order Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from order.models.order_money import OrderMoney
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderDataPromotionInfo(BaseModel):
    """
    OrderDataPromotionInfo
    """ # noqa: E501
    promotion_grn: Optional[StrictStr] = Field(default=None, alias="promotionGrn")
    type: StrictStr
    additional_info: Optional[StrictStr] = Field(default=None, alias="additionalInfo")
    name: StrictStr
    description: Optional[StrictStr] = None
    amount: OrderMoney
    coupon_code: Optional[StrictStr] = Field(default=None, alias="couponCode")
    vat_amount: Optional[OrderMoney] = Field(default=None, alias="vatAmount")
    vat_percentage: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="vatPercentage")
    vat_inaccurate: Optional[StrictBool] = Field(default=None, alias="vatInaccurate")
    vat_calculated: Optional[StrictBool] = Field(default=None, alias="vatCalculated")
    __properties: ClassVar[List[str]] = ["promotionGrn", "type", "additionalInfo", "name", "description", "amount", "couponCode", "vatAmount", "vatPercentage", "vatInaccurate", "vatCalculated"]

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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrderDataPromotionInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vat_amount
        if self.vat_amount:
            _dict['vatAmount'] = self.vat_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderDataPromotionInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "promotionGrn": obj.get("promotionGrn"),
            "type": obj.get("type"),
            "additionalInfo": obj.get("additionalInfo"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "amount": OrderMoney.from_dict(obj.get("amount")) if obj.get("amount") is not None else None,
            "couponCode": obj.get("couponCode"),
            "vatAmount": OrderMoney.from_dict(obj.get("vatAmount")) if obj.get("vatAmount") is not None else None,
            "vatPercentage": obj.get("vatPercentage"),
            "vatInaccurate": obj.get("vatInaccurate"),
            "vatCalculated": obj.get("vatCalculated")
        })
        return _obj


