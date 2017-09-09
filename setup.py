from setuptools import setup, find_packages

setup(
    name = 'line_pay_sdk',
    version = '0.0.1',
    keywords = ["line", "pay"],
    description = 'just a simple line pay sdk',
    license = 'MIT License',
    install_requires = [
        'optionaldict',
        'six',
    ],

    author = 'bamwang',
    author_email = 'wangzhucn+dev@gmail.com',
    
    packages = find_packages(),
    platforms = 'any'
)
