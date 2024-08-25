from paylink import Paylink, PaylinkProduct

paylinkInstance = Paylink(env='production')

print('\n================= Start: Add Invoice ================\n')
invoiceDetails = paylinkInstance.add_invoice(
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

print('=== Result:\n', invoiceDetails)
print('=== Transaction No:\n', invoiceDetails['transactionNo'])
print('=== Payment Url:\n', invoiceDetails['url'])
print('\n=================== End: Add Invoice ================\n')


print('\n================= Start: Get Invoice ================\n')
getInvoice = paylinkInstance.get_invoice(invoiceDetails['transactionNo'])
print('=== Payment Status:\n', getInvoice['orderStatus'])
print('\n=================== End: Get Invoice ================\n')