# coding: utf-8

"""
    IotaService

    Affinidi IotaService Structure

    The version of the OpenAPI document: 1.0.0
    Contact: nucleus.team@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr, validator

class ConsentDto(BaseModel):
    """
    ConsentDto
    """
    project_id: StrictStr = Field(..., alias="projectId")
    id: StrictStr = Field(..., description="id of the record")
    user_id: StrictStr = Field(..., alias="userId", description="unique identifier of the user")
    vc_type: StrictStr = Field(..., alias="vcType", description="VC type of shared vc. If the actual VC has several VC types (excluding base types as VerifiableCredential) then for each of the a separate record will be added")
    status: StrictStr = Field(...)
    modified_at: StrictStr = Field(..., alias="modifiedAt")
    modified_by: StrictStr = Field(..., alias="modifiedBy")
    created_at: StrictStr = Field(..., alias="createdAt")
    created_by: StrictStr = Field(..., alias="createdBy")
    __properties = ["projectId", "id", "userId", "vcType", "status", "modifiedAt", "modifiedBy", "createdAt", "createdBy"]

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('GIVEN'):
            raise ValueError("must be one of enum values ('GIVEN')")
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
    def from_json(cls, json_str: str) -> ConsentDto:
        """Create an instance of ConsentDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConsentDto:
        """Create an instance of ConsentDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConsentDto.parse_obj(obj)

        _obj = ConsentDto.parse_obj({
            "project_id": obj.get("projectId"),
            "id": obj.get("id"),
            "user_id": obj.get("userId"),
            "vc_type": obj.get("vcType"),
            "status": obj.get("status"),
            "modified_at": obj.get("modifiedAt"),
            "modified_by": obj.get("modifiedBy"),
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy")
        })
        return _obj


