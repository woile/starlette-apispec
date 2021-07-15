import typing

from starlette.routing import BaseRoute
from starlette.schemas import BaseSchemaGenerator


def make_plain_datastructure(data: dict) -> dict:
    """
    Some of the children of the dict might have specialized datatypes.
    """
    if isinstance(data, list):
        return [make_plain_datastructure(item) for item in data]
    elif isinstance(data, dict):
        return {key: make_plain_datastructure(value) for key, value in data.items()}
    return data


class APISpecSchemaGenerator(BaseSchemaGenerator):
    def __init__(self, spec: typing.Type) -> None:
        self.spec = spec

    def get_schema(self, routes: typing.List[BaseRoute]) -> dict:
        endpoints = self.get_endpoints(routes)
        for endpoint in endpoints:
            self.spec.path(
                path=endpoint.path,
                operations={endpoint.http_method: self.parse_docstring(endpoint.func)},
            )
        return make_plain_datastructure(self.spec.to_dict())
