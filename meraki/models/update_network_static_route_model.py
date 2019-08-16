# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkStaticRouteModel(object):

    """Implementation of the 'updateNetworkStaticRoute' model.

    TODO: type model description here.

    Attributes:
        subnet (string): The subnet of the static route
        name (string): The name of the static route
        gateway_ip (string): The gateway IP (next hop) of the static route
        enabled (string): The enabled state of the static route
        reserved_ip_ranges (string): The DHCP reserved IP ranges on the static
            route
        fixed_ip_assignments (string): The DHCP fixed IP assignments on the
            static route

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "subnet":'subnet',
        "name":'name',
        "gateway_ip":'gatewayIp',
        "enabled":'enabled',
        "reserved_ip_ranges":'reservedIpRanges',
        "fixed_ip_assignments":'fixedIpAssignments'
    }

    def __init__(self,
                 subnet=None,
                 name=None,
                 gateway_ip=None,
                 enabled=None,
                 reserved_ip_ranges=None,
                 fixed_ip_assignments=None):
        """Constructor for the UpdateNetworkStaticRouteModel class"""

        # Initialize members of the class
        self.subnet = subnet
        self.name = name
        self.gateway_ip = gateway_ip
        self.enabled = enabled
        self.reserved_ip_ranges = reserved_ip_ranges
        self.fixed_ip_assignments = fixed_ip_assignments


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
        enabled = dictionary.get('enabled')
        reserved_ip_ranges = dictionary.get('reservedIpRanges')
        fixed_ip_assignments = dictionary.get('fixedIpAssignments')

        # Return an object of this model
        return cls(subnet,
                   name,
                   gateway_ip,
                   enabled,
                   reserved_ip_ranges,
                   fixed_ip_assignments)


