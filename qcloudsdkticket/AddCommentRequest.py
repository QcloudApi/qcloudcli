# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class AddCommentRequest(Request):

    def __init__(self):
        super(AddCommentRequest, self).__init__(
            'ticket', 'qcloudcliV1', 'AddComment', 'ticket.api.qcloud.com')

    def get_comment(self):
        return self.get_params().get('comment')

    def set_comment(self, comment):
        self.add_param('comment', comment)

    def get_handler(self):
        return self.get_params().get('handler')

    def set_handler(self, handler):
        self.add_param('handler', handler)

    def get_hasAttach(self):
        return self.get_params().get('hasAttach')

    def set_hasAttach(self, hasAttach):
        self.add_param('hasAttach', hasAttach)

    def get_ownerUin(self):
        return self.get_params().get('ownerUin')

    def set_ownerUin(self, ownerUin):
        self.add_param('ownerUin', ownerUin)

    def get_secret_content(self):
        return self.get_params().get('secret_content')

    def set_secret_content(self, secret_content):
        self.add_param('secret_content', secret_content)

    def get_ticketId(self):
        return self.get_params().get('ticketId')

    def set_ticketId(self, ticketId):
        self.add_param('ticketId', ticketId)
