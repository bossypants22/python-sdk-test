# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CheckinNetworkSmDevicesModel(object):

    """Implementation of the 'checkinNetworkSmDevices' model.

    TODO: type model description here.

    Attributes:
        serials (string): The serials of the devices to be checked-in.
        scope (string): The scope (one of all, none, withAny, withAll,
            withoutAny, or withoutAll) and a set of tags of the devices to be
            checked-in.
        ids (string): The ids of the devices to be checked-in.
        wifi_macs (string): The wifiMacs of the devices to be checked-in.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "serials":'serials',
        "scope":'scope',
        "ids":'ids',
        "wifi_macs":'wifiMacs'
    }

    def __init__(self,
                 serials=None,
                 scope=None,
                 ids=None,
                 wifi_macs=None):
        """Constructor for the CheckinNetworkSmDevicesModel class"""

        # Initialize members of the class
        self.serials = serials
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
        scope = dictionary.get('scope')
        ids = dictionary.get('ids')
        wifi_macs = dictionary.get('wifiMacs')

        # Return an object of this model
        return cls(serials,
                   scope,
                   ids,
                   wifi_macs)


