# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.wan2_model
import meraki.models.wan1_model

class UpdateNetworkDeviceManagementInterfaceSettingsModel(object):

    """Implementation of the 'updateNetworkDeviceManagementInterfaceSettings' model.

    TODO: type model description here.

    Attributes:
        wan_2 (Wan2Model): WAN 2 settings (only for MX devices)
        wan_1 (Wan1Model): WAN 1 settings

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "wan2":'wan2',
        "wan1":'wan1'
    }

    def __init__(self,
                 wan2=None,
                 wan1=None):
        """Constructor for the UpdateNetworkDeviceManagementInterfaceSettingsModel class"""

        # Initialize members of the class
        self.wan2 = wan2
        self.wan1 = wan1


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
        wan2 = meraki.models.wan2_model.Wan2Model.from_dictionary(dictionary.get('wan2')) if dictionary.get('wan2') else None
        wan1 = meraki.models.wan1_model.Wan1Model.from_dictionary(dictionary.get('wan1')) if dictionary.get('wan1') else None

        # Return an object of this model
        return cls(wan2,
                   wan1)


