# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetProjectListRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetProjectListRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetProjectList', 'tdsql.api.qcloud.com')
