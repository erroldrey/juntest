# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class UpdateUserModel(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, first_name: str=None, last_name: str=None, other_name: str=None, email: str=None, phone: str=None, birthday: date=None):  # noqa: E501
        """UpdateUserModel - a model defined in Swagger

        :param first_name: The first_name of this UpdateUserModel.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this UpdateUserModel.  # noqa: E501
        :type last_name: str
        :param other_name: The other_name of this UpdateUserModel.  # noqa: E501
        :type other_name: str
        :param email: The email of this UpdateUserModel.  # noqa: E501
        :type email: str
        :param phone: The phone of this UpdateUserModel.  # noqa: E501
        :type phone: str
        :param birthday: The birthday of this UpdateUserModel.  # noqa: E501
        :type birthday: date
        """
        self.swagger_types = {
            'first_name': str,
            'last_name': str,
            'other_name': str,
            'email': str,
            'phone': str,
            'birthday': date
        }

        self.attribute_map = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'other_name': 'other_name',
            'email': 'email',
            'phone': 'phone',
            'birthday': 'birthday'
        }
        self._first_name = first_name
        self._last_name = last_name
        self._other_name = other_name
        self._email = email
        self._phone = phone
        self._birthday = birthday

    @classmethod
    def from_dict(cls, dikt) -> 'UpdateUserModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The UpdateUserModel of this UpdateUserModel.  # noqa: E501
        :rtype: UpdateUserModel
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_name(self) -> str:
        """Gets the first_name of this UpdateUserModel.


        :return: The first_name of this UpdateUserModel.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this UpdateUserModel.


        :param first_name: The first_name of this UpdateUserModel.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this UpdateUserModel.


        :return: The last_name of this UpdateUserModel.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this UpdateUserModel.


        :param last_name: The last_name of this UpdateUserModel.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def other_name(self) -> str:
        """Gets the other_name of this UpdateUserModel.


        :return: The other_name of this UpdateUserModel.
        :rtype: str
        """
        return self._other_name

    @other_name.setter
    def other_name(self, other_name: str):
        """Sets the other_name of this UpdateUserModel.


        :param other_name: The other_name of this UpdateUserModel.
        :type other_name: str
        """

        self._other_name = other_name

    @property
    def email(self) -> str:
        """Gets the email of this UpdateUserModel.


        :return: The email of this UpdateUserModel.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this UpdateUserModel.


        :param email: The email of this UpdateUserModel.
        :type email: str
        """

        self._email = email

    @property
    def phone(self) -> str:
        """Gets the phone of this UpdateUserModel.


        :return: The phone of this UpdateUserModel.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        """Sets the phone of this UpdateUserModel.


        :param phone: The phone of this UpdateUserModel.
        :type phone: str
        """

        self._phone = phone

    @property
    def birthday(self) -> date:
        """Gets the birthday of this UpdateUserModel.


        :return: The birthday of this UpdateUserModel.
        :rtype: date
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday: date):
        """Sets the birthday of this UpdateUserModel.


        :param birthday: The birthday of this UpdateUserModel.
        :type birthday: date
        """

        self._birthday = birthday
