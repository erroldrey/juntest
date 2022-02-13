import connexion
import six

from swagger_server.models.error_response_model import ErrorResponseModel  # noqa: E501
from swagger_server.models.http_validation_error import HTTPValidationError  # noqa: E501
from swagger_server.models.private_create_user_model import PrivateCreateUserModel  # noqa: E501
from swagger_server.models.private_detail_user_response_model import PrivateDetailUserResponseModel  # noqa: E501
from swagger_server.models.private_update_user_model import PrivateUpdateUserModel  # noqa: E501
from swagger_server.models.private_users_list_response_model import PrivateUsersListResponseModel  # noqa: E501
from swagger_server import util



def private_create_users_private_users_post(body):  # noqa: E501
    app.add_url_rule(f'{prefix}/', 'create_account',
                     admin_controller.create_account, methods=['POST'])
    """Создание пользователя

    Здесь возможно занести в базу нового пользователя о нем # noqa: E501
    :param body:  
    :type body: dict | bytes

    :rtype: PrivateDetailUserResponseModel
    """
    if connexion.request.is_json:
        body = PrivateCreateUserModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def private_delete_user_private_users_pk_delete(pk):  # noqa: E501
    app.add_url_rule(f'{prefix}/<username>', 'delete_account',
                     admin_controller.delete_account, methods=['DELETE'])
    """Удаление пользователя

    Удаление пользователя # noqa: E501

    :param pk: 
    :type pk: int

    :rtype: None
    """
    return 'do some magic!'


def private_get_user_private_users_pk_get(pk):  # noqa: E501
    app.add_url_rule(f'{prefix}/<username>', 'get_account_info',
                     admin_controller.get_account_info, methods=['GET'])
    """Детальное получение информации о пользователе

    Здесь администратор может увидеть всю существующую пользовательскую информацию # noqa: E501

    :param pk: 
    :type pk: int

    :rtype: PrivateDetailUserResponseModel
    """
    return 'do some magic!'


def private_patch_user_private_users_pk_patch(body, pk):  # noqa: E501
    app.add_url_rule(f'{prefix}/<username>', 'patch_account',
                     admin_controller.patch_account, methods=['PATCH'])
    """Изменение информации о пользователе

    Здесь администратор может изменить любую информацию о пользователе # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pk: 
    :type pk: int

    :rtype: PrivateDetailUserResponseModel
    """
    if connexion.request.is_json:
        body = PrivateUpdateUserModel.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def private_users_private_users_get_accounts_list(page, size):  # noqa: E501
    app.add_url_rule(f'{prefix}/<username>', 'get_accounts_list',
                     admin_controller.get_accounts_list, methods=['GET'])
    """Постраничное получение кратких данных обо всех пользователях

    Здесь находится вся информация, доступная пользователю о других пользователях # noqa: E501

    :param page: 
    :type page: int
    :param size: 
    :type size: int

    :rtype: PrivateUsersListResponseModel
    """
    return 'do some magic!'
