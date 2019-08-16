# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ApTagsAndVlanIdModel(object):

    """Implementation of the 'ApTagsAndVlanId' model.

    TODO: type model description here.

    Attributes:
        vlan_id (int): Numerical identifier that is assigned to the VLAN
        tags (string): Comma-separated list of AP tags

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vlan_id":'vlanId',
        "tags":'tags'
    }

    def __init__(self,
                 vlan_id=None,
                 tags=None):
        """Constructor for the ApTagsAndVlanIdModel class"""

        # Initialize members of the class
        self.vlan_id = vlan_id
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
        vlan_id = dictionary.get('vlanId')
        tags = dictionary.get('tags')

        # Return an object of this model
        return cls(vlan_id,
                   tags)


