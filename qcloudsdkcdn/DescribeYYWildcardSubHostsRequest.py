# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeYYWildcardSubHostsRequest(Request):

    def __init__(self):
        super(DescribeYYWildcardSubHostsRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'DescribeYYWildcardSubHosts', 'cdn.api.qcloud.com')

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)
