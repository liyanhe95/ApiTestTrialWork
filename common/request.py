import requests
from common import logger
from common.utils import get_token


logger = logger.get_logger("request")
class Request:
    # 定义一个requests类
    def __init__(self):

        read_token = get_token()
        self.search_header = {"Token":read_token,'Content-Type':'application/json','charset':'UTF-8'}
        self.url =  "https://broker-gateway-sit.zhuanxinbaoxian.com/product/ratetrial/getTrialValue"


    def request(self,data):

        resp = requests.request('post',url=self.url,json=data,headers = self.search_header)# 调用get方法，使用params传参（url传参）
        logger.info('response: {0}'.format(resp.text))
        return resp







if __name__ == '__main__':
    import json
    data = {"productCode":"PL00025","planCode":"","preOrderNo":"","trialGenes":{}}
    request = Request().request(data)
    json_temp = json.loads(request.text)
    print(json_temp)
