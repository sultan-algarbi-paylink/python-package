from setuptools import setup, find_packages

setup(
    name='paylink_package',
    version='1.0.3',
    packages=find_packages(),
    install_requires=[
        'requests',  # Add any other dependencies here
    ],
    tests_require=[
        'pytest',
    ],
    description='A Python package for interacting with the Paylink API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sultan Algarbi',
    author_email='sultanye8@gmail.com',
    license='MIT',
    url='https://github.com/sultan-algarbi-paylink/python-package.git',
)
