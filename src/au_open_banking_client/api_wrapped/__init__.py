from typing import Optional

from au_open_banking_spec import ApiClient
from .products_api import AsyncProductsApi


class AsyncApiBundle:
    products: AsyncProductsApi

    def __init__(self, api_client: Optional[ApiClient] = None):
        self.api_client = api_client
        self.products = AsyncProductsApi(api_client)
