==================
Starlette APISpec
==================

    Easy APISpec integration for Starlette

.. image:: https://img.shields.io/travis/Woile/starlette-apispec.svg?style=flat-square
    :alt: Travis
    :target: https://travis-ci.org/Woile/starlette-apispec

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
    from starlette.applications import Starlette
    from starlette_apispec import APISpecSchemaGenerator

    app = Starlette()
    app.schema_generator = APISpecSchemaGenerator(
        APISpec(
            title="Example API",
            version="1.0",
            openapi_version="3.0.0",
            info={"description": "explanation of the api purpose"},
            plugins=["apispec.ext.marshmallow"],
        )
    )

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

`Starlette <https://www.starlette.io/>`_ is a is a lightweight ASGI framework/toolkit,
which is ideal for building high performance asyncio services.

`APISpec <https://apispec.readthedocs.io/en/stable/>`_ supports the `OpenApi Specification <https://github.com/OAI/OpenAPI-Specification>`_
and it has some useful plugins like `marshmallow <https://marshmallow.readthedocs.io/en/3.0/>`_ support.

Version supported: :code:`0.39.0`


Usage
=====


This example includes `marshmallow <https://marshmallow.readthedocs.io/en/3.0/>`_ integration

.. code-block:: python

    from apispec import APISpec

    from marshmallow import Schema, fields

    from starlette.applications import Starlette
    from starlette.endpoints import HTTPEndpoint
    from starlette.schemas import OpenAPIResponse
    from starlette_apispec import APISpecSchemaGenerator


    class UserSchema(Schema):
        username = fields.Str(required=True)


    app = Starlette()
    app.schema_generator = APISpecSchemaGenerator(
        APISpec(
            title="Example API",
            version="1.0",
            openapi_version="3.0.0",
            info={"description": "explanation of the api purpose"},
            plugins=["apispec.ext.marshmallow"],
        )
    )
    app.schema_generator.spec.definition("User", schema=UserSchema)


    @app.route("/users", methods=["GET", "HEAD"])
    def list_users(request):
        """
        responses:
        200:
            description: A list of users.
            schema: UserSchema
            examples:
            [{"username": "tom"}, {"username": "lucy"}]
        """
        raise NotImplementedError()


    @app.route("/users", methods=["POST"])
    def create_user(request):
        """
        responses:
        200:
            description: A user.
            schema: UserSchema
            examples:
            {"username": "tom"}
        """
        raise NotImplementedError()


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
            raise NotImplementedError()

        def post(self, request):
            """
            responses:
            200:
                description: An organisation.
                examples:
                {"name": "Foo Corp."}
            """
            raise NotImplementedError()


    @app.route("/schema", methods=["GET"], include_in_schema=False)
    def schema(request):
        return OpenAPIResponse(app.schema)

More documentation
==================

This package is basically a proxy, so if you wonder how to do something,
here are the sources you need:

`Starlette documentation <https://www.starlette.io/>`_

`APISpec Documentation <https://apispec.readthedocs.io/en/stable/>`_


Testing
=======

1. Clone the repo
2. Install dependencies

::

    poetry install

3. Run tests

::

    poetry run pytest -s --cov-report term-missing --cov=starlette_apispec tests/


Contributing
============

**PRs are welcome!**
