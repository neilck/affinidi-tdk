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



from pydantic import BaseModel, Field, StrictBool
from affinidi_tdk_credential_verification_client.models.verify_presentation_output_errors import VerifyPresentationOutputErrors

class VerifyPresentationOutput(BaseModel):
    """
    Response model of /verify-vp  # noqa: E501
    """
    errors: VerifyPresentationOutputErrors = Field(...)
    is_valid: StrictBool = Field(..., alias="isValid", description="Verification result")
    __properties = ["errors", "isValid"]

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
    def from_json(cls, json_str: str) -> VerifyPresentationOutput:
        """Create an instance of VerifyPresentationOutput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of errors
        if self.errors:
            _dict['errors'] = self.errors.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VerifyPresentationOutput:
        """Create an instance of VerifyPresentationOutput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VerifyPresentationOutput.parse_obj(obj)

        _obj = VerifyPresentationOutput.parse_obj({
            "errors": VerifyPresentationOutputErrors.from_dict(obj.get("errors")) if obj.get("errors") is not None else None,
            "is_valid": obj.get("isValid")
        })
        return _obj


