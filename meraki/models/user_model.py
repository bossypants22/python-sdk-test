# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UserModel(object):

    """Implementation of the 'User' model.

    TODO: type model description here.

    Attributes:
        passphrase (string): The passphrase for the SNMP user. Required.
        username (string): The username for the SNMP user. Required.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "passphrase":'passphrase',
        "username":'username'
    }

    def __init__(self,
                 passphrase=None,
                 username=None):
        """Constructor for the UserModel class"""

        # Initialize members of the class
        self.passphrase = passphrase
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
        passphrase = dictionary.get('passphrase')
        username = dictionary.get('username')

        # Return an object of this model
        return cls(passphrase,
                   username)


