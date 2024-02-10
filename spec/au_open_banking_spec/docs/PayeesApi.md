# au_open_banking_spec.PayeesApi

All URIs are relative to *https://data.holder.com.au/cds-au/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payee_detail**](PayeesApi.md#get_payee_detail) | **GET** /banking/payees/{payeeId} | Get Payee Detail
[**list_payees**](PayeesApi.md#list_payees) | **GET** /banking/payees | Get Payees


# **get_payee_detail**
> ResponseBankingPayeeByIdV2 get_payee_detail(payee_id, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Payee Detail

Obtain detailed information on a single payee.  Note that the payee sub-structure should be selected to represent the payment destination only rather than any known characteristics of the payment recipient.  Obsolete versions: [v1](includes/obsolete/get-payee-detail-v1.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_payee_by_id_v2 import ResponseBankingPayeeByIdV2
from au_open_banking_spec.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://data.holder.com.au/cds-au/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = au_open_banking_spec.Configuration(
    host = "https://data.holder.com.au/cds-au/v1"
)


# Enter a context with an instance of the API client
async with au_open_banking_spec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = au_open_banking_spec.PayeesApi(api_client)
    payee_id = 'payee_id_example' # str | The ID used to locate the details of a particular payee
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Payee Detail
        api_response = await api_instance.get_payee_detail(payee_id, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of PayeesApi->get_payee_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayeesApi->get_payee_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The ID used to locate the details of a particular payee | 
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingPayeeByIdV2**](ResponseBankingPayeeByIdV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;li&gt;[400 - Invalid Page Size](#error-400-field-invalid-page-size)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**404** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[404 - Unavailable Resource](#error-404-resource-unavailable)&lt;/li&gt;&lt;li&gt;[404 - Invalid Resource](#error-404-resource-invalid)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**422** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[422 - Invalid Page](#error-422-field-invalid-page)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payees**
> ResponseBankingPayeeListV2 list_payees(type=type, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Payees

Obtain a list of pre-registered payees.  Obsolete versions: [v1](includes/obsolete/get-payees-v1.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_payee_list_v2 import ResponseBankingPayeeListV2
from au_open_banking_spec.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://data.holder.com.au/cds-au/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = au_open_banking_spec.Configuration(
    host = "https://data.holder.com.au/cds-au/v1"
)


# Enter a context with an instance of the API client
async with au_open_banking_spec.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = au_open_banking_spec.PayeesApi(api_client)
    type = 'ALL' # str | Filter on the payee type field.  In addition to normal type field values, ALL can be specified to retrieve all payees.  If absent the assumed value is ALL (optional) (default to 'ALL')
    page = 1 # int | Page of results to request (standard pagination) (optional) (default to 1)
    page_size = 25 # int | Page size to request. Default is 25 (standard pagination) (optional) (default to 25)
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Payees
        api_response = await api_instance.list_payees(type=type, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of PayeesApi->list_payees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PayeesApi->list_payees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter on the payee type field.  In addition to normal type field values, ALL can be specified to retrieve all payees.  If absent the assumed value is ALL | [optional] [default to &#39;ALL&#39;]
 **page** | **int**| Page of results to request (standard pagination) | [optional] [default to 1]
 **page_size** | **int**| Page size to request. Default is 25 (standard pagination) | [optional] [default to 25]
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingPayeeListV2**](ResponseBankingPayeeListV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;li&gt;[400 - Invalid Page Size](#error-400-field-invalid-page-size)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**422** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[422 - Invalid Page](#error-422-field-invalid-page)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

