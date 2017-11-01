# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class OnlineDsaHostRequest(Request):

    def __init__(self):
        super(OnlineDsaHostRequest, self).__init__(
            'dsa', 'qcloudcliV1', 'OnlineDsaHost', 'dsa.api.qcloud.com')

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)
