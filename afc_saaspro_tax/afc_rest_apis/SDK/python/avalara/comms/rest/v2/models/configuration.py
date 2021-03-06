# coding: utf-8

"""
    SaasPro

    APIs to interface with communications tax engine.<br />The API requires Basic authentication.<br />Users with access to multiple clients must also set request header parameter for <code>client_id</code>.<br />Set <code>client_profile_id</code> to specify profile to be used for taxation.  # noqa: E501

    The version of the OpenAPI document: v2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from avalara.comms.rest.v2.configuration import Configuration


class Configuration(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'traffic_study_overrides': 'list[TrafficStudyOverride]',
        'return_non_billable': 'bool',
        'tax_on_tax_algorithm': 'int',
        'self_tax_algorithm': 'int'
    }

    attribute_map = {
        'traffic_study_overrides': 'TrafficStudyOverrides',
        'return_non_billable': 'ReturnNonBillable',
        'tax_on_tax_algorithm': 'TaxOnTaxAlgorithm',
        'self_tax_algorithm': 'SelfTaxAlgorithm'
    }

    def __init__(self, traffic_study_overrides=None, return_non_billable=None, tax_on_tax_algorithm=None, self_tax_algorithm=None, local_vars_configuration=None):  # noqa: E501
        """Configuration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._traffic_study_overrides = None
        self._return_non_billable = None
        self._tax_on_tax_algorithm = None
        self._self_tax_algorithm = None
        self.discriminator = None

        self.traffic_study_overrides = traffic_study_overrides
        self.return_non_billable = return_non_billable
        self.tax_on_tax_algorithm = tax_on_tax_algorithm
        self.self_tax_algorithm = self_tax_algorithm

    @property
    def traffic_study_overrides(self):
        """Gets the traffic_study_overrides of this Configuration.  # noqa: E501

        List of Traffic Study Overrides  # noqa: E501

        :return: The traffic_study_overrides of this Configuration.  # noqa: E501
        :rtype: list[TrafficStudyOverride]
        """
        return self._traffic_study_overrides

    @traffic_study_overrides.setter
    def traffic_study_overrides(self, traffic_study_overrides):
        """Sets the traffic_study_overrides of this Configuration.

        List of Traffic Study Overrides  # noqa: E501

        :param traffic_study_overrides: The traffic_study_overrides of this Configuration.  # noqa: E501
        :type: list[TrafficStudyOverride]
        """

        self._traffic_study_overrides = traffic_study_overrides

    @property
    def return_non_billable(self):
        """Gets the return_non_billable of this Configuration.  # noqa: E501

        true : Return both non-billable and billable taxes in taxation response  false (default) : Return billable taxes only in taxation response  Default: false  # noqa: E501

        :return: The return_non_billable of this Configuration.  # noqa: E501
        :rtype: bool
        """
        return self._return_non_billable

    @return_non_billable.setter
    def return_non_billable(self, return_non_billable):
        """Sets the return_non_billable of this Configuration.

        true : Return both non-billable and billable taxes in taxation response  false (default) : Return billable taxes only in taxation response  Default: false  # noqa: E501

        :param return_non_billable: The return_non_billable of this Configuration.  # noqa: E501
        :type: bool
        """

        self._return_non_billable = return_non_billable

    @property
    def tax_on_tax_algorithm(self):
        """Gets the tax_on_tax_algorithm of this Configuration.  # noqa: E501

        Tax-on-tax algorithm to be used in tax calculations  0 : Single pass  1 (default) : IterateOnTaxAmount  2 : IterateOnTaxableMeasure  # noqa: E501

        :return: The tax_on_tax_algorithm of this Configuration.  # noqa: E501
        :rtype: int
        """
        return self._tax_on_tax_algorithm

    @tax_on_tax_algorithm.setter
    def tax_on_tax_algorithm(self, tax_on_tax_algorithm):
        """Sets the tax_on_tax_algorithm of this Configuration.

        Tax-on-tax algorithm to be used in tax calculations  0 : Single pass  1 (default) : IterateOnTaxAmount  2 : IterateOnTaxableMeasure  # noqa: E501

        :param tax_on_tax_algorithm: The tax_on_tax_algorithm of this Configuration.  # noqa: E501
        :type: int
        """

        self._tax_on_tax_algorithm = tax_on_tax_algorithm

    @property
    def self_tax_algorithm(self):
        """Gets the self_tax_algorithm of this Configuration.  # noqa: E501

        Self-tax algorithm to be used in tax calculations  0 (default) : Calculate tax on individual self-taxing taxes  1 : Calculate tax on aggregate of self-taxing taxes  # noqa: E501

        :return: The self_tax_algorithm of this Configuration.  # noqa: E501
        :rtype: int
        """
        return self._self_tax_algorithm

    @self_tax_algorithm.setter
    def self_tax_algorithm(self, self_tax_algorithm):
        """Sets the self_tax_algorithm of this Configuration.

        Self-tax algorithm to be used in tax calculations  0 (default) : Calculate tax on individual self-taxing taxes  1 : Calculate tax on aggregate of self-taxing taxes  # noqa: E501

        :param self_tax_algorithm: The self_tax_algorithm of this Configuration.  # noqa: E501
        :type: int
        """

        self._self_tax_algorithm = self_tax_algorithm

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Configuration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Configuration):
            return True

        return self.to_dict() != other.to_dict()
