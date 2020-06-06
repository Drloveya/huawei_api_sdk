from aiohttp import ClientSession
from huawei_api_sdk.signature.signer import HttpRequest, Signer

HEADERS = {"content-type": "application/json"}


class ASYHWSClient:

    def __init__(self, Endpoint, HUAWEI_KEY, HUAWEI_SECRET):
        self.Endpoint = Endpoint
        self.HUAWEI_KEY = HUAWEI_KEY
        self.HUAWEI_SECRET = HUAWEI_SECRET
        self.sig = Signer(self.HUAWEI_KEY, self.HUAWEI_SECRET)

    async def get(self, uri, **kwargs):
        body = ""
        headers = HEADERS
        kwargs.setdefault('allow_redirects', True)
        r = HttpRequest("GET", uri=self.Endpoint + uri, headers=headers, body=body)
        self.sig.Sign(r)
        return await _request(r, **kwargs)

    async def post(self, uri, body="", **kwargs):
        headers = HEADERS
        kwargs.setdefault('allow_redirects', True)
        r = HttpRequest("POST", uri=self.Endpoint + uri, headers=headers, body=body)
        self.sig.Sign(r)
        return await _request(r, **kwargs)

    async def put(self, uri, body="", **kwargs):
        headers = HEADERS
        kwargs.setdefault('allow_redirects', True)
        r = HttpRequest("PUT", uri=self.Endpoint + uri, headers=headers, body=body)
        self.sig.Sign(r)
        return await _request(r, **kwargs)

    async def options(self, uri, body="", **kwargs):
        headers = HEADERS
        kwargs.setdefault('allow_redirects', True)
        r = HttpRequest("OPTIONS", uri=self.Endpoint + uri, headers=headers, body=body)
        self.sig.Sign(r)
        return await _request(r, **kwargs)

    async def head(self, uri, body="", **kwargs):
        headers = HEADERS
        kwargs.setdefault('allow_redirects', True)
        r = HttpRequest("HEAD", uri=self.Endpoint + uri, headers=headers, body=body)
        self.sig.Sign(r)
        return await _request(r, **kwargs)

    async def patch(self, uri, body="", **kwargs):
        headers = HEADERS
        kwargs.setdefault('allow_redirects', True)
        r = HttpRequest("PATCH", uri=self.Endpoint + uri, headers=headers, body=body)
        self.sig.Sign(r)
        return await _request(r, **kwargs)

    async def delete(self, uri, body="", **kwargs):
        headers = HEADERS
        kwargs.setdefault('allow_redirects', True)
        r = HttpRequest("DELETE", uri=self.Endpoint + uri, headers=headers, body=body)
        self.sig.Sign(r)
        return await _request(r, **kwargs)

    async def request(self, method, uri, body="", **kwargs):
        headers = HEADERS
        r = HttpRequest(method, uri=self.Endpoint + uri, headers=headers, body=body)
        self.sig.Sign(r)
        return await _request(r, **kwargs)


async def _request(sig, **kwargs):
    if sig.method == "GET":
        async with ClientSession() as session:
            return await session.request(sig.method, sig.scheme + "://" + sig.host + sig.uri,
                                         headers=sig.headers, **kwargs)
    else:
        async with ClientSession() as session:
            return await session.request(sig.method, sig.scheme + "://" + sig.host + sig.uri,
                                         headers=sig.headers, data=sig.body, **kwargs)
