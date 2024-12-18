# stockPrice
这是一个实时获取股票价格的脚本，每5秒更新一次，每分钟记录一次。

## 使用方法

该程序由Python编写，需要自行安装python3环境

### 1、安装所需库

安装库requests 

```python
pip install requests -y
```

### 2、运行程序

直接运行即可

```python
python get_price.py
```
## 修改股票代码

默认是上证指数，且仅支持上交所的股票，需要修改的话将url中的query=000001&code=000001进行修改即可

```python
https://finance.pae.baidu.com/vapi/v1/getquotation?srcid=5353&all=1&pointType=string&group=quotation_index_minute&query=000001&code=000001&market_type=ab&newFormat=1&finClientType=pc
```
修改为
```python
https://finance.pae.baidu.com/vapi/v1/getquotation?srcid=5353&all=1&pointType=string&group=quotation_index_minute&query=000065&code=000065&market_type=ab&newFormat=1&finClientType=pc
```
