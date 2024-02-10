# Australian CDS Open Banking Client
This is a client library for the Australian CDS Open Banking API. It is handy wrapper from the OpenAPI specification.
It provides a simple way to interact with the API using either sync or async clients.

---
### ⚠️ DRAFT warning
### This project is a work in progress and is not yet ready for use.


### Usage
You can use endpoints directly

```python
from au_open_banking_client.api_wrapped import AsyncApiBundle
from au_open_banking_client.client.async_client import AsyncClient
from au_open_banking_client.schemas.BankEndpoint import KnownBankHost
from au_open_banking_spec import Configuration, ApiClient

configuration = Configuration(
    host=KnownBankHost.COMMBANK.value
)

client = AsyncClient(AsyncApiBundle(ApiClient(configuration)))

await cl.api.products.get_product_detail(product_id="id")
```

OR with some wrappers\
(you can also inherit and add you own helper methods)

```python
async for product in client.get_all_products():
    print(f"{product.name} -  {product.application_uri}")
```

go-task install (modern make replacement)
```shell
# macOS
brew install go-task

# windows
choco install go-task

# linux
npm install -g @go-task/cli
# + reffer to https://taskfile.dev/#/installation
```

### CDS open Banking Client
https://consumerdatastandardsaustralia.github.io/standards/includes/swagger/cds_banking.yaml


### TODO:
- [ ] sync/async client factory
