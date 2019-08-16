# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CombineOrganizationNetworksModel(object):

    """Implementation of the 'combineOrganizationNetworks' model.

    TODO: type model description here.

    Attributes:
        network_ids (list of string): A list of the network IDs that will be
            combined. If an ID of a combined network is included in this list,
            the other networks in the list will be grouped into that network
        name (string): The name of the combined network

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "network_ids":'networkIds',
        "name":'name'
    }

    def __init__(self,
                 network_ids=None,
                 name=None):
        """Constructor for the CombineOrganizationNetworksModel class"""

        # Initialize members of the class
        self.network_ids = network_ids
        self.name = name


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
        network_ids = dictionary.get('networkIds')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(network_ids,
                   name)


