# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetGroupRequest(Request):

    def __init__(self):
        super(GetGroupRequest, self).__init__(
            'cam', 'qcloudcliV1', 'GetGroup', 'cam.api.qcloud.com')

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)
