import au_open_banking_spec
from au_open_banking_client.wrapper.AnyApiWrapperMixin import AnyApiWrapperMixin


class AsyncProductsApi(
    AnyApiWrapperMixin,
    au_open_banking_spec.ProductsApi,
):
    ...


if __name__ == "__main__":
    a = AsyncProductsApi()
    a.get_product_detail()
