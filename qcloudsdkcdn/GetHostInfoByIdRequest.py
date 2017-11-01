# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetHostInfoByIdRequest(Request):

    def __init__(self):
        super(GetHostInfoByIdRequest, self).__init__(
            'cdn', 'qcloudcliV1', 'GetHostInfoById', 'cdn.api.qcloud.com')

    def get_ids(self):
        return self.get_params().get('ids')

    def set_ids(self, ids):
        self.add_param('ids', ids)
