#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudsdkcore.request import Request
class GetCategoryListRequest(Request):

	def __init__(self):
		Request.__init__(self, 'ticket', 'qcloudcliV1', 'GetCategoryList', 'ticket.api.qcloud.com')

