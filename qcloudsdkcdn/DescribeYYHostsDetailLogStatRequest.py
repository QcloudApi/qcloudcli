# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeYYHostsDetailLogStatRequest(Request):

    def __init__(self):
        super(DescribeYYHostsDetailLogStatRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'DescribeYYHostsDetailLogStat', 'cdn.api.qcloud.com')

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_hosts(self):
        return self.get_params().get('hosts')

    def set_hosts(self, hosts):
        self.add_param('hosts', hosts)

    def get_scheme(self):
        return self.get_params().get('scheme')

    def set_scheme(self, scheme):
        self.add_param('scheme', scheme)

    def get_showDirBandwidth(self):
        return self.get_params().get('showDirBandwidth')

    def set_showDirBandwidth(self, showDirBandwidth):
        self.add_param('showDirBandwidth', showDirBandwidth)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)

    def get_statTypes(self):
        return self.get_params().get('statTypes')

    def set_statTypes(self, statTypes):
        self.add_param('statTypes', statTypes)
