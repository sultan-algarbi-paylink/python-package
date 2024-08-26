from typing import Optional
from .paylink_gateway_order_request import PaylinkGatewayOrderRequest


class PaylinkInvoiceResponse:
    def __init__(
        self,
        gateway_order_request: PaylinkGatewayOrderRequest,
        amount: float,
        transaction_no: str,
        order_status: str,
        payment_errors: Optional[any],
        url: str,
        qr_url: str,
        mobile_url: str,
        check_url: str,
        success: bool,
        digital_order: bool,
        foreign_currency_rate: Optional[any],
        payment_receipt: Optional[any],
        metadata: Optional[any],
    ):
        self.gateway_order_request = gateway_order_request
        self.amount = amount
        self.transaction_no = transaction_no
        self.order_status = order_status
        self.payment_errors = payment_errors
        self.url = url
        self.qr_url = qr_url
        self.mobile_url = mobile_url
        self.check_url = check_url
        self.success = success
        self.digital_order = digital_order
        self.foreign_currency_rate = foreign_currency_rate
        self.payment_receipt = payment_receipt
        self.metadata = metadata

    @classmethod
    def from_response_data(cls, data: dict):
        gateway_order_request = PaylinkGatewayOrderRequest.from_dict(
            data.get("gatewayOrderRequest", {})
        )

        return cls(
            gateway_order_request=gateway_order_request,
            amount=data.get("amount", 0.0),
            transaction_no=data.get("transactionNo", ""),
            order_status=data.get("orderStatus", ""),
            payment_errors=data.get("paymentErrors"),
            url=data.get("url", ""),
            qr_url=data.get("qrUrl", ""),
            mobile_url=data.get("mobileUrl", ""),
            check_url=data.get("checkUrl", ""),
            success=data.get("success", False),
            digital_order=data.get("digitalOrder", False),
            foreign_currency_rate=data.get("foreignCurrencyRate"),
            payment_receipt=data.get("paymentReceipt"),
            metadata=data.get("metadata"),
        )
