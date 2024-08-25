import pytest
from paylink import Paylink, PaylinkProduct

def test_add_invoice():
    paylink = Paylink(env='dev') # api_id & secret_key are required for production environment
    invoice_details = paylink.add_invoice(
        amount=10,
        client_mobile='966123456789',
        client_name='John Doe',
        order_number='1234567890',
        products=[
            PaylinkProduct(title='Hand bag', price=4, qty=1),
            PaylinkProduct(title='Book', price=3, qty=2),
        ],
        callback_url='https://paylink.sa/',
        currency='USD',
    )
    assert 'transactionNo' in invoice_details
    assert 'url' in invoice_details

def test_get_invoice():
    paylink = Paylink(env='dev')
    invoice_details = paylink.add_invoice(
        amount=10,
        client_mobile='966123456789',
        client_name='John Doe',
        order_number='1234567890',
        products=[
            PaylinkProduct(title='Hand bag', price=4, qty=1),
            PaylinkProduct(title='Book', price=3, qty=2),
        ],
        callback_url='https://paylink.sa/',
        currency='USD',
    )
    get_invoice = paylink.get_invoice(invoice_details['transactionNo'])
    assert 'orderStatus' in get_invoice