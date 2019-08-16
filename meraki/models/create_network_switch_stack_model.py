# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkSwitchStackModel(object):

    """Implementation of the 'createNetworkSwitchStack' model.

    TODO: type model description here.

    Attributes:
        serials (list of string): An array of switch serials to be added into
            the new stack
        name (string): The name of the new stack

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "serials":'serials',
        "name":'name'
    }

    def __init__(self,
                 serials=None,
                 name=None):
        """Constructor for the CreateNetworkSwitchStackModel class"""

        # Initialize members of the class
        self.serials = serials
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
        serials = dictionary.get('serials')
        name = dictionary.get('name')

        # Return an object of this model
        return cls(serials,
                   name)


