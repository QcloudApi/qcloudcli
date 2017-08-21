#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class DescribeAllClassRequest(Request):

	def __init__(self):
		Request.__init__(self, 'vod', 'qcloudcliV1', 'DescribeAllClass', 'vod.api.qcloud.com')

