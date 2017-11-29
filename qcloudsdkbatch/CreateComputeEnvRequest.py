# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateComputeEnvRequest(Request):

    def __init__(self):
        super(CreateComputeEnvRequest, self).__init__(
            'batch', 'qcloudcliV1', 'CreateComputeEnv', 'batch.api.qcloud.com')

    def get_ClientToken(self):
        return self.get_params().get('ClientToken')

    def set_ClientToken(self, ClientToken):
        self.add_param('ClientToken', ClientToken)

    def get_ComputeEnv(self):
        return self.get_params().get('ComputeEnv')

    def set_ComputeEnv(self, ComputeEnv):
        self.add_param('ComputeEnv', ComputeEnv)

    def get_Placement(self):
        return self.get_params().get('Placement')

    def set_Placement(self, Placement):
        self.add_param('Placement', Placement)

    def get_Version(self):
        return self.get_params().get('Version')

    def set_Version(self, Version):
        self.add_param('Version', Version)
