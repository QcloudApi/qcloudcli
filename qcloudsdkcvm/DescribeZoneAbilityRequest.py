#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeZoneAbilityRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cvm', 'qcloudcliV1', 'DescribeZoneAbility', 'cvm.api.qcloud.com')

	def get_zoneId(self):
		return self.get_params().get('zoneId')

	def set_zoneId(self, zoneId):
		self.add_param('zoneId', zoneId)

	def get_capacity(self):
		return self.get_params().get('capacity')

	def set_capacity(self, capacity):
		self.add_param('capacity', capacity)

