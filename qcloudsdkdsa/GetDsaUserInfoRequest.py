#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetDsaUserInfoRequest(Request):

	def __init__(self):
		Request.__init__(self, 'dsa', 'qcloudcliV1', 'GetDsaUserInfo', 'dsa.api.qcloud.com')

