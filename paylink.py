import requests
from typing import List, Optional, Dict, Any

# Paylink
from paylink_product import PaylinkProduct
import config;

class Paylink:
    def __init__(self, env: str = 'production'):
        if env == 'production':
            self.api_link = 'https://restapi.paylink.sa'
            self.payment_page_prefix = 'https://payment.paylink.sa/pay/order'
            self.api_id = config.PAYLINK_API_ID
            self.secret_key = config.PAYLINK_SECRET_KEY
            self.persist_token = False
        else: # development & test
            self.api_link = 'https://restpilot.paylink.sa'
            self.payment_page_prefix = 'https://paymentpilot.paylink.sa/pay/info'
            self.api_id = 'APP_ID_1123453311' # Test App ID
            self.secret_key = '0662abb5-13c7-38ab-cd12-236e58f43766' # Test Secret Key
            self.persist_token = False

        self.id_token = None

    def _authenticate(self) -> None:
        try:
            request_body = {
                'apiId': self.api_id,
                'secretKey': self.secret_key,
                'persistToken': self.persist_token,
            }

            response = requests.post(f"{self.api_link}/api/auth", json=request_body, headers={
                'accept': 'application/json',
                'content-type': 'application/json',
            })

            response_data = response.json()

            if response.status_code != 200 or not response_data or 'id_token' not in response_data:
                error_msg = response.text if response.text else f"Status code: {response.status_code}"
                raise Exception(f"Failed to authenticate. {error_msg}")

            self.id_token = response_data['id_token']
        except Exception as e:
            self.id_token = None
            raise e

    def add_invoice(
        self,
        amount: float,
        client_mobile: str,
        client_name: str,
        order_number: str,
        products: List[PaylinkProduct],
        callback_url: str,
        cancel_url: Optional[str] = None,
        client_email: Optional[str] = None,
        currency: Optional[str] = None,
        note: Optional[str] = None,
        sms_message: Optional[str] = None,
        supported_card_brands: Optional[List[str]] = None,
        display_pending: Optional[bool] = True
    ) -> Dict[str, Any]:
        try:
            if not self.id_token:
                self._authenticate()

            # Convert products to a list of dictionaries
            products_list = [product.to_dict() for product in products]

            request_body = {
                'amount': amount,
                'callBackUrl': callback_url,
                'cancelUrl': cancel_url,
                'clientEmail': client_email,
                'clientMobile': client_mobile,
                'currency': currency,
                'clientName': client_name,
                'note': note,
                'orderNumber': order_number,
                'products': products_list,
                'smsMessage': sms_message,
                'supportedCardBrands': supported_card_brands,
                'displayPending': display_pending,
            }

            response = requests.post(f"{self.api_link}/api/addInvoice", json=request_body, headers={
                'accept': 'application/json',
                'content-type': 'application/json',
                'Authorization': f'Bearer {self.id_token}',
            })

            order_details = response.json()

            if response.status_code != 200 or not order_details:
                error_msg = response.text if response.text else f"Status code: {response.status_code}"
                raise Exception(f"Failed to add the invoice. {error_msg}")

            return order_details
        except Exception as e:
            raise e

    def get_invoice(self, transaction_no: str) -> Dict[str, Any]:
        try:
            if not self.id_token:
                self._authenticate()

            response = requests.get(f"{self.api_link}/api/getInvoice/{transaction_no}", headers={
                'accept': 'application/json',
                'content-type': 'application/json',
                'Authorization': f'Bearer {self.id_token}',
            })

            order_details = response.json()

            if response.status_code != 200 or not order_details:
                error_msg = response.text if response.text else f"Status code: {response.status_code}"
                raise Exception(f"Failed to retrieve the invoice. {error_msg}")

            return order_details
        except Exception as e:
            raise e