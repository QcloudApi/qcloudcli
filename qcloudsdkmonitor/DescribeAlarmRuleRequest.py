# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAlarmRuleRequest(Request):

    def __init__(self):
        super(DescribeAlarmRuleRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeAlarmRule', 'monitor.api.qcloud.com')
