#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DisableTopicRuleRequest(Request):

	def __init__(self):
		Request.__init__(self, 'iiot', 'qcloudcliV1', 'DisableTopicRule', 'iiot.api.qcloud.com')

	def get_ruleName(self):
		return self.get_params().get('ruleName')

	def set_ruleName(self, ruleName):
		self.add_param('ruleName', ruleName)

