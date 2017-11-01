# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCurrentTimestampRequest(Request):

    def __init__(self):
        super(DescribeCurrentTimestampRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeCurrentTimestamp', 'monitor.api.qcloud.com')
