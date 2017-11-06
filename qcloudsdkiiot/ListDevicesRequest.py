# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ListDevicesRequest(Request):

    def __init__(self):
        super(ListDevicesRequest, self).__init__(
            'iiot', 'qcloudcliV1', 'ListDevices', 'iiot.api.qcloud.com')

    def get_attributeName(self):
        return self.get_params().get('attributeName')

    def set_attributeName(self, attributeName):
        self.add_param('attributeName', attributeName)

    def get_attributeValue(self):
        return self.get_params().get('attributeValue')

    def set_attributeValue(self, attributeValue):
        self.add_param('attributeValue', attributeValue)

    def get_maxResults(self):
        return self.get_params().get('maxResults')

    def set_maxResults(self, maxResults):
        self.add_param('maxResults', maxResults)

    def get_nextToken(self):
        return self.get_params().get('nextToken')

    def set_nextToken(self, nextToken):
        self.add_param('nextToken', nextToken)

    def get_productName(self):
        return self.get_params().get('productName')

    def set_productName(self, productName):
        self.add_param('productName', productName)
