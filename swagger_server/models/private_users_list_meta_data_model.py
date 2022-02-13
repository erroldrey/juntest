# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.paginated_meta_data_model import PaginatedMetaDataModel  # noqa: F401,E501
from swagger_server.models.private_users_list_hint_meta_model import PrivateUsersListHintMetaModel  # noqa: F401,E501
from swagger_server import util


class PrivateUsersListMetaDataModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, pagination: PaginatedMetaDataModel=None, hint: PrivateUsersListHintMetaModel=None):  # noqa: E501
        """PrivateUsersListMetaDataModel - a model defined in Swagger

        :param pagination: The pagination of this PrivateUsersListMetaDataModel.  # noqa: E501
        :type pagination: PaginatedMetaDataModel
        :param hint: The hint of this PrivateUsersListMetaDataModel.  # noqa: E501
        :type hint: PrivateUsersListHintMetaModel
        """
        self.swagger_types = {
            'pagination': PaginatedMetaDataModel,
            'hint': PrivateUsersListHintMetaModel
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'hint': 'hint'
        }
        self._pagination = pagination
        self._hint = hint

    @classmethod
    def from_dict(cls, dikt) -> 'PrivateUsersListMetaDataModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PrivateUsersListMetaDataModel of this PrivateUsersListMetaDataModel.  # noqa: E501
        :rtype: PrivateUsersListMetaDataModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self) -> PaginatedMetaDataModel:
        """Gets the pagination of this PrivateUsersListMetaDataModel.


        :return: The pagination of this PrivateUsersListMetaDataModel.
        :rtype: PaginatedMetaDataModel
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination: PaginatedMetaDataModel):
        """Sets the pagination of this PrivateUsersListMetaDataModel.


        :param pagination: The pagination of this PrivateUsersListMetaDataModel.
        :type pagination: PaginatedMetaDataModel
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination

    @property
    def hint(self) -> PrivateUsersListHintMetaModel:
        """Gets the hint of this PrivateUsersListMetaDataModel.


        :return: The hint of this PrivateUsersListMetaDataModel.
        :rtype: PrivateUsersListHintMetaModel
        """
        return self._hint

    @hint.setter
    def hint(self, hint: PrivateUsersListHintMetaModel):
        """Sets the hint of this PrivateUsersListMetaDataModel.


        :param hint: The hint of this PrivateUsersListMetaDataModel.
        :type hint: PrivateUsersListHintMetaModel
        """
        if hint is None:
            raise ValueError("Invalid value for `hint`, must not be `None`")  # noqa: E501

        self._hint = hint