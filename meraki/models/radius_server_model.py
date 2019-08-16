# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RadiusServerModel(object):

    """Implementation of the 'RadiusServer' model.

    TODO: type model description here.

    Attributes:
        port (int): UDP port the RADIUS server listens on for Access-requests
        host (string): IP address of your RADIUS server
        secret (string): RADIUS client shared secret

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "port":'port',
        "host":'host',
        "secret":'secret'
    }

    def __init__(self,
                 port=None,
                 host=None,
                 secret=None):
        """Constructor for the RadiusServerModel class"""

        # Initialize members of the class
        self.port = port
        self.host = host
        self.secret = secret


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
        port = dictionary.get('port')
        host = dictionary.get('host')
        secret = dictionary.get('secret')

        # Return an object of this model
        return cls(port,
                   host,
                   secret)


