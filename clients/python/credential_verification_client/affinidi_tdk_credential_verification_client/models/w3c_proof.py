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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class W3cProof(BaseModel):
    """
    W3cProof
    """
    type: Optional[StrictStr] = None
    created: Optional[StrictStr] = None
    verification_method: StrictStr = Field(..., alias="verificationMethod")
    proof_purpose: StrictStr = Field(..., alias="proofPurpose")
    jws: Optional[StrictStr] = None
    proof_value: Optional[StrictStr] = Field(None, alias="proofValue")
    nonce: Optional[StrictStr] = None
    __properties = ["type", "created", "verificationMethod", "proofPurpose", "jws", "proofValue", "nonce"]

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
    def from_json(cls, json_str: str) -> W3cProof:
        """Create an instance of W3cProof from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if created (nullable) is None
        # and __fields_set__ contains the field
        if self.created is None and "created" in self.__fields_set__:
            _dict['created'] = None

        # set to None if jws (nullable) is None
        # and __fields_set__ contains the field
        if self.jws is None and "jws" in self.__fields_set__:
            _dict['jws'] = None

        # set to None if proof_value (nullable) is None
        # and __fields_set__ contains the field
        if self.proof_value is None and "proof_value" in self.__fields_set__:
            _dict['proofValue'] = None

        # set to None if nonce (nullable) is None
        # and __fields_set__ contains the field
        if self.nonce is None and "nonce" in self.__fields_set__:
            _dict['nonce'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> W3cProof:
        """Create an instance of W3cProof from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return W3cProof.parse_obj(obj)

        _obj = W3cProof.parse_obj({
            "type": obj.get("type"),
            "created": obj.get("created"),
            "verification_method": obj.get("verificationMethod"),
            "proof_purpose": obj.get("proofPurpose"),
            "jws": obj.get("jws"),
            "proof_value": obj.get("proofValue"),
            "nonce": obj.get("nonce")
        })
        return _obj


