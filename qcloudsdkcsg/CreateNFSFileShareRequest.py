# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateNFSFileShareRequest(Request):

    def __init__(self):
        super(CreateNFSFileShareRequest, self).__init__(
            'csg', 'qcloudcliV1', 'CreateNFSFileShare', 'csg.api.qcloud.com')

    def get_ClientList(self):
        return self.get_params().get('ClientList')

    def set_ClientList(self, ClientList):
        self.add_param('ClientList', ClientList)

    def get_FileShareName(self):
        return self.get_params().get('FileShareName')

    def set_FileShareName(self, FileShareName):
        self.add_param('FileShareName', FileShareName)

    def get_GatewayURN(self):
        return self.get_params().get('GatewayURN')

    def set_GatewayURN(self, GatewayURN):
        self.add_param('GatewayURN', GatewayURN)
