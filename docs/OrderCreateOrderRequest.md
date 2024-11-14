# # OrderCreateOrderRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   |
**number**| **str** |   |
**channel**| **str** |   | [optional]
**market**| **str** |   |
**locale**| **str** |   |
**items**| [**List[OrderOrderDataItem]**](OrderOrderDataItem.md) |   |
**payments_info**| [**List[OrderDataPaymentInfo]**](OrderDataPaymentInfo.md) |   | [optional]
**shipments_info**| [**List[OrderDataShipmentInfo]**](OrderDataShipmentInfo.md) |   | [optional]
**promotions**| [**List[OrderDataPromotionInfo]**](OrderDataPromotionInfo.md) |   | [optional]
**payments**| [**List[CreateOrderRequestInitialPayment]**](CreateOrderRequestInitialPayment.md) |   | [optional]
**currency**| [**OrderCurrency**](OrderCurrency.md) |  for more information please, see Model/OrderCurrency.php  | [default to OrderCurrency.XXX]
**subtotals**| [**Dict[str, OrderDataSubtotal]**](OrderDataSubtotal.md) |   |
**totals**| [**Dict[str, OrderDataTotal]**](OrderDataTotal.md) |   |
**vat_included**| **bool** |   |
**billing_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   |
**shipping_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   |
**customer_info**| [**OrderDataCustomerInfo**](OrderDataCustomerInfo.md) |   |
**cart_grn**| **str** |   | [optional]
**on_hold**| **bool** |   | [optional]
**notes**| **str** |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

