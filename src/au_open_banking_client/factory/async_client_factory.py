class AsyncClientFactory:
    def __init__(self, config: ClientConfig):
        self.config = config

    def create_client(self) -> AsyncClient:
        return AsyncClient(
            base_url=self.config.base_url,
            headers=self.config.headers,
            timeout=self.config.timeout,
        )
