# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpgradeRedisRequest(Request):

    def __init__(self):
        super(UpgradeRedisRequest, self).__init__(
            'redis', 'qcloudcliV1', 'UpgradeRedis', 'redis.api.qcloud.com')

    def get_memSize(self):
        return self.get_params().get('memSize')

    def set_memSize(self, memSize):
        self.add_param('memSize', memSize)

    def get_redisId(self):
        return self.get_params().get('redisId')

    def set_redisId(self, redisId):
        self.add_param('redisId', redisId)
