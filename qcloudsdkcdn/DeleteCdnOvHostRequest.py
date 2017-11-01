# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteCdnOvHostRequest(Request):

    def __init__(self):
        super(DeleteCdnOvHostRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'DeleteCdnOvHost', 'cdn.api.qcloud.com')

    def get_hostId(self):
        return self.get_params().get('hostId')

    def set_hostId(self, hostId):
        self.add_param('hostId', hostId)
