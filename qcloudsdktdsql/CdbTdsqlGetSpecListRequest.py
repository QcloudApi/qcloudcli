# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetSpecListRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetSpecListRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetSpecList', 'tdsql.api.qcloud.com')
