# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DeletePolicyObjectRequest(Request):

    def __init__(self):
        super(DeletePolicyObjectRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DeletePolicyObject', 'monitor.api.qcloud.com')

    def get_groupId(self):
        return self.get_params().get('groupId')

    def set_groupId(self, groupId):
        self.add_param('groupId', groupId)

    def get_uniqueId(self):
        return self.get_params().get('uniqueId')

    def set_uniqueId(self, uniqueId):
        self.add_param('uniqueId', uniqueId)
