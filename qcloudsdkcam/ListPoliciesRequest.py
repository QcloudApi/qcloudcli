# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListPoliciesRequest(Request):

    def __init__(self):
        super(ListPoliciesRequest, self).__init__(
            'cam', 'qcloudcliV1', 'ListPolicies', 'cam.api.qcloud.com')
