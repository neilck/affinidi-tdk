# coding: utf-8

"""
    CloudWalletEssentials

    Cloud Wallet For Enterprise Structure

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
from pydantic import BaseModel
from affinidi_tdk_wallets_client.models.wallet_dto import WalletDto

class CreateWalletResponse(BaseModel):
    """
    wallet dto  # noqa: E501
    """
    wallet: Optional[WalletDto] = None
    __properties = ["wallet"]

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
    def from_json(cls, json_str: str) -> CreateWalletResponse:
        """Create an instance of CreateWalletResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of wallet
        if self.wallet:
            _dict['wallet'] = self.wallet.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateWalletResponse:
        """Create an instance of CreateWalletResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateWalletResponse.parse_obj(obj)

        _obj = CreateWalletResponse.parse_obj({
            "wallet": WalletDto.from_dict(obj.get("wallet")) if obj.get("wallet") is not None else None
        })
        return _obj


