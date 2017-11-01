# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifyUserGwRequest(Request):

    def __init__(self):
        super(ModifyUserGwRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'ModifyUserGw', 'vpc.api.qcloud.com')

    def get_userGwId(self):
        return self.get_params().get('userGwId')

    def set_userGwId(self, userGwId):
        self.add_param('userGwId', userGwId)

    def get_userGwName(self):
        return self.get_params().get('userGwName')

    def set_userGwName(self, userGwName):
        self.add_param('userGwName', userGwName)
