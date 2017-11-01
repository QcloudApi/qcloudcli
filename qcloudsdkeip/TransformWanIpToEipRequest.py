# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class TransformWanIpToEipRequest(Request):

    def __init__(self):
        super(TransformWanIpToEipRequest, self).__init__(
            'eip', 'qcloudcliV1', 'TransformWanIpToEip', 'eip.api.qcloud.com')

    def get_unInstanceId(self):
        return self.get_params().get('unInstanceId')

    def set_unInstanceId(self, unInstanceId):
        self.add_param('unInstanceId', unInstanceId)
