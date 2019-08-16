# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkHttpServerModel(object):

    """Implementation of the 'updateNetworkHttpServer' model.

    TODO: type model description here.

    Attributes:
        name (string): A name for easy reference to the HTTP server
        shared_secret (string): A shared secret that will be included in POSTs
            sent to the HTTP server. This secret can be used to verify that
            the request was sent by Meraki.
        url (string): The URL of the HTTP server

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "shared_secret":'sharedSecret',
        "url":'url'
    }

    def __init__(self,
                 name=None,
                 shared_secret=None,
                 url=None):
        """Constructor for the UpdateNetworkHttpServerModel class"""

        # Initialize members of the class
        self.name = name
        self.shared_secret = shared_secret
        self.url = url


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
        shared_secret = dictionary.get('sharedSecret')
        url = dictionary.get('url')

        # Return an object of this model
        return cls(name,
                   shared_secret,
                   url)


