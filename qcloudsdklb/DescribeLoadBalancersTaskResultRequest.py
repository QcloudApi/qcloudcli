#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeLoadBalancersTaskResultRequest(Request):

	def __init__(self):
		Request.__init__(self, 'lb', 'qcloudcliV1', 'DescribeLoadBalancersTaskResult', 'lb.api.qcloud.com')

	def get_requestId(self):
		return self.get_params().get('requestId')

	def set_requestId(self, requestId):
		self.add_param('requestId', requestId)

