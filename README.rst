==================
Starlette APISpec
==================

    Easy APISpec integration for Starlette


.. image:: https://github.com/Woile/starlette-apispec/actions/workflows/pythonpackage.yml/badge.svg?style=flat-square
    :alt: GitHub Workflow Status
    :target: https://github.com/Woile/starlette-apispec/actions/workflows/pythonpackage.yml

.. image:: https://img.shields.io/codecov/c/github/Woile/starlette-apispec.svg?style=flat-square
    :alt: Codecov
    :target: https://codecov.io/gh/Woile/starlette-apispec

.. image:: https://img.shields.io/pypi/v/starlette-apispec.svg?style=flat-square
    :alt: PyPI
    :target: https://pypi.org/project/starlette-apispec/

.. image:: https://img.shields.io/pypi/pyversions/starlette-apispec.svg?style=flat-square
    :alt: PyPI - Python Version
    :target: https://pypi.org/project/starlette-apispec/

.. contents::
    :depth: 2

.. code-block:: python

    from apispec import APISpec
    from apispec.ext.marshmallow import MarshmallowPlugin
    from starlette.applications import Starlette
    from starlette_apispec import APISpecSchemaGenerator

    app = Starlette()

    schemas = APISpecSchemaGenerator(
        APISpec(
            title="Example API",
            version="1.0",
            openapi_version="3.0.0",
            info={"description": "explanation of the api purpose"},
            plugins=[MarshmallowPlugin()],
        )
    )

    @app.route("/schema", methods=["GET"], include_in_schema=False)
    def schema(request):
        return schemas.OpenAPIResponse(request=request)


Installation
============

::

    pip install -U starlette-apispec

Alternatively you can do

::

    poetry add starlette-apispec

About
-----

This library helps you easily document your REST API built with starlette.

Starlette_ is a is a lightweight ASGI framework/toolkit,
which is ideal for building high performance asyncio services.

APISpec_ supports the `OpenApi Specification <https://github.com/OAI/OpenAPI-Specification>`_
and it has some useful plugins like marshmallow_ support.

Version supported: :code:`^1.0.0`


Usage
=====


This example includes marshmallow_ integration

.. code-block:: python

    from apispec import APISpec

    from starlette.applications import Starlette
    from starlette.endpoints import HTTPEndpoint
    from starlette.testclient import TestClient

    from starlette_apispec import APISpecSchemaGenerator


    app = Starlette()

    schemas = APISpecSchemaGenerator(
        APISpec(
            title="Example API",
            version="1.0",
            openapi_version="3.0.0",
            info={"description": "explanation of the api purpose"},
        )
    )


    @app.websocket_route("/ws")
    def ws(session):
        """ws"""
        pass  # pragma: no cover


    @app.route("/users", methods=["GET", "HEAD"])
    def list_users(request):
        """
        responses:
        200:
            description: A list of users.
            examples:
            [{"username": "tom"}, {"username": "lucy"}]
        """
        pass  # pragma: no cover


    @app.route("/users", methods=["POST"])
    def create_user(request):
        """
        responses:
        200:
            description: A user.
            examples:
            {"username": "tom"}
        """
        pass  # pragma: no cover


    @app.route("/orgs")
    class OrganisationsEndpoint(HTTPEndpoint):
        def get(self, request):
            """
            responses:
            200:
                description: A list of organisations.
                examples:
                [{"name": "Foo Corp."}, {"name": "Acme Ltd."}]
            """
            pass  # pragma: no cover

        def post(self, request):
            """
            responses:
            200:
                description: An organisation.
                examples:
                {"name": "Foo Corp."}
            """
            pass  # pragma: no cover


    @app.route("/schema", methods=["GET"], include_in_schema=False)
    def schema(request):
        return schemas.OpenAPIResponse(request=request)

More documentation
==================

This package is basically a proxy, so if you wonder how to do something,
here are the sources you need:

`Starlette documentation`_

`APISpec documentation`_


Testing
=======

1. Clone the repo
2. Activate venv ``. venv/bin/activate``
3. Install dependencies

::

    poetry install

4. Run tests

::

    ./scripts/test


Contributing
============

**PRs are welcome!**


.. _marshmallow: https://marshmallow.readthedocs.io/
.. _APISpec: https://apispec.readthedocs.io/en/stable/
.. _Starlette: https://www.starlette.io/
.. _`Starlette documentation`: https://www.starlette.io/
.. _`APISpec documentation`: https://apispec.readthedocs.io/en/stable/
