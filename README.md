# Paylink Package

This package is ideal for Python developers looking to integrate Paylink's payment processing capabilities into their applications with minimal effort. It provides functionality to add and retrieve invoices.

## Installation

You can install the package using pip:

```bash
pip install paylink-package==1.0.6
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
# Cancel Invoice

cancellation_success = paylink.cancel_invoice(transaction_no=17214351564123) # true-false

```

```python
# Payment Status

status = paylink.order_status(transaction_no=17214351564123)
print('Payment Status:', status)

```

## Package Features:

The Paylink Python package provides a comprehensive integration with the Paylink Payment Gateway, enabling developers to create, manage, and track payment invoices easily. Key features include:

1. **Environment Configuration**:

   - Supports both **production** and **test** environments.
   - Easy setup with API credentials for authentication.

2. **Authentication**:

   - Secure authentication to obtain an ID token required for API interactions.

3. **Invoice Management**:

   - **Create Invoice**: Generate new invoices with detailed product information, client details, and callback URLs.
   - **Retrieve Invoice**: Fetch invoice details using the transaction number.
   - **Order Status**: Retrieve the status of an order by its transaction number.

4. **Product Management**:

   - **PaylinkProduct Class**: Create product objects with attributes like title, price, quantity, description, VAT, and digital product options.
   - Convert product data to and from dictionary format for easy serialization and deserialization.

5. **Comprehensive Response Handling**:

   - **PaylinkInvoiceResponse Class**: Parse and manage responses from the Paylink API, including transaction details, order status, payment errors, and more.

6. **Error Handling**:

   - Robust error handling with meaningful exception messages for authentication, invoice creation, and data retrieval processes.

7. **Ease of Use**:
   - Designed with Python developers in mind, offering clear methods for interacting with the Paylink API.
   - Helper methods for initializing the package in different environments (`test` and `production`).

## Changelog

- **1.0.6**

  - **New Method Added:** `cancel_invoice` to cancel an existing invoice using the Paylink API.

- **1.0.5**

  - **Updated README File:** Added detailed information about package features to provide users with a comprehensive overview of capabilities and functionalities.
  - **Enhanced Changelog:** Included a changelog section in the README file to keep users informed about updates and changes in each version.

- **1.0.4**
  - **PaylinkProduct Class:**
    - Developed a `PaylinkProduct` class to create and manage product objects with attributes such as title, price, quantity, description, VAT, and options for digital products.
    - Implemented methods for converting product data to and from dictionary format, facilitating easy serialization and deserialization for various use cases.
  - **PaylinkInvoiceResponse Class:**
    - Introduced the `PaylinkInvoiceResponse` class to parse and handle responses from the Paylink API. This includes managing transaction details, order status, payment errors, and other relevant information.
  - **Order Status Retrieval:** Added functionality to retrieve the status of an order using its transaction number, allowing for effective tracking and management of orders.
