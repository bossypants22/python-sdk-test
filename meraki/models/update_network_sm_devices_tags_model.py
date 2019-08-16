# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmDevicesTagsModel(object):

    """Implementation of the 'updateNetworkSmDevicesTags' model.

    TODO: type model description here.

    Attributes:
        update_action (string): One of add, delete, or update. Only devices
            that have been modified will be returned.
        serials (string): The serials of the devices to be modified.
        scope (string): The scope (one of all, none, withAny, withAll,
            withoutAny, or withoutAll) and a set of tags of the devices to be
            modified.
        ids (string): The ids of the devices to be modified.
        wifi_macs (string): The wifiMacs of the devices to be modified.
        tags (string): The tags to be added, deleted, or updated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "update_action":'updateAction',
        "tags":'tags',
        "serials":'serials',
        "scope":'scope',
        "ids":'ids',
        "wifi_macs":'wifiMacs'
    }

    def __init__(self,
                 update_action=None,
                 tags=None,
                 serials=None,
                 scope=None,
                 ids=None,
                 wifi_macs=None):
        """Constructor for the UpdateNetworkSmDevicesTagsModel class"""

        # Initialize members of the class
        self.update_action = update_action
        self.serials = serials
        self.scope = scope
        self.ids = ids
        self.wifi_macs = wifi_macs
        self.tags = tags


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
        update_action = dictionary.get('updateAction')
        tags = dictionary.get('tags')
        serials = dictionary.get('serials')
        scope = dictionary.get('scope')
        ids = dictionary.get('ids')
        wifi_macs = dictionary.get('wifiMacs')

        # Return an object of this model
        return cls(update_action,
                   tags,
                   serials,
                   scope,
                   ids,
                   wifi_macs)


