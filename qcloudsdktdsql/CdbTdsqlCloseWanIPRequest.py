# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlCloseWanIPRequest(Request):

    def __init__(self):
        super(CdbTdsqlCloseWanIPRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlCloseWanIP', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)
