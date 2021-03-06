# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ApiVersion(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The request must send the following parameters as a URL Encoded form; grant_type -
    client_credentials; resource - 62d94f6c-d599-489b-a797-3e10e42fbe22; client_id - AAD Registered
    App Client ID; client_secret - AAD Registered App Client Secret
    """

    TWO_THOUSAND_EIGHTEEN08_31 = "2018-08-31"
    TWO_THOUSAND_EIGHTEEN09_15 = "2018-09-15"

class UsageEventConflictResponseAdditionalInfoStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Accepted|NotProcessed|Expired
    """

    ACCEPTED = "Accepted"
    NOT_PROCESSED = "NotProcessed"
    EXPIRED = "Expired"

class UsageEventStatusEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the operation.
    """

    ACCEPTED = "Accepted"
    EXPIRED = "Expired"
    DUPLICATE = "Duplicate"
    ERROR = "Error"
    RESOURCE_NOT_FOUND = "ResourceNotFound"
    RESOURCE_NOT_AUTHORIZED = "ResourceNotAuthorized"
    INVALID_DIMENSION_BAD_ARGUMENT = "InvalidDimension|BadArgument"
