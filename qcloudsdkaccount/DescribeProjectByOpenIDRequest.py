# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeProjectByOpenIDRequest(Request):

    def __init__(self):
        super(DescribeProjectByOpenIDRequest, self).__init__(
            'account', 'qcloudcliV1', 'DescribeProjectByOpenID', 'account.api.qcloud.com')
