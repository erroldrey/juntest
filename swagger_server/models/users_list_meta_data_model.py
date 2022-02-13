# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.paginated_meta_data_model import PaginatedMetaDataModel  # noqa: F401,E501
from swagger_server import util


class UsersListMetaDataModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, pagination: PaginatedMetaDataModel=None):  # noqa: E501
        """UsersListMetaDataModel - a model defined in Swagger

        :param pagination: The pagination of this UsersListMetaDataModel.  # noqa: E501
        :type pagination: PaginatedMetaDataModel
        """
        self.swagger_types = {
            'pagination': PaginatedMetaDataModel
        }

        self.attribute_map = {
            'pagination': 'pagination'
        }
        self._pagination = pagination

    @classmethod
    def from_dict(cls, dikt) -> 'UsersListMetaDataModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UsersListMetaDataModel of this UsersListMetaDataModel.  # noqa: E501
        :rtype: UsersListMetaDataModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pagination(self) -> PaginatedMetaDataModel:
        """Gets the pagination of this UsersListMetaDataModel.


        :return: The pagination of this UsersListMetaDataModel.
        :rtype: PaginatedMetaDataModel
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination: PaginatedMetaDataModel):
        """Sets the pagination of this UsersListMetaDataModel.


        :param pagination: The pagination of this UsersListMetaDataModel.
        :type pagination: PaginatedMetaDataModel
        """
        if pagination is None:
            raise ValueError("Invalid value for `pagination`, must not be `None`")  # noqa: E501

        self._pagination = pagination