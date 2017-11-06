# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetOverseaCdnLogListRequest(Request):

    def __init__(self):
        super(GetOverseaCdnLogListRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GetOverseaCdnLogList', 'cdn.api.qcloud.com')

    def get_endDate(self):
        return self.get_params().get('endDate')

    def set_endDate(self, endDate):
        self.add_param('endDate', endDate)

    def get_host(self):
        return self.get_params().get('host')

    def set_host(self, host):
        self.add_param('host', host)

    def get_startDate(self):
        return self.get_params().get('startDate')

    def set_startDate(self, startDate):
        self.add_param('startDate', startDate)
