# huawei_api_sdk

## install

```
pip install huawei_api_sdk
```

## use

```
from huawei_api_sdk import HWSClient
req = HWSClient(endpoint, key, secret)
res = req.get(url)
```
async

```
from huawei_api_sdk import ASYHWSClient
req = ASYHWSClient(endpoint, key, secret)
res = await req.get(url)
```
