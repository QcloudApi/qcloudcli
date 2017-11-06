# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetSlowLogAnalysisRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetSlowLogAnalysisRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetSlowLogAnalysis', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_checkSum(self):
        return self.get_params().get('checkSum')

    def set_checkSum(self, checkSum):
        self.add_param('checkSum', checkSum)

    def get_db(self):
        return self.get_params().get('db')

    def set_db(self, db):
        self.add_param('db', db)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)

    def get_user(self):
        return self.get_params().get('user')

    def set_user(self, user):
        self.add_param('user', user)
