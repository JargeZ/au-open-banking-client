# au_open_banking_spec.AccountsApi

All URIs are relative to *https://data.holder.com.au/cds-au/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_detail**](AccountsApi.md#get_account_detail) | **GET** /banking/accounts/{accountId} | Get Account Detail
[**get_balance**](AccountsApi.md#get_balance) | **GET** /banking/accounts/{accountId}/balance | Get Account Balance
[**get_transaction_detail**](AccountsApi.md#get_transaction_detail) | **GET** /banking/accounts/{accountId}/transactions/{transactionId} | Get Transaction Detail
[**get_transactions**](AccountsApi.md#get_transactions) | **GET** /banking/accounts/{accountId}/transactions | Get Transactions For Account
[**list_accounts**](AccountsApi.md#list_accounts) | **GET** /banking/accounts | Get Accounts
[**list_balances_bulk**](AccountsApi.md#list_balances_bulk) | **GET** /banking/accounts/balances | Get Bulk Balances
[**list_balances_specific_accounts**](AccountsApi.md#list_balances_specific_accounts) | **POST** /banking/accounts/balances | Get Balances For Specific Accounts


# **get_account_detail**
> ResponseBankingAccountByIdV3 get_account_detail(account_id, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Account Detail

Obtain detailed information on a single account.  Obsolete versions: [v1](includes/obsolete/get-account-detail-v1.html), [v2](includes/obsolete/get-account-detail-v2.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_account_by_id_v3 import ResponseBankingAccountByIdV3
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
    api_instance = au_open_banking_spec.AccountsApi(api_client)
    account_id = 'account_id_example' # str | A tokenised identifier for the account which is unique but not shareable
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Account Detail
        api_response = await api_instance.get_account_detail(account_id, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of AccountsApi->get_account_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_account_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| A tokenised identifier for the account which is unique but not shareable | 
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingAccountByIdV3**](ResponseBankingAccountByIdV3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**404** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[404 - Unavailable Banking Account](#error-404-authorisation-unavailable-banking-account)&lt;/li&gt;&lt;li&gt;[404 - Invalid Banking Account](#error-404-authorisation-invalid-banking-account)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance**
> ResponseBankingAccountsBalanceById get_balance(account_id, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Account Balance

Obtain the balance for a single specified account

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_accounts_balance_by_id import ResponseBankingAccountsBalanceById
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
    api_instance = au_open_banking_spec.AccountsApi(api_client)
    account_id = 'account_id_example' # str | ID of the specific account requested
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Account Balance
        api_response = await api_instance.get_balance(account_id, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of AccountsApi->get_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the specific account requested | 
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingAccountsBalanceById**](ResponseBankingAccountsBalanceById.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**404** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[404 - Unavailable Banking Account](#error-404-authorisation-unavailable-banking-account)&lt;/li&gt;&lt;li&gt;[404 - Invalid Banking Account](#error-404-authorisation-invalid-banking-account)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_detail**
> ResponseBankingTransactionById get_transaction_detail(account_id, transaction_id, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Transaction Detail

Obtain detailed information on a transaction for a specific account

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_transaction_by_id import ResponseBankingTransactionById
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
    api_instance = au_open_banking_spec.AccountsApi(api_client)
    account_id = 'account_id_example' # str | ID of the account to get transactions for.  Must have previously been returned by one of the account list end points
    transaction_id = 'transaction_id_example' # str | ID of the transaction obtained from a previous call to one of the other transaction end points
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Transaction Detail
        api_response = await api_instance.get_transaction_detail(account_id, transaction_id, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of AccountsApi->get_transaction_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_transaction_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account to get transactions for.  Must have previously been returned by one of the account list end points | 
 **transaction_id** | **str**| ID of the transaction obtained from a previous call to one of the other transaction end points | 
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingTransactionById**](ResponseBankingTransactionById.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;li&gt;[400 - Invalid Date](#error-400-field-invalid-date-time)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**404** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[404 - Unavailable Banking Account](#error-404-authorisation-unavailable-banking-account)&lt;/li&gt;&lt;li&gt;[404 - Invalid Banking Account](#error-404-authorisation-invalid-banking-account)&lt;/li&gt;&lt;li&gt;[404 - Unavailable Resource](#error-404-resource-unavailable)&lt;/li&gt;&lt;li&gt;[404 - Invalid Resource](#error-404-resource-invalid)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> ResponseBankingTransactionList get_transactions(account_id, oldest_time=oldest_time, newest_time=newest_time, min_amount=min_amount, max_amount=max_amount, text=text, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Transactions For Account

Obtain transactions for a specific account.  Some general notes that apply to all end points that retrieve transactions:  - Where multiple transactions are returned, transactions should be ordered according to effective date in descending order - As the date and time for a transaction can alter depending on status and transaction type two separate date/times are included in the payload. There are still some scenarios where neither of these time stamps is available. For the purpose of filtering and ordering it is expected that the data holder will use the \"effective\" date/time which will be defined as:   - Posted date/time if available, then   - Execution date/time if available, then   - A reasonable date/time nominated by the data holder using internal data structures - For transaction amounts it should be assumed that a negative value indicates a reduction of the available balance on the account while a positive value indicates an increase in the available balance on the account - For aggregated transactions (ie. groups of sub transactions reported as a single entry for the account) only the aggregated information, with as much consistent information across the subsidiary transactions as possible, is required to be shared

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_transaction_list import ResponseBankingTransactionList
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
    api_instance = au_open_banking_spec.AccountsApi(api_client)
    account_id = 'account_id_example' # str | ID of the account to get transactions for.  Must have previously been returned by one of the account list end points.
    oldest_time = 'oldest_time_example' # str | Constrain the transaction history request to transactions with effective time at or after this date/time. If absent defaults to newest-time minus 90 days.  Format is aligned to DateTimeString common type (optional)
    newest_time = 'newest_time_example' # str | Constrain the transaction history request to transactions with effective time at or before this date/time.  If absent defaults to today.  Format is aligned to DateTimeString common type (optional)
    min_amount = 'min_amount_example' # str | Filter transactions to only transactions with amounts higher than or equal to this amount (optional)
    max_amount = 'max_amount_example' # str | Filter transactions to only transactions with amounts less than or equal to this amount (optional)
    text = 'text_example' # str | Filter transactions to only transactions where this string value is found as a substring of either the reference or description fields. Format is arbitrary ASCII string. This parameter is optionally implemented by data holders. If it is not implemented then a response should be provided as normal without text filtering applied and an additional boolean field named isQueryParamUnsupported should be included in the meta object and set to true (whether the text parameter is supplied or not) (optional)
    page = 1 # int | Page of results to request (standard pagination) (optional) (default to 1)
    page_size = 25 # int | Page size to request. Default is 25 (standard pagination) (optional) (default to 25)
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Transactions For Account
        api_response = await api_instance.get_transactions(account_id, oldest_time=oldest_time, newest_time=newest_time, min_amount=min_amount, max_amount=max_amount, text=text, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of AccountsApi->get_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->get_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| ID of the account to get transactions for.  Must have previously been returned by one of the account list end points. | 
 **oldest_time** | **str**| Constrain the transaction history request to transactions with effective time at or after this date/time. If absent defaults to newest-time minus 90 days.  Format is aligned to DateTimeString common type | [optional] 
 **newest_time** | **str**| Constrain the transaction history request to transactions with effective time at or before this date/time.  If absent defaults to today.  Format is aligned to DateTimeString common type | [optional] 
 **min_amount** | **str**| Filter transactions to only transactions with amounts higher than or equal to this amount | [optional] 
 **max_amount** | **str**| Filter transactions to only transactions with amounts less than or equal to this amount | [optional] 
 **text** | **str**| Filter transactions to only transactions where this string value is found as a substring of either the reference or description fields. Format is arbitrary ASCII string. This parameter is optionally implemented by data holders. If it is not implemented then a response should be provided as normal without text filtering applied and an additional boolean field named isQueryParamUnsupported should be included in the meta object and set to true (whether the text parameter is supplied or not) | [optional] 
 **page** | **int**| Page of results to request (standard pagination) | [optional] [default to 1]
 **page_size** | **int**| Page size to request. Default is 25 (standard pagination) | [optional] [default to 25]
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingTransactionList**](ResponseBankingTransactionList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;li&gt;[400 - Invalid Page Size](#error-400-field-invalid-page-size)&lt;/li&gt;&lt;li&gt;[400 - Invalid Date](#error-400-field-invalid-date-time)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**404** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[404 - Unavailable Banking Account](#error-404-authorisation-unavailable-banking-account)&lt;/li&gt;&lt;li&gt;[404 - Invalid Banking Account](#error-404-authorisation-invalid-banking-account)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |
**422** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[422 - Invalid Page](#error-422-field-invalid-page)&lt;/li&gt;&lt;/ul&gt; |  * x-fapi-interaction-id - An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_accounts**
> ResponseBankingAccountListV2 list_accounts(product_category=product_category, open_status=open_status, is_owned=is_owned, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Accounts

Obtain a list of accounts.  Obsolete versions: [v1](includes/obsolete/get-accounts-v1.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_account_list_v2 import ResponseBankingAccountListV2
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
    api_instance = au_open_banking_spec.AccountsApi(api_client)
    product_category = 'product_category_example' # str | Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned.) (optional)
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
        # Get Accounts
        api_response = await api_instance.list_accounts(product_category=product_category, open_status=open_status, is_owned=is_owned, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of AccountsApi->list_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_category** | **str**| Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned.) | [optional] 
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

[**ResponseBankingAccountListV2**](ResponseBankingAccountListV2.md)

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

# **list_balances_bulk**
> ResponseBankingAccountsBalanceList list_balances_bulk(product_category=product_category, open_status=open_status, is_owned=is_owned, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Bulk Balances

Obtain balances for multiple, filtered accounts

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_accounts_balance_list import ResponseBankingAccountsBalanceList
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
    api_instance = au_open_banking_spec.AccountsApi(api_client)
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
        # Get Bulk Balances
        api_response = await api_instance.list_balances_bulk(product_category=product_category, open_status=open_status, is_owned=is_owned, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of AccountsApi->list_balances_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_balances_bulk: %s\n" % e)
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

[**ResponseBankingAccountsBalanceList**](ResponseBankingAccountsBalanceList.md)

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

# **list_balances_specific_accounts**
> ResponseBankingAccountsBalanceList list_balances_specific_accounts(account_ids, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)

Get Balances For Specific Accounts

Obtain balances for a specified list of accounts

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.request_account_ids import RequestAccountIds
from au_open_banking_spec.models.response_banking_accounts_balance_list import ResponseBankingAccountsBalanceList
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
    api_instance = au_open_banking_spec.AccountsApi(api_client)
    account_ids = au_open_banking_spec.RequestAccountIds() # RequestAccountIds | The list of account IDs to obtain balances for
    page = 1 # int | Page of results to request (standard pagination) (optional) (default to 1)
    page_size = 25 # int | Page size to request. Default is 25 (standard pagination) (optional) (default to 25)
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)
    x_fapi_interaction_id = 'x_fapi_interaction_id_example' # str | An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. (optional)
    x_fapi_auth_date = 'x_fapi_auth_date_example' # str | The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. (optional)
    x_fapi_customer_ip_address = 'x_fapi_customer_ip_address_example' # str | The customer's original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. (optional)
    x_cds_client_headers = 'x_cds_client_headers_example' # str | The customer's original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. (optional)

    try:
        # Get Balances For Specific Accounts
        api_response = await api_instance.list_balances_specific_accounts(account_ids, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v, x_fapi_interaction_id=x_fapi_interaction_id, x_fapi_auth_date=x_fapi_auth_date, x_fapi_customer_ip_address=x_fapi_customer_ip_address, x_cds_client_headers=x_cds_client_headers)
        print("The response of AccountsApi->list_balances_specific_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountsApi->list_balances_specific_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**RequestAccountIds**](RequestAccountIds.md)| The list of account IDs to obtain balances for | 
 **page** | **int**| Page of results to request (standard pagination) | [optional] [default to 1]
 **page_size** | **int**| Page size to request. Default is 25 (standard pagination) | [optional] [default to 25]
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 
 **x_fapi_interaction_id** | **str**| An **[[RFC4122]](#nref-RFC4122)** UUID used as a correlation id. If provided, the data holder must play back this value in the x-fapi-interaction-id response header. If not provided a **[[RFC4122]](#nref-RFC4122)** UUID value is required to be provided in the response header to track the interaction. | [optional] 
 **x_fapi_auth_date** | **str**| The time when the customer last logged in to the Data Recipient Software Product as described in **[[FAPI-1.0-Baseline]](#nref-FAPI-1-0-Baseline)**.  Required for all resource calls (customer present and unattended). Not required for unauthenticated calls. | [optional] 
 **x_fapi_customer_ip_address** | **str**| The customer&#39;s original IP address if the customer is currently logged in to the Data Recipient Software Product. The presence of this header indicates that the API is being called in a customer present context. Not to be included for unauthenticated calls. | [optional] 
 **x_cds_client_headers** | **str**| The customer&#39;s original standard http headers [Base64](#common-field-types) encoded, including the original User Agent header, if the customer is currently logged in to the Data Recipient Software Product. Mandatory for customer present calls.  Not required for unattended or unauthenticated calls. | [optional] 

### Return type

[**ResponseBankingAccountsBalanceList**](ResponseBankingAccountsBalanceList.md)

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

