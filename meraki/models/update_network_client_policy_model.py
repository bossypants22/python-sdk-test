# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkClientPolicyModel(object):

    """Implementation of the 'updateNetworkClientPolicy' model.

    TODO: type model description here.

    Attributes:
        group_policy_id (string): [optional] If devicePolicy param is set to
            'Group policy' this param is used to specify the group ID.
        device_policy (string): The group policy (Whitelisted, Blocked,
            Normal, Group policy)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_policy_id":'groupPolicyId',
        "device_policy":'devicePolicy'
    }

    def __init__(self,
                 group_policy_id=None,
                 device_policy=None):
        """Constructor for the UpdateNetworkClientPolicyModel class"""

        # Initialize members of the class
        self.group_policy_id = group_policy_id
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
        group_policy_id = dictionary.get('groupPolicyId')
        device_policy = dictionary.get('devicePolicy')

        # Return an object of this model
        return cls(group_policy_id,
                   device_policy)


