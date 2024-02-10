# au_open_banking_spec.ProductsApi

All URIs are relative to *https://data.holder.com.au/cds-au/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_detail**](ProductsApi.md#get_product_detail) | **GET** /banking/products/{productId} | Get Product Detail
[**list_products**](ProductsApi.md#list_products) | **GET** /banking/products | Get Products


# **get_product_detail**
> ResponseBankingProductByIdV4 get_product_detail(product_id, x_v=x_v, x_min_v=x_min_v)

Get Product Detail

Obtain detailed information on a single product offered openly to the market.  Obsolete versions: [v1](includes/obsolete/get-product-detail-v1.html) [v2](includes/obsolete/get-product-detail-v2.html) [v3](includes/obsolete/get-product-detail-v3.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_product_by_id_v4 import ResponseBankingProductByIdV4
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
    api_instance = au_open_banking_spec.ProductsApi(api_client)
    product_id = 'product_id_example' # str | ID of the specific product requested
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)

    try:
        # Get Product Detail
        api_response = await api_instance.get_product_detail(product_id, x_v=x_v, x_min_v=x_min_v)
        print("The response of ProductsApi->get_product_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| ID of the specific product requested | 
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 

### Return type

[**ResponseBankingProductByIdV4**](ResponseBankingProductByIdV4.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;/ul&gt; |  -  |
**404** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[404 - Unavailable Resource](#error-404-resource-unavailable)&lt;/li&gt;&lt;li&gt;[404 - Invalid Resource](#error-404-resource-invalid)&lt;/li&gt;&lt;/ul&gt; |  -  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_products**
> ResponseBankingProductListV2 list_products(effective=effective, updated_since=updated_since, brand=brand, product_category=product_category, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v)

Get Products

Obtain a list of products that are currently openly offered to the market  Note that the results returned by this end point are expected to be ordered in descending order according to ``lastUpdated``.  ### Conventions In the product reference payloads there are a number of recurring conventions that are explained here, in one place.  #### Arrays Of Features  In the product detail payload there are a number of arrays articulating generic features, constraints, prices, etc. The intent of these arrays is as follows:  - Each element in an array has the same structure so that clients can reliably interpret the payloads - Each element as a type element that is an enumeration of the specific aspect of a product being described, such as types of fees. - Each element has a field name [additionalValue](#productfeaturetypedoc).  This is a generic field with contents that will vary based on the type of object being described. The contents of this field for the ADDITIONAL_CARDS feature is the number of cards allowed while the contents of this field for the MAX_LIMIT constraint would be the maximum credit limit allowed for the product. - An element in these arrays of the same type may appear more than once. For instance, a product may offer two separate loyalty programs that the customer can select from. A fixed term mortgage may have different rates for different term lengths. - An element in these arrays may contain an additionalInfo and additionalInfoUri field. The additionalInfo field is used to provide displayable text clarifying the purpose of the element in some way when the product is presented to a customer. The additionalInfoUri provides a link to externally hosted information specifically relevant to that feature of the product. - Depending on the type of data being represented there may be additional specific fields.  #### URIs To More Information  As the complexities and nuances of a financial product can not easily be fully expressed in a data structure without a high degree of complexity it is necessary to provide additional reference information that a potential customer can access so that they are fully informed of the features and implications of the product. The payloads for product reference therefore contain numerous fields that are provided to allow the product holder to describe the product more fully using a web page hosted on their online channels.  These URIs do not need to all link to different pages. If desired, they can all link to a single hosted page and use difference HTML anchors to focus on a specific topic such as eligibility or fees.  #### Linkage To Accounts From the moment that a customer applies for a product and an account is created the account and the product that spawned it will diverge.  Rates and features of the product may change and a discount may be negotiated for the account.  For this reason, while productCategory is a common field between accounts and products, there is no specific ID that can be used to link an account to a product within the regime.  Similarly, many of the fields and objects in the product payload will appear in the account detail payload but the structures and semantics are not identical as one refers to a product that can potentially be originated and one refers to an account that actually has been instantiated and created along with the associated decisions inherent in that process.  #### Dates It is expected that data consumers needing this data will call relatively frequently to ensure the data they have is representative of the current offering from a bank.  To minimise the volume and frequency of these calls the ability to set a lastUpdated field with the date and time of the last update to this product is included.  A call for a list of products can then be filtered to only return products that have been updated since the last time that data was obtained using the updated-since query parameter.  In addition, the concept of effective date and time has also been included.  This allows for a product to be marked for obsolescence, or introduction, from a certain time without the need for an update to show that a product has been changed.  The inclusion of these dates also removes the need to represent deleted products in the payload.  Products that are no long offered can be marked not effective for a few weeks before they are then removed from the product set as an option entirely.  Obsolete versions: [v1](includes/obsolete/get-products-v1.html) [v2](includes/obsolete/get-products-v2.html)

### Example


```python
import au_open_banking_spec
from au_open_banking_spec.models.response_banking_product_list_v2 import ResponseBankingProductListV2
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
    api_instance = au_open_banking_spec.ProductsApi(api_client)
    effective = 'CURRENT' # str | Allows for the filtering of products based on whether the current time is within the period of time defined as effective by the effectiveFrom and effectiveTo fields. Valid values are ‘CURRENT’, ‘FUTURE’ and ‘ALL’. If absent defaults to 'CURRENT' (optional) (default to 'CURRENT')
    updated_since = 'updated_since_example' # str | Only include products that have been updated after the specified date and time. If absent defaults to include all products (optional)
    brand = 'brand_example' # str | Filter results based on a specific brand (optional)
    product_category = 'product_category_example' # str | Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned. (optional)
    page = 1 # int | Page of results to request (standard pagination) (optional) (default to 1)
    page_size = 25 # int | Page size to request. Default is 25 (standard pagination) (optional) (default to 25)
    x_v = 'x_v_example' # str | Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) (optional)
    x_min_v = 'x_min_v_example' # str | Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. (optional)

    try:
        # Get Products
        api_response = await api_instance.list_products(effective=effective, updated_since=updated_since, brand=brand, product_category=product_category, page=page, page_size=page_size, x_v=x_v, x_min_v=x_min_v)
        print("The response of ProductsApi->list_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->list_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **effective** | **str**| Allows for the filtering of products based on whether the current time is within the period of time defined as effective by the effectiveFrom and effectiveTo fields. Valid values are ‘CURRENT’, ‘FUTURE’ and ‘ALL’. If absent defaults to &#39;CURRENT&#39; | [optional] [default to &#39;CURRENT&#39;]
 **updated_since** | **str**| Only include products that have been updated after the specified date and time. If absent defaults to include all products | [optional] 
 **brand** | **str**| Filter results based on a specific brand | [optional] 
 **product_category** | **str**| Used to filter results on the productCategory field applicable to accounts. Any one of the valid values for this field can be supplied. If absent then all accounts returned. | [optional] 
 **page** | **int**| Page of results to request (standard pagination) | [optional] [default to 1]
 **page_size** | **int**| Page size to request. Default is 25 (standard pagination) | [optional] [default to 25]
 **x_v** | **str**| Version of the API end point requested by the client. Must be set to a positive integer. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If the value of [x-min-v](#request-headers) is equal to or higher than the value of [x-v](#request-headers) then the [x-min-v](#request-headers) header should be treated as absent. If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. See [HTTP Headers](#request-headers) | [optional] 
 **x_min_v** | **str**| Minimum version of the API end point requested by the client. Must be set to a positive integer if provided. The data holder should respond with the highest supported version between [x-min-v](#request-headers) and [x-v](#request-headers). If all versions requested are not supported then the data holder must respond with a 406 Not Acceptable. | [optional] 

### Return type

[**ResponseBankingProductListV2**](ResponseBankingProductListV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * x-v - The [version](#response-headers) of the API end point that the data holder has responded with. <br>  |
**400** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[400 - Invalid Field](#error-400-field-invalid)&lt;/li&gt;&lt;li&gt;[400 - Missing Field](#error-400-field-missing)&lt;/li&gt;&lt;li&gt;[400 - Invalid Version](#error-400-header-invalid-version)&lt;/li&gt;&lt;li&gt;[400 - Invalid Date](#error-400-field-invalid-date-time)&lt;/li&gt;&lt;li&gt;[400 - Invalid Page Size](#error-400-field-invalid-page-size)&lt;/li&gt;&lt;/ul&gt; |  -  |
**406** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[406 - Unsupported Version](#error-406-header-unsupported-version)&lt;/li&gt;&lt;/ul&gt; |  -  |
**422** | The following error codes MUST be supported:&lt;br/&gt;&lt;ul class&#x3D;\&quot;error-code-list\&quot;&gt;&lt;li&gt;[422 - Invalid Page](#error-422-field-invalid-page)&lt;/li&gt;&lt;/ul&gt; |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

