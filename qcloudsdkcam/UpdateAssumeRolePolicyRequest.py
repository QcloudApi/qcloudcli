# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class UpdateAssumeRolePolicyRequest(Request):

    def __init__(self):
        super(UpdateAssumeRolePolicyRequest, self).__init__(
            'cam', 'qcloudcliV1', 'UpdateAssumeRolePolicy', 'cam.api.qcloud.com')
