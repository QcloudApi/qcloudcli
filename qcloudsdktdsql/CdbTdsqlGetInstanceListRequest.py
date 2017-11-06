# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CdbTdsqlGetInstanceListRequest(Request):

    def __init__(self):
        super(CdbTdsqlGetInstanceListRequest, self).__init__(
            'tdsql', 'qcloudcliV1', 'CdbTdsqlGetInstanceList', 'tdsql.api.qcloud.com')

    def get_cdbInstanceIds(self):
        return self.get_params().get('cdbInstanceIds')

    def set_cdbInstanceIds(self, cdbInstanceIds):
        self.add_param('cdbInstanceIds', cdbInstanceIds)

    def get_isFilterVpc(self):
        return self.get_params().get('isFilterVpc')

    def set_isFilterVpc(self, isFilterVpc):
        self.add_param('isFilterVpc', isFilterVpc)

    def get_orderBy(self):
        return self.get_params().get('orderBy')

    def set_orderBy(self, orderBy):
        self.add_param('orderBy', orderBy)

    def get_orderByType(self):
        return self.get_params().get('orderByType')

    def set_orderByType(self, orderByType):
        self.add_param('orderByType', orderByType)

    def get_originSerialIds(self):
        return self.get_params().get('originSerialIds')

    def set_originSerialIds(self, originSerialIds):
        self.add_param('originSerialIds', originSerialIds)

    def get_pageNo(self):
        return self.get_params().get('pageNo')

    def set_pageNo(self, pageNo):
        self.add_param('pageNo', pageNo)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)

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

    def get_uuids(self):
        return self.get_params().get('uuids')

    def set_uuids(self, uuids):
        self.add_param('uuids', uuids)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
