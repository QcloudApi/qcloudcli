# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdnStatTopRequest(Request):

    def __init__(self):
        super(GetCdnStatTopRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GetCdnStatTop', 'cdn.api.qcloud.com')

    def get_endDate(self):
        return self.get_params().get('endDate')

    def set_endDate(self, endDate):
        self.add_param('endDate', endDate)

    def get_hosts(self):
        return self.get_params().get('hosts')

    def set_hosts(self, hosts):
        self.add_param('hosts', hosts)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_projects(self):
        return self.get_params().get('projects')

    def set_projects(self, projects):
        self.add_param('projects', projects)

    def get_startDate(self):
        return self.get_params().get('startDate')

    def set_startDate(self, startDate):
        self.add_param('startDate', startDate)

    def get_statType(self):
        return self.get_params().get('statType')

    def set_statType(self, statType):
        self.add_param('statType', statType)
