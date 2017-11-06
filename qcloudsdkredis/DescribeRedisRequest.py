# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRedisRequest(Request):

    def __init__(self):
        super(DescribeRedisRequest, self).__init__(
            'redis', 'qcloudcliV1', 'DescribeRedis', 'redis.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderBy(self):
        return self.get_params().get('orderBy')

    def set_orderBy(self, orderBy):
        self.add_param('orderBy', orderBy)

    def get_orderType(self):
        return self.get_params().get('orderType')

    def set_orderType(self, orderType):
        self.add_param('orderType', orderType)

    def get_projectIds(self):
        return self.get_params().get('projectIds')

    def set_projectIds(self, projectIds):
        self.add_param('projectIds', projectIds)

    def get_redisId(self):
        return self.get_params().get('redisId')

    def set_redisId(self, redisId):
        self.add_param('redisId', redisId)

    def get_redisName(self):
        return self.get_params().get('redisName')

    def set_redisName(self, redisName):
        self.add_param('redisName', redisName)

    def get_subnetIds(self):
        return self.get_params().get('subnetIds')

    def set_subnetIds(self, subnetIds):
        self.add_param('subnetIds', subnetIds)

    def get_unSubnetIds(self):
        return self.get_params().get('unSubnetIds')

    def set_unSubnetIds(self, unSubnetIds):
        self.add_param('unSubnetIds', unSubnetIds)

    def get_unVpcIds(self):
        return self.get_params().get('unVpcIds')

    def set_unVpcIds(self, unVpcIds):
        self.add_param('unVpcIds', unVpcIds)

    def get_vpcIds(self):
        return self.get_params().get('vpcIds')

    def set_vpcIds(self, vpcIds):
        self.add_param('vpcIds', vpcIds)
