# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetInstanceCountRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetInstanceCountRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetInstanceCount', 'tdsql.api.qcloud.com')

    def get_countByVpcId(self):
        return self.get_params().get('countByVpcId')

    def set_countByVpcId(self, countByVpcId):
        self.add_param('countByVpcId', countByVpcId)

    def get_projectIds(self):
        return self.get_params().get('projectIds')

    def set_projectIds(self, projectIds):
        self.add_param('projectIds', projectIds)

    def get_vpcIds(self):
        return self.get_params().get('vpcIds')

    def set_vpcIds(self, vpcIds):
        self.add_param('vpcIds', vpcIds)
