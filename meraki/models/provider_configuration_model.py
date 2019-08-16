# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ProviderConfigurationModel(object):

    """Implementation of the 'ProviderConfiguration' model.

    TODO: type model description here.

    Attributes:
        mtype (string): The type for an object in ProviderConfiguration. Can
            be one of 'manual_string', 'manual_int', 'manual_boolean',
            'manual_choice', 'manual_multiselect', 'manual_list',
            'auto_username', 'auto_email', 'auto_mac_address',
            'auto_serial_number', 'auto_notes' or 'auto_name'
        value (string): The value for an object in ProviderConfiguration
        key (string): The key for an object in ProviderConfiguration

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype":'type',
        "key":'key',
        "value":'value'
    }

    def __init__(self,
                 mtype=None,
                 key=None,
                 value=None):
        """Constructor for the ProviderConfigurationModel class"""

        # Initialize members of the class
        self.mtype = mtype
        self.value = value
        self.key = key


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        mtype = dictionary.get('type')
        key = dictionary.get('key')
        value = dictionary.get('value')

        # Return an object of this model
        return cls(mtype,
                   key,
                   value)


