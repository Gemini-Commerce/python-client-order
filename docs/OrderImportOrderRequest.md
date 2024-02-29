# # OrderImportOrderRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   | [optional]
**created_at**| **datetime** |   | [optional]
**number**| **str** |   | [optional]
**channel**| **str** |   | [optional]
**market**| **str** |   | [optional]
**locale**| **str** |   | [optional]
**customer_info**| [**OrderDataCustomerInfo**](OrderDataCustomerInfo.md) |   | [optional]
**shipping_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   | [optional]
**billing_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   | [optional]
**payments**| [**List[ImportOrderRequestImportedPayment]**](ImportOrderRequestImportedPayment.md) |   | [optional]
**payments_info**| [**List[OrderDataPaymentInfo]**](OrderDataPaymentInfo.md) |   | [optional]
**shipments_info**| [**List[OrderDataShipmentInfo]**](OrderDataShipmentInfo.md) |   | [optional]
**items**| [**List[OrderOrderDataItem]**](OrderOrderDataItem.md) |   | [optional]
**subtotals**| [**Dict[str, OrderDataSubtotal]**](OrderDataSubtotal.md) |   | [optional]
**totals**| [**Dict[str, OrderDataTotal]**](OrderDataTotal.md) |   | [optional]
**status**| **str** |   | [optional]
**currency**| [**OrderCurrency**](OrderCurrency.md) |  for more information please, see Model/OrderCurrency.php  | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

