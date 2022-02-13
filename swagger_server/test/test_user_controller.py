# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.current_user_response_model import CurrentUserResponseModel  # noqa: E501
from swagger_server.models.error_response_model import ErrorResponseModel  # noqa: E501
from swagger_server.models.http_validation_error import HTTPValidationError  # noqa: E501
from swagger_server.models.update_user_model import UpdateUserModel  # noqa: E501
from swagger_server.models.update_user_response_model import UpdateUserResponseModel  # noqa: E501
from swagger_server.models.users_list_response_model import UsersListResponseModel  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_current_user_users_current_get(self):
        """Test case for current_user_users_current_get

        Получение данных о текущем пользователе
        """
        response = self.client.open(
            '/users/current',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_user_users_pk_patch(self):
        """Test case for edit_user_users_pk_patch

        Изменение данных пользователя
        """
        body = UpdateUserModel()
        response = self.client.open(
            '/users/{pk}'.format(pk=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_users_get(self):
        """Test case for users_users_get

        Постраничное получение кратких данных обо всех пользователях
        """
        query_string = [('page', 56),
                        ('size', 56)]
        response = self.client.open(
            '/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
