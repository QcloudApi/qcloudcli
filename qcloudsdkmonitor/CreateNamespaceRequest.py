# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class CreateNamespaceRequest(Request):

    def __init__(self):
        super(CreateNamespaceRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'CreateNamespace', 'monitor.api.qcloud.com')

    def get_namespace(self):
        return self.get_params().get('namespace')

    def set_namespace(self, namespace):
        self.add_param('namespace', namespace)
