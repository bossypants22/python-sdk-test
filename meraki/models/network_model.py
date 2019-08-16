# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class NetworkModel(object):

    """Implementation of the 'Network' model.

    TODO: type model description here.

    Attributes:
        access (string): The privilege of the SAML administrator on the
            network
        id (string): The network ID

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "access":'access',
        "id":'id'
    }

    def __init__(self,
                 access=None,
                 id=None):
        """Constructor for the NetworkModel class"""

        # Initialize members of the class
        self.access = access
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
        access = dictionary.get('access')
        id = dictionary.get('id')

        # Return an object of this model
        return cls(access,
                   id)


