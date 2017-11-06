# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDsaHostStatisticsRequest(Request):

    def __init__(self):
        super(GetDsaHostStatisticsRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'GetDsaHostStatistics', 'dsa.api.qcloud.com')

    def get_endDate(self):
        return self.get_params().get('endDate')

    def set_endDate(self, endDate):
        self.add_param('endDate', endDate)

    def get_hosts(self):
        return self.get_params().get('hosts')

    def set_hosts(self, hosts):
        self.add_param('hosts', hosts)

    def get_length(self):
        return self.get_params().get('length')

    def set_length(self, length):
        self.add_param('length', length)

    def get_metrics(self):
        return self.get_params().get('metrics')

    def set_metrics(self, metrics):
        self.add_param('metrics', metrics)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_projects(self):
        return self.get_params().get('projects')

    def set_projects(self, projects):
        self.add_param('projects', projects)

    def get_startDate(self):
        return self.get_params().get('startDate')

    def set_startDate(self, startDate):
        self.add_param('startDate', startDate)
