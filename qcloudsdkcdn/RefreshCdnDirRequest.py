#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class RefreshCdnDirRequest(Request):

	def __init__(self):
		Request.__init__(self, 'cdn', 'qcloudcliV1', 'RefreshCdnDir', 'cdn.api.qcloud.com')

	def get_dirs(self):
		return self.get_params().get('dirs')

	def set_dirs(self, dirs):
		self.add_param('dirs', dirs)

