# Paylink Package

A Python package for interacting with the Paylink API. It provides functionality to add and retrieve invoices.

## Installation

You can install the package using pip:

```bash
pip install paylink-package==1.0.4
```

## Usage

```python
from paylink import Paylink, PaylinkProduct
```

```python
# For Development & Test
paylink = Paylink.test()

# For Production
paylink = Paylink.production(api_id='xxxxx', secret_key='xxxxx')
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
print('Transaction No:', invoice_details.transaction_no)
print('Payment Url:', invoice_details.url)
```

```python
# Get Invoice

invoice_details = paylink.get_invoice(transaction_no=17214351564123)

print('Payment Status:', invoice_details.order_status)
print('Payment Url:', invoice_details.url)
```

```python
# Payment Status

status = paylink.order_status(transaction_no=17214351564123)
print('Payment Status:', status)

```
