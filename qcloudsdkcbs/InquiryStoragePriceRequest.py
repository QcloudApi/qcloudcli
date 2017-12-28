# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class InquiryStoragePriceRequest(Request):

    def __init__(self):
        super(InquiryStoragePriceRequest, self).__init__(
            'cbs', 'qcloudcliV1', 'InquiryStoragePrice', 'cbs.api.qcloud.com')

    def get_chargeSet(self):
        return self.get_params().get('chargeSet')

    def set_chargeSet(self, chargeSet):
        self.add_param('chargeSet', chargeSet)

    def get_goodsNum(self):
        return self.get_params().get('goodsNum')

    def set_goodsNum(self, goodsNum):
        self.add_param('goodsNum', goodsNum)

    def get_inquiryType(self):
        return self.get_params().get('inquiryType')

    def set_inquiryType(self, inquiryType):
        self.add_param('inquiryType', inquiryType)

    def get_newDeadline(self):
        return self.get_params().get('newDeadline')

    def set_newDeadline(self, newDeadline):
        self.add_param('newDeadline', newDeadline)

    def get_payMode(self):
        return self.get_params().get('payMode')

    def set_payMode(self, payMode):
        self.add_param('payMode', payMode)

    def get_period(self):
        return self.get_params().get('period')

    def set_period(self, period):
        self.add_param('period', period)

    def get_periods(self):
        return self.get_params().get('periods')

    def set_periods(self, periods):
        self.add_param('periods', periods)

    def get_storageId(self):
        return self.get_params().get('storageId')

    def set_storageId(self, storageId):
        self.add_param('storageId', storageId)

    def get_storageIds(self):
        return self.get_params().get('storageIds')

    def set_storageIds(self, storageIds):
        self.add_param('storageIds', storageIds)

    def get_storageSize(self):
        return self.get_params().get('storageSize')

    def set_storageSize(self, storageSize):
        self.add_param('storageSize', storageSize)

    def get_storageType(self):
        return self.get_params().get('storageType')

    def set_storageType(self, storageType):
        self.add_param('storageType', storageType)

    def get_timeUnit(self):
        return self.get_params().get('timeUnit')

    def set_timeUnit(self, timeUnit):
        self.add_param('timeUnit', timeUnit)
