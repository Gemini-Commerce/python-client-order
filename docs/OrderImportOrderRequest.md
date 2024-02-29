# # OrderImportOrderRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   |
**created_at**| **datetime** |   | [optional]
**number**| **str** |   |
**channel**| **str** |   | [optional]
**market**| **str** |   |
**locale**| **str** |   |
**customer_info**| [**OrderDataCustomerInfo**](OrderDataCustomerInfo.md) |   |
**shipping_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   |
**billing_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   |
**payments**| [**List[ImportOrderRequestImportedPayment]**](ImportOrderRequestImportedPayment.md) |   |
**payments_info**| [**List[OrderDataPaymentInfo]**](OrderDataPaymentInfo.md) |   |
**shipments_info**| [**List[OrderDataShipmentInfo]**](OrderDataShipmentInfo.md) |   |
**items**| [**List[OrderOrderDataItem]**](OrderOrderDataItem.md) |   |
**subtotals**| [**Dict[str, OrderDataSubtotal]**](OrderDataSubtotal.md) |   |
**totals**| [**Dict[str, OrderDataTotal]**](OrderDataTotal.md) |   |
**status**| **str** |   |
**currency**| [**OrderCurrency**](OrderCurrency.md) |  for more information please, see Model/OrderCurrency.php  |


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

