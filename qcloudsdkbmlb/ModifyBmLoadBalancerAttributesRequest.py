#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ModifyBmLoadBalancerAttributesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'bmlb', 'qcloudcliV1', 'ModifyBmLoadBalancerAttributes', 'bmlb.api.qcloud.com')

	def get_loadBalancerId(self):
		return self.get_params().get('loadBalancerId')

	def set_loadBalancerId(self, loadBalancerId):
		self.add_param('loadBalancerId', loadBalancerId)

	def get_loadBalancerName(self):
		return self.get_params().get('loadBalancerName')

	def set_loadBalancerName(self, loadBalancerName):
		self.add_param('loadBalancerName', loadBalancerName)

	def get_domainPrefix(self):
		return self.get_params().get('domainPrefix')

	def set_domainPrefix(self, domainPrefix):
		self.add_param('domainPrefix', domainPrefix)

	def get_loadBalancerId(self):
		return self.get_params().get('loadBalancerId')

	def set_loadBalancerId(self, loadBalancerId):
		self.add_param('loadBalancerId', loadBalancerId)

	def get_loadBalancerName(self):
		return self.get_params().get('loadBalancerName')

	def set_loadBalancerName(self, loadBalancerName):
		self.add_param('loadBalancerName', loadBalancerName)

	def get_domainPrefix(self):
		return self.get_params().get('domainPrefix')

	def set_domainPrefix(self, domainPrefix):
		self.add_param('domainPrefix', domainPrefix)

