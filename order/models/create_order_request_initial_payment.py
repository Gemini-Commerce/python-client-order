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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from order.models.initial_payment_initial_transaction import InitialPaymentInitialTransaction
from order.models.order_money import OrderMoney
from order.models.payment_cc_info import PaymentCcInfo
from typing import Optional, Set
from typing_extensions import Self

class CreateOrderRequestInitialPayment(BaseModel):
    """
    CreateOrderRequestInitialPayment
    """ # noqa: E501
    code: StrictStr
    additional_info: Optional[StrictStr] = Field(default=None, alias="additionalInfo")
    amount: OrderMoney
    cc_info: Optional[PaymentCcInfo] = Field(default=None, alias="ccInfo")
    transaction: Optional[InitialPaymentInitialTransaction] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["code", "additionalInfo", "amount", "ccInfo", "transaction"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreateOrderRequestInitialPayment from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of amount
        if self.amount:
            _dict['amount'] = self.amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cc_info
        if self.cc_info:
            _dict['ccInfo'] = self.cc_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOrderRequestInitialPayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "code": obj.get("code"),
            "additionalInfo": obj.get("additionalInfo"),
            "amount": OrderMoney.from_dict(obj["amount"]) if obj.get("amount") is not None else None,
            "ccInfo": PaymentCcInfo.from_dict(obj["ccInfo"]) if obj.get("ccInfo") is not None else None,
            "transaction": InitialPaymentInitialTransaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


