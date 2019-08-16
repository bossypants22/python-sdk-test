# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class RadiusAccountingServerModel(object):

    """Implementation of the 'RadiusAccountingServer' model.

    TODO: type model description here.

    Attributes:
        port (int): Port on the RADIUS server that is listening for accounting
            messages
        host (string): IP address to which the APs will send RADIUS accounting
            messages
        secret (string): Shared key used to authenticate messages between the
            APs and RADIUS server

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
        """Constructor for the RadiusAccountingServerModel class"""

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


