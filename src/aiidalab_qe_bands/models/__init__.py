import typing as t

from .input import BandsInput


def get_plugin() -> dict[str, t.Any]:
    return {
        "id": "bands",
        "label": "Electronic band structure",
        "input": {
            "schema": BandsInput.model_json_schema(),
            "ui": {},
        },
    }
