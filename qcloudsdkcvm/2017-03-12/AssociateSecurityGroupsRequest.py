# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AssociateSecurityGroupsRequest(Request):

    def __init__(self):
        super(AssociateSecurityGroupsRequest, self).__init__(
            'cvm', 'qcloudcliV1', 'AssociateSecurityGroups', 'cvm.api.qcloud.com')
