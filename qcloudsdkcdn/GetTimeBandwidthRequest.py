# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetTimeBandwidthRequest(Request):

    def __init__(self):
        super(GetTimeBandwidthRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GetTimeBandwidth', 'cdn.api.qcloud.com')

    def get_end(self):
        return self.get_params().get('end')

    def set_end(self, end):
        self.add_param('end', end)

    def get_hosts(self):
        return self.get_params().get('hosts')

    def set_hosts(self, hosts):
        self.add_param('hosts', hosts)

    def get_start(self):
        return self.get_params().get('start')

    def set_start(self, start):
        self.add_param('start', start)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
