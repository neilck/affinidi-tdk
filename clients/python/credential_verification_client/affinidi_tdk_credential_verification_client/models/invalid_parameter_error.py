# coding: utf-8

"""
    VerificationService

    Affinidi VerificationService Structure

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from affinidi_tdk_credential_verification_client.models.not_found_error_details_inner import NotFoundErrorDetailsInner

class InvalidParameterError(BaseModel):
    """
    InvalidParameterError
    """
    name: StrictStr = Field(...)
    message: StrictStr = Field(...)
    http_status_code: Union[StrictFloat, StrictInt] = Field(..., alias="httpStatusCode")
    trace_id: StrictStr = Field(..., alias="traceId")
    details: Optional[conlist(NotFoundErrorDetailsInner)] = None
    __properties = ["name", "message", "httpStatusCode", "traceId", "details"]

    @validator('name')
    def name_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('InvalidParameterError'):
            raise ValueError("must be one of enum values ('InvalidParameterError')")
        return value

    @validator('message')
    def message_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Invalid parameter: ${param}.'):
            raise ValueError("must be one of enum values ('Invalid parameter: ${param}.')")
        return value

    @validator('http_status_code')
    def http_status_code_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (400):
            raise ValueError("must be one of enum values (400)")
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
    def from_json(cls, json_str: str) -> InvalidParameterError:
        """Create an instance of InvalidParameterError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item in self.details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['details'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InvalidParameterError:
        """Create an instance of InvalidParameterError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InvalidParameterError.parse_obj(obj)

        _obj = InvalidParameterError.parse_obj({
            "name": obj.get("name"),
            "message": obj.get("message"),
            "http_status_code": obj.get("httpStatusCode"),
            "trace_id": obj.get("traceId"),
            "details": [NotFoundErrorDetailsInner.from_dict(_item) for _item in obj.get("details")] if obj.get("details") is not None else None
        })
        return _obj


