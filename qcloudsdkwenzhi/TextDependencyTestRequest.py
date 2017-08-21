#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class TextDependencyTestRequest(Request):

	def __init__(self):
		Request.__init__(self, 'wenzhi', 'qcloudcliV1', 'TextDependencyTest', 'wenzhi.api.qcloud.com')

	def get_content(self):
		return self.get_params().get('content')

	def set_content(self, content):
		self.add_param('content', content)

