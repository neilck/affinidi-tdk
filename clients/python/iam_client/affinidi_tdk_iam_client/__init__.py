# coding: utf-8

# flake8: noqa

"""
    Iam

    Affinidi IAM

    The version of the OpenAPI document: 1.0.0
    Contact: nucleus.team@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from affinidi_tdk_iam_client.api.consumer_auth_api import ConsumerAuthApi
from affinidi_tdk_iam_client.api.default_api import DefaultApi
from affinidi_tdk_iam_client.api.policies_api import PoliciesApi
from affinidi_tdk_iam_client.api.projects_api import ProjectsApi
from affinidi_tdk_iam_client.api.sts_api import StsApi
from affinidi_tdk_iam_client.api.tokens_api import TokensApi
from affinidi_tdk_iam_client.api.well_known_api import WellKnownApi

# import ApiClient
from affinidi_tdk_iam_client.api_response import ApiResponse
from affinidi_tdk_iam_client.api_client import ApiClient
from affinidi_tdk_iam_client.configuration import Configuration
from affinidi_tdk_iam_client.exceptions import OpenApiException
from affinidi_tdk_iam_client.exceptions import ApiTypeError
from affinidi_tdk_iam_client.exceptions import ApiValueError
from affinidi_tdk_iam_client.exceptions import ApiKeyError
from affinidi_tdk_iam_client.exceptions import ApiAttributeError
from affinidi_tdk_iam_client.exceptions import ApiException

# import models into sdk package
from affinidi_tdk_iam_client.models.action_forbidden_error import ActionForbiddenError
from affinidi_tdk_iam_client.models.add_user_to_project_input import AddUserToProjectInput
from affinidi_tdk_iam_client.models.consumer_auth_token_endpoint_input import ConsumerAuthTokenEndpointInput
from affinidi_tdk_iam_client.models.consumer_auth_token_endpoint_output import ConsumerAuthTokenEndpointOutput
from affinidi_tdk_iam_client.models.cors_consumer_auth_token_endpoint_ok import CorsConsumerAuthTokenEndpointOK
from affinidi_tdk_iam_client.models.create_project_input import CreateProjectInput
from affinidi_tdk_iam_client.models.create_project_scoped_token_input import CreateProjectScopedTokenInput
from affinidi_tdk_iam_client.models.create_project_scoped_token_output import CreateProjectScopedTokenOutput
from affinidi_tdk_iam_client.models.create_token_input import CreateTokenInput
from affinidi_tdk_iam_client.models.get_well_known_did_ok import GetWellKnownDidOK
from affinidi_tdk_iam_client.models.invalid_jwt_token_error import InvalidJwtTokenError
from affinidi_tdk_iam_client.models.invalid_parameter_error import InvalidParameterError
from affinidi_tdk_iam_client.models.json_web_key_dto import JsonWebKeyDto
from affinidi_tdk_iam_client.models.json_web_key_set_dto import JsonWebKeySetDto
from affinidi_tdk_iam_client.models.not_found_error import NotFoundError
from affinidi_tdk_iam_client.models.policy_dto import PolicyDto
from affinidi_tdk_iam_client.models.policy_statement_dto import PolicyStatementDto
from affinidi_tdk_iam_client.models.principal_cannot_be_deleted_error import PrincipalCannotBeDeletedError
from affinidi_tdk_iam_client.models.principal_does_not_belong_to_project_error import PrincipalDoesNotBelongToProjectError
from affinidi_tdk_iam_client.models.project_dto import ProjectDto
from affinidi_tdk_iam_client.models.project_list import ProjectList
from affinidi_tdk_iam_client.models.service_error_response import ServiceErrorResponse
from affinidi_tdk_iam_client.models.service_error_response_details_inner import ServiceErrorResponseDetailsInner
from affinidi_tdk_iam_client.models.token_authentication_method_dto import TokenAuthenticationMethodDto
from affinidi_tdk_iam_client.models.token_dto import TokenDto
from affinidi_tdk_iam_client.models.token_list import TokenList
from affinidi_tdk_iam_client.models.token_private_key_authentication_method_dto import TokenPrivateKeyAuthenticationMethodDto
from affinidi_tdk_iam_client.models.token_private_key_authentication_method_dto_public_key_info import TokenPrivateKeyAuthenticationMethodDtoPublicKeyInfo
from affinidi_tdk_iam_client.models.token_private_key_authentication_method_dto_public_key_info_one_of import TokenPrivateKeyAuthenticationMethodDtoPublicKeyInfoOneOf
from affinidi_tdk_iam_client.models.token_private_key_authentication_method_dto_public_key_info_one_of1 import TokenPrivateKeyAuthenticationMethodDtoPublicKeyInfoOneOf1
from affinidi_tdk_iam_client.models.typed_pricipal_id import TypedPricipalId
from affinidi_tdk_iam_client.models.unauthorized_error import UnauthorizedError
from affinidi_tdk_iam_client.models.unexpected_error import UnexpectedError
from affinidi_tdk_iam_client.models.update_project_input import UpdateProjectInput
from affinidi_tdk_iam_client.models.update_token_input import UpdateTokenInput
from affinidi_tdk_iam_client.models.update_token_private_key_authentication_method_dto import UpdateTokenPrivateKeyAuthenticationMethodDto
from affinidi_tdk_iam_client.models.user_dto import UserDto
from affinidi_tdk_iam_client.models.user_list import UserList
from affinidi_tdk_iam_client.models.whoami_dto import WhoamiDto
