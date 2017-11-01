# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeInstancesCbsNumRequest(Request):

    def __init__(self):
        super(DescribeInstancesCbsNumRequest, self).__init__(
            'cbs', 'qcloudcliV1', 'DescribeInstancesCbsNum', 'cbs.api.qcloud.com')

    def get_uInstanceIds(self):
        return self.get_params().get('uInstanceIds')

    def set_uInstanceIds(self, uInstanceIds):
        self.add_param('uInstanceIds', uInstanceIds)
