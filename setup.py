from setuptools import setup, find_packages

setup(
    name="paylink_package",
    version="1.0.6",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    tests_require=[
        "pytest",
    ],
    description="A Python package designed for seamless integration with the Paylink API, ideal for developers who want to incorporate Paylink's payment processing capabilities into their applications effortlessly. It offers straightforward functionality for adding and retrieving invoices.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Sultan Algarbi",
    author_email="sultanye8@gmail.com",
    license="MIT",
    url="https://github.com/sultan-algarbi-paylink/python-package.git",
)
