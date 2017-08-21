#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DeleteBmLoadBalancerListenersRequest(Request):

	def __init__(self):
		Request.__init__(self, 'lb', 'qcloudcliV1', 'DeleteBmLoadBalancerListeners', 'lb.api.qcloud.com')

	def get_loadBalancerId(self):
		return self.get_params().get('loadBalancerId')

	def set_loadBalancerId(self, loadBalancerId):
		self.add_param('loadBalancerId', loadBalancerId)

	def get_listenerIds(self):
		return self.get_params().get('listenerIds')

	def set_listenerIds(self, listenerIds):
		self.add_param('listenerIds', listenerIds)

