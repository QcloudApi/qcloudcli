# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class ModifySecurityGroupAttributesRequest(Request):

    def __init__(self):
        super(ModifySecurityGroupAttributesRequest, self).__init__(
            'dfw', 'qcloudcliV1', 'ModifySecurityGroupAttributes', 'dfw.api.qcloud.com')

    def get_sgId(self):
        return self.get_params().get('sgId')

    def set_sgId(self, sgId):
        self.add_param('sgId', sgId)

    def get_sgName(self):
        return self.get_params().get('sgName')

    def set_sgName(self, sgName):
        self.add_param('sgName', sgName)

    def get_sgRemark(self):
        return self.get_params().get('sgRemark')

    def set_sgRemark(self, sgRemark):
        self.add_param('sgRemark', sgRemark)
