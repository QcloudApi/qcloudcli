# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class EnterpriseAccountOpenRequest(Request):

    def __init__(self):
        super(EnterpriseAccountOpenRequest, self).__init__(
            'ds', 'qcloudcliV1', 'EnterpriseAccountOpen', 'ds.api.qcloud.com')

    def get_email(self):
        return self.get_params().get('email')

    def set_email(self, email):
        self.add_param('email', email)

    def get_identNo(self):
        return self.get_params().get('identNo')

    def set_identNo(self, identNo):
        self.add_param('identNo', identNo)

    def get_identType(self):
        return self.get_params().get('identType')

    def set_identType(self, identType):
        self.add_param('identType', identType)

    def get_landlinePhone(self):
        return self.get_params().get('landlinePhone')

    def set_landlinePhone(self, landlinePhone):
        self.add_param('landlinePhone', landlinePhone)

    def get_mobilePhone(self):
        return self.get_params().get('mobilePhone')

    def set_mobilePhone(self, mobilePhone):
        self.add_param('mobilePhone', mobilePhone)

    def get_module(self):
        return self.get_params().get('module')

    def set_module(self, module):
        self.add_param('module', module)

    def get_name(self):
        return self.get_params().get('name')

    def set_name(self, name):
        self.add_param('name', name)

    def get_operation(self):
        return self.get_params().get('operation')

    def set_operation(self, operation):
        self.add_param('operation', operation)

    def get_transactorAddress(self):
        return self.get_params().get('transactorAddress')

    def set_transactorAddress(self, transactorAddress):
        self.add_param('transactorAddress', transactorAddress)

    def get_transactorIdentNo(self):
        return self.get_params().get('transactorIdentNo')

    def set_transactorIdentNo(self, transactorIdentNo):
        self.add_param('transactorIdentNo', transactorIdentNo)

    def get_transactorIdentType(self):
        return self.get_params().get('transactorIdentType')

    def set_transactorIdentType(self, transactorIdentType):
        self.add_param('transactorIdentType', transactorIdentType)

    def get_transactorName(self):
        return self.get_params().get('transactorName')

    def set_transactorName(self, transactorName):
        self.add_param('transactorName', transactorName)
