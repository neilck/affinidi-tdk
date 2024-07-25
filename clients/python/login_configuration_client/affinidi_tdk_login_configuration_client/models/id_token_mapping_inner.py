# coding: utf-8

"""
    OidcVpAdapterBackend

    Affinidi OIDC VP Adapter Backend  An authorization token is necessary to create or obtain a project Access Token and access Admin APIs. Follow these step-by-step [instructions](https://lemmatree.atlassian.net/wiki/spaces/NETCORE/pages/2735317648020/ASA+Developer+Flow#Instructions-on-how-to-create-the-Project.) to set up an authorization token 

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
from pydantic import BaseModel, Field, StrictStr

class IdTokenMappingInner(BaseModel):
    """
    IdTokenMappingInner
    """
    source_field: StrictStr = Field(..., alias="sourceField", description="Name(path) of the corresponding field in the vp_token")
    id_token_claim: StrictStr = Field(..., alias="idTokenClaim", description="Name of the corresponding field in the id_token")
    input_descriptor_id: Optional[StrictStr] = Field(None, alias="inputDescriptorId", description="Id of related input descriptor from presentation definition")
    __properties = ["sourceField", "idTokenClaim", "inputDescriptorId"]

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
    def from_json(cls, json_str: str) -> IdTokenMappingInner:
        """Create an instance of IdTokenMappingInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdTokenMappingInner:
        """Create an instance of IdTokenMappingInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IdTokenMappingInner.parse_obj(obj)

        _obj = IdTokenMappingInner.parse_obj({
            "source_field": obj.get("sourceField"),
            "id_token_claim": obj.get("idTokenClaim"),
            "input_descriptor_id": obj.get("inputDescriptorId")
        })
        return _obj


