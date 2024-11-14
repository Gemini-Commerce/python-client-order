# order.OrderApi

All URIs are relative to *https://dom.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_order**](OrderApi.md#approve_order) | **POST** /order.Order/ApproveOrder | Approve Order
[**assign_shipment**](OrderApi.md#assign_shipment) | **POST** /order.Order/AssignShipment | Assign Shipment
[**calculate_refund**](OrderApi.md#calculate_refund) | **POST** /order.Order/CalculateRefund | Calculate Refund
[**cancel_fulfillment**](OrderApi.md#cancel_fulfillment) | **POST** /order.Order/CancelFulfillment | Cancel Fulfillment
[**cancel_order**](OrderApi.md#cancel_order) | **POST** /order.Order/CancelOrder | Cancel Order
[**cancel_shipment**](OrderApi.md#cancel_shipment) | **POST** /order.Order/CancelShipment | Cancel Shipment
[**complete_shipment_packing**](OrderApi.md#complete_shipment_packing) | **POST** /order.Order/CompleteShipmentPacking | Complete Shipment Packing
[**create_fulfillment**](OrderApi.md#create_fulfillment) | **POST** /order.Order/CreateFulfillment | Create Fulfillment
[**create_order**](OrderApi.md#create_order) | **POST** /order.Order/CreateOrder | Create Order
[**create_order_history**](OrderApi.md#create_order_history) | **POST** /order.Order/CreateHistory | Create Order History
[**create_payment**](OrderApi.md#create_payment) | **POST** /order.Order/CreatePayment | Create Payment
[**create_payment_transaction**](OrderApi.md#create_payment_transaction) | **POST** /order.Order/CreatePaymentTransaction | Create Payment Transaction
[**create_refund**](OrderApi.md#create_refund) | **POST** /order.Order/CreateRefund | Create Refund
[**create_refund_transaction**](OrderApi.md#create_refund_transaction) | **POST** /order.Order/CreateRefundTransaction | Create Refund Transaction
[**create_shipment**](OrderApi.md#create_shipment) | **POST** /order.Order/CreateShipment | Create Shipment
[**delete_order**](OrderApi.md#delete_order) | **POST** /order.Order/DeleteOrder | Delete Order
[**get_fulfillment**](OrderApi.md#get_fulfillment) | **POST** /order.Order/GetFulfillment | Get Fulfillment
[**get_order**](OrderApi.md#get_order) | **POST** /order.Order/GetOrder | Get Order
[**get_order_by_cart_id**](OrderApi.md#get_order_by_cart_id) | **POST** /order.Order/GetOrderByCartId | Get Order by Cart ID
[**get_order_by_order_number**](OrderApi.md#get_order_by_order_number) | **POST** /order.Order/GetOrderByOrderNumber | Get Order by Order Number
[**get_payment**](OrderApi.md#get_payment) | **POST** /order.Order/GetPayment | Get Payment
[**get_shipment**](OrderApi.md#get_shipment) | **POST** /order.Order/GetShipment | Get Shipment
[**get_transaction**](OrderApi.md#get_transaction) | **POST** /order.Order/GetTransaction | Get Transaction
[**hold_order**](OrderApi.md#hold_order) | **POST** /order.Order/HoldOrder | Hold Order
[**import_order**](OrderApi.md#import_order) | **POST** /order.Order/ImportOrder | Import Order
[**list_fulfillments**](OrderApi.md#list_fulfillments) | **POST** /order.Order/ListFulfillments | List Fulfillments
[**list_orders**](OrderApi.md#list_orders) | **POST** /order.Order/ListOrders | List Orders
[**list_orders_by_customer**](OrderApi.md#list_orders_by_customer) | **POST** /order.Order/ListOrdersByCustomer | List Orders by Customer
[**list_orders_by_numbers**](OrderApi.md#list_orders_by_numbers) | **POST** /order.Order/ListOrdersByNumbers | List Orders by Numbers
[**list_shipments**](OrderApi.md#list_shipments) | **POST** /order.Order/ListShipments | List Shipments
[**order_add_document**](OrderApi.md#order_add_document) | **POST** /order.Order/AddDocument | Documents
[**order_remove_document_by_code**](OrderApi.md#order_remove_document_by_code) | **POST** /order.Order/RemoveDocumentByCode | 
[**print_orders_labels**](OrderApi.md#print_orders_labels) | **POST** /order.Order/PrintOrdersLabels | Print Orders Labels
[**quash_fulfillment**](OrderApi.md#quash_fulfillment) | **POST** /order.Order/QuashFulfillment | Quash Fulfillment
[**quash_shipment**](OrderApi.md#quash_shipment) | **POST** /order.Order/QuashShipment | Quash Shipment
[**receive_fulfillment**](OrderApi.md#receive_fulfillment) | **POST** /order.Order/ReceiveFulfillment | Receive Fulfillment
[**report_fulfillment_error**](OrderApi.md#report_fulfillment_error) | **POST** /order.Order/ReportFulfillmentError | Report Fulfillment Error
[**report_fulfillment_not_resolvable**](OrderApi.md#report_fulfillment_not_resolvable) | **POST** /order.Order/ReportFulfillmentNotResolvable | Report Fulfillment Not Resolvable
[**report_fulfillment_ready**](OrderApi.md#report_fulfillment_ready) | **POST** /order.Order/ReportFulfillmentReady | Report Fulfillment Ready
[**report_shipment_delivery**](OrderApi.md#report_shipment_delivery) | **POST** /order.Order/ReportShipmentDelivery | Report Shipment Delivery
[**report_shipment_missing_stock**](OrderApi.md#report_shipment_missing_stock) | **POST** /order.Order/ReportShipmentMissingStock | Report Shipment Missing Stock
[**resolve_shipment_missing_stock**](OrderApi.md#resolve_shipment_missing_stock) | **POST** /order.Order/ResolveShipmentMissingStock | Resolve Shipment Missing Stock
[**retry_fulfillment**](OrderApi.md#retry_fulfillment) | **POST** /order.Order/RetryFulfillment | Retry Fulfillment
[**search_orders**](OrderApi.md#search_orders) | **POST** /order.Order/SearchOrders | Search Orders
[**send_fulfillment**](OrderApi.md#send_fulfillment) | **POST** /order.Order/SendFulfillment | Send Fulfillment
[**send_order_notification**](OrderApi.md#send_order_notification) | **POST** /order.Order/SendOrderNotification | Send Order Notification
[**start_fulfillment_processing**](OrderApi.md#start_fulfillment_processing) | **POST** /order.Order/StartFulfillmentProcessing | Start Fulfillment Processing
[**start_shipment_processing**](OrderApi.md#start_shipment_processing) | **POST** /order.Order/StartShipmentProcessing | Start Shipment Processing
[**unhold_order**](OrderApi.md#unhold_order) | **POST** /order.Order/UnholdOrder | Unhold Order
[**update_order**](OrderApi.md#update_order) | **POST** /order.Order/UpdateOrder | Update Order
[**update_payment**](OrderApi.md#update_payment) | **POST** /order.Order/UpdatePayment | Update Payment


# **approve_order**
> object approve_order(body)

Approve Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_approve_order_request import OrderApproveOrderRequest
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
    except Exception as e:
        print("Exception when calling OrderApi->approve_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderApproveOrderRequest**](OrderApproveOrderRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_shipment**
> object assign_shipment(body)

Assign Shipment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_assign_shipment_request import OrderAssignShipmentRequest
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
    body = order.OrderAssignShipmentRequest() # OrderAssignShipmentRequest | 

    try:
        # Assign Shipment
        api_response = api_instance.assign_shipment(body)
        print("The response of OrderApi->assign_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->assign_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderAssignShipmentRequest**](OrderAssignShipmentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_refund**
> OrderCalculateRefundResponse calculate_refund(body)

Calculate Refund

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_calculate_refund_request import OrderCalculateRefundRequest
from order.models.order_calculate_refund_response import OrderCalculateRefundResponse
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
    body = order.OrderCalculateRefundRequest() # OrderCalculateRefundRequest | 

    try:
        # Calculate Refund
        api_response = api_instance.calculate_refund(body)
        print("The response of OrderApi->calculate_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->calculate_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCalculateRefundRequest**](OrderCalculateRefundRequest.md)|  | 

### Return type

[**OrderCalculateRefundResponse**](OrderCalculateRefundResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_fulfillment**
> object cancel_fulfillment(body)

Cancel Fulfillment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_cancel_fulfillment_request import OrderCancelFulfillmentRequest
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
    body = order.OrderCancelFulfillmentRequest() # OrderCancelFulfillmentRequest | 

    try:
        # Cancel Fulfillment
        api_response = api_instance.cancel_fulfillment(body)
        print("The response of OrderApi->cancel_fulfillment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->cancel_fulfillment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCancelFulfillmentRequest**](OrderCancelFulfillmentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> object cancel_order(body)

Cancel Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_cancel_order_request import OrderCancelOrderRequest
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
    body = order.OrderCancelOrderRequest() # OrderCancelOrderRequest | 

    try:
        # Cancel Order
        api_response = api_instance.cancel_order(body)
        print("The response of OrderApi->cancel_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCancelOrderRequest**](OrderCancelOrderRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_shipment**
> object cancel_shipment(body)

Cancel Shipment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_cancel_shipment_request import OrderCancelShipmentRequest
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
    body = order.OrderCancelShipmentRequest() # OrderCancelShipmentRequest | 

    try:
        # Cancel Shipment
        api_response = api_instance.cancel_shipment(body)
        print("The response of OrderApi->cancel_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->cancel_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCancelShipmentRequest**](OrderCancelShipmentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_shipment_packing**
> object complete_shipment_packing(body)

Complete Shipment Packing

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_complete_shipment_packing_request import OrderCompleteShipmentPackingRequest
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
    body = order.OrderCompleteShipmentPackingRequest() # OrderCompleteShipmentPackingRequest | 

    try:
        # Complete Shipment Packing
        api_response = api_instance.complete_shipment_packing(body)
        print("The response of OrderApi->complete_shipment_packing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->complete_shipment_packing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCompleteShipmentPackingRequest**](OrderCompleteShipmentPackingRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fulfillment**
> OrderFulfillment create_fulfillment(body)

Create Fulfillment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_create_fulfillment_request import OrderCreateFulfillmentRequest
from order.models.order_fulfillment import OrderFulfillment
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
    body = order.OrderCreateFulfillmentRequest() # OrderCreateFulfillmentRequest | 

    try:
        # Create Fulfillment
        api_response = api_instance.create_fulfillment(body)
        print("The response of OrderApi->create_fulfillment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_fulfillment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCreateFulfillmentRequest**](OrderCreateFulfillmentRequest.md)|  | 

### Return type

[**OrderFulfillment**](OrderFulfillment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> OrderOrderData create_order(body)

Create Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_create_order_request import OrderCreateOrderRequest
from order.models.order_order_data import OrderOrderData
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
    body = order.OrderCreateOrderRequest() # OrderCreateOrderRequest | 

    try:
        # Create Order
        api_response = api_instance.create_order(body)
        print("The response of OrderApi->create_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCreateOrderRequest**](OrderCreateOrderRequest.md)|  | 

### Return type

[**OrderOrderData**](OrderOrderData.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order_history**
> OrderDataHistory create_order_history(body)

Create Order History

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_create_history_request import OrderCreateHistoryRequest
from order.models.order_data_history import OrderDataHistory
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
    body = order.OrderCreateHistoryRequest() # OrderCreateHistoryRequest | 

    try:
        # Create Order History
        api_response = api_instance.create_order_history(body)
        print("The response of OrderApi->create_order_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_order_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCreateHistoryRequest**](OrderCreateHistoryRequest.md)|  | 

### Return type

[**OrderDataHistory**](OrderDataHistory.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment**
> OrderPayment create_payment(body)

Create Payment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_create_payment_request import OrderCreatePaymentRequest
from order.models.order_payment import OrderPayment
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
    body = order.OrderCreatePaymentRequest() # OrderCreatePaymentRequest | 

    try:
        # Create Payment
        api_response = api_instance.create_payment(body)
        print("The response of OrderApi->create_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCreatePaymentRequest**](OrderCreatePaymentRequest.md)|  | 

### Return type

[**OrderPayment**](OrderPayment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_transaction**
> OrderTransaction create_payment_transaction(body)

Create Payment Transaction

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_create_payment_transaction_request import OrderCreatePaymentTransactionRequest
from order.models.order_transaction import OrderTransaction
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
    body = order.OrderCreatePaymentTransactionRequest() # OrderCreatePaymentTransactionRequest | 

    try:
        # Create Payment Transaction
        api_response = api_instance.create_payment_transaction(body)
        print("The response of OrderApi->create_payment_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_payment_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCreatePaymentTransactionRequest**](OrderCreatePaymentTransactionRequest.md)|  | 

### Return type

[**OrderTransaction**](OrderTransaction.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_refund**
> OrderRefund create_refund(body)

Create Refund

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_create_refund_request import OrderCreateRefundRequest
from order.models.order_refund import OrderRefund
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
    body = order.OrderCreateRefundRequest() # OrderCreateRefundRequest | 

    try:
        # Create Refund
        api_response = api_instance.create_refund(body)
        print("The response of OrderApi->create_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCreateRefundRequest**](OrderCreateRefundRequest.md)|  | 

### Return type

[**OrderRefund**](OrderRefund.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_refund_transaction**
> OrderTransaction create_refund_transaction(body)

Create Refund Transaction

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_create_refund_transaction_request import OrderCreateRefundTransactionRequest
from order.models.order_transaction import OrderTransaction
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
    body = order.OrderCreateRefundTransactionRequest() # OrderCreateRefundTransactionRequest | 

    try:
        # Create Refund Transaction
        api_response = api_instance.create_refund_transaction(body)
        print("The response of OrderApi->create_refund_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_refund_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCreateRefundTransactionRequest**](OrderCreateRefundTransactionRequest.md)|  | 

### Return type

[**OrderTransaction**](OrderTransaction.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_shipment**
> OrderShipment create_shipment(body)

Create Shipment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_create_shipment_request import OrderCreateShipmentRequest
from order.models.order_shipment import OrderShipment
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
    body = order.OrderCreateShipmentRequest() # OrderCreateShipmentRequest | 

    try:
        # Create Shipment
        api_response = api_instance.create_shipment(body)
        print("The response of OrderApi->create_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->create_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderCreateShipmentRequest**](OrderCreateShipmentRequest.md)|  | 

### Return type

[**OrderShipment**](OrderShipment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_order**
> object delete_order(body)

Delete Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_delete_order_request import OrderDeleteOrderRequest
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
    body = order.OrderDeleteOrderRequest() # OrderDeleteOrderRequest | 

    try:
        # Delete Order
        api_response = api_instance.delete_order(body)
        print("The response of OrderApi->delete_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->delete_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderDeleteOrderRequest**](OrderDeleteOrderRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fulfillment**
> OrderFulfillment get_fulfillment(body)

Get Fulfillment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_fulfillment import OrderFulfillment
from order.models.order_get_fulfillment_request import OrderGetFulfillmentRequest
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
    body = order.OrderGetFulfillmentRequest() # OrderGetFulfillmentRequest | 

    try:
        # Get Fulfillment
        api_response = api_instance.get_fulfillment(body)
        print("The response of OrderApi->get_fulfillment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_fulfillment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderGetFulfillmentRequest**](OrderGetFulfillmentRequest.md)|  | 

### Return type

[**OrderFulfillment**](OrderFulfillment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> OrderOrderData get_order(body)

Get Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_get_order_request import OrderGetOrderRequest
from order.models.order_order_data import OrderOrderData
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
    body = order.OrderGetOrderRequest() # OrderGetOrderRequest | 

    try:
        # Get Order
        api_response = api_instance.get_order(body)
        print("The response of OrderApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderGetOrderRequest**](OrderGetOrderRequest.md)|  | 

### Return type

[**OrderOrderData**](OrderOrderData.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_cart_id**
> OrderOrderData get_order_by_cart_id(body)

Get Order by Cart ID

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_get_order_by_cart_id_request import OrderGetOrderByCartIdRequest
from order.models.order_order_data import OrderOrderData
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
    body = order.OrderGetOrderByCartIdRequest() # OrderGetOrderByCartIdRequest | 

    try:
        # Get Order by Cart ID
        api_response = api_instance.get_order_by_cart_id(body)
        print("The response of OrderApi->get_order_by_cart_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_order_by_cart_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderGetOrderByCartIdRequest**](OrderGetOrderByCartIdRequest.md)|  | 

### Return type

[**OrderOrderData**](OrderOrderData.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_order_number**
> OrderOrderData get_order_by_order_number(body)

Get Order by Order Number

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_get_order_by_order_number_request import OrderGetOrderByOrderNumberRequest
from order.models.order_order_data import OrderOrderData
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
    body = order.OrderGetOrderByOrderNumberRequest() # OrderGetOrderByOrderNumberRequest | 

    try:
        # Get Order by Order Number
        api_response = api_instance.get_order_by_order_number(body)
        print("The response of OrderApi->get_order_by_order_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_order_by_order_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderGetOrderByOrderNumberRequest**](OrderGetOrderByOrderNumberRequest.md)|  | 

### Return type

[**OrderOrderData**](OrderOrderData.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment**
> OrderPayment get_payment(body)

Get Payment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_get_payment_request import OrderGetPaymentRequest
from order.models.order_payment import OrderPayment
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
    body = order.OrderGetPaymentRequest() # OrderGetPaymentRequest | 

    try:
        # Get Payment
        api_response = api_instance.get_payment(body)
        print("The response of OrderApi->get_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderGetPaymentRequest**](OrderGetPaymentRequest.md)|  | 

### Return type

[**OrderPayment**](OrderPayment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment**
> OrderShipment get_shipment(body)

Get Shipment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_get_shipment_request import OrderGetShipmentRequest
from order.models.order_shipment import OrderShipment
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
    body = order.OrderGetShipmentRequest() # OrderGetShipmentRequest | 

    try:
        # Get Shipment
        api_response = api_instance.get_shipment(body)
        print("The response of OrderApi->get_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderGetShipmentRequest**](OrderGetShipmentRequest.md)|  | 

### Return type

[**OrderShipment**](OrderShipment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> OrderTransaction get_transaction(body)

Get Transaction

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_get_transaction_request import OrderGetTransactionRequest
from order.models.order_transaction import OrderTransaction
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
    body = order.OrderGetTransactionRequest() # OrderGetTransactionRequest | 

    try:
        # Get Transaction
        api_response = api_instance.get_transaction(body)
        print("The response of OrderApi->get_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->get_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderGetTransactionRequest**](OrderGetTransactionRequest.md)|  | 

### Return type

[**OrderTransaction**](OrderTransaction.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hold_order**
> object hold_order(body)

Hold Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_hold_order_request import OrderHoldOrderRequest
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
    body = order.OrderHoldOrderRequest() # OrderHoldOrderRequest | 

    try:
        # Hold Order
        api_response = api_instance.hold_order(body)
        print("The response of OrderApi->hold_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->hold_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderHoldOrderRequest**](OrderHoldOrderRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_order**
> OrderOrderData import_order(body)

Import Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_import_order_request import OrderImportOrderRequest
from order.models.order_order_data import OrderOrderData
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
    body = order.OrderImportOrderRequest() # OrderImportOrderRequest | 

    try:
        # Import Order
        api_response = api_instance.import_order(body)
        print("The response of OrderApi->import_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->import_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderImportOrderRequest**](OrderImportOrderRequest.md)|  | 

### Return type

[**OrderOrderData**](OrderOrderData.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_fulfillments**
> OrderListFulfillmentsResponse list_fulfillments(body)

List Fulfillments

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_list_fulfillments_request import OrderListFulfillmentsRequest
from order.models.order_list_fulfillments_response import OrderListFulfillmentsResponse
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
    body = order.OrderListFulfillmentsRequest() # OrderListFulfillmentsRequest | 

    try:
        # List Fulfillments
        api_response = api_instance.list_fulfillments(body)
        print("The response of OrderApi->list_fulfillments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->list_fulfillments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderListFulfillmentsRequest**](OrderListFulfillmentsRequest.md)|  | 

### Return type

[**OrderListFulfillmentsResponse**](OrderListFulfillmentsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> OrderListOrdersResponse list_orders(body)

List Orders

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_list_orders_request import OrderListOrdersRequest
from order.models.order_list_orders_response import OrderListOrdersResponse
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
    body = order.OrderListOrdersRequest() # OrderListOrdersRequest | 

    try:
        # List Orders
        api_response = api_instance.list_orders(body)
        print("The response of OrderApi->list_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->list_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderListOrdersRequest**](OrderListOrdersRequest.md)|  | 

### Return type

[**OrderListOrdersResponse**](OrderListOrdersResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders_by_customer**
> OrderListOrdersByCustomerResponse list_orders_by_customer(body)

List Orders by Customer

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_list_orders_by_customer_request import OrderListOrdersByCustomerRequest
from order.models.order_list_orders_by_customer_response import OrderListOrdersByCustomerResponse
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
    body = order.OrderListOrdersByCustomerRequest() # OrderListOrdersByCustomerRequest | 

    try:
        # List Orders by Customer
        api_response = api_instance.list_orders_by_customer(body)
        print("The response of OrderApi->list_orders_by_customer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->list_orders_by_customer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderListOrdersByCustomerRequest**](OrderListOrdersByCustomerRequest.md)|  | 

### Return type

[**OrderListOrdersByCustomerResponse**](OrderListOrdersByCustomerResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders_by_numbers**
> OrderListOrdersByNumbersResponse list_orders_by_numbers(body)

List Orders by Numbers

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_list_orders_by_numbers_request import OrderListOrdersByNumbersRequest
from order.models.order_list_orders_by_numbers_response import OrderListOrdersByNumbersResponse
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
    body = order.OrderListOrdersByNumbersRequest() # OrderListOrdersByNumbersRequest | 

    try:
        # List Orders by Numbers
        api_response = api_instance.list_orders_by_numbers(body)
        print("The response of OrderApi->list_orders_by_numbers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->list_orders_by_numbers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderListOrdersByNumbersRequest**](OrderListOrdersByNumbersRequest.md)|  | 

### Return type

[**OrderListOrdersByNumbersResponse**](OrderListOrdersByNumbersResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipments**
> OrderListShipmentsResponse list_shipments(body)

List Shipments

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_list_shipments_request import OrderListShipmentsRequest
from order.models.order_list_shipments_response import OrderListShipmentsResponse
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
    body = order.OrderListShipmentsRequest() # OrderListShipmentsRequest | 

    try:
        # List Shipments
        api_response = api_instance.list_shipments(body)
        print("The response of OrderApi->list_shipments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->list_shipments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderListShipmentsRequest**](OrderListShipmentsRequest.md)|  | 

### Return type

[**OrderListShipmentsResponse**](OrderListShipmentsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_add_document**
> object order_add_document(body)

Documents

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_add_document_request import OrderAddDocumentRequest
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
    body = order.OrderAddDocumentRequest() # OrderAddDocumentRequest | 

    try:
        # Documents
        api_response = api_instance.order_add_document(body)
        print("The response of OrderApi->order_add_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_add_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderAddDocumentRequest**](OrderAddDocumentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_remove_document_by_code**
> object order_remove_document_by_code(body)



### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_remove_document_by_code_request import OrderRemoveDocumentByCodeRequest
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
    body = order.OrderRemoveDocumentByCodeRequest() # OrderRemoveDocumentByCodeRequest | 

    try:
        api_response = api_instance.order_remove_document_by_code(body)
        print("The response of OrderApi->order_remove_document_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->order_remove_document_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderRemoveDocumentByCodeRequest**](OrderRemoveDocumentByCodeRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **print_orders_labels**
> OrderPrintOrdersLabelsResponse print_orders_labels(body)

Print Orders Labels

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_print_orders_labels_request import OrderPrintOrdersLabelsRequest
from order.models.order_print_orders_labels_response import OrderPrintOrdersLabelsResponse
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
    body = order.OrderPrintOrdersLabelsRequest() # OrderPrintOrdersLabelsRequest | 

    try:
        # Print Orders Labels
        api_response = api_instance.print_orders_labels(body)
        print("The response of OrderApi->print_orders_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->print_orders_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderPrintOrdersLabelsRequest**](OrderPrintOrdersLabelsRequest.md)|  | 

### Return type

[**OrderPrintOrdersLabelsResponse**](OrderPrintOrdersLabelsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quash_fulfillment**
> object quash_fulfillment(body)

Quash Fulfillment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_quash_fulfillment_request import OrderQuashFulfillmentRequest
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
    body = order.OrderQuashFulfillmentRequest() # OrderQuashFulfillmentRequest | 

    try:
        # Quash Fulfillment
        api_response = api_instance.quash_fulfillment(body)
        print("The response of OrderApi->quash_fulfillment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->quash_fulfillment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderQuashFulfillmentRequest**](OrderQuashFulfillmentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quash_shipment**
> object quash_shipment(body)

Quash Shipment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_quash_shipment_request import OrderQuashShipmentRequest
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
    body = order.OrderQuashShipmentRequest() # OrderQuashShipmentRequest | 

    try:
        # Quash Shipment
        api_response = api_instance.quash_shipment(body)
        print("The response of OrderApi->quash_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->quash_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderQuashShipmentRequest**](OrderQuashShipmentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **receive_fulfillment**
> object receive_fulfillment(body)

Receive Fulfillment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_receive_fulfillment_request import OrderReceiveFulfillmentRequest
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
    body = order.OrderReceiveFulfillmentRequest() # OrderReceiveFulfillmentRequest | 

    try:
        # Receive Fulfillment
        api_response = api_instance.receive_fulfillment(body)
        print("The response of OrderApi->receive_fulfillment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->receive_fulfillment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderReceiveFulfillmentRequest**](OrderReceiveFulfillmentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_fulfillment_error**
> object report_fulfillment_error(body)

Report Fulfillment Error

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_report_fulfillment_error_request import OrderReportFulfillmentErrorRequest
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
    body = order.OrderReportFulfillmentErrorRequest() # OrderReportFulfillmentErrorRequest | 

    try:
        # Report Fulfillment Error
        api_response = api_instance.report_fulfillment_error(body)
        print("The response of OrderApi->report_fulfillment_error:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->report_fulfillment_error: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderReportFulfillmentErrorRequest**](OrderReportFulfillmentErrorRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_fulfillment_not_resolvable**
> object report_fulfillment_not_resolvable(body)

Report Fulfillment Not Resolvable

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_report_fulfillment_not_resolvable_request import OrderReportFulfillmentNotResolvableRequest
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
    body = order.OrderReportFulfillmentNotResolvableRequest() # OrderReportFulfillmentNotResolvableRequest | 

    try:
        # Report Fulfillment Not Resolvable
        api_response = api_instance.report_fulfillment_not_resolvable(body)
        print("The response of OrderApi->report_fulfillment_not_resolvable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->report_fulfillment_not_resolvable: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderReportFulfillmentNotResolvableRequest**](OrderReportFulfillmentNotResolvableRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_fulfillment_ready**
> object report_fulfillment_ready(body)

Report Fulfillment Ready

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_report_fulfillment_ready_request import OrderReportFulfillmentReadyRequest
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
    body = order.OrderReportFulfillmentReadyRequest() # OrderReportFulfillmentReadyRequest | 

    try:
        # Report Fulfillment Ready
        api_response = api_instance.report_fulfillment_ready(body)
        print("The response of OrderApi->report_fulfillment_ready:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->report_fulfillment_ready: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderReportFulfillmentReadyRequest**](OrderReportFulfillmentReadyRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_shipment_delivery**
> object report_shipment_delivery(body)

Report Shipment Delivery

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_report_shipment_delivery_request import OrderReportShipmentDeliveryRequest
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
    body = order.OrderReportShipmentDeliveryRequest() # OrderReportShipmentDeliveryRequest | 

    try:
        # Report Shipment Delivery
        api_response = api_instance.report_shipment_delivery(body)
        print("The response of OrderApi->report_shipment_delivery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->report_shipment_delivery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderReportShipmentDeliveryRequest**](OrderReportShipmentDeliveryRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_shipment_missing_stock**
> object report_shipment_missing_stock(body)

Report Shipment Missing Stock

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_report_shipment_missing_stock_request import OrderReportShipmentMissingStockRequest
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
    body = order.OrderReportShipmentMissingStockRequest() # OrderReportShipmentMissingStockRequest | 

    try:
        # Report Shipment Missing Stock
        api_response = api_instance.report_shipment_missing_stock(body)
        print("The response of OrderApi->report_shipment_missing_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->report_shipment_missing_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderReportShipmentMissingStockRequest**](OrderReportShipmentMissingStockRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_shipment_missing_stock**
> object resolve_shipment_missing_stock(body)

Resolve Shipment Missing Stock

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_resolve_shipment_missing_stock_request import OrderResolveShipmentMissingStockRequest
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
    body = order.OrderResolveShipmentMissingStockRequest() # OrderResolveShipmentMissingStockRequest | 

    try:
        # Resolve Shipment Missing Stock
        api_response = api_instance.resolve_shipment_missing_stock(body)
        print("The response of OrderApi->resolve_shipment_missing_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->resolve_shipment_missing_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderResolveShipmentMissingStockRequest**](OrderResolveShipmentMissingStockRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_fulfillment**
> object retry_fulfillment(body)

Retry Fulfillment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_retry_fulfillment_request import OrderRetryFulfillmentRequest
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
    body = order.OrderRetryFulfillmentRequest() # OrderRetryFulfillmentRequest | 

    try:
        # Retry Fulfillment
        api_response = api_instance.retry_fulfillment(body)
        print("The response of OrderApi->retry_fulfillment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->retry_fulfillment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderRetryFulfillmentRequest**](OrderRetryFulfillmentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_orders**
> OrderSearchOrdersResponse search_orders(body)

Search Orders

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_search_orders_request import OrderSearchOrdersRequest
from order.models.order_search_orders_response import OrderSearchOrdersResponse
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
    body = order.OrderSearchOrdersRequest() # OrderSearchOrdersRequest | 

    try:
        # Search Orders
        api_response = api_instance.search_orders(body)
        print("The response of OrderApi->search_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->search_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSearchOrdersRequest**](OrderSearchOrdersRequest.md)|  | 

### Return type

[**OrderSearchOrdersResponse**](OrderSearchOrdersResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_fulfillment**
> object send_fulfillment(body)

Send Fulfillment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_send_fulfillment_request import OrderSendFulfillmentRequest
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
    body = order.OrderSendFulfillmentRequest() # OrderSendFulfillmentRequest | 

    try:
        # Send Fulfillment
        api_response = api_instance.send_fulfillment(body)
        print("The response of OrderApi->send_fulfillment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->send_fulfillment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSendFulfillmentRequest**](OrderSendFulfillmentRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_order_notification**
> object send_order_notification(body)

Send Order Notification

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_send_order_notification_request import OrderSendOrderNotificationRequest
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
    body = order.OrderSendOrderNotificationRequest() # OrderSendOrderNotificationRequest | 

    try:
        # Send Order Notification
        api_response = api_instance.send_order_notification(body)
        print("The response of OrderApi->send_order_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->send_order_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderSendOrderNotificationRequest**](OrderSendOrderNotificationRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_fulfillment_processing**
> object start_fulfillment_processing(body)

Start Fulfillment Processing

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_start_fulfillment_processing_request import OrderStartFulfillmentProcessingRequest
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
    body = order.OrderStartFulfillmentProcessingRequest() # OrderStartFulfillmentProcessingRequest | 

    try:
        # Start Fulfillment Processing
        api_response = api_instance.start_fulfillment_processing(body)
        print("The response of OrderApi->start_fulfillment_processing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->start_fulfillment_processing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderStartFulfillmentProcessingRequest**](OrderStartFulfillmentProcessingRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_shipment_processing**
> object start_shipment_processing(body)

Start Shipment Processing

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_start_shipment_processing_request import OrderStartShipmentProcessingRequest
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
    body = order.OrderStartShipmentProcessingRequest() # OrderStartShipmentProcessingRequest | 

    try:
        # Start Shipment Processing
        api_response = api_instance.start_shipment_processing(body)
        print("The response of OrderApi->start_shipment_processing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->start_shipment_processing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderStartShipmentProcessingRequest**](OrderStartShipmentProcessingRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unhold_order**
> object unhold_order(body)

Unhold Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_unhold_order_request import OrderUnholdOrderRequest
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
    body = order.OrderUnholdOrderRequest() # OrderUnholdOrderRequest | 

    try:
        # Unhold Order
        api_response = api_instance.unhold_order(body)
        print("The response of OrderApi->unhold_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->unhold_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderUnholdOrderRequest**](OrderUnholdOrderRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order**
> OrderOrderData update_order(body)

Update Order

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_order_data import OrderOrderData
from order.models.order_update_order_request import OrderUpdateOrderRequest
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
    body = order.OrderUpdateOrderRequest() # OrderUpdateOrderRequest | 

    try:
        # Update Order
        api_response = api_instance.update_order(body)
        print("The response of OrderApi->update_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->update_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderUpdateOrderRequest**](OrderUpdateOrderRequest.md)|  | 

### Return type

[**OrderOrderData**](OrderOrderData.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> OrderPayment update_payment(body)

Update Payment

### Example

* Api Key Authentication (Authorization):

```python
import order
from order.models.order_payment import OrderPayment
from order.models.order_update_payment_request import OrderUpdatePaymentRequest
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
    body = order.OrderUpdatePaymentRequest() # OrderUpdatePaymentRequest | 

    try:
        # Update Payment
        api_response = api_instance.update_payment(body)
        print("The response of OrderApi->update_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrderApi->update_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderUpdatePaymentRequest**](OrderUpdatePaymentRequest.md)|  | 

### Return type

[**OrderPayment**](OrderPayment.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

