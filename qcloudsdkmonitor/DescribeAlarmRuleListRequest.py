# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAlarmRuleListRequest(Request):

    def __init__(self):
        super(DescribeAlarmRuleListRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeAlarmRuleList', 'monitor.api.qcloud.com')

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
