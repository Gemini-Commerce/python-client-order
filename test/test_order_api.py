# coding: utf-8

"""
    order Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@gemini-commerce.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from order.api.order_api import OrderApi


class TestOrderApi(unittest.TestCase):
    """OrderApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrderApi()

    def tearDown(self) -> None:
        pass

    def test_approve_order(self) -> None:
        """Test case for approve_order

        Approve Order
        """
        pass

    def test_assign_shipment(self) -> None:
        """Test case for assign_shipment

        Assign Shipment
        """
        pass

    def test_calculate_refund(self) -> None:
        """Test case for calculate_refund

        Calculate Refund
        """
        pass

    def test_cancel_fulfillment(self) -> None:
        """Test case for cancel_fulfillment

        Cancel Fulfillment
        """
        pass

    def test_cancel_order(self) -> None:
        """Test case for cancel_order

        Cancel Order
        """
        pass

    def test_cancel_shipment(self) -> None:
        """Test case for cancel_shipment

        Cancel Shipment
        """
        pass

    def test_complete_shipment_packing(self) -> None:
        """Test case for complete_shipment_packing

        Complete Shipment Packing
        """
        pass

    def test_create_fulfillment(self) -> None:
        """Test case for create_fulfillment

        Create Fulfillment
        """
        pass

    def test_create_order(self) -> None:
        """Test case for create_order

        Create Order
        """
        pass

    def test_create_order_history(self) -> None:
        """Test case for create_order_history

        Create Order History
        """
        pass

    def test_create_payment(self) -> None:
        """Test case for create_payment

        Create Payment
        """
        pass

    def test_create_payment_transaction(self) -> None:
        """Test case for create_payment_transaction

        Create Payment Transaction
        """
        pass

    def test_create_refund(self) -> None:
        """Test case for create_refund

        Create Refund
        """
        pass

    def test_create_refund_transaction(self) -> None:
        """Test case for create_refund_transaction

        Create Refund Transaction
        """
        pass

    def test_create_shipment(self) -> None:
        """Test case for create_shipment

        Create Shipment
        """
        pass

    def test_delete_order(self) -> None:
        """Test case for delete_order

        Delete Order
        """
        pass

    def test_get_fulfillment(self) -> None:
        """Test case for get_fulfillment

        Get Fulfillment
        """
        pass

    def test_get_order(self) -> None:
        """Test case for get_order

        Get Order
        """
        pass

    def test_get_order_by_cart_id(self) -> None:
        """Test case for get_order_by_cart_id

        Get Order by Cart ID
        """
        pass

    def test_get_order_by_order_number(self) -> None:
        """Test case for get_order_by_order_number

        Get Order by Order Number
        """
        pass

    def test_get_payment(self) -> None:
        """Test case for get_payment

        Get Payment
        """
        pass

    def test_get_shipment(self) -> None:
        """Test case for get_shipment

        Get Shipment
        """
        pass

    def test_get_transaction(self) -> None:
        """Test case for get_transaction

        Get Transaction
        """
        pass

    def test_hold_order(self) -> None:
        """Test case for hold_order

        Hold Order
        """
        pass

    def test_import_order(self) -> None:
        """Test case for import_order

        Import Order
        """
        pass

    def test_list_fulfillments(self) -> None:
        """Test case for list_fulfillments

        List Fulfillments
        """
        pass

    def test_list_orders(self) -> None:
        """Test case for list_orders

        List Orders
        """
        pass

    def test_list_orders_by_customer(self) -> None:
        """Test case for list_orders_by_customer

        List Orders by Customer
        """
        pass

    def test_list_orders_by_numbers(self) -> None:
        """Test case for list_orders_by_numbers

        List Orders by Numbers
        """
        pass

    def test_list_shipments(self) -> None:
        """Test case for list_shipments

        List Shipments
        """
        pass

    def test_print_orders_labels(self) -> None:
        """Test case for print_orders_labels

        Print Orders Labels
        """
        pass

    def test_quash_fulfillment(self) -> None:
        """Test case for quash_fulfillment

        Quash Fulfillment
        """
        pass

    def test_quash_shipment(self) -> None:
        """Test case for quash_shipment

        Quash Shipment
        """
        pass

    def test_receive_fulfillment(self) -> None:
        """Test case for receive_fulfillment

        Receive Fulfillment
        """
        pass

    def test_report_fulfillment_error(self) -> None:
        """Test case for report_fulfillment_error

        Report Fulfillment Error
        """
        pass

    def test_report_fulfillment_not_resolvable(self) -> None:
        """Test case for report_fulfillment_not_resolvable

        Report Fulfillment Not Resolvable
        """
        pass

    def test_report_fulfillment_ready(self) -> None:
        """Test case for report_fulfillment_ready

        Report Fulfillment Ready
        """
        pass

    def test_report_shipment_delivery(self) -> None:
        """Test case for report_shipment_delivery

        Report Shipment Delivery
        """
        pass

    def test_report_shipment_missing_stock(self) -> None:
        """Test case for report_shipment_missing_stock

        Report Shipment Missing Stock
        """
        pass

    def test_resolve_shipment_missing_stock(self) -> None:
        """Test case for resolve_shipment_missing_stock

        Resolve Shipment Missing Stock
        """
        pass

    def test_retry_fulfillment(self) -> None:
        """Test case for retry_fulfillment

        Retry Fulfillment
        """
        pass

    def test_search_orders(self) -> None:
        """Test case for search_orders

        Search Orders
        """
        pass

    def test_send_fulfillment(self) -> None:
        """Test case for send_fulfillment

        Send Fulfillment
        """
        pass

    def test_send_order_notification(self) -> None:
        """Test case for send_order_notification

        Send Order Notification
        """
        pass

    def test_start_fulfillment_processing(self) -> None:
        """Test case for start_fulfillment_processing

        Start Fulfillment Processing
        """
        pass

    def test_start_shipment_processing(self) -> None:
        """Test case for start_shipment_processing

        Start Shipment Processing
        """
        pass

    def test_unhold_order(self) -> None:
        """Test case for unhold_order

        Unhold Order
        """
        pass

    def test_update_order(self) -> None:
        """Test case for update_order

        Update Order
        """
        pass

    def test_update_payment(self) -> None:
        """Test case for update_payment

        Update Payment
        """
        pass


if __name__ == '__main__':
    unittest.main()