# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRedisZonesRequest(Request):

    def __init__(self):
        super(DescribeRedisZonesRequest, self).__init__(
            'redis', 'qcloudcliV1', 'DescribeRedisZones', 'redis.api.qcloud.com')
