#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class BgpipQueryResourcesRequest(Request):

	def __init__(self):
		Request.__init__(self, 'bgpip', 'qcloudcliV1', 'BgpipQueryResources', 'bgpip.api.qcloud.com')

	def get_resourceIds(self):
		return self.get_params().get('resourceIds')

	def set_resourceIds(self, resourceIds):
		self.add_param('resourceIds', resourceIds)

	def get_region(self):
		return self.get_params().get('region')

	def set_region(self, region):
		self.add_param('region', region)

