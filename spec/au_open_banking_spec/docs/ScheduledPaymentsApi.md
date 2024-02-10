# au_open_banking_spec.ScheduledPaymentsApi

All URIs are relative to *https://data.holder.com.au/cds-au/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_scheduled_payments**](ScheduledPaymentsApi.md#list_scheduled_payments) | **GET** /banking/accounts/{accountId}/payments/scheduled | Get Scheduled Payments for Account
[**list_scheduled_payments_bulk**](ScheduledPaymentsApi.md#list_scheduled_payments_bulk) | **GET** /banking/payments/scheduled | Get Scheduled Payments Bulk
[**list_scheduled_payments_specific_accounts**](ScheduledPaymentsApi.md#list_scheduled_payments_specific_accounts) | **POST** /banking/payments/scheduled | Get Scheduled Payments For Specific Accounts


# **list_scheduled_payments**
> ResponseBankingScheduledPaymentsListV2 list_scheduled_payments(account_id, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Scheduled Payments for Account

Obtain scheduled, outgoing payments for a specific account  Obsolete versions: [v1](includes/obsolete/get-scheduled-payments-for-account-v1.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_scheduled_payments_list_v2 import ResponseBankingScheduledPaymentsListV2
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
    api_instance = au_open_banking_spec.ScheduledPaymentsApi(api_client)
    account_id = 'account_id_example' # str | ID of the account to get scheduled payments for. Must have previously been returned by one of the account list end points. The account specified is the source account for the payment
    page = 1 # int | Page of results to request (standard pagination) (optional) (default to 1)
    page_size = 25 # int | Page size to request. Default is 25 (standard pagination) (optional) (default to 25)
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Scheduled Payments for Account
        api_response = await api_instance.list_scheduled_payments(account_id, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of ScheduledPaymentsApi->list_scheduled_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledPaymentsApi->list_scheduled_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account to get scheduled payments for. Must have previously been returned by one of the account list end points. The account specified is the source account for the payment | 
 **page** | **int**| Page of results to request (standard pagination) | [optional] [default to 1]
 **page_size** | **int**| Page size to request. Default is 25 (standard pagination) | [optional] [default to 25]
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingScheduledPaymentsListV2**](ResponseBankingScheduledPaymentsListV2.md)

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
**404** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[404 - Unavailable Banking Account](#error-404-authorisation-unavailable-banking-account)&lt;/li&gt;&lt;li&gt;[404 - Invalid Banking Account](#error-404-authorisation-invalid-banking-account)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**422** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[422 - Invalid Page](#error-422-field-invalid-page)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scheduled_payments_bulk**
> ResponseBankingScheduledPaymentsListV2 list_scheduled_payments_bulk(product_category=product_category, open_status=open_status, is_owned=is_owned, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Scheduled Payments Bulk

Obtain scheduled payments for multiple, filtered accounts that are the source of funds for the payments  Obsolete versions: [v1](includes/obsolete/get-scheduled-payments-bulk-v1.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_scheduled_payments_list_v2 import ResponseBankingScheduledPaymentsListV2
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
    api_instance = au_open_banking_spec.ScheduledPaymentsApi(api_client)
    product_category = 'product_category_example' # str | Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned. (optional)
    open_status = 'ALL' # str | Used to filter results according to open/closed status. Values can be OPEN, CLOSED or ALL. If absent then ALL is assumed (optional) (default to 'ALL')
    is_owned = True # bool | Filters accounts based on whether they are owned by the authorised customer.  True for owned accounts, false for unowned accounts and absent for all accounts (optional)
    page = 1 # int | Page of results to request (standard pagination) (optional) (default to 1)
    page_size = 25 # int | Page size to request. Default is 25 (standard pagination) (optional) (default to 25)
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Scheduled Payments Bulk
        api_response = await api_instance.list_scheduled_payments_bulk(product_category=product_category, open_status=open_status, is_owned=is_owned, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of ScheduledPaymentsApi->list_scheduled_payments_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledPaymentsApi->list_scheduled_payments_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_category** | **str**| Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned. | [optional] 
 **open_status** | **str**| Used to filter results according to open/closed status. Values can be OPEN, CLOSED or ALL. If absent then ALL is assumed | [optional] [default to &#39;ALL&#39;]
 **is_owned** | **bool**| Filters accounts based on whether they are owned by the authorised customer.  True for owned accounts, false for unowned accounts and absent for all accounts | [optional] 
 **page** | **int**| Page of results to request (standard pagination) | [optional] [default to 1]
 **page_size** | **int**| Page size to request. Default is 25 (standard pagination) | [optional] [default to 25]
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingScheduledPaymentsListV2**](ResponseBankingScheduledPaymentsListV2.md)

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

# **list_scheduled_payments_specific_accounts**
> ResponseBankingScheduledPaymentsListV2 list_scheduled_payments_specific_accounts(account_ids, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Scheduled Payments For Specific Accounts

Obtain scheduled payments for a specified list of accounts  Obsolete versions: [v1](includes/obsolete/get-scheduled-payments-for-specific-accounts-v1.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.request_account_ids import RequestAccountIds
from au_open_banking_spec.models.response_banking_scheduled_payments_list_v2 import ResponseBankingScheduledPaymentsListV2
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
    api_instance = au_open_banking_spec.ScheduledPaymentsApi(api_client)
    account_ids = au_open_banking_spec.RequestAccountIds() # RequestAccountIds | Array of specific accountIds to obtain scheduled payments for.  The accounts specified are the source of funds for the payments returned
    page = 1 # int | Page of results to request (standard pagination) (optional) (default to 1)
    page_size = 25 # int | Page size to request. Default is 25 (standard pagination) (optional) (default to 25)
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Scheduled Payments For Specific Accounts
        api_response = await api_instance.list_scheduled_payments_specific_accounts(account_ids, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of ScheduledPaymentsApi->list_scheduled_payments_specific_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScheduledPaymentsApi->list_scheduled_payments_specific_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**RequestAccountIds**](RequestAccountIds.md)| Array of specific accountIds to obtain scheduled payments for.  The accounts specified are the source of funds for the payments returned | 
 **page** | **int**| Page of results to request (standard pagination) | [optional] [default to 1]
 **page_size** | **int**| Page size to request. Default is 25 (standard pagination) | [optional] [default to 25]
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingScheduledPaymentsListV2**](ResponseBankingScheduledPaymentsListV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;li&gt;[400 - Invalid Page Size](#error-400-field-invalid-page-size)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**422** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[422 - Invalid Page](#error-422-field-invalid-page)&lt;/li&gt;&lt;li&gt;[422 - Unavailable Banking Account](#error-422-authorisation-unavailable-banking-account)&lt;/li&gt;&lt;li&gt;[422 - Invalid Banking Account](#error-422-authorisation-invalid-banking-account)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

