# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_response_model import ErrorResponseModel  # noqa: E501
from swagger_server.models.http_validation_error import HTTPValidationError  # noqa: E501
from swagger_server.models.private_create_user_model import PrivateCreateUserModel  # noqa: E501
from swagger_server.models.private_detail_user_response_model import PrivateDetailUserResponseModel  # noqa: E501
from swagger_server.models.private_update_user_model import PrivateUpdateUserModel  # noqa: E501
from swagger_server.models.private_users_list_response_model import PrivateUsersListResponseModel  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminController(BaseTestCase):
    """AdminController integration test stubs"""

    def test_private_create_users_private_users_post(self):
        """Test case for private_create_users_private_users_post

        Создание пользователя
        """
        body = PrivateCreateUserModel()
        response = self.client.open(
            '/private/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_private_delete_user_private_users_pk_delete(self):
        """Test case for private_delete_user_private_users_pk_delete

        Удаление пользователя
        """
        response = self.client.open(
            '/private/users/{pk}'.format(pk=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_private_get_user_private_users_pk_get(self):
        """Test case for private_get_user_private_users_pk_get

        Детальное получение информации о пользователе
        """
        response = self.client.open(
            '/private/users/{pk}'.format(pk=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_private_patch_user_private_users_pk_patch(self):
        """Test case for private_patch_user_private_users_pk_patch

        Изменение информации о пользователе
        """
        body = PrivateUpdateUserModel()
        response = self.client.open(
            '/private/users/{pk}'.format(pk=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_private_users_private_users_get(self):
        """Test case for private_users_private_users_get

        Постраничное получение кратких данных обо всех пользователях
        """
        query_string = [('page', 56),
                        ('size', 56)]
        response = self.client.open(
            '/private/users',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
