# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetSlowLogListRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetSlowLogListRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetSlowLogList', 'tdsql.api.qcloud.com')

    def get_cdbInstanceId(self):
        return self.get_params().get('cdbInstanceId')

    def set_cdbInstanceId(self, cdbInstanceId):
        self.add_param('cdbInstanceId', cdbInstanceId)

    def get_db(self):
        return self.get_params().get('db')

    def set_db(self, db):
        self.add_param('db', db)

    def get_endTime(self):
        return self.get_params().get('endTime')

    def set_endTime(self, endTime):
        self.add_param('endTime', endTime)

    def get_num(self):
        return self.get_params().get('num')

    def set_num(self, num):
        self.add_param('num', num)

    def get_orderBy(self):
        return self.get_params().get('orderBy')

    def set_orderBy(self, orderBy):
        self.add_param('orderBy', orderBy)

    def get_orderByType(self):
        return self.get_params().get('orderByType')

    def set_orderByType(self, orderByType):
        self.add_param('orderByType', orderByType)

    def get_start(self):
        return self.get_params().get('start')

    def set_start(self, start):
        self.add_param('start', start)

    def get_startTime(self):
        return self.get_params().get('startTime')

    def set_startTime(self, startTime):
        self.add_param('startTime', startTime)
