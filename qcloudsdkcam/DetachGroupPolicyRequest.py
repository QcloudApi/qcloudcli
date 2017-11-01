# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DetachGroupPolicyRequest(Request):

    def __init__(self):
        super(DetachGroupPolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DetachGroupPolicy', 'cam.api.qcloud.com')

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)
