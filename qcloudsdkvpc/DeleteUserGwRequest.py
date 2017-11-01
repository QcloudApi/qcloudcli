# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeleteUserGwRequest(Request):

    def __init__(self):
        super(DeleteUserGwRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DeleteUserGw', 'vpc.api.qcloud.com')

    def get_userGwId(self):
        return self.get_params().get('userGwId')

    def set_userGwId(self, userGwId):
        self.add_param('userGwId', userGwId)
