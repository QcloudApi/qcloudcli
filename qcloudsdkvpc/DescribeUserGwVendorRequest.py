# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeUserGwVendorRequest(Request):

    def __init__(self):
        super(DescribeUserGwVendorRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeUserGwVendor', 'vpc.api.qcloud.com')
