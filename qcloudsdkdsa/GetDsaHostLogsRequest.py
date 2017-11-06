# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDsaHostLogsRequest(Request):

    def __init__(self):
        super(GetDsaHostLogsRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'GetDsaHostLogs', 'dsa.api.qcloud.com')

    def get_endDate(self):
        return self.get_params().get('endDate')

    def set_endDate(self, endDate):
        self.add_param('endDate', endDate)

    def get_hosts(self):
        return self.get_params().get('hosts')

    def set_hosts(self, hosts):
        self.add_param('hosts', hosts)

    def get_startDate(self):
        return self.get_params().get('startDate')

    def set_startDate(self, startDate):
        self.add_param('startDate', startDate)
