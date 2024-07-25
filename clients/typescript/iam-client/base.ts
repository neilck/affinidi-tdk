/* tslint:disable */
/* eslint-disable */
/**
 * Iam
 * Affinidi IAM
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: info@affinidi.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import type { Configuration } from './configuration'
// Some imports not used depending on template conditions
// @ts-ignore
import type { AxiosPromise, AxiosInstance, RawAxiosRequestConfig } from 'axios'
import globalAxios, { AxiosError } from 'axios'
import axiosRetry, { IAxiosRetryConfig } from 'axios-retry'

export class SdkError extends Error {
  private readonly details: undefined
  private readonly traceId: string
  private readonly httpStatusCode: number | undefined

  constructor(originalError: unknown = {}) {
    const isAxiosError = originalError instanceof AxiosError

    if (!isAxiosError) {
      throw originalError
    }

    super(originalError.response?.data?.message)

    this.name = originalError.response?.data?.name
    this.details = originalError.response?.data?.details
    this.message = originalError.response?.data?.message
    this.traceId = originalError.response?.data?.traceId
    this.httpStatusCode = originalError.response?.status
  }
}

export const BASE_PATH = 'https://apse1.api.affinidi.io/iam'.replace(/\/+$/, '')
const DEFAULT_REQUEST_RETRIES = 3

/**
 *
 * @export
 */
export const COLLECTION_FORMATS = {
  csv: ',',
  ssv: ' ',
  tsv: '\t',
  pipes: '|',
}

/**
 *
 * @export
 * @interface RequestArgs
 */
export interface RequestArgs {
  url: string
  options: RawAxiosRequestConfig
}

type RetryConfig = {
  retries?: number
  isExponentialDelay?: boolean
}

/**
 *
 * @export
 * @class BaseAPI
 */
export class BaseAPI {
  protected configuration: Configuration | undefined
  protected retryConfig: IAxiosRetryConfig

  constructor(
    configuration?: Configuration,
    retryConfig?: RetryConfig,
    protected basePath: string = BASE_PATH,
    protected axios: AxiosInstance = globalAxios,
  ) {
    if (configuration) {
      this.configuration = configuration
      this.basePath = configuration.basePath ?? basePath
    }

    this.retryConfig = {
      retries:
        retryConfig?.retries >= 0 &&
        retryConfig?.retries <= DEFAULT_REQUEST_RETRIES
          ? retryConfig.retries
          : DEFAULT_REQUEST_RETRIES,
      retryDelay: retryConfig?.isExponentialDelay
        ? axiosRetry.exponentialDelay
        : () => {
            return 0
          },
      retryCondition: (error: AxiosError) => {
        if (
          axiosRetry.isNetworkOrIdempotentRequestError(error) ||
          axiosRetry.isNetworkError(error)
        ) {
          return true
        }

        throw new SdkError(error)
      },
    }

    axiosRetry(globalAxios, this.retryConfig)
  }
}

/**
 *
 * @export
 * @class RequiredError
 * @extends {Error}
 */
export class RequiredError extends Error {
  constructor(
    public field: string,
    msg?: string,
  ) {
    super(msg)
    this.name = 'RequiredError'
  }
}

interface ServerMap {
  [key: string]: {
    url: string
    description: string
  }[]
}

/**
 *
 * @export
 */
export const operationServerMap: ServerMap = {}
