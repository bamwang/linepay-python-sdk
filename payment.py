from . import BaseLINEPayAPI

class LINEPayPayment(BaseLINEPayAPI):
    def request(self,
        order_id,
        product_name,
        amount,
        currency, 
        confirm_url,
        product_image_url=None,
        confirm_url_type="CLIENT",
        cancel_url=None,
        ):
        data = {
            'orderId': order_id,
            'productName': product_name,
            'amount': amount,
            'currency': currency,
            'confirmUrl': confirm_url,
            'productImageUrl': product_image_url,
            'confirmUrlType': confirm_url_type,
            'cancelUrl': cancel_url,
        }
        self._post('/v2/payments/request', data=data)

    def confirm(
        self,
        transactionId,
        amount,
        currency,
    ):
        data = {
            'amount': amount,
            'currency': currency,
        }
        self._post('/v2/payments/%s/confirm' % transactionId, data=data)

    def refund(
        self,
        transactionId,
        refund_amount=None,
    ):
        data = {
            'refundAmount': refund_amount,
        }
        self._post('/v2/payments/%s/refund' % transactionId, data=data)
