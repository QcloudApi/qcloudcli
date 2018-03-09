# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdnHostsDetailStatisticsRequest(Request):

    def __init__(self):
        super(GetCdnHostsDetailStatisticsRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GetCdnHostsDetailStatistics', 'cdn.api.qcloud.com')

    def get_detail(self):
        return self.get_params().get('detail')

    def set_detail(self, detail):
        self.add_param('detail', detail)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_hosts(self):
        return self.get_params().get('hosts')

    def set_hosts(self, hosts):
        self.add_param('hosts', hosts)

    def get_projects(self):
        return self.get_params().get('projects')

    def set_projects(self, projects):
        self.add_param('projects', projects)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)

    def get_statType(self):
        return self.get_params().get('statType')

    def set_statType(self, statType):
        self.add_param('statType', statType)
