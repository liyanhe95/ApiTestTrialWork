import pytest
from common import contants
from common.request import Request
from common import logger
from common.make_requests_data import MakeRequestsData
import json
import jsonpath

logger = logger.get_logger("zhengqingchun")#获取logger实例

class TestTrial():

    cases = MakeRequestsData(contants.case_zhengqingchun).make_requestsdata(contants.json_zhengqingchun)
    request = Request()

    def setUp(self):
        logger.info('开始执行正青春试算脚本')

    ids =  [case['casename'] for case in cases] # testData 为参数列表
    @pytest.mark.parametrize('item',cases,ids=ids)
    def test_huagui_zhengqingchun(self,item):  #用一个变量来解释data传递的数据
        item['id'] = int(item['id'])
        logger.info("开始执行第{}用例".format(item['id']))
        # 使用封装好的request 来完成请求
        resp = self.request.request(item['requests_data'])
        json_temp = json.loads(resp.text)
        resp = jsonpath.jsonpath(json_temp, str(item['getResponseValue']))
        if isinstance(resp, list) and len(resp) == 1:
            resp = resp[0]
        if isinstance(resp, float):
            resp = str(resp)

        try:
            '''将返回结果和期望结果进行匹配'''
            assert (resp == item["assert_value"])
            logger.info("第{}用例执行结果：PASS".format(item['id']))
        except AssertionError as e:
            logger.error("第{}用例执行结果：FAIL".format(item['id']))
            raise e

    def tearDown(self):
        logger.info('正青春试算脚本执行结束')
#
#
# if __name__ == '__main__':
#     pytest.main(' --pytest-tmreport-name=reports/report.html')
#     '''命令行用法：pytest --pytest-tmreport-name=reports/report.html'''
#     '''cmd执行pytest用例有三种方法,以下三种方法都可以，一般推荐第一个
#     pytest
#     py.test
#     python -m pytest'''
#

