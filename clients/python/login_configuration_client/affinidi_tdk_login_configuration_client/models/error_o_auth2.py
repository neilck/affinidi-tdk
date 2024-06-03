# coding: utf-8

"""
    OidcVpAdapterBackend

    Affinidi OIDC VP Adapter Backend  An authorization token is necessary to create or obtain a project Access Token and access Admin APIs. Follow these step-by-step [instructions](https://lemmatree.atlassian.net/wiki/spaces/NETCORE/pages/2735317648020/ASA+Developer+Flow#Instructions-on-how-to-create-the-Project.) to set up an authorization token 

    The version of the OpenAPI document: 1.0.0
    Contact: nucleus.team@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class ErrorOAuth2(BaseModel):
    """
    ErrorOAuth2
    """
    error: StrictStr = Field(..., description="Error")
    error_debug: Optional[StrictStr] = Field(None, description="Error Debug Information. Only available in dev mode.")
    error_description: StrictStr = Field(..., description="Error Description")
    error_hint: Optional[StrictStr] = Field(None, description="Error Hint. Helps the user identify the error cause.")
    status_code: StrictStr = Field(..., description="HTTP Status Code")
    __properties = ["error", "error_debug", "error_description", "error_hint", "status_code"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ErrorOAuth2:
        """Create an instance of ErrorOAuth2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorOAuth2:
        """Create an instance of ErrorOAuth2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorOAuth2.parse_obj(obj)

        _obj = ErrorOAuth2.parse_obj({
            "error": obj.get("error"),
            "error_debug": obj.get("error_debug"),
            "error_description": obj.get("error_description"),
            "error_hint": obj.get("error_hint"),
            "status_code": obj.get("status_code")
        })
        return _obj


