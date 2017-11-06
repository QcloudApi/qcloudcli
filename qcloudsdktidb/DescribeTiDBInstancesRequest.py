# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeTiDBInstancesRequest(Request):

    def __init__(self):
        super(DescribeTiDBInstancesRequest, self).__init__(
            'tidb', 'qcloudcliV1', 'DescribeTiDBInstances', 'tidb.api.qcloud.com')

    def get_instanceIds(self):
        return self.get_params().get('instanceIds')

    def set_instanceIds(self, instanceIds):
        self.add_param('instanceIds', instanceIds)

    def get_isFilterVpc(self):
        return self.get_params().get('isFilterVpc')

    def set_isFilterVpc(self, isFilterVpc):
        self.add_param('isFilterVpc', isFilterVpc)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_orderBy(self):
        return self.get_params().get('orderBy')

    def set_orderBy(self, orderBy):
        self.add_param('orderBy', orderBy)

    def get_orderByType(self):
        return self.get_params().get('orderByType')

    def set_orderByType(self, orderByType):
        self.add_param('orderByType', orderByType)

    def get_projectIds(self):
        return self.get_params().get('projectIds')

    def set_projectIds(self, projectIds):
        self.add_param('projectIds', projectIds)

    def get_searchKey(self):
        return self.get_params().get('searchKey')

    def set_searchKey(self, searchKey):
        self.add_param('searchKey', searchKey)

    def get_subnetId(self):
        return self.get_params().get('subnetId')

    def set_subnetId(self, subnetId):
        self.add_param('subnetId', subnetId)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
