# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeProjectRequest(Request):

    def __init__(self):
        super(DescribeProjectRequest, self).__init__(
            'account', 'qcloudcliV1', 'DescribeProject', 'account.api.qcloud.com')
