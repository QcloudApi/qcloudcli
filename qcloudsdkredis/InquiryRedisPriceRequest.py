# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class InquiryRedisPriceRequest(Request):

    def __init__(self):
        super(InquiryRedisPriceRequest, self).__init__(
            'redis', 'qcloudcliV1', 'InquiryRedisPrice', 'redis.api.qcloud.com')

    def get_goodsNum(self):
        return self.get_params().get('goodsNum')

    def set_goodsNum(self, goodsNum):
        self.add_param('goodsNum', goodsNum)

    def get_memSize(self):
        return self.get_params().get('memSize')

    def set_memSize(self, memSize):
        self.add_param('memSize', memSize)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_typeId(self):
        return self.get_params().get('typeId')

    def set_typeId(self, typeId):
        self.add_param('typeId', typeId)

    def get_zoneId(self):
        return self.get_params().get('zoneId')

    def set_zoneId(self, zoneId):
        self.add_param('zoneId', zoneId)
