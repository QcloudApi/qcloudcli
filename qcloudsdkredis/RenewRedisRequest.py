# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RenewRedisRequest(Request):

    def __init__(self):
        super(RenewRedisRequest, self).__init__(
            'redis', 'qcloudcliV1', 'RenewRedis', 'redis.api.qcloud.com')

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_redisId(self):
        return self.get_params().get('redisId')

    def set_redisId(self, redisId):
        self.add_param('redisId', redisId)
