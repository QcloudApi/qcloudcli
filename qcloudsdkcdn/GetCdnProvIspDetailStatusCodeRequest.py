# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdnProvIspDetailStatusCodeRequest(Request):

    def __init__(self):
        super(GetCdnProvIspDetailStatusCodeRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GetCdnProvIspDetailStatusCode', 'cdn.api.qcloud.com')

    def get_date(self):
        return self.get_params().get('date')

    def set_date(self, date):
        self.add_param('date', date)

    def get_hosts(self):
        return self.get_params().get('hosts')

    def set_hosts(self, hosts):
        self.add_param('hosts', hosts)

    def get_isps(self):
        return self.get_params().get('isps')

    def set_isps(self, isps):
        self.add_param('isps', isps)

    def get_provs(self):
        return self.get_params().get('provs')

    def set_provs(self, provs):
        self.add_param('provs', provs)
