# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AttachGroupsPolicyRequest(Request):

    def __init__(self):
        super(AttachGroupsPolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'AttachGroupsPolicy', 'cam.api.qcloud.com')

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)
