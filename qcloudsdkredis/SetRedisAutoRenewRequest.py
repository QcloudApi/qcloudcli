# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class SetRedisAutoRenewRequest(Request):

    def __init__(self):
        super(SetRedisAutoRenewRequest, self).__init__(
            'redis', 'qcloudcliV1', 'SetRedisAutoRenew', 'redis.api.qcloud.com')

    def get_isAutoRenew(self):
        return self.get_params().get('isAutoRenew')

    def set_isAutoRenew(self, isAutoRenew):
        self.add_param('isAutoRenew', isAutoRenew)

    def get_redisIds(self):
        return self.get_params().get('redisIds')

    def set_redisIds(self, redisIds):
        self.add_param('redisIds', redisIds)
