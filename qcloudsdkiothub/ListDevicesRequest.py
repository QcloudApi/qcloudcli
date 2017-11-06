# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListDevicesRequest(Request):

    def __init__(self):
        super(ListDevicesRequest, self).__init__(
            'iothub', 'qcloudcliV1', 'ListDevices', 'iothub.api.qcloud.com')

    def get_attributeName(self):
        return self.get_params().get('attributeName')

    def set_attributeName(self, attributeName):
        self.add_param('attributeName', attributeName)

    def get_attributeValue(self):
        return self.get_params().get('attributeValue')

    def set_attributeValue(self, attributeValue):
        self.add_param('attributeValue', attributeValue)

    def get_pageNum(self):
        return self.get_params().get('pageNum')

    def set_pageNum(self, pageNum):
        self.add_param('pageNum', pageNum)

    def get_pageSize(self):
        return self.get_params().get('pageSize')

    def set_pageSize(self, pageSize):
        self.add_param('pageSize', pageSize)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
