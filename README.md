# python-ponominalu
Python client for Ponominalu API http://api.cultserv.ru/public/docs/

Installation
------------
```
pip install python-ponominalu
```
Requires
--------
  * python2.7
  * requests


Ponominalu API docs
-------------------
[Ponominalu developer site](http://api.cultserv.ru/public/docs/)


Usage example
-------------

```
from ponominalu.client import PonominaluAPI
client = PonominaluAPI()
categories = client.categories()
```