#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetUserBaseInfoRequest(Request):

	def __init__(self):
		Request.__init__(self, 'open', 'qcloudcliV1', 'GetUserBaseInfo', 'open.api.qcloud.com')

