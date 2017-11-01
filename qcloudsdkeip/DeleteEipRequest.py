# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteEipRequest(Request):

    def __init__(self):
        super(DeleteEipRequest, self).__init__(
            'eip', 'qcloudcliV1', 'DeleteEip', 'eip.api.qcloud.com')

    def get_eipIds(self):
        return self.get_params().get('eipIds')

    def set_eipIds(self, eipIds):
        self.add_param('eipIds', eipIds)
