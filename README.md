# PyDuinoCoin
![Build Status](https://travis-ci.com/BackrndSource/pyduinocoin.svg?branch=master)

PyDuinoCoin is a simple python integration for the [DuinoCoin REST API](https://github.com/revoxhere/duco-rest-api), that allows developers to communicate with DuinoCoin Main Server.

## Install

> PyDuinoCoin is available on the Python Package Index (PyPI):
https://pypi.python.org/pypi/pyduinocoin

You can install PyDuinoCoin using pip.

```bash
$ pip install pyduinocoin
```

### Making queries

You can use the `DuinoClient` object instance to perform queries. 

Most methods of the `DuinoClient` class have the same name as the REST API endpoints.

> Check out the REST API Documentation: https://github.com/revoxhere/duco-rest-api

All responses will return a `DictObj` object or a `list` object. All `dict` objects in the response will be transformed into `DictObj`. You can access to the data of a `DictObj` object as you would with a `dict` object, or do it through the attributes. An example to illustrate this:

```python
client = DuinoClient()
response = client.user('example')

# It is the same::
for response['balance']['username']
for response.balance['username']
for response['balance'].username
for response.balance.username # I love this one

# DictObj is iterable:
for key, value in response.items():
    print(key)
    print(value)
```

## Examples

Usage examples can be found in the [/examples](https://github.com/BackrndSource/pyduinocoin/blob/master/examples) folder of the project

## Tests

You can run the tests via the command line.

Place your terminal at the root of the project and run the following command.

```bash
$ python -m unittest discover tests "*_test.py"
```

## Greetings

[@revoxhere](https://github.com/revoxhere) by [duco-rest-api](https://github.com/revoxhere/duco-rest-api) for the REST API documented.
[@dansinclair25](https://github.com/dansinclair25) by [duco-rest-api](https://github.com/dansinclair25/duco-rest-api) for the original REST API.
