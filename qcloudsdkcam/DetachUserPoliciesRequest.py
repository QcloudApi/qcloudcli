# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DetachUserPoliciesRequest(Request):

    def __init__(self):
        super(DetachUserPoliciesRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DetachUserPolicies', 'cam.api.qcloud.com')

    def get_uin(self):
        return self.get_params().get('uin')

    def set_uin(self, uin):
        self.add_param('uin', uin)
