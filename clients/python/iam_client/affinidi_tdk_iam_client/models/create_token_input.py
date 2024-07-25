# coding: utf-8

"""
    Iam

    Affinidi IAM

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator
from affinidi_tdk_iam_client.models.token_authentication_method_dto import TokenAuthenticationMethodDto

class CreateTokenInput(BaseModel):
    """
    CreateTokenInput
    """
    name: constr(strict=True) = Field(...)
    authentication_method: TokenAuthenticationMethodDto = Field(..., alias="authenticationMethod")
    description: Optional[StrictStr] = None
    __properties = ["name", "authenticationMethod", "description"]

    @validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r".{3,}", value):
            raise ValueError(r"must validate the regular expression /.{3,}/")
        return value

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
    def from_json(cls, json_str: str) -> CreateTokenInput:
        """Create an instance of CreateTokenInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of authentication_method
        if self.authentication_method:
            _dict['authenticationMethod'] = self.authentication_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateTokenInput:
        """Create an instance of CreateTokenInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateTokenInput.parse_obj(obj)

        _obj = CreateTokenInput.parse_obj({
            "name": obj.get("name"),
            "authentication_method": TokenAuthenticationMethodDto.from_dict(obj.get("authenticationMethod")) if obj.get("authenticationMethod") is not None else None,
            "description": obj.get("description")
        })
        return _obj


