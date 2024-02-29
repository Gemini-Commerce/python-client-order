# order
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-order.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-order.git`)

Then import the package:
```python
import order
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import order
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import order
from order.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dom.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = order.Configuration(
    host = "https://dom.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'


# Enter a context with an instance of the API client
with order.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = order.OrderApi(api_client)
    body = order.OrderApproveOrderRequest() # OrderApproveOrderRequest | 

    try:
        # Approve Order
        api_response = api_instance.approve_order(body)
        print("The response of OrderApi->approve_order:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling OrderApi->approve_order: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://dom.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*OrderApi* | [**approve_order**](docs/OrderApi.md#approve_order) | **POST** /order.Order/ApproveOrder | Approve Order
*OrderApi* | [**assign_shipment**](docs/OrderApi.md#assign_shipment) | **POST** /order.Order/AssignShipment | Assign Shipment
*OrderApi* | [**calculate_refund**](docs/OrderApi.md#calculate_refund) | **POST** /order.Order/CalculateRefund | Calculate Refund
*OrderApi* | [**cancel_fulfillment**](docs/OrderApi.md#cancel_fulfillment) | **POST** /order.Order/CancelFulfillment | Cancel Fulfillment
*OrderApi* | [**cancel_order**](docs/OrderApi.md#cancel_order) | **POST** /order.Order/CancelOrder | Cancel Order
*OrderApi* | [**cancel_shipment**](docs/OrderApi.md#cancel_shipment) | **POST** /order.Order/CancelShipment | Cancel Shipment
*OrderApi* | [**complete_shipment_packing**](docs/OrderApi.md#complete_shipment_packing) | **POST** /order.Order/CompleteShipmentPacking | Complete Shipment Packing
*OrderApi* | [**create_fulfillment**](docs/OrderApi.md#create_fulfillment) | **POST** /order.Order/CreateFulfillment | Create Fulfillment
*OrderApi* | [**create_order**](docs/OrderApi.md#create_order) | **POST** /order.Order/CreateOrder | Create Order
*OrderApi* | [**create_order_history**](docs/OrderApi.md#create_order_history) | **POST** /order.Order/CreateHistory | Create Order History
*OrderApi* | [**create_payment**](docs/OrderApi.md#create_payment) | **POST** /order.Order/CreatePayment | Create Payment
*OrderApi* | [**create_payment_transaction**](docs/OrderApi.md#create_payment_transaction) | **POST** /order.Order/CreatePaymentTransaction | Create Payment Transaction
*OrderApi* | [**create_refund**](docs/OrderApi.md#create_refund) | **POST** /order.Order/CreateRefund | Create Refund
*OrderApi* | [**create_refund_transaction**](docs/OrderApi.md#create_refund_transaction) | **POST** /order.Order/CreateRefundTransaction | Create Refund Transaction
*OrderApi* | [**create_shipment**](docs/OrderApi.md#create_shipment) | **POST** /order.Order/CreateShipment | Create Shipment
*OrderApi* | [**delete_order**](docs/OrderApi.md#delete_order) | **POST** /order.Order/DeleteOrder | Delete Order
*OrderApi* | [**get_fulfillment**](docs/OrderApi.md#get_fulfillment) | **POST** /order.Order/GetFulfillment | Get Fulfillment
*OrderApi* | [**get_order**](docs/OrderApi.md#get_order) | **POST** /order.Order/GetOrder | Get Order
*OrderApi* | [**get_order_by_cart_id**](docs/OrderApi.md#get_order_by_cart_id) | **POST** /order.Order/GetOrderByCartId | Get Order by Cart ID
*OrderApi* | [**get_order_by_order_number**](docs/OrderApi.md#get_order_by_order_number) | **POST** /order.Order/GetOrderByOrderNumber | Get Order by Order Number
*OrderApi* | [**get_payment**](docs/OrderApi.md#get_payment) | **POST** /order.Order/GetPayment | Get Payment
*OrderApi* | [**get_shipment**](docs/OrderApi.md#get_shipment) | **POST** /order.Order/GetShipment | Get Shipment
*OrderApi* | [**get_transaction**](docs/OrderApi.md#get_transaction) | **POST** /order.Order/GetTransaction | Get Transaction
*OrderApi* | [**hold_order**](docs/OrderApi.md#hold_order) | **POST** /order.Order/HoldOrder | Hold Order
*OrderApi* | [**import_order**](docs/OrderApi.md#import_order) | **POST** /order.Order/ImportOrder | Import Order
*OrderApi* | [**list_fulfillments**](docs/OrderApi.md#list_fulfillments) | **POST** /order.Order/ListFulfillments | List Fulfillments
*OrderApi* | [**list_orders**](docs/OrderApi.md#list_orders) | **POST** /order.Order/ListOrders | List Orders
*OrderApi* | [**list_orders_by_customer**](docs/OrderApi.md#list_orders_by_customer) | **POST** /order.Order/ListOrdersByCustomer | List Orders by Customer
*OrderApi* | [**list_orders_by_numbers**](docs/OrderApi.md#list_orders_by_numbers) | **POST** /order.Order/ListOrdersByNumbers | List Orders by Numbers
*OrderApi* | [**list_shipments**](docs/OrderApi.md#list_shipments) | **POST** /order.Order/ListShipments | List Shipments
*OrderApi* | [**order_add_document**](docs/OrderApi.md#order_add_document) | **POST** /order.Order/AddDocument | Documents
*OrderApi* | [**order_remove_document_by_code**](docs/OrderApi.md#order_remove_document_by_code) | **POST** /order.Order/RemoveDocumentByCode | 
*OrderApi* | [**print_orders_labels**](docs/OrderApi.md#print_orders_labels) | **POST** /order.Order/PrintOrdersLabels | Print Orders Labels
*OrderApi* | [**quash_fulfillment**](docs/OrderApi.md#quash_fulfillment) | **POST** /order.Order/QuashFulfillment | Quash Fulfillment
*OrderApi* | [**quash_shipment**](docs/OrderApi.md#quash_shipment) | **POST** /order.Order/QuashShipment | Quash Shipment
*OrderApi* | [**receive_fulfillment**](docs/OrderApi.md#receive_fulfillment) | **POST** /order.Order/ReceiveFulfillment | Receive Fulfillment
*OrderApi* | [**report_fulfillment_error**](docs/OrderApi.md#report_fulfillment_error) | **POST** /order.Order/ReportFulfillmentError | Report Fulfillment Error
*OrderApi* | [**report_fulfillment_not_resolvable**](docs/OrderApi.md#report_fulfillment_not_resolvable) | **POST** /order.Order/ReportFulfillmentNotResolvable | Report Fulfillment Not Resolvable
*OrderApi* | [**report_fulfillment_ready**](docs/OrderApi.md#report_fulfillment_ready) | **POST** /order.Order/ReportFulfillmentReady | Report Fulfillment Ready
*OrderApi* | [**report_shipment_delivery**](docs/OrderApi.md#report_shipment_delivery) | **POST** /order.Order/ReportShipmentDelivery | Report Shipment Delivery
*OrderApi* | [**report_shipment_missing_stock**](docs/OrderApi.md#report_shipment_missing_stock) | **POST** /order.Order/ReportShipmentMissingStock | Report Shipment Missing Stock
*OrderApi* | [**resolve_shipment_missing_stock**](docs/OrderApi.md#resolve_shipment_missing_stock) | **POST** /order.Order/ResolveShipmentMissingStock | Resolve Shipment Missing Stock
*OrderApi* | [**retry_fulfillment**](docs/OrderApi.md#retry_fulfillment) | **POST** /order.Order/RetryFulfillment | Retry Fulfillment
*OrderApi* | [**search_orders**](docs/OrderApi.md#search_orders) | **POST** /order.Order/SearchOrders | Search Orders
*OrderApi* | [**send_fulfillment**](docs/OrderApi.md#send_fulfillment) | **POST** /order.Order/SendFulfillment | Send Fulfillment
*OrderApi* | [**send_order_notification**](docs/OrderApi.md#send_order_notification) | **POST** /order.Order/SendOrderNotification | Send Order Notification
*OrderApi* | [**start_fulfillment_processing**](docs/OrderApi.md#start_fulfillment_processing) | **POST** /order.Order/StartFulfillmentProcessing | Start Fulfillment Processing
*OrderApi* | [**start_shipment_processing**](docs/OrderApi.md#start_shipment_processing) | **POST** /order.Order/StartShipmentProcessing | Start Shipment Processing
*OrderApi* | [**unhold_order**](docs/OrderApi.md#unhold_order) | **POST** /order.Order/UnholdOrder | Unhold Order
*OrderApi* | [**update_order**](docs/OrderApi.md#update_order) | **POST** /order.Order/UpdateOrder | Update Order
*OrderApi* | [**update_payment**](docs/OrderApi.md#update_payment) | **POST** /order.Order/UpdatePayment | Update Payment


## Documentation For Models

 - [CreateOrderRequestInitialPayment](docs/CreateOrderRequestInitialPayment.md)
 - [ImportOrderRequestImportedPayment](docs/ImportOrderRequestImportedPayment.md)
 - [InitialPaymentInitialTransaction](docs/InitialPaymentInitialTransaction.md)
 - [ItemProductConfigurationStep](docs/ItemProductConfigurationStep.md)
 - [OptionImage](docs/OptionImage.md)
 - [OrderAddDocumentRequest](docs/OrderAddDocumentRequest.md)
 - [OrderApproveOrderRequest](docs/OrderApproveOrderRequest.md)
 - [OrderAssignShipmentRequest](docs/OrderAssignShipmentRequest.md)
 - [OrderByDirection](docs/OrderByDirection.md)
 - [OrderCalculateRefundRequest](docs/OrderCalculateRefundRequest.md)
 - [OrderCalculateRefundResponse](docs/OrderCalculateRefundResponse.md)
 - [OrderCancelFulfillmentRequest](docs/OrderCancelFulfillmentRequest.md)
 - [OrderCancelOrderRequest](docs/OrderCancelOrderRequest.md)
 - [OrderCancelShipmentRequest](docs/OrderCancelShipmentRequest.md)
 - [OrderCompleteShipmentPackingRequest](docs/OrderCompleteShipmentPackingRequest.md)
 - [OrderCreateFulfillmentRequest](docs/OrderCreateFulfillmentRequest.md)
 - [OrderCreateHistoryRequest](docs/OrderCreateHistoryRequest.md)
 - [OrderCreateOrderRequest](docs/OrderCreateOrderRequest.md)
 - [OrderCreatePaymentRequest](docs/OrderCreatePaymentRequest.md)
 - [OrderCreatePaymentTransactionRequest](docs/OrderCreatePaymentTransactionRequest.md)
 - [OrderCreateRefundRequest](docs/OrderCreateRefundRequest.md)
 - [OrderCreateRefundTransactionRequest](docs/OrderCreateRefundTransactionRequest.md)
 - [OrderCreateShipmentRequest](docs/OrderCreateShipmentRequest.md)
 - [OrderCurrency](docs/OrderCurrency.md)
 - [OrderDataCustomerInfo](docs/OrderDataCustomerInfo.md)
 - [OrderDataDocument](docs/OrderDataDocument.md)
 - [OrderDataHistory](docs/OrderDataHistory.md)
 - [OrderDataPaymentInfo](docs/OrderDataPaymentInfo.md)
 - [OrderDataPromotionInfo](docs/OrderDataPromotionInfo.md)
 - [OrderDataShipmentInfo](docs/OrderDataShipmentInfo.md)
 - [OrderDataSubtotal](docs/OrderDataSubtotal.md)
 - [OrderDataSubtotalCode](docs/OrderDataSubtotalCode.md)
 - [OrderDataTotal](docs/OrderDataTotal.md)
 - [OrderDataTotalCode](docs/OrderDataTotalCode.md)
 - [OrderDeleteOrderRequest](docs/OrderDeleteOrderRequest.md)
 - [OrderFulfillment](docs/OrderFulfillment.md)
 - [OrderFulfillmentItem](docs/OrderFulfillmentItem.md)
 - [OrderGetFulfillmentRequest](docs/OrderGetFulfillmentRequest.md)
 - [OrderGetOrderByCartIdRequest](docs/OrderGetOrderByCartIdRequest.md)
 - [OrderGetOrderByOrderNumberRequest](docs/OrderGetOrderByOrderNumberRequest.md)
 - [OrderGetOrderRequest](docs/OrderGetOrderRequest.md)
 - [OrderGetPaymentRequest](docs/OrderGetPaymentRequest.md)
 - [OrderGetShipmentRequest](docs/OrderGetShipmentRequest.md)
 - [OrderGetTransactionRequest](docs/OrderGetTransactionRequest.md)
 - [OrderHoldOrderRequest](docs/OrderHoldOrderRequest.md)
 - [OrderImportOrderRequest](docs/OrderImportOrderRequest.md)
 - [OrderListFulfillmentsRequest](docs/OrderListFulfillmentsRequest.md)
 - [OrderListFulfillmentsResponse](docs/OrderListFulfillmentsResponse.md)
 - [OrderListOrdersByCustomerRequest](docs/OrderListOrdersByCustomerRequest.md)
 - [OrderListOrdersByCustomerResponse](docs/OrderListOrdersByCustomerResponse.md)
 - [OrderListOrdersByNumbersRequest](docs/OrderListOrdersByNumbersRequest.md)
 - [OrderListOrdersByNumbersResponse](docs/OrderListOrdersByNumbersResponse.md)
 - [OrderListOrdersRequest](docs/OrderListOrdersRequest.md)
 - [OrderListOrdersResponse](docs/OrderListOrdersResponse.md)
 - [OrderListShipmentsRequest](docs/OrderListShipmentsRequest.md)
 - [OrderListShipmentsResponse](docs/OrderListShipmentsResponse.md)
 - [OrderLocalizedText](docs/OrderLocalizedText.md)
 - [OrderMoney](docs/OrderMoney.md)
 - [OrderOrderBy](docs/OrderOrderBy.md)
 - [OrderOrderData](docs/OrderOrderData.md)
 - [OrderOrderDataItem](docs/OrderOrderDataItem.md)
 - [OrderPayment](docs/OrderPayment.md)
 - [OrderPaymentAmount](docs/OrderPaymentAmount.md)
 - [OrderPaymentAmountCode](docs/OrderPaymentAmountCode.md)
 - [OrderPaymentFilter](docs/OrderPaymentFilter.md)
 - [OrderPaymentFilterCondition](docs/OrderPaymentFilterCondition.md)
 - [OrderPostalAddress](docs/OrderPostalAddress.md)
 - [OrderPrintOrdersLabelsRequest](docs/OrderPrintOrdersLabelsRequest.md)
 - [OrderPrintOrdersLabelsResponse](docs/OrderPrintOrdersLabelsResponse.md)
 - [OrderQuashFulfillmentRequest](docs/OrderQuashFulfillmentRequest.md)
 - [OrderQuashShipmentRequest](docs/OrderQuashShipmentRequest.md)
 - [OrderReceiveFulfillmentRequest](docs/OrderReceiveFulfillmentRequest.md)
 - [OrderRefund](docs/OrderRefund.md)
 - [OrderRefundAmount](docs/OrderRefundAmount.md)
 - [OrderRefundAmountCode](docs/OrderRefundAmountCode.md)
 - [OrderRefundItem](docs/OrderRefundItem.md)
 - [OrderRemoveDocumentByCodeRequest](docs/OrderRemoveDocumentByCodeRequest.md)
 - [OrderReportFulfillmentErrorRequest](docs/OrderReportFulfillmentErrorRequest.md)
 - [OrderReportFulfillmentNotResolvableRequest](docs/OrderReportFulfillmentNotResolvableRequest.md)
 - [OrderReportFulfillmentReadyRequest](docs/OrderReportFulfillmentReadyRequest.md)
 - [OrderReportShipmentDeliveryRequest](docs/OrderReportShipmentDeliveryRequest.md)
 - [OrderReportShipmentMissingStockRequest](docs/OrderReportShipmentMissingStockRequest.md)
 - [OrderResolveShipmentMissingStockRequest](docs/OrderResolveShipmentMissingStockRequest.md)
 - [OrderRetryFulfillmentRequest](docs/OrderRetryFulfillmentRequest.md)
 - [OrderSearchOrdersRequest](docs/OrderSearchOrdersRequest.md)
 - [OrderSearchOrdersResponse](docs/OrderSearchOrdersResponse.md)
 - [OrderSendFulfillmentRequest](docs/OrderSendFulfillmentRequest.md)
 - [OrderSendOrderNotificationRequest](docs/OrderSendOrderNotificationRequest.md)
 - [OrderShipment](docs/OrderShipment.md)
 - [OrderShipmentItem](docs/OrderShipmentItem.md)
 - [OrderStartFulfillmentProcessingRequest](docs/OrderStartFulfillmentProcessingRequest.md)
 - [OrderStartShipmentProcessingRequest](docs/OrderStartShipmentProcessingRequest.md)
 - [OrderStatusFilter](docs/OrderStatusFilter.md)
 - [OrderStatusFilterCondition](docs/OrderStatusFilterCondition.md)
 - [OrderTransaction](docs/OrderTransaction.md)
 - [OrderTransactionType](docs/OrderTransactionType.md)
 - [OrderUnholdOrderRequest](docs/OrderUnholdOrderRequest.md)
 - [OrderUpdateOrderRequest](docs/OrderUpdateOrderRequest.md)
 - [OrderUpdatePaymentRequest](docs/OrderUpdatePaymentRequest.md)
 - [PaymentCcInfo](docs/PaymentCcInfo.md)
 - [PrintOrdersLabelsResponseFailedOrder](docs/PrintOrdersLabelsResponseFailedOrder.md)
 - [ProductConfigurationStepOption](docs/ProductConfigurationStepOption.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [ProtobufNullValue](docs/ProtobufNullValue.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [ShipmentTracking](docs/ShipmentTracking.md)
 - [UpdateOrderRequestPayload](docs/UpdateOrderRequestPayload.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Authorization"></a>
### Authorization

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

<a id="standardAuthorization"></a>
### standardAuthorization

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: 
- **Scopes**: N/A


## Author

info@gemini-commerce.com


