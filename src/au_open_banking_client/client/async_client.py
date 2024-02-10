from typing import Optional, AsyncGenerator

from au_open_banking_client.api_wrapped import AsyncApiBundle
from au_open_banking_client.client.utils import paginate
from au_open_banking_spec import BankingProductCategory, BankingProductV4


class AsyncClient:
    api: AsyncApiBundle

    def __init__(self, api: AsyncApiBundle):
        self.api = api

    async def get_all_products(
        self, product_category: Optional[BankingProductCategory] = None, batch_size: int = 100
    ) -> AsyncGenerator[BankingProductV4, None]:

        paginator = paginate(self.api.products.list_products)(
            product_category=product_category,
            page_size=batch_size,
        )

        async for page in paginator:
            for product in page.data.products:
                yield product

