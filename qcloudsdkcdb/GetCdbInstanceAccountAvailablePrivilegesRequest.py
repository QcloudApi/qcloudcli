# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class GetCdbInstanceAccountAvailablePrivilegesRequest(Request):

    def __init__(self):
        super(GetCdbInstanceAccountAvailablePrivilegesRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'GetCdbInstanceAccountAvailablePrivileges', 'cdb.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)
