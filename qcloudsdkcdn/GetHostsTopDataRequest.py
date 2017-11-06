# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetHostsTopDataRequest(Request):

    def __init__(self):
        super(GetHostsTopDataRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GetHostsTopData', 'cdn.api.qcloud.com')

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

    def get_statType(self):
        return self.get_params().get('statType')

    def set_statType(self, statType):
        self.add_param('statType', statType)

    def get_type(self):
        return self.get_params().get('type')

    def set_type(self, type):
        self.add_param('type', type)
