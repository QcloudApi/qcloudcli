# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdbDeviceMonitorInfoRequest(Request):

    def __init__(self):
        super(GetCdbDeviceMonitorInfoRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'GetCdbDeviceMonitorInfo', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_count5Min(self):
        return self.get_params().get('count5Min')

    def set_count5Min(self, count5Min):
        self.add_param('count5Min', count5Min)
