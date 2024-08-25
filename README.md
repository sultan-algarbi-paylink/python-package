# Paylink Package

A Python package for interacting with the Paylink API. It provides functionality to add and retrieve invoices.

## Installation

You can install the package using pip:

```bash
pip install paylink
```

## Usage
```python
from paylink import Paylink, PaylinkProduct
```

```python
paylink = Paylink(env='production')
```

```python
# Add Invoice

invoice_details = paylink.add_invoice(
    amount=10,
    client_mobile='966123456789',
    client_name='John Doe',
    order_number='1234567890',
    products=[
        PaylinkProduct(title='Hand bag', price=4, qty=1),
        PaylinkProduct(title='Book', price=3, qty=2),
    ],
    callback_url='https://paylink.sa/test-python-sdk',
    currency='USD',
)

print(invoice_details)
print('Transaction No:', invoiceDetails['transactionNo'])
print('Payment Url:', invoiceDetails['url'])
```

```python
# Get Invoice

invoice_details = paylink.get_invoice(invoice_details['transactionNo'])

print('Payment Status:', invoice_details['orderStatus'])
```

