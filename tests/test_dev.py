import asyncio

import pytest

import au_open_banking_spec
from au_open_banking_client.api_wrapped import AsyncApiBundle
from au_open_banking_client.client.async_client import AsyncClient
from au_open_banking_client.schemas.BankEndpoint import KnownBankHost
from au_open_banking_spec import ApiClient


@pytest.mark.asyncio
async def test_get_all_products():
    configuration = au_open_banking_spec.Configuration(
        host = KnownBankHost.COMMBANK.value
    )

    cl = AsyncClient(AsyncApiBundle(ApiClient(configuration)))

    async for product in cl.get_all_products():
        print(f"""
{product.product_category} ({product.name})
| {product.description}
| link: {product.application_uri}
""")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test_get_all_products())
    loop.close()