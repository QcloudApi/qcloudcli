# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlRenameInstanceRequest(Request):

    def __init__(self):
        super(CdbTdsqlRenameInstanceRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlRenameInstance', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_name(self):
        return self.get_params().get('name')

    def set_name(self, name):
        self.add_param('name', name)
