# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeSnapshotsRequest(Request):

    def __init__(self):
        super(DescribeSnapshotsRequest, self).__init__(
            'snapshot', 'qcloudcliV1', 'DescribeSnapshots', 'snapshot.api.qcloud.com')

    def get_diskType(self):
        return self.get_params().get('diskType')

    def set_diskType(self, diskType):
        self.add_param('diskType', diskType)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_order(self):
        return self.get_params().get('order')

    def set_order(self, order):
        self.add_param('order', order)

    def get_orderBy(self):
        return self.get_params().get('orderBy')

    def set_orderBy(self, orderBy):
        self.add_param('orderBy', orderBy)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_projectIds(self):
        return self.get_params().get('projectIds')

    def set_projectIds(self, projectIds):
        self.add_param('projectIds', projectIds)

    def get_searchValue(self):
        return self.get_params().get('searchValue')

    def set_searchValue(self, searchValue):
        self.add_param('searchValue', searchValue)

    def get_snapshotIds(self):
        return self.get_params().get('snapshotIds')

    def set_snapshotIds(self, snapshotIds):
        self.add_param('snapshotIds', snapshotIds)

    def get_snapshotStatus(self):
        return self.get_params().get('snapshotStatus')

    def set_snapshotStatus(self, snapshotStatus):
        self.add_param('snapshotStatus', snapshotStatus)

    def get_storageIds(self):
        return self.get_params().get('storageIds')

    def set_storageIds(self, storageIds):
        self.add_param('storageIds', storageIds)

    def get_storageTypes(self):
        return self.get_params().get('storageTypes')

    def set_storageTypes(self, storageTypes):
        self.add_param('storageTypes', storageTypes)

    def get_zoneId(self):
        return self.get_params().get('zoneId')

    def set_zoneId(self, zoneId):
        self.add_param('zoneId', zoneId)
