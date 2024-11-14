# # OrderOrderData


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at**| **datetime** |   | [optional] [readonly]
**updated_at**| **datetime** |   | [optional] [readonly]
**id**| **str** |   | [optional] [readonly]
**grn**| **str** |   | [optional] [readonly]
**number**| **str** |   | [optional]
**status**| **str** |   | [optional] [readonly]
**channel**| **str** |   | [optional]
**market**| **str** |   | [optional]
**locale**| **str** |   |
**additional_info**| **object** |   | [optional]
**documents**| [**List[OrderDataDocument]**](OrderDataDocument.md) |   | [optional]
**items**| [**List[OrderOrderDataItem]**](OrderOrderDataItem.md) |   | [optional]
**payments**| [**List[OrderPayment]**](OrderPayment.md) |   | [optional]
**shipments**| [**List[OrderShipment]**](OrderShipment.md) |   | [optional]
**payments_info**| [**List[OrderDataPaymentInfo]**](OrderDataPaymentInfo.md) |   | [optional]
**shipments_info**| [**List[OrderDataShipmentInfo]**](OrderDataShipmentInfo.md) |   | [optional]
**promotions**| [**List[OrderDataPromotionInfo]**](OrderDataPromotionInfo.md) |   | [optional]
**currency**| [**OrderCurrency**](OrderCurrency.md) |  for more information please, see Model/OrderCurrency.php  | [optional] [default to OrderCurrency.XXX]
**subtotals**| [**Dict[str, OrderDataSubtotal]**](OrderDataSubtotal.md) |   | [optional]
**totals**| [**Dict[str, OrderDataTotal]**](OrderDataTotal.md) |   | [optional]
**vat_included**| **bool** |   | [optional]
**billing_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   | [optional]
**shipping_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   | [optional]
**customer_info**| [**OrderDataCustomerInfo**](OrderDataCustomerInfo.md) |   | [optional]
**cart_grn**| **str** |   | [optional]
**on_hold**| **bool** |   | [optional]
**history_events**| [**List[OrderDataHistory]**](OrderDataHistory.md) |   | [optional]
**fulfillments**| [**List[OrderFulfillment]**](OrderFulfillment.md) |   | [optional] [readonly]
**notes**| **str** |   | [optional]
**is_deleted**| **bool** | this field is used to delete an order in \&quot;soft-delete mode\&quot;. This field must be used from get/list endpoint to exclude these orders.  | [optional]
**inserted_at**| **datetime** | this field is used to save the original created_at order date. The created_at field is used to filter data.  | [optional] [readonly]
**deleted_at**| **datetime** |   | [optional] [readonly]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

