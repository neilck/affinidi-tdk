# coding: utf-8

"""
    IotaService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field

from affinidi_tdk_iota_client.models.aws_exchange_credentials import AwsExchangeCredentials
from affinidi_tdk_iota_client.models.aws_exchange_credentials_ok import AwsExchangeCredentialsOK
from affinidi_tdk_iota_client.models.aws_exchange_credentials_project_token import AwsExchangeCredentialsProjectToken
from affinidi_tdk_iota_client.models.fetch_iotavp_response_input import FetchIOTAVPResponseInput
from affinidi_tdk_iota_client.models.fetch_iotavp_response_ok import FetchIOTAVPResponseOK
from affinidi_tdk_iota_client.models.initiate_data_sharing_request_input import InitiateDataSharingRequestInput
from affinidi_tdk_iota_client.models.initiate_data_sharing_request_ok import InitiateDataSharingRequestOK
from affinidi_tdk_iota_client.models.iota_exchange_credentials import IotaExchangeCredentials
from affinidi_tdk_iota_client.models.iota_exchange_credentials_ok import IotaExchangeCredentialsOK

from affinidi_tdk_iota_client.api_client import ApiClient
from affinidi_tdk_iota_client.api_response import ApiResponse
from affinidi_tdk_iota_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class IotaApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def aws_exchange_credentials(self, aws_exchange_credentials : Annotated[AwsExchangeCredentials, Field(..., description="AwsExchangeCredentials")], **kwargs) -> AwsExchangeCredentialsOK:  # noqa: E501
        """aws_exchange_credentials  # noqa: E501

        It exchanges limited token into cognito  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.aws_exchange_credentials(aws_exchange_credentials, async_req=True)
        >>> result = thread.get()

        :param aws_exchange_credentials: AwsExchangeCredentials (required)
        :type aws_exchange_credentials: AwsExchangeCredentials
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AwsExchangeCredentialsOK
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the aws_exchange_credentials_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.aws_exchange_credentials_with_http_info(aws_exchange_credentials, **kwargs)  # noqa: E501

    @validate_arguments
    def aws_exchange_credentials_with_http_info(self, aws_exchange_credentials : Annotated[AwsExchangeCredentials, Field(..., description="AwsExchangeCredentials")], **kwargs) -> ApiResponse:  # noqa: E501
        """aws_exchange_credentials  # noqa: E501

        It exchanges limited token into cognito  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.aws_exchange_credentials_with_http_info(aws_exchange_credentials, async_req=True)
        >>> result = thread.get()

        :param aws_exchange_credentials: AwsExchangeCredentials (required)
        :type aws_exchange_credentials: AwsExchangeCredentials
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AwsExchangeCredentialsOK, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'aws_exchange_credentials'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aws_exchange_credentials" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['aws_exchange_credentials'] is not None:
            _body_params = _params['aws_exchange_credentials']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "AwsExchangeCredentialsOK",
            '400': "InvalidParameterError",
            '403': "OperationForbiddenError",
        }

        return self.api_client.call_api(
            '/v1/aws-exchange-credentials', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def aws_exchange_credentials_project_token(self, aws_exchange_credentials_project_token : Annotated[AwsExchangeCredentialsProjectToken, Field(..., description="AwsExchangeCredentialsProjectToken")], **kwargs) -> IotaExchangeCredentialsOK:  # noqa: E501
        """aws_exchange_credentials_project_token  # noqa: E501

        It exchanges project token into cognito  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.aws_exchange_credentials_project_token(aws_exchange_credentials_project_token, async_req=True)
        >>> result = thread.get()

        :param aws_exchange_credentials_project_token: AwsExchangeCredentialsProjectToken (required)
        :type aws_exchange_credentials_project_token: AwsExchangeCredentialsProjectToken
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: IotaExchangeCredentialsOK
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the aws_exchange_credentials_project_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.aws_exchange_credentials_project_token_with_http_info(aws_exchange_credentials_project_token, **kwargs)  # noqa: E501

    @validate_arguments
    def aws_exchange_credentials_project_token_with_http_info(self, aws_exchange_credentials_project_token : Annotated[AwsExchangeCredentialsProjectToken, Field(..., description="AwsExchangeCredentialsProjectToken")], **kwargs) -> ApiResponse:  # noqa: E501
        """aws_exchange_credentials_project_token  # noqa: E501

        It exchanges project token into cognito  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.aws_exchange_credentials_project_token_with_http_info(aws_exchange_credentials_project_token, async_req=True)
        >>> result = thread.get()

        :param aws_exchange_credentials_project_token: AwsExchangeCredentialsProjectToken (required)
        :type aws_exchange_credentials_project_token: AwsExchangeCredentialsProjectToken
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(IotaExchangeCredentialsOK, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'aws_exchange_credentials_project_token'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method aws_exchange_credentials_project_token" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['aws_exchange_credentials_project_token'] is not None:
            _body_params = _params['aws_exchange_credentials_project_token']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ProjectTokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "IotaExchangeCredentialsOK",
            '400': "InvalidParameterError",
            '403': "OperationForbiddenError",
        }

        return self.api_client.call_api(
            '/v1/aws-exchange-credentials/project-token', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def fetch_iota_vp_response(self, fetch_iotavp_response_input : Annotated[FetchIOTAVPResponseInput, Field(..., description="FetchIOTAVPResponseInput")], **kwargs) -> FetchIOTAVPResponseOK:  # noqa: E501
        """fetch_iota_vp_response  # noqa: E501

        This will get the final data response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_iota_vp_response(fetch_iotavp_response_input, async_req=True)
        >>> result = thread.get()

        :param fetch_iotavp_response_input: FetchIOTAVPResponseInput (required)
        :type fetch_iotavp_response_input: FetchIOTAVPResponseInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FetchIOTAVPResponseOK
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the fetch_iota_vp_response_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.fetch_iota_vp_response_with_http_info(fetch_iotavp_response_input, **kwargs)  # noqa: E501

    @validate_arguments
    def fetch_iota_vp_response_with_http_info(self, fetch_iotavp_response_input : Annotated[FetchIOTAVPResponseInput, Field(..., description="FetchIOTAVPResponseInput")], **kwargs) -> ApiResponse:  # noqa: E501
        """fetch_iota_vp_response  # noqa: E501

        This will get the final data response  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_iota_vp_response_with_http_info(fetch_iotavp_response_input, async_req=True)
        >>> result = thread.get()

        :param fetch_iotavp_response_input: FetchIOTAVPResponseInput (required)
        :type fetch_iotavp_response_input: FetchIOTAVPResponseInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(FetchIOTAVPResponseOK, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fetch_iotavp_response_input'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_iota_vp_response" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['fetch_iotavp_response_input'] is not None:
            _body_params = _params['fetch_iotavp_response_input']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ProjectTokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "FetchIOTAVPResponseOK",
            '400': "InvalidParameterError",
            '403': "OperationForbiddenError",
        }

        return self.api_client.call_api(
            '/v1/fetch-iota-response', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def initiate_data_sharing_request(self, initiate_data_sharing_request_input : Annotated[InitiateDataSharingRequestInput, Field(..., description="InitiateDataSharingRequestInput")], **kwargs) -> InitiateDataSharingRequestOK:  # noqa: E501
        """initiate_data_sharing_request  # noqa: E501

        This will initiate data sharing request for the data sharing flow  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.initiate_data_sharing_request(initiate_data_sharing_request_input, async_req=True)
        >>> result = thread.get()

        :param initiate_data_sharing_request_input: InitiateDataSharingRequestInput (required)
        :type initiate_data_sharing_request_input: InitiateDataSharingRequestInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InitiateDataSharingRequestOK
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the initiate_data_sharing_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.initiate_data_sharing_request_with_http_info(initiate_data_sharing_request_input, **kwargs)  # noqa: E501

    @validate_arguments
    def initiate_data_sharing_request_with_http_info(self, initiate_data_sharing_request_input : Annotated[InitiateDataSharingRequestInput, Field(..., description="InitiateDataSharingRequestInput")], **kwargs) -> ApiResponse:  # noqa: E501
        """initiate_data_sharing_request  # noqa: E501

        This will initiate data sharing request for the data sharing flow  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.initiate_data_sharing_request_with_http_info(initiate_data_sharing_request_input, async_req=True)
        >>> result = thread.get()

        :param initiate_data_sharing_request_input: InitiateDataSharingRequestInput (required)
        :type initiate_data_sharing_request_input: InitiateDataSharingRequestInput
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(InitiateDataSharingRequestOK, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'initiate_data_sharing_request_input'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method initiate_data_sharing_request" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['initiate_data_sharing_request_input'] is not None:
            _body_params = _params['initiate_data_sharing_request_input']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ProjectTokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "InitiateDataSharingRequestOK",
            '400': "InvalidParameterError",
            '403': "OperationForbiddenError",
        }

        return self.api_client.call_api(
            '/v1/initiate-data-sharing-request', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def iota_exchange_credentials(self, iota_exchange_credentials : Annotated[IotaExchangeCredentials, Field(..., description="IotaAwsExchangeCredentials")], **kwargs) -> IotaExchangeCredentialsOK:  # noqa: E501
        """iota_exchange_credentials  # noqa: E501

        It exchanges limited token into cognito sts identity credentials  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.iota_exchange_credentials(iota_exchange_credentials, async_req=True)
        >>> result = thread.get()

        :param iota_exchange_credentials: IotaAwsExchangeCredentials (required)
        :type iota_exchange_credentials: IotaExchangeCredentials
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: IotaExchangeCredentialsOK
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the iota_exchange_credentials_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.iota_exchange_credentials_with_http_info(iota_exchange_credentials, **kwargs)  # noqa: E501

    @validate_arguments
    def iota_exchange_credentials_with_http_info(self, iota_exchange_credentials : Annotated[IotaExchangeCredentials, Field(..., description="IotaAwsExchangeCredentials")], **kwargs) -> ApiResponse:  # noqa: E501
        """iota_exchange_credentials  # noqa: E501

        It exchanges limited token into cognito sts identity credentials  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.iota_exchange_credentials_with_http_info(iota_exchange_credentials, async_req=True)
        >>> result = thread.get()

        :param iota_exchange_credentials: IotaAwsExchangeCredentials (required)
        :type iota_exchange_credentials: IotaExchangeCredentials
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(IotaExchangeCredentialsOK, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'iota_exchange_credentials'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method iota_exchange_credentials" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['iota_exchange_credentials'] is not None:
            _body_params = _params['iota_exchange_credentials']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "IotaExchangeCredentialsOK",
            '400': "InvalidParameterError",
            '403': "OperationForbiddenError",
        }

        return self.api_client.call_api(
            '/v1/exchange-credentials', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
