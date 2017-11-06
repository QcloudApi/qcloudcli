# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetDsaStatisticsRequest(Request):

    def __init__(self):
        super(GetDsaStatisticsRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'GetDsaStatistics', 'dsa.api.qcloud.com')

    def get_endDate(self):
        return self.get_params().get('endDate')

    def set_endDate(self, endDate):
        self.add_param('endDate', endDate)

    def get_granularity(self):
        return self.get_params().get('granularity')

    def set_granularity(self, granularity):
        self.add_param('granularity', granularity)

    def get_hosts(self):
        return self.get_params().get('hosts')

    def set_hosts(self, hosts):
        self.add_param('hosts', hosts)

    def get_metrics(self):
        return self.get_params().get('metrics')

    def set_metrics(self, metrics):
        self.add_param('metrics', metrics)

    def get_projects(self):
        return self.get_params().get('projects')

    def set_projects(self, projects):
        self.add_param('projects', projects)

    def get_startDate(self):
        return self.get_params().get('startDate')

    def set_startDate(self, startDate):
        self.add_param('startDate', startDate)
