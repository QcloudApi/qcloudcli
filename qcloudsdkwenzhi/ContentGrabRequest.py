#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class ContentGrabRequest(Request):

	def __init__(self):
		Request.__init__(self, 'wenzhi', 'qcloudcliV1', 'ContentGrab', 'wenzhi.api.qcloud.com')

	def get_url(self):
		return self.get_params().get('url')

	def set_url(self, url):
		self.add_param('url', url)

