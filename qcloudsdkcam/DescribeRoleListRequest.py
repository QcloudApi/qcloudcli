# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeRoleListRequest(Request):

    def __init__(self):
        super(DescribeRoleListRequest, self).__init__(
            'cam', 'qcloudcliV1', 'DescribeRoleList', 'cam.api.qcloud.com')
