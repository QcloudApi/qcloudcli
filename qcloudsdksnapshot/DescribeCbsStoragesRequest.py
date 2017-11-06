# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeCbsStoragesRequest(Request):

    def __init__(self):
        super(DescribeCbsStoragesRequest, self).__init__(
            'snapshot', 'qcloudcliV1', 'DescribeCbsStorages', 'snapshot.api.qcloud.com')

    def get_attached(self):
        return self.get_params().get('attached')

    def set_attached(self, attached):
        self.add_param('attached', attached)

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

    def get_payMode(self):
        return self.get_params().get('payMode')

    def set_payMode(self, payMode):
        self.add_param('payMode', payMode)

    def get_portable(self):
        return self.get_params().get('portable')

    def set_portable(self, portable):
        self.add_param('portable', portable)

    def get_projectId(self):
        return self.get_params().get('projectId')

    def set_projectId(self, projectId):
        self.add_param('projectId', projectId)

    def get_searchValue(self):
        return self.get_params().get('searchValue')

    def set_searchValue(self, searchValue):
        self.add_param('searchValue', searchValue)

    def get_storageIds(self):
        return self.get_params().get('storageIds')

    def set_storageIds(self, storageIds):
        self.add_param('storageIds', storageIds)

    def get_storageStatus(self):
        return self.get_params().get('storageStatus')

    def set_storageStatus(self, storageStatus):
        self.add_param('storageStatus', storageStatus)

    def get_storageType(self):
        return self.get_params().get('storageType')

    def set_storageType(self, storageType):
        self.add_param('storageType', storageType)

    def get_storageTypes(self):
        return self.get_params().get('storageTypes')

    def set_storageTypes(self, storageTypes):
        self.add_param('storageTypes', storageTypes)

    def get_uInstanceIds(self):
        return self.get_params().get('uInstanceIds')

    def set_uInstanceIds(self, uInstanceIds):
        self.add_param('uInstanceIds', uInstanceIds)

    def get_zone(self):
        return self.get_params().get('zone')

    def set_zone(self, zone):
        self.add_param('zone', zone)

    def get_zoneId(self):
        return self.get_params().get('zoneId')

    def set_zoneId(self, zoneId):
        self.add_param('zoneId', zoneId)
