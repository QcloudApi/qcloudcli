# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AttachGroupPoliciesRequest(Request):

    def __init__(self):
        super(AttachGroupPoliciesRequest, self).__init__(
            'cam', 'qcloudcliV1', 'AttachGroupPolicies', 'cam.api.qcloud.com')

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)
