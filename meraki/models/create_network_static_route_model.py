# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkStaticRouteModel(object):

    """Implementation of the 'createNetworkStaticRoute' model.

    TODO: type model description here.

    Attributes:
        subnet (string): The subnet of the static route
        name (string): The name of the new static route
        gateway_ip (string): The gateway IP (next hop) of the static route

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subnet":'subnet',
        "name":'name',
        "gateway_ip":'gatewayIp'
    }

    def __init__(self,
                 subnet=None,
                 name=None,
                 gateway_ip=None):
        """Constructor for the CreateNetworkStaticRouteModel class"""

        # Initialize members of the class
        self.subnet = subnet
        self.name = name
        self.gateway_ip = gateway_ip


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
        subnet = dictionary.get('subnet')
        name = dictionary.get('name')
        gateway_ip = dictionary.get('gatewayIp')

        # Return an object of this model
        return cls(subnet,
                   name,
                   gateway_ip)


