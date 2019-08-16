# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkPiiRequestModel(object):

    """Implementation of the 'createNetworkPiiRequest' model.

    TODO: type model description here.

    Attributes:
        sm_device_id (string): The sm_device_id of a Systems Manager device.
            The only way to "restrict processing" or "delete" a Systems
            Manager device. Must include "device" in the dataset for a
            "delete" request to destroy the device.
        datasets (list of string): The datasets related to the provided key
            that should be deleted. Only applies to "delete" requests. The
            value "all" will be expanded to all datasets applicable to this
            type. The datasets by applicable to each type are: mac (usage,
            events, traffic), email (users, loginAttempts), username (users,
            loginAttempts), bluetoothMac (client, connectivity), smDeviceId
            (device), smUserId (user)
        mtype (Type7Enum): One of "delete" or "restrict processing"
        email (string): The email of a network user account. Only applies to
            "delete" requests.
        mac (string): The MAC of a network client device. Applies to both
            "restrict processing" and "delete" requests.
        sm_user_id (string): The sm_user_id of a Systems Manager user. The
            only way to "restrict processing" or "delete" a Systems Manager
            user. Must include "user" in the dataset for a "delete" request to
            destroy the user.
        username (string): The username of a network log in. Only applies to
            "delete" requests.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sm_device_id":'smDeviceId',
        "datasets":'datasets',
        "mtype":'type',
        "email":'email',
        "mac":'mac',
        "sm_user_id":'smUserId',
        "username":'username'
    }

    def __init__(self,
                 sm_device_id=None,
                 datasets=None,
                 mtype=None,
                 email=None,
                 mac=None,
                 sm_user_id=None,
                 username=None):
        """Constructor for the CreateNetworkPiiRequestModel class"""

        # Initialize members of the class
        self.sm_device_id = sm_device_id
        self.datasets = datasets
        self.mtype = mtype
        self.email = email
        self.mac = mac
        self.sm_user_id = sm_user_id
        self.username = username


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
        sm_device_id = dictionary.get('smDeviceId')
        datasets = dictionary.get('datasets')
        mtype = dictionary.get('type')
        email = dictionary.get('email')
        mac = dictionary.get('mac')
        sm_user_id = dictionary.get('smUserId')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(sm_device_id,
                   datasets,
                   mtype,
                   email,
                   mac,
                   sm_user_id,
                   username)


