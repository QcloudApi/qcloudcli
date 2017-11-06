# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRedisProductRequest(Request):

    def __init__(self):
        super(DescribeRedisProductRequest, self).__init__(
            'redis', 'qcloudcliV1', 'DescribeRedisProduct', 'redis.api.qcloud.com')

    def get_typeId(self):
        return self.get_params().get('typeId')

    def set_typeId(self, typeId):
        self.add_param('typeId', typeId)

    def get_zoneIds(self):
        return self.get_params().get('zoneIds')

    def set_zoneIds(self, zoneIds):
        self.add_param('zoneIds', zoneIds)
