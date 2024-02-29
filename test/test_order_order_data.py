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
import datetime

from order.models.order_order_data import OrderOrderData

class TestOrderOrderData(unittest.TestCase):
    """OrderOrderData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrderOrderData:
        """Test OrderOrderData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrderOrderData`
        """
        model = OrderOrderData()
        if include_optional:
            return OrderOrderData(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                grn = '',
                number = '',
                status = '',
                channel = '',
                market = '',
                locale = '',
                additional_info = order.models.additional_info.additionalInfo(),
                documents = [
                    order.models.order_data_document.OrderDataDocument(
                        code = '', 
                        label = '', 
                        asset_grn = '', 
                        url = '', 
                        inserted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                items = [
                    order.models.order_order_data_item.orderOrderDataItem(
                        id = '', 
                        product_grn = '', 
                        qty_ordered = 56, 
                        qty_committed = 56, 
                        unit_sale_price = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), 
                        unit_list_price = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), 
                        unit_base_price = , 
                        unit_vat_amount = , 
                        row_sale_price = , 
                        row_list_price = , 
                        row_vat_amount = , 
                        discount_amount = , 
                        row_base_price = , 
                        unit_custom_price = , 
                        row_custom_price = , 
                        vat_percentage = 1.337, 
                        vat_inaccurate = True, 
                        vat_calculated = True, 
                        product_name = '', 
                        product_code = '', 
                        product_sku = '', 
                        product_options = '', 
                        product_img = '', 
                        product_data = '', 
                        shipment_info_reference = '', 
                        promotion_grn = [
                            ''
                            ], 
                        product_is_virtual = True, 
                        product_configuration = [
                            order.models.item_product_configuration_step.ItemProductConfigurationStep(
                                id = '', 
                                grn = '', 
                                label = '', 
                                description = '', 
                                options = [
                                    order.models.product_configuration_step_option.ProductConfigurationStepOption(
                                        id = '', 
                                        grn = '', 
                                        label = '', 
                                        price_variation = , 
                                        image = order.models.option_image.OptionImage(
                                            grn = '', 
                                            url = '', ), 
                                        has_quantity = True, 
                                        quantity = 56, )
                                    ], )
                            ], )
                    ],
                payments = [
                    order.models.order_payment.orderPayment(
                        order_id = '', 
                        id = '', 
                        code = '', 
                        additional_info = '', 
                        amounts = [
                            order.models.order_payment_amount.orderPaymentAmount(
                                code = 'UNKNOWN', 
                                value = order.models.order_money.orderMoney(
                                    units = '', 
                                    micros = 56, ), )
                            ], 
                        cc_info = order.models.payment_cc_info.PaymentCcInfo(
                            approval = '', 
                            exp_month = 56, 
                            exp_year = '', 
                            last4 = '', 
                            number_enc = '', 
                            owner = '', 
                            avs_status = '', 
                            type = '', ), 
                        transactions = [
                            order.models.order_transaction.orderTransaction(
                                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                payment_id = '', 
                                id = '', 
                                type = 'UNKNOWN', 
                                additional_info = '', 
                                child_transactions = [
                                    order.models.order_transaction.orderTransaction(
                                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                        payment_id = '', 
                                        id = '', 
                                        additional_info = '', )
                                    ], )
                            ], )
                    ],
                shipments = [
                    order.models.order_shipment.orderShipment(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        order_id = '', 
                        id = '', 
                        status = '', 
                        items = [
                            order.models.order_shipment_item.orderShipmentItem(
                                order_item_id = '', 
                                qty = 56, 
                                row_weight = '', )
                            ], 
                        address = order.models.order_postal_address.orderPostalAddress(
                            revision = 56, 
                            region_code = '', 
                            language_code = '', 
                            postal_code = '', 
                            sorting_code = '', 
                            administrative_area = '', 
                            locality = '', 
                            sublocality = '', 
                            address_lines = [
                                ''
                                ], 
                            recipients = [
                                ''
                                ], 
                            organization = '', 
                            phone_number = '', 
                            additional_info = order.models.additional_info.additionalInfo(), ), 
                        from_address = order.models.order_postal_address.orderPostalAddress(
                            revision = 56, 
                            region_code = '', 
                            language_code = '', 
                            postal_code = '', 
                            sorting_code = '', 
                            administrative_area = '', 
                            locality = '', 
                            sublocality = '', 
                            organization = '', 
                            phone_number = '', 
                            additional_info = order.models.additional_info.additionalInfo(), ), 
                        return_address = , 
                        tracking = [
                            order.models.shipment_tracking.ShipmentTracking(
                                carrier_code = '', 
                                carrier_title = '', 
                                url = '', 
                                number = '', 
                                label_url = '', )
                            ], 
                        return_tracking = [
                            order.models.shipment_tracking.ShipmentTracking(
                                carrier_code = '', 
                                carrier_title = '', 
                                url = '', 
                                number = '', 
                                label_url = '', )
                            ], )
                    ],
                payments_info = [
                    order.models.order_data_payment_info.OrderDataPaymentInfo(
                        code = '', 
                        additional_info = '', 
                        amount = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), 
                        fee = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), 
                        vat_amount = , 
                        vat_percentage = 1.337, 
                        vat_inaccurate = True, 
                        vat_calculated = True, 
                        title = order.models.order_localized_text.orderLocalizedText(
                            value = {
                                'key' : ''
                                }, ), 
                        label = order.models.order_localized_text.orderLocalizedText(), )
                    ],
                shipments_info = [
                    order.models.order_data_shipment_info.OrderDataShipmentInfo(
                        reference = '', 
                        code = '', 
                        method = '', 
                        title = '', 
                        additional_info = '', 
                        amount = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), 
                        fee = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), 
                        vat_amount = , 
                        vat_percentage = 1.337, 
                        vat_inaccurate = True, 
                        vat_calculated = True, 
                        grn = '', 
                        from_address = order.models.order_postal_address.orderPostalAddress(
                            revision = 56, 
                            region_code = '', 
                            language_code = '', 
                            postal_code = '', 
                            sorting_code = '', 
                            administrative_area = '', 
                            locality = '', 
                            sublocality = '', 
                            address_lines = [
                                ''
                                ], 
                            recipients = [
                                ''
                                ], 
                            organization = '', 
                            phone_number = '', 
                            additional_info = order.models.additional_info.additionalInfo(), ), 
                        return_address = order.models.order_postal_address.orderPostalAddress(
                            revision = 56, 
                            region_code = '', 
                            language_code = '', 
                            postal_code = '', 
                            sorting_code = '', 
                            administrative_area = '', 
                            locality = '', 
                            sublocality = '', 
                            organization = '', 
                            phone_number = '', 
                            additional_info = order.models.additional_info.additionalInfo(), ), )
                    ],
                promotions = [
                    order.models.order_data_promotion_info.OrderDataPromotionInfo(
                        promotion_grn = '', 
                        type = '', 
                        additional_info = '', 
                        name = '', 
                        description = '', 
                        amount = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), 
                        coupon_code = '', 
                        vat_amount = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), 
                        vat_percentage = 1.337, 
                        vat_inaccurate = True, 
                        vat_calculated = True, )
                    ],
                currency = 'XXX',
                subtotals = {
                    'key' : order.models.order_data_subtotal.OrderDataSubtotal(
                        code = 'UNKNOWN', 
                        value = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), )
                    },
                totals = {
                    'key' : order.models.order_data_total.OrderDataTotal(
                        code = 'UNKNOWN', 
                        value = order.models.order_money.orderMoney(
                            units = '', 
                            micros = 56, ), )
                    },
                vat_included = True,
                billing_address = order.models.order_postal_address.orderPostalAddress(
                    revision = 56, 
                    region_code = '', 
                    language_code = '', 
                    postal_code = '', 
                    sorting_code = '', 
                    administrative_area = '', 
                    locality = '', 
                    sublocality = '', 
                    address_lines = [
                        ''
                        ], 
                    recipients = [
                        ''
                        ], 
                    organization = '', 
                    phone_number = '', 
                    additional_info = order.models.additional_info.additionalInfo(), ),
                shipping_address = order.models.order_postal_address.orderPostalAddress(
                    revision = 56, 
                    region_code = '', 
                    language_code = '', 
                    postal_code = '', 
                    sorting_code = '', 
                    administrative_area = '', 
                    locality = '', 
                    sublocality = '', 
                    address_lines = [
                        ''
                        ], 
                    recipients = [
                        ''
                        ], 
                    organization = '', 
                    phone_number = '', 
                    additional_info = order.models.additional_info.additionalInfo(), ),
                customer_info = order.models.order_data_customer_info.OrderDataCustomerInfo(
                    grn = '', 
                    firstname = '', 
                    lastname = '', 
                    email = '', 
                    phone = '', 
                    segment = '', 
                    data = '', 
                    certified_email = '', 
                    tax_code = '', 
                    sdi_code = '', 
                    fiscal_code = '', 
                    company_name = '', 
                    agent_grn = '', ),
                cart_grn = '',
                on_hold = True,
                history_events = [
                    order.models.order_data_history.OrderDataHistory(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        status = '', 
                        comment = '', )
                    ],
                fulfillments = [
                    order.models.order_fulfillment.orderFulfillment(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        order_id = '', 
                        id = '', 
                        status = '', 
                        items = [
                            order.models.order_fulfillment_item.orderFulfillmentItem(
                                order_item_id = '', 
                                qty = 56, )
                            ], )
                    ],
                notes = '',
                is_deleted = True,
                inserted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return OrderOrderData(
                locale = '',
        )
        """

    def testOrderOrderData(self):
        """Test OrderOrderData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
