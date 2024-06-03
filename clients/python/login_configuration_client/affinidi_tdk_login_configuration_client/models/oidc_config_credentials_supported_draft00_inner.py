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


from typing import List, Optional
from pydantic import BaseModel, StrictStr, conlist

class OIDCConfigCredentialsSupportedDraft00Inner(BaseModel):
    """
    OIDCConfigCredentialsSupportedDraft00Inner
    """
    cryptographic_binding_methods_supported: Optional[conlist(StrictStr)] = None
    cryptographic_suites_supported: Optional[conlist(StrictStr)] = None
    format: Optional[StrictStr] = None
    types: Optional[conlist(StrictStr)] = None
    __properties = ["cryptographic_binding_methods_supported", "cryptographic_suites_supported", "format", "types"]

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
    def from_json(cls, json_str: str) -> OIDCConfigCredentialsSupportedDraft00Inner:
        """Create an instance of OIDCConfigCredentialsSupportedDraft00Inner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OIDCConfigCredentialsSupportedDraft00Inner:
        """Create an instance of OIDCConfigCredentialsSupportedDraft00Inner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OIDCConfigCredentialsSupportedDraft00Inner.parse_obj(obj)

        _obj = OIDCConfigCredentialsSupportedDraft00Inner.parse_obj({
            "cryptographic_binding_methods_supported": obj.get("cryptographic_binding_methods_supported"),
            "cryptographic_suites_supported": obj.get("cryptographic_suites_supported"),
            "format": obj.get("format"),
            "types": obj.get("types")
        })
        return _obj


