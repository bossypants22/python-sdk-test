# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class WipeNetworkSmDeviceModel(object):

    """Implementation of the 'wipeNetworkSmDevice' model.

    TODO: type model description here.

    Attributes:
        pin (int): The pin number (a six digit value) for wiping a macOS
            device. Required only for macOS devices.
        serial (string): The serial of the device to be wiped.
        wifi_mac (string): The wifiMac of the device to be wiped.
        id (string): The id of the device to be wiped.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pin":'pin',
        "serial":'serial',
        "wifi_mac":'wifiMac',
        "id":'id'
    }

    def __init__(self,
                 pin=None,
                 serial=None,
                 wifi_mac=None,
                 id=None):
        """Constructor for the WipeNetworkSmDeviceModel class"""

        # Initialize members of the class
        self.pin = pin
        self.serial = serial
        self.wifi_mac = wifi_mac
        self.id = id


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
        pin = dictionary.get('pin')
        serial = dictionary.get('serial')
        wifi_mac = dictionary.get('wifiMac')
        id = dictionary.get('id')

        # Return an object of this model
        return cls(pin,
                   serial,
                   wifi_mac,
                   id)


