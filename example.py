# -*- coding: utf-8 -*-
"""
    example
    ~~~~~~~

    Some example of use cases.

    :copyright: (c) 2015 by Rambler&Co.
"""

from ponominalu.client import PonominaluAPI


if __name__ == '__main__':
    client = PonominaluAPI()
    categories = client.categories()
    print categories
