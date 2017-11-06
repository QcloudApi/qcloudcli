# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModfiyRedisPasswordRequest(Request):

    def __init__(self):
        super(ModfiyRedisPasswordRequest, self).__init__(
            'redis', 'qcloudcliV1', 'ModfiyRedisPassword', 'redis.api.qcloud.com')

    def get_oldPassword(self):
        return self.get_params().get('oldPassword')

    def set_oldPassword(self, oldPassword):
        self.add_param('oldPassword', oldPassword)

    def get_password(self):
        return self.get_params().get('password')

    def set_password(self, password):
        self.add_param('password', password)

    def get_redisId(self):
        return self.get_params().get('redisId')

    def set_redisId(self, redisId):
        self.add_param('redisId', redisId)
