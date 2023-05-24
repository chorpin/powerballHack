from polygon import RESTClient


class PolygonClient:
    api_key = "CI9HVEK_mRyWZaOlrhMw5NFhaR86H9N4"

    def __init__(self):
        pass

    def create_client(self):
        # api_key is used
        client = RESTClient("CI9HVEK_mRyWZaOlrhMw5NFhaR86H9N4")
        return client
