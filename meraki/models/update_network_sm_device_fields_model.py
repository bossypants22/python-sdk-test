# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.device_fields_model

class UpdateNetworkSmDeviceFieldsModel(object):

    """Implementation of the 'updateNetworkSmDeviceFields' model.

    TODO: type model description here.

    Attributes:
        device_fields (DeviceFieldsModel): The new fields of the device. Each
            field of this object is optional.
        serial (string): The serial of the device to be modified.
        wifi_mac (string): The wifiMac of the device to be modified.
        id (string): The id of the device to be modified.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_fields":'deviceFields',
        "serial":'serial',
        "wifi_mac":'wifiMac',
        "id":'id'
    }

    def __init__(self,
                 device_fields=None,
                 serial=None,
                 wifi_mac=None,
                 id=None):
        """Constructor for the UpdateNetworkSmDeviceFieldsModel class"""

        # Initialize members of the class
        self.device_fields = device_fields
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
        device_fields = meraki.models.device_fields_model.DeviceFieldsModel.from_dictionary(dictionary.get('deviceFields')) if dictionary.get('deviceFields') else None
        serial = dictionary.get('serial')
        wifi_mac = dictionary.get('wifiMac')
        id = dictionary.get('id')

        # Return an object of this model
        return cls(device_fields,
                   serial,
                   wifi_mac,
                   id)


