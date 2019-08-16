# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkVlanModel(object):

    """Implementation of the 'createNetworkVlan' model.

    TODO: type model description here.

    Attributes:
        subnet (string): The subnet of the VLAN
        name (string): The name of the new VLAN
        id (string): The VLAN ID of the new VLAN (must be between 1 and 4094)
        appliance_ip (string): The local IP of the appliance on the VLAN

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subnet":'subnet',
        "name":'name',
        "id":'id',
        "appliance_ip":'applianceIp'
    }

    def __init__(self,
                 subnet=None,
                 name=None,
                 id=None,
                 appliance_ip=None):
        """Constructor for the CreateNetworkVlanModel class"""

        # Initialize members of the class
        self.subnet = subnet
        self.name = name
        self.id = id
        self.appliance_ip = appliance_ip


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
        id = dictionary.get('id')
        appliance_ip = dictionary.get('applianceIp')

        # Return an object of this model
        return cls(subnet,
                   name,
                   id,
                   appliance_ip)


