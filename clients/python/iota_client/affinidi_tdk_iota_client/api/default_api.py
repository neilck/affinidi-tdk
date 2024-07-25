# coding: utf-8

"""
    IotaService

    Affinidi IotaService Structure

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
from pydantic import Field, StrictStr, conint, constr

from typing import Optional

from affinidi_tdk_iota_client.models.list_logged_consents_ok import ListLoggedConsentsOK

from affinidi_tdk_iota_client.api_client import ApiClient
from affinidi_tdk_iota_client.api_response import ApiResponse
from affinidi_tdk_iota_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def list_logged_consents(self, user_id : Optional[StrictStr] = None, limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Maximum number of records to fetch in a list")] = None, exclusive_start_key : Annotated[Optional[constr(strict=True, max_length=3000)], Field(description="The base64url encoded key of the first item that this operation will evaluate (it is not returned). Use the value that was returned in the previous operation.")] = None, **kwargs) -> ListLoggedConsentsOK:  # noqa: E501
        """list_logged_consents  # noqa: E501

        returns a list of logged consents for the project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_logged_consents(user_id, limit, exclusive_start_key, async_req=True)
        >>> result = thread.get()

        :param user_id:
        :type user_id: str
        :param limit: Maximum number of records to fetch in a list
        :type limit: int
        :param exclusive_start_key: The base64url encoded key of the first item that this operation will evaluate (it is not returned). Use the value that was returned in the previous operation.
        :type exclusive_start_key: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListLoggedConsentsOK
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the list_logged_consents_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.list_logged_consents_with_http_info(user_id, limit, exclusive_start_key, **kwargs)  # noqa: E501

    @validate_arguments
    def list_logged_consents_with_http_info(self, user_id : Optional[StrictStr] = None, limit : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Maximum number of records to fetch in a list")] = None, exclusive_start_key : Annotated[Optional[constr(strict=True, max_length=3000)], Field(description="The base64url encoded key of the first item that this operation will evaluate (it is not returned). Use the value that was returned in the previous operation.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """list_logged_consents  # noqa: E501

        returns a list of logged consents for the project  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_logged_consents_with_http_info(user_id, limit, exclusive_start_key, async_req=True)
        >>> result = thread.get()

        :param user_id:
        :type user_id: str
        :param limit: Maximum number of records to fetch in a list
        :type limit: int
        :param exclusive_start_key: The base64url encoded key of the first item that this operation will evaluate (it is not returned). Use the value that was returned in the previous operation.
        :type exclusive_start_key: str
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
        :rtype: tuple(ListLoggedConsentsOK, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'user_id',
            'limit',
            'exclusive_start_key'
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
                    " to method list_logged_consents" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('user_id') is not None:  # noqa: E501
            _query_params.append(('userId', _params['user_id']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('exclusive_start_key') is not None:  # noqa: E501
            _query_params.append(('exclusiveStartKey', _params['exclusive_start_key']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ProjectTokenAuth']  # noqa: E501

        _response_types_map = {
            '200': "ListLoggedConsentsOK",
            '400': "InvalidParameterError",
            '403': "OperationForbiddenError",
        }

        return self.api_client.call_api(
            '/v1/logged-consents', 'GET',
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
