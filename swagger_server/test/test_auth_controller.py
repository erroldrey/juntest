# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.current_user_response_model import CurrentUserResponseModel  # noqa: E501
from swagger_server.models.error_response_model import ErrorResponseModel  # noqa: E501
from swagger_server.models.http_validation_error import HTTPValidationError  # noqa: E501
from swagger_server.models.login_model import LoginModel  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_login_login_post(self):
        """Test case for login_login_post

        Вход в систему
        """
        body = LoginModel()
        response = self.client.open(
            '/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_logout_get(self):
        """Test case for logout_logout_get

        Выход из системы
        """
        response = self.client.open(
            '/logout',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
