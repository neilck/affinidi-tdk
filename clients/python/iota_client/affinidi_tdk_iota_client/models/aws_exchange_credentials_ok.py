# coding: utf-8

"""
    IotaService

    Affinidi IotaService Structure

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr
from affinidi_tdk_iota_client.models.aws_exchange_credentials_ok_credentials import AwsExchangeCredentialsOKCredentials

class AwsExchangeCredentialsOK(BaseModel):
    """
    AwsExchangeCredentialsOK
    """
    connection_client_id: StrictStr = Field(..., alias="connectionClientId")
    credentials: AwsExchangeCredentialsOKCredentials = Field(...)
    __properties = ["connectionClientId", "credentials"]

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
    def from_json(cls, json_str: str) -> AwsExchangeCredentialsOK:
        """Create an instance of AwsExchangeCredentialsOK from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of credentials
        if self.credentials:
            _dict['credentials'] = self.credentials.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AwsExchangeCredentialsOK:
        """Create an instance of AwsExchangeCredentialsOK from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AwsExchangeCredentialsOK.parse_obj(obj)

        _obj = AwsExchangeCredentialsOK.parse_obj({
            "connection_client_id": obj.get("connectionClientId"),
            "credentials": AwsExchangeCredentialsOKCredentials.from_dict(obj.get("credentials")) if obj.get("credentials") is not None else None
        })
        return _obj


