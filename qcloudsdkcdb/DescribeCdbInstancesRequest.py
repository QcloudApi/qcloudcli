# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCdbInstancesRequest(Request):

    def __init__(self):
        super(DescribeCdbInstancesRequest, self).__init__(
            'cdb', 'qcloudcliV1', 'DescribeCdbInstances', 'cdb.api.qcloud.com')

    def get_cdbInstanceIds(self):
        return self.get_params().get('cdbInstanceIds')

    def set_cdbInstanceIds(self, cdbInstanceIds):
        self.add_param('cdbInstanceIds', cdbInstanceIds)

    def get_cdbInstanceTypes(self):
        return self.get_params().get('cdbInstanceTypes')

    def set_cdbInstanceTypes(self, cdbInstanceTypes):
        self.add_param('cdbInstanceTypes', cdbInstanceTypes)

    def get_cdbInstanceVips(self):
        return self.get_params().get('cdbInstanceVips')

    def set_cdbInstanceVips(self, cdbInstanceVips):
        self.add_param('cdbInstanceVips', cdbInstanceVips)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_status(self):
        return self.get_params().get('status')

    def set_status(self, status):
        self.add_param('status', status)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
