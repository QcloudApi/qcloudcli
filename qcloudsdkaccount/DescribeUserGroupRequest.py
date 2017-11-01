# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeUserGroupRequest(Request):

    def __init__(self):
        super(DescribeUserGroupRequest, self).__init__(
            'account', 'qcloudcliV1', 'DescribeUserGroup', 'account.api.qcloud.com')

    def get_groupIds(self):
        return self.get_params().get('groupIds')

    def set_groupIds(self, groupIds):
        self.add_param('groupIds', groupIds)
