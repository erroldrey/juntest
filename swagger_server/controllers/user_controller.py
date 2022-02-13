import connexion
import six

from swagger_server.models.current_user_response_model import CurrentUserResponseModel  # noqa: E501
from swagger_server.models.error_response_model import ErrorResponseModel  # noqa: E501
from swagger_server.models.http_validation_error import HTTPValidationError  # noqa: E501
from swagger_server.models.update_user_model import UpdateUserModel  # noqa: E501
from swagger_server.models.update_user_response_model import UpdateUserResponseModel  # noqa: E501
from swagger_server.models.users_list_response_model import UsersListResponseModel  # noqa: E501
from swagger_server import util


def current_user_users_current_get():  # noqa: E501
    app.add_url_rule(f'{prefix}/', 'get_current_info',
                     users_controller.get_current_info, methods=['GET'])

    """Получение данных о текущем пользователе

    Здесь находится вся информация, доступная пользователю о самом себе, а так же информация является ли он администратором # noqa: E501


    :rtype: CurrentUserResponseModel
    """
    return 'do some magic!'


def edit_user_users_pk_patch(body, pk):  # noqa: E501
    app.add_url_rule(f'{prefix}/', 'patch_my_account',
                     users_controller.patch_my_account, methods=['PATCH'])
    """Изменение данных пользователя

    Здесь пользователь имеет возможность изменить свои данные # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pk: 
    :type pk: int

    :rtype: UpdateUserResponseModel
    """
    if connexion.request.is_json:
        body = UpdateUserModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_users_get(page, size):  # noqa: E501
    app.add_url_rule(f'{prefix}/', 'get_users_list',
                     users_controller.create_account, methods=['GET'])
    """Постраничное получение кратких данных обо всех пользователях

    Здесь находится вся информация, доступная пользователю о других пользователях # noqa: E501

    :param page: 
    :type page: int
    :param size: 
    :type size: int

    :rtype: UsersListResponseModel
    """
    return 'do some magic!'
