# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeletePolicyGroupRequest(Request):

    def __init__(self):
        super(DeletePolicyGroupRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DeletePolicyGroup', 'monitor.api.qcloud.com')

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)
