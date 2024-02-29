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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from order.models.import_order_request_imported_payment import ImportOrderRequestImportedPayment
from order.models.order_currency import OrderCurrency
from order.models.order_data_customer_info import OrderDataCustomerInfo
from order.models.order_data_payment_info import OrderDataPaymentInfo
from order.models.order_data_shipment_info import OrderDataShipmentInfo
from order.models.order_data_subtotal import OrderDataSubtotal
from order.models.order_data_total import OrderDataTotal
from order.models.order_order_data_item import OrderOrderDataItem
from order.models.order_postal_address import OrderPostalAddress
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderImportOrderRequest(BaseModel):
    """
    OrderImportOrderRequest
    """ # noqa: E501
    tenant_id: Optional[StrictStr] = Field(default=None, alias="tenantId")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    number: Optional[StrictStr] = None
    channel: Optional[StrictStr] = None
    market: Optional[StrictStr] = None
    locale: Optional[StrictStr] = None
    customer_info: Optional[OrderDataCustomerInfo] = Field(default=None, alias="customerInfo")
    shipping_address: Optional[OrderPostalAddress] = Field(default=None, alias="shippingAddress")
    billing_address: Optional[OrderPostalAddress] = Field(default=None, alias="billingAddress")
    payments: Optional[List[ImportOrderRequestImportedPayment]] = None
    payments_info: Optional[List[OrderDataPaymentInfo]] = Field(default=None, alias="paymentsInfo")
    shipments_info: Optional[List[OrderDataShipmentInfo]] = Field(default=None, alias="shipmentsInfo")
    items: Optional[List[OrderOrderDataItem]] = None
    subtotals: Optional[Dict[str, OrderDataSubtotal]] = None
    totals: Optional[Dict[str, OrderDataTotal]] = None
    status: Optional[StrictStr] = None
    currency: Optional[OrderCurrency] = None
    __properties: ClassVar[List[str]] = ["tenantId", "createdAt", "number", "channel", "market", "locale", "customerInfo", "shippingAddress", "billingAddress", "payments", "paymentsInfo", "shipmentsInfo", "items", "subtotals", "totals", "status", "currency"]

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
        """Create an instance of OrderImportOrderRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of customer_info
        if self.customer_info:
            _dict['customerInfo'] = self.customer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['shippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item in self.payments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments_info (list)
        _items = []
        if self.payments_info:
            for _item in self.payments_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['paymentsInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shipments_info (list)
        _items = []
        if self.shipments_info:
            for _item in self.shipments_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shipmentsInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in subtotals (dict)
        _field_dict = {}
        if self.subtotals:
            for _key in self.subtotals:
                if self.subtotals[_key]:
                    _field_dict[_key] = self.subtotals[_key].to_dict()
            _dict['subtotals'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of each value in totals (dict)
        _field_dict = {}
        if self.totals:
            for _key in self.totals:
                if self.totals[_key]:
                    _field_dict[_key] = self.totals[_key].to_dict()
            _dict['totals'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderImportOrderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "createdAt": obj.get("createdAt"),
            "number": obj.get("number"),
            "channel": obj.get("channel"),
            "market": obj.get("market"),
            "locale": obj.get("locale"),
            "customerInfo": OrderDataCustomerInfo.from_dict(obj.get("customerInfo")) if obj.get("customerInfo") is not None else None,
            "shippingAddress": OrderPostalAddress.from_dict(obj.get("shippingAddress")) if obj.get("shippingAddress") is not None else None,
            "billingAddress": OrderPostalAddress.from_dict(obj.get("billingAddress")) if obj.get("billingAddress") is not None else None,
            "payments": [ImportOrderRequestImportedPayment.from_dict(_item) for _item in obj.get("payments")] if obj.get("payments") is not None else None,
            "paymentsInfo": [OrderDataPaymentInfo.from_dict(_item) for _item in obj.get("paymentsInfo")] if obj.get("paymentsInfo") is not None else None,
            "shipmentsInfo": [OrderDataShipmentInfo.from_dict(_item) for _item in obj.get("shipmentsInfo")] if obj.get("shipmentsInfo") is not None else None,
            "items": [OrderOrderDataItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "subtotals": dict(
                (_k, OrderDataSubtotal.from_dict(_v))
                for _k, _v in obj.get("subtotals").items()
            )
            if obj.get("subtotals") is not None
            else None,
            "totals": dict(
                (_k, OrderDataTotal.from_dict(_v))
                for _k, _v in obj.get("totals").items()
            )
            if obj.get("totals") is not None
            else None,
            "status": obj.get("status"),
            "currency": obj.get("currency")
        })
        return _obj


