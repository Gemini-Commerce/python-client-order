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
from order.models.order_postal_address import OrderPostalAddress
from order.models.order_shipment_item import OrderShipmentItem
from order.models.shipment_tracking import ShipmentTracking
from typing import Optional, Set
from typing_extensions import Self

class OrderCreateShipmentRequest(BaseModel):
    """
    OrderCreateShipmentRequest
    """ # noqa: E501
    tenant_id: StrictStr = Field(alias="tenantId")
    order_id: StrictStr = Field(alias="orderId")
    items: List[OrderShipmentItem]
    address: OrderPostalAddress
    from_address: Optional[OrderPostalAddress] = Field(default=None, alias="fromAddress")
    return_address: Optional[OrderPostalAddress] = Field(default=None, alias="returnAddress")
    tracking: Optional[List[ShipmentTracking]] = None
    return_tracking: Optional[List[ShipmentTracking]] = Field(default=None, alias="returnTracking")
    code: Optional[StrictStr] = None
    method: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["tenantId", "orderId", "items", "address", "fromAddress", "returnAddress", "tracking", "returnTracking", "code", "method"]

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
        """Create an instance of OrderCreateShipmentRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of from_address
        if self.from_address:
            _dict['fromAddress'] = self.from_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of return_address
        if self.return_address:
            _dict['returnAddress'] = self.return_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tracking (list)
        _items = []
        if self.tracking:
            for _item_tracking in self.tracking:
                if _item_tracking:
                    _items.append(_item_tracking.to_dict())
            _dict['tracking'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in return_tracking (list)
        _items = []
        if self.return_tracking:
            for _item_return_tracking in self.return_tracking:
                if _item_return_tracking:
                    _items.append(_item_return_tracking.to_dict())
            _dict['returnTracking'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderCreateShipmentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "orderId": obj.get("orderId"),
            "items": [OrderShipmentItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "address": OrderPostalAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "fromAddress": OrderPostalAddress.from_dict(obj["fromAddress"]) if obj.get("fromAddress") is not None else None,
            "returnAddress": OrderPostalAddress.from_dict(obj["returnAddress"]) if obj.get("returnAddress") is not None else None,
            "tracking": [ShipmentTracking.from_dict(_item) for _item in obj["tracking"]] if obj.get("tracking") is not None else None,
            "returnTracking": [ShipmentTracking.from_dict(_item) for _item in obj["returnTracking"]] if obj.get("returnTracking") is not None else None,
            "code": obj.get("code"),
            "method": obj.get("method")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


