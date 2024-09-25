from paylink import Paylink, PaylinkProduct


def test_add_invoice():
    # Create an instance of the Paylink class
    paylink = Paylink.test()

    # Add an invoice
    invoice_details = paylink.add_invoice(
        amount=10,
        client_mobile="966123456789",
        client_name="John Doe",
        order_number="1234567890",
        products=[
            PaylinkProduct(title="Hand bag", price=4, qty=1),
            PaylinkProduct(title="Book", price=3, qty=2),
        ],
        callback_url="https://paylink.sa/",
        currency="USD",
    )

    # Check the invoice details
    assert invoice_details.transaction_no is not None
    assert invoice_details.url is not None


def test_get_invoice():
    # Create an instance of the Paylink class
    paylink = Paylink.test()

    # Add an invoice
    invoice_details = paylink.add_invoice(
        amount=10,
        client_mobile="966123456789",
        client_name="John Doe",
        order_number="1234567890",
        products=[
            PaylinkProduct(title="Hand bag", price=4, qty=1),
            PaylinkProduct(title="Book", price=3, qty=2),
        ],
        callback_url="https://paylink.sa/",
        currency="USD",
    )

    # Get the invoice
    get_invoice = paylink.get_invoice(invoice_details.transaction_no)

    # Check the invoice details
    assert get_invoice.order_status is not None
    assert get_invoice.order_status.lower() == "pending"


def test_cancel_invoice():
    # Create an instance of the Paylink class
    paylink = Paylink.test()

    # Add an invoice
    invoice_details = paylink.add_invoice(
        amount=10,
        client_mobile="966123456789",
        client_name="John Doe",
        order_number="1234567890",
        products=[
            PaylinkProduct(title="Hand bag", price=4, qty=1),
            PaylinkProduct(title="Book", price=3, qty=2),
        ],
        callback_url="https://paylink.sa/",
        currency="USD",
    )

    # Cancel the invoice
    cancellation_success = paylink.cancel_invoice(invoice_details.transaction_no)

    # Check if the invoice was successfully canceled
    assert cancellation_success is True
