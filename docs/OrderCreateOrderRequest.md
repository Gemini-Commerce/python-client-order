# # OrderCreateOrderRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   | [optional]
**number**| **str** |   | [optional]
**channel**| **str** |   | [optional]
**market**| **str** |   | [optional]
**locale**| **str** |   | [optional]
**items**| [**List[OrderOrderDataItem]**](OrderOrderDataItem.md) |   | [optional]
**payments_info**| [**List[OrderDataPaymentInfo]**](OrderDataPaymentInfo.md) |   | [optional]
**shipments_info**| [**List[OrderDataShipmentInfo]**](OrderDataShipmentInfo.md) |   | [optional]
**promotions**| [**List[OrderDataPromotionInfo]**](OrderDataPromotionInfo.md) |   | [optional]
**payments**| [**List[CreateOrderRequestInitialPayment]**](CreateOrderRequestInitialPayment.md) |   | [optional]
**currency**| [**OrderCurrency**](OrderCurrency.md) |  for more information please, see Model/OrderCurrency.php  | [optional]
**subtotals**| [**Dict[str, OrderDataSubtotal]**](OrderDataSubtotal.md) |   | [optional]
**totals**| [**Dict[str, OrderDataTotal]**](OrderDataTotal.md) |   | [optional]
**vat_included**| **bool** |   | [optional]
**billing_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   | [optional]
**shipping_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   | [optional]
**customer_info**| [**OrderDataCustomerInfo**](OrderDataCustomerInfo.md) |   | [optional]
**cart_grn**| **str** |   | [optional]
**on_hold**| **bool** |   | [optional]
**notes**| **str** |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

