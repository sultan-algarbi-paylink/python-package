from typing import List, Optional
from .paylink_product import PaylinkProduct


class PaylinkGatewayOrderRequest:
    def __init__(
        self,
        amount: float,
        order_number: str,
        call_back_url: str,
        client_email: str,
        client_name: str,
        client_mobile: str,
        note: str,
        cancel_url: str,
        products: List[PaylinkProduct],
        supported_card_brands: List[str],
        currency: str,
        sms_message: str,
        display_pending: bool,
        receivers: Optional[any],
        partner_portion: Optional[any],
        metadata: Optional[any],
    ):
        self.amount = amount
        self.order_number = order_number
        self.call_back_url = call_back_url
        self.client_email = client_email
        self.client_name = client_name
        self.client_mobile = client_mobile
        self.note = note
        self.cancel_url = cancel_url
        self.products = products
        self.supported_card_brands = supported_card_brands
        self.currency = currency
        self.sms_message = sms_message
        self.display_pending = display_pending
        self.receivers = receivers
        self.partner_portion = partner_portion
        self.metadata = metadata

    @classmethod
    def from_dict(cls, data: dict):
        products = [
            PaylinkProduct.from_dict(product) for product in data.get("products", [])
        ]

        return cls(
            amount=data.get("amount", 0.0),
            order_number=data.get("orderNumber", ""),
            call_back_url=data.get("callBackUrl", ""),
            client_email=data.get("clientEmail", ""),
            client_name=data.get("clientName", ""),
            client_mobile=data.get("clientMobile", ""),
            note=data.get("note", ""),
            cancel_url=data.get("cancelUrl", ""),
            products=products,
            supported_card_brands=data.get("supportedCardBrands", []),
            currency=data.get("currency", ""),
            sms_message=data.get("smsMessage", ""),
            display_pending=data.get("displayPending", True),
            receivers=data.get("receivers", None),
            partner_portion=data.get("partnerPortion", None),
            metadata=data.get("metadata", None),
        )
