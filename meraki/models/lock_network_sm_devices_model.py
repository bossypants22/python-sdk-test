# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class LockNetworkSmDevicesModel(object):

    """Implementation of the 'lockNetworkSmDevices' model.

    TODO: type model description here.

    Attributes:
        serials (string): The serials of the devices to be locked.
        pin (int): The pin number for locking macOS devices (a six digit
            number). Required only for macOS devices.
        scope (string): The scope (one of all, none, withAny, withAll,
            withoutAny, or withoutAll) and a set of tags of the devices to be
            wiped.
        ids (string): The ids of the devices to be locked.
        wifi_macs (string): The wifiMacs of the devices to be locked.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "serials":'serials',
        "pin":'pin',
        "scope":'scope',
        "ids":'ids',
        "wifi_macs":'wifiMacs'
    }

    def __init__(self,
                 serials=None,
                 pin=None,
                 scope=None,
                 ids=None,
                 wifi_macs=None):
        """Constructor for the LockNetworkSmDevicesModel class"""

        # Initialize members of the class
        self.serials = serials
        self.pin = pin
        self.scope = scope
        self.ids = ids
        self.wifi_macs = wifi_macs


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
        serials = dictionary.get('serials')
        pin = dictionary.get('pin')
        scope = dictionary.get('scope')
        ids = dictionary.get('ids')
        wifi_macs = dictionary.get('wifiMacs')

        # Return an object of this model
        return cls(serials,
                   pin,
                   scope,
                   ids,
                   wifi_macs)


