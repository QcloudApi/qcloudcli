# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class BgpipCheckCreateRequest(Request):

    def __init__(self):
        super(BgpipCheckCreateRequest, self).__init__(
            'bgpip', 'qcloudcliV1', 'BgpipCheckCreate', 'bgpip.api.qcloud.com')

    def get_bandwidth(self):
        return self.get_params().get('bandwidth')

    def set_bandwidth(self, bandwidth):
        self.add_param('bandwidth', bandwidth)

    def get_elastic(self):
        return self.get_params().get('elastic')

    def set_elastic(self, elastic):
        self.add_param('elastic', elastic)

    def get_goodsNum(self):
        return self.get_params().get('goodsNum')

    def set_goodsNum(self, goodsNum):
        self.add_param('goodsNum', goodsNum)

    def get_region(self):
        return self.get_params().get('region')

    def set_region(self, region):
        self.add_param('region', region)

    def get_timeSpan(self):
        return self.get_params().get('timeSpan')

    def set_timeSpan(self, timeSpan):
        self.add_param('timeSpan', timeSpan)

    def get_timeUnit(self):
        return self.get_params().get('timeUnit')

    def set_timeUnit(self, timeUnit):
        self.add_param('timeUnit', timeUnit)
