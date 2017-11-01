# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListAttachedRolePoliciesRequest(Request):

    def __init__(self):
        super(ListAttachedRolePoliciesRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListAttachedRolePolicies', 'cam.api.qcloud.com')
