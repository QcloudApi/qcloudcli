# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AssumeRoleRequest(Request):

    def __init__(self):
        super(AssumeRoleRequest, self).__init__(
            'sts', 'qcloudcliV1', 'AssumeRole', 'sts.api.qcloud.com')
