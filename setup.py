from setuptools import setup, find_packages


setup(
    name='python-ponominalu',
    version='0.0.2',
    url='https://github.com/abogoyavlensky/python-ponominalu',
    license='MIT',
    author='Andrey Bogoyavlensky',
    author_email='abogoyavlensky@gmail.com',
    description='Python client for Ponominalu API.',
    platforms='any',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    keywords='rambler ponominalu api',
)
