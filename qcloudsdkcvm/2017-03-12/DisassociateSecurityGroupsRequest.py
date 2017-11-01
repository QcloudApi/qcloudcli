# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DisassociateSecurityGroupsRequest(Request):

    def __init__(self):
        super(DisassociateSecurityGroupsRequest, self).__init__(
            'cvm', 'qcloudcliV1', 'DisassociateSecurityGroups', 'cvm.api.qcloud.com')
