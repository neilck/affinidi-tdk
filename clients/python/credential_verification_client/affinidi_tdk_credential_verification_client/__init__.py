# coding: utf-8

# flake8: noqa

"""
    VerificationService

    Affinidi VerificationService Structure

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from affinidi_tdk_credential_verification_client.api.default_api import DefaultApi

# import ApiClient
from affinidi_tdk_credential_verification_client.api_response import ApiResponse
from affinidi_tdk_credential_verification_client.api_client import ApiClient
from affinidi_tdk_credential_verification_client.configuration import Configuration
from affinidi_tdk_credential_verification_client.exceptions import OpenApiException
from affinidi_tdk_credential_verification_client.exceptions import ApiTypeError
from affinidi_tdk_credential_verification_client.exceptions import ApiValueError
from affinidi_tdk_credential_verification_client.exceptions import ApiKeyError
from affinidi_tdk_credential_verification_client.exceptions import ApiAttributeError
from affinidi_tdk_credential_verification_client.exceptions import ApiException

# import models into sdk package
from affinidi_tdk_credential_verification_client.models.constraints import Constraints
from affinidi_tdk_credential_verification_client.models.constraints_statuses import ConstraintsStatuses
from affinidi_tdk_credential_verification_client.models.credential_requirements import CredentialRequirements
from affinidi_tdk_credential_verification_client.models.credential_requirements_constraints import CredentialRequirementsConstraints
from affinidi_tdk_credential_verification_client.models.descriptor import Descriptor
from affinidi_tdk_credential_verification_client.models.error import Error
from affinidi_tdk_credential_verification_client.models.error_detail import ErrorDetail
from affinidi_tdk_credential_verification_client.models.evaluate_vp_output import EvaluateVpOutput
from affinidi_tdk_credential_verification_client.models.field import Field
from affinidi_tdk_credential_verification_client.models.filter import Filter
from affinidi_tdk_credential_verification_client.models.filter_const import FilterConst
from affinidi_tdk_credential_verification_client.models.filter_items import FilterItems
from affinidi_tdk_credential_verification_client.models.format import Format
from affinidi_tdk_credential_verification_client.models.free_form_object import FreeFormObject
from affinidi_tdk_credential_verification_client.models.holder_subject import HolderSubject
from affinidi_tdk_credential_verification_client.models.input_descriptor import InputDescriptor
from affinidi_tdk_credential_verification_client.models.invalid_parameter_error import InvalidParameterError
from affinidi_tdk_credential_verification_client.models.jwt_object import JwtObject
from affinidi_tdk_credential_verification_client.models.ldp_object import LdpObject
from affinidi_tdk_credential_verification_client.models.nested_descriptor import NestedDescriptor
from affinidi_tdk_credential_verification_client.models.not_found_error import NotFoundError
from affinidi_tdk_credential_verification_client.models.not_found_error_details_inner import NotFoundErrorDetailsInner
from affinidi_tdk_credential_verification_client.models.pd_status import PdStatus
from affinidi_tdk_credential_verification_client.models.presentation_definition import PresentationDefinition
from affinidi_tdk_credential_verification_client.models.presentation_submission import PresentationSubmission
from affinidi_tdk_credential_verification_client.models.submission_requirement import SubmissionRequirement
from affinidi_tdk_credential_verification_client.models.validate_jwt_input import ValidateJwtInput
from affinidi_tdk_credential_verification_client.models.validate_jwt_output import ValidateJwtOutput
from affinidi_tdk_credential_verification_client.models.verify_credential_input import VerifyCredentialInput
from affinidi_tdk_credential_verification_client.models.verify_credential_output import VerifyCredentialOutput
from affinidi_tdk_credential_verification_client.models.verify_presentation_input import VerifyPresentationInput
from affinidi_tdk_credential_verification_client.models.verify_presentation_output import VerifyPresentationOutput
from affinidi_tdk_credential_verification_client.models.verify_presentation_output_errors import VerifyPresentationOutputErrors
from affinidi_tdk_credential_verification_client.models.w3c_credential import W3cCredential
from affinidi_tdk_credential_verification_client.models.w3c_credential_credential_schema import W3cCredentialCredentialSchema
from affinidi_tdk_credential_verification_client.models.w3c_credential_credential_subject import W3cCredentialCredentialSubject
from affinidi_tdk_credential_verification_client.models.w3c_credential_holder import W3cCredentialHolder
from affinidi_tdk_credential_verification_client.models.w3c_credential_status import W3cCredentialStatus
from affinidi_tdk_credential_verification_client.models.w3c_presentation import W3cPresentation
from affinidi_tdk_credential_verification_client.models.w3c_presentation_context import W3cPresentationContext
from affinidi_tdk_credential_verification_client.models.w3c_presentation_context_one_of_inner import W3cPresentationContextOneOfInner
from affinidi_tdk_credential_verification_client.models.w3c_proof import W3cProof
