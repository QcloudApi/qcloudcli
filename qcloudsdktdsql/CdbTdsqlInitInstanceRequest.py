# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlInitInstanceRequest(Request):

    def __init__(self):
        super(CdbTdsqlInitInstanceRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlInitInstance', 'tdsql.api.qcloud.com')

    def get_cdbInstanceIds(self):
        return self.get_params().get('cdbInstanceIds')

    def set_cdbInstanceIds(self, cdbInstanceIds):
        self.add_param('cdbInstanceIds', cdbInstanceIds)

    def get_config(self):
        return self.get_params().get('config')

    def set_config(self, config):
        self.add_param('config', config)
