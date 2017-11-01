# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeClassRequest(Request):

    def __init__(self):
        super(DescribeClassRequest, self).__init__(
            'vod', 'qcloudcliV1', 'DescribeClass', 'vod.api.qcloud.com')
