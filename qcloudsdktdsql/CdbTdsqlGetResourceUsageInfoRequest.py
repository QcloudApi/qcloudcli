# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetResourceUsageInfoRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetResourceUsageInfoRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetResourceUsageInfo', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_shardId(self):
        return self.get_params().get('shardId')

    def set_shardId(self, shardId):
        self.add_param('shardId', shardId)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)
