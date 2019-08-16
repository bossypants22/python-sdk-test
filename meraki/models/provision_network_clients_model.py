# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ProvisionNetworkClientsModel(object):

    """Implementation of the 'provisionNetworkClients' model.

    TODO: type model description here.

    Attributes:
        name (string): The display name for the client. Optional. Limited to
            255 bytes.
        group_policy_id (string): The ID of the desired group policy to apply
            to the client. Required if 'devicePolicy' is set to "Group
            policy". Otherwise this is ignored.
        mac (string): The MAC address of the client. Required.
        device_policy (string): The policy to apply to the specified client.
            Can be 'Whitelisted', 'Blocked', 'Normal' or 'Group policy'.
            Required.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "group_policy_id":'groupPolicyId',
        "mac":'mac',
        "device_policy":'devicePolicy'
    }

    def __init__(self,
                 name=None,
                 group_policy_id=None,
                 mac=None,
                 device_policy=None):
        """Constructor for the ProvisionNetworkClientsModel class"""

        # Initialize members of the class
        self.name = name
        self.group_policy_id = group_policy_id
        self.mac = mac
        self.device_policy = device_policy


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
        name = dictionary.get('name')
        group_policy_id = dictionary.get('groupPolicyId')
        mac = dictionary.get('mac')
        device_policy = dictionary.get('devicePolicy')

        # Return an object of this model
        return cls(name,
                   group_policy_id,
                   mac,
                   device_policy)


