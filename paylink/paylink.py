import requests
from typing import List, Optional

# Paylink
from .paylink_product import PaylinkProduct
from .paylink_invoice_response import PaylinkInvoiceResponse


class Paylink:
    PRODUCTION_API_URL = "https://restapi.paylink.sa"
    TEST_API_URL = "https://restpilot.paylink.sa"
    DEFAULT_TEST_API_ID = "APP_ID_1123453311"
    DEFAULT_TEST_SECRET_KEY = "0662abb5-13c7-38ab-cd12-236e58f43766"

    def __init__(
        self,
        environment: str = "production",
        api_id: Optional[str] = None,
        secret_key: Optional[str] = None,
    ):
        """
        Initialize the Paylink client with environment-specific configurations.

        Args:
            environment (str): The environment to use ("production" or "test").
            api_id (str, optional): The API ID for authentication in production.
            secret_key (str, optional): The secret key for authentication in production.
        """
        self.api_base_url = (
            self.PRODUCTION_API_URL
            if environment == "production"
            else self.TEST_API_URL
        )

        self.api_id = api_id or (
            None if environment == "production" else self.DEFAULT_TEST_API_ID
        )
        self.secret_key = secret_key or (
            None if environment == "production" else self.DEFAULT_TEST_SECRET_KEY
        )
        self.persist_token = False

        if environment == "production" and (not self.api_id or not self.secret_key):
            raise ValueError(
                "API_ID and Secret_Key are required for the production environment"
            )

        self.id_token = None

    @classmethod
    def test(cls):
        """
        Initialize the Paylink client for the test environment.
        """
        return cls(environment="test")

    @classmethod
    def production(cls, api_id: str, secret_key: str):
        """
        Initialize the Paylink client for the production environment.

        Args:
            api_id (str): The API ID for authentication.
            secret_key (str): The secret key for authentication.
        """
        return cls(environment="production", api_id=api_id, secret_key=secret_key)

    def _authenticate(self) -> None:
        """
        Authenticate with the Paylink API to obtain an ID token.

        Raises:
            RuntimeError: If authentication fails or the response is invalid.
        """
        try:
            # Prepare the request body for authentication
            auth_payload = {
                "apiId": self.api_id,
                "secretKey": self.secret_key,
                "persistToken": self.persist_token,
            }

            # Send the authentication request
            response = requests.post(
                f"{self.api_base_url}/api/auth",
                json=auth_payload,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                },
            )

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse the response data
            response_data = response.json()

            # Check for successful authentication
            if not response_data or "id_token" not in response_data:
                raise RuntimeError(
                    "Authentication failed: Missing 'id_token' in response"
                )

            self.id_token = response_data["id_token"]
        except requests.exceptions.RequestException as e:
            self.id_token = None
            raise RuntimeError(f"Authentication failed: {e}")

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
        display_pending: Optional[bool] = True,
    ) -> PaylinkInvoiceResponse:
        """
        Create a new invoice using the Paylink API.

        Args:
            amount (float): The total amount for the invoice.
            client_mobile (str): The client's mobile number.
            client_name (str): The client's name.
            order_number (str): The order number associated with the invoice.
            products (List[PaylinkProduct]): A list of products included in the invoice.
            callback_url (str): The URL to redirect to after payment completion.
            cancel_url (Optional[str]): The URL to redirect to if payment is canceled.
            client_email (Optional[str]): The client's email address.
            currency (Optional[str]): The currency for the invoice (default is SAR).
            note (Optional[str]): Additional notes for the invoice.
            sms_message (Optional[str]): SMS message to send to the client.
            supported_card_brands (Optional[List[str]]): Supported card brands for payment.
            display_pending (Optional[bool]): Whether to display pending transactions.

        Returns:
            PaylinkInvoiceResponse: The response object containing invoice details.

        Raises:
            RuntimeError: If invoice creation fails or the response is invalid.
        """
        if not self.id_token:
            self._authenticate()

        # Convert the product objects to dictionaries
        products_payload = [product.to_dict() for product in products]

        # Prepare the request body for invoice creation
        invoice_payload = {
            "amount": amount,
            "callBackUrl": callback_url,
            "cancelUrl": cancel_url,
            "clientEmail": client_email,
            "clientMobile": client_mobile,
            "currency": currency,
            "clientName": client_name,
            "note": note,
            "orderNumber": order_number,
            "products": products_payload,
            "smsMessage": sms_message,
            "supportedCardBrands": supported_card_brands,
            "displayPending": display_pending,
        }

        try:
            # Send the invoice creation request
            response = requests.post(
                f"{self.api_base_url}/api/addInvoice",
                json=invoice_payload,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.id_token}",
                },
            )

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse and return the invoice response object
            return PaylinkInvoiceResponse.from_response_data(response.json())
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Invoice creation failed: {e}")

    def get_invoice(self, transaction_no: str) -> PaylinkInvoiceResponse:
        """
        Retrieve an invoice by its transaction number from the Paylink API.

        Args:
            transaction_no (str): The transaction number of the invoice to retrieve.

        Returns:
            PaylinkInvoiceResponse: The response object containing invoice details.

        Raises:
            RuntimeError: If invoice retrieval fails or the response is invalid.
        """
        if not self.id_token:
            self._authenticate()

        try:
            # Send the request to retrieve the invoice
            response = requests.get(
                f"{self.api_base_url}/api/getInvoice/{transaction_no}",
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.id_token}",
                },
            )

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse and return the invoice response object
            return PaylinkInvoiceResponse.from_response_data(response.json())
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Invoice retrieval failed: {e}")

    def cancel_invoice(self, transaction_no: str) -> bool:
        """
        Cancel an existing invoice using the Paylink API.

        Args:
            transaction_no (str): The transaction number of the invoice to be canceled.

        Returns:
            bool: True if the cancellation is successful, False otherwise.

        Raises:
            RuntimeError: If invoice cancellation fails or the response is invalid.
        """
        if not self.id_token:
            self._authenticate()

        try:
            # Prepare the request body for invoice cancellation
            cancel_payload = {
                "transactionNo": transaction_no,
            }

            # Send the cancellation request
            response = requests.post(
                f"{self.api_base_url}/api/cancelInvoice",
                json=cancel_payload,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.id_token}",
                },
            )

            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse the response data
            response_data = response.json()

            # Return success status
            return response_data.get("success", "false").lower() == "true"

        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Invoice cancellation failed: {e}")

    def order_status(self, transaction_no: str) -> str:
        """
        Get the status of an order by its transaction number.

        Args:
            transaction_no (str): The transaction number of the order.

        Returns:
            str: The status of the order.

        Raises:
            RuntimeError: If there is an error retrieving the order status.
        """
        try:
            # Fetch the invoice details and extract the order status
            invoice = self.get_invoice(transaction_no)
            return invoice.order_status
        except RuntimeError as e:
            raise RuntimeError(f"Failed to retrieve order status: {e}")
