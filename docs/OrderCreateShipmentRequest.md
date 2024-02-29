# # OrderCreateShipmentRequest


## Properties 


Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id**| **str** |   |
**order_id**| **str** |   |
**items**| [**List[OrderShipmentItem]**](OrderShipmentItem.md) |   |
**address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   |
**from_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   | [optional]
**return_address**| [**OrderPostalAddress**](OrderPostalAddress.md) |   | [optional]
**tracking**| [**List[ShipmentTracking]**](ShipmentTracking.md) |   | [optional]
**return_tracking**| [**List[ShipmentTracking]**](ShipmentTracking.md) |   | [optional]
**code**| **str** |   | [optional]
**method**| **str** |   | [optional]


[[Back to Model list]](../../README.md#models) [[Back to API list]](../../README.md#endpoints) [[Back to README]](../../README.md)

