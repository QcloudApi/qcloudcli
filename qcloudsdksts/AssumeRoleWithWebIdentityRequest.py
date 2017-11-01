# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AssumeRoleWithWebIdentityRequest(Request):

    def __init__(self):
        super(AssumeRoleWithWebIdentityRequest, self).__init__(
            'sts', 'qcloudcliV1', 'AssumeRoleWithWebIdentity', 'sts.api.qcloud.com')
