# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class OfflineOvHostRequest(Request):

    def __init__(self):
        super(OfflineOvHostRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'OfflineOvHost', 'cdn.api.qcloud.com')

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)
