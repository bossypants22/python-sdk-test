# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkBluetoothSettingsModel(object):

    """Implementation of the 'updateNetworkBluetoothSettings' model.

    TODO: type model description here.

    Attributes:
        major (int): The major number to be used in the beacon identifier.
            Only valid in 'Non-unique' mode.
        minor (int): The minor number to be used in the beacon identifier.
            Only valid in 'Non-unique' mode.
        major_minor_assignment_mode (string): The way major and minor number
            should be assigned to nodes in the network. ('Unique',
            'Non-unique')
        scanning_enabled (bool): Whether APs will scan for Bluetooth enabled
            clients. (true, false)
        uuid (string): The UUID to be used in the beacon identifier.
        advertising_enabled (bool): Whether APs will advertise beacons. (true,
            false)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "major":'major',
        "minor":'minor',
        "major_minor_assignment_mode":'majorMinorAssignmentMode',
        "scanning_enabled":'scanningEnabled',
        "uuid":'uuid',
        "advertising_enabled":'advertisingEnabled'
    }

    def __init__(self,
                 major=None,
                 minor=None,
                 major_minor_assignment_mode=None,
                 scanning_enabled=None,
                 uuid=None,
                 advertising_enabled=None):
        """Constructor for the UpdateNetworkBluetoothSettingsModel class"""

        # Initialize members of the class
        self.major = major
        self.minor = minor
        self.major_minor_assignment_mode = major_minor_assignment_mode
        self.scanning_enabled = scanning_enabled
        self.uuid = uuid
        self.advertising_enabled = advertising_enabled


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
        major = dictionary.get('major')
        minor = dictionary.get('minor')
        major_minor_assignment_mode = dictionary.get('majorMinorAssignmentMode')
        scanning_enabled = dictionary.get('scanningEnabled')
        uuid = dictionary.get('uuid')
        advertising_enabled = dictionary.get('advertisingEnabled')

        # Return an object of this model
        return cls(major,
                   minor,
                   major_minor_assignment_mode,
                   scanning_enabled,
                   uuid,
                   advertising_enabled)


