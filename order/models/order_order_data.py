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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from order.models.order_currency import OrderCurrency
from order.models.order_data_customer_info import OrderDataCustomerInfo
from order.models.order_data_document import OrderDataDocument
from order.models.order_data_history import OrderDataHistory
from order.models.order_data_payment_info import OrderDataPaymentInfo
from order.models.order_data_promotion_info import OrderDataPromotionInfo
from order.models.order_data_shipment_info import OrderDataShipmentInfo
from order.models.order_data_subtotal import OrderDataSubtotal
from order.models.order_data_total import OrderDataTotal
from order.models.order_fulfillment import OrderFulfillment
from order.models.order_order_data_item import OrderOrderDataItem
from order.models.order_payment import OrderPayment
from order.models.order_postal_address import OrderPostalAddress
from order.models.order_shipment import OrderShipment
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OrderOrderData(BaseModel):
    """
    OrderOrderData
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
    id: Optional[StrictStr] = None
    grn: Optional[StrictStr] = None
    number: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    channel: Optional[StrictStr] = None
    market: Optional[StrictStr] = None
    locale: StrictStr
    additional_info: Optional[Dict[str, Any]] = Field(default=None, alias="additionalInfo")
    documents: Optional[List[OrderDataDocument]] = None
    items: Optional[List[OrderOrderDataItem]] = None
    payments: Optional[List[OrderPayment]] = None
    shipments: Optional[List[OrderShipment]] = None
    payments_info: Optional[List[OrderDataPaymentInfo]] = Field(default=None, alias="paymentsInfo")
    shipments_info: Optional[List[OrderDataShipmentInfo]] = Field(default=None, alias="shipmentsInfo")
    promotions: Optional[List[OrderDataPromotionInfo]] = None
    currency: Optional[OrderCurrency] = None
    subtotals: Optional[Dict[str, OrderDataSubtotal]] = None
    totals: Optional[Dict[str, OrderDataTotal]] = None
    vat_included: Optional[StrictBool] = Field(default=None, alias="vatIncluded")
    billing_address: Optional[OrderPostalAddress] = Field(default=None, alias="billingAddress")
    shipping_address: Optional[OrderPostalAddress] = Field(default=None, alias="shippingAddress")
    customer_info: Optional[OrderDataCustomerInfo] = Field(default=None, alias="customerInfo")
    cart_grn: Optional[StrictStr] = Field(default=None, alias="cartGrn")
    on_hold: Optional[StrictBool] = Field(default=None, alias="onHold")
    history_events: Optional[List[OrderDataHistory]] = Field(default=None, alias="historyEvents")
    fulfillments: Optional[List[OrderFulfillment]] = None
    notes: Optional[StrictStr] = None
    is_deleted: Optional[StrictBool] = Field(default=None, description="this field is used to delete an order in \"soft-delete mode\". This field must be used from get/list endpoint to exclude these orders.", alias="isDeleted")
    inserted_at: Optional[datetime] = Field(default=None, description="this field is used to save the original created_at order date. The created_at field is used to filter data.", alias="insertedAt")
    deleted_at: Optional[datetime] = Field(default=None, alias="deletedAt")
    __properties: ClassVar[List[str]] = ["createdAt", "updatedAt", "id", "grn", "number", "status", "channel", "market", "locale", "additionalInfo", "documents", "items", "payments", "shipments", "paymentsInfo", "shipmentsInfo", "promotions", "currency", "subtotals", "totals", "vatIncluded", "billingAddress", "shippingAddress", "customerInfo", "cartGrn", "onHold", "historyEvents", "fulfillments", "notes", "isDeleted", "insertedAt", "deletedAt"]

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
        """Create an instance of OrderOrderData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "updated_at",
                "id",
                "grn",
                "status",
                "fulfillments",
                "inserted_at",
                "deleted_at",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item in self.documents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item in self.payments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shipments (list)
        _items = []
        if self.shipments:
            for _item in self.shipments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shipments'] = _items
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
        # override the default output from pydantic by calling `to_dict()` of each item in promotions (list)
        _items = []
        if self.promotions:
            for _item in self.promotions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['promotions'] = _items
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
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['shippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of customer_info
        if self.customer_info:
            _dict['customerInfo'] = self.customer_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in history_events (list)
        _items = []
        if self.history_events:
            for _item in self.history_events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['historyEvents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fulfillments (list)
        _items = []
        if self.fulfillments:
            for _item in self.fulfillments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fulfillments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OrderOrderData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "id": obj.get("id"),
            "grn": obj.get("grn"),
            "number": obj.get("number"),
            "status": obj.get("status"),
            "channel": obj.get("channel"),
            "market": obj.get("market"),
            "locale": obj.get("locale"),
            "additionalInfo": obj.get("additionalInfo"),
            "documents": [OrderDataDocument.from_dict(_item) for _item in obj.get("documents")] if obj.get("documents") is not None else None,
            "items": [OrderOrderDataItem.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "payments": [OrderPayment.from_dict(_item) for _item in obj.get("payments")] if obj.get("payments") is not None else None,
            "shipments": [OrderShipment.from_dict(_item) for _item in obj.get("shipments")] if obj.get("shipments") is not None else None,
            "paymentsInfo": [OrderDataPaymentInfo.from_dict(_item) for _item in obj.get("paymentsInfo")] if obj.get("paymentsInfo") is not None else None,
            "shipmentsInfo": [OrderDataShipmentInfo.from_dict(_item) for _item in obj.get("shipmentsInfo")] if obj.get("shipmentsInfo") is not None else None,
            "promotions": [OrderDataPromotionInfo.from_dict(_item) for _item in obj.get("promotions")] if obj.get("promotions") is not None else None,
            "currency": obj.get("currency"),
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
            "vatIncluded": obj.get("vatIncluded"),
            "billingAddress": OrderPostalAddress.from_dict(obj.get("billingAddress")) if obj.get("billingAddress") is not None else None,
            "shippingAddress": OrderPostalAddress.from_dict(obj.get("shippingAddress")) if obj.get("shippingAddress") is not None else None,
            "customerInfo": OrderDataCustomerInfo.from_dict(obj.get("customerInfo")) if obj.get("customerInfo") is not None else None,
            "cartGrn": obj.get("cartGrn"),
            "onHold": obj.get("onHold"),
            "historyEvents": [OrderDataHistory.from_dict(_item) for _item in obj.get("historyEvents")] if obj.get("historyEvents") is not None else None,
            "fulfillments": [OrderFulfillment.from_dict(_item) for _item in obj.get("fulfillments")] if obj.get("fulfillments") is not None else None,
            "notes": obj.get("notes"),
            "isDeleted": obj.get("isDeleted"),
            "insertedAt": obj.get("insertedAt"),
            "deletedAt": obj.get("deletedAt")
        })
        return _obj


