#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeAlarmRuleObjectsRequest(Request):

	def __init__(self):
		Request.__init__(self, 'monitor', 'qcloudcliV1', 'DescribeAlarmRuleObjects', 'monitor.api.qcloud.com')

	def get_alarmRuleId(self):
		return self.get_params().get('alarmRuleId')

	def set_alarmRuleId(self, alarmRuleId):
		self.add_param('alarmRuleId', alarmRuleId)

