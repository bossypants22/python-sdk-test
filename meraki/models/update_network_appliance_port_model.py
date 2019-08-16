# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkAppliancePortModel(object):

    """Implementation of the 'updateNetworkAppliancePort' model.

    TODO: type model description here.

    Attributes:
        vlan (int): Native VLAN when the port is in Trunk mode. Access VLAN
            when the port is in Access mode.
        drop_untagged_traffic (bool): Trunk port can Drop all Untagged
            traffic. When true, no VLAN is required. Access ports cannot have
            dropUntaggedTraffic set to true.
        access_policy (string): The name of the policy. Only applicable to
            Access ports. Valid values are: 'open', '8021x-radius',
            'mac-radius', 'hybris-radius' for MX64 or Z3 or any MX supporting
            the per port authentication feature. Otherwise, 'open' is the only
            valid value and 'open' is the default value if the field is
            missing.
        mtype (string): The type of the port: 'access' or 'trunk'.
        enabled (bool): The status of the port
        allowed_vlans (string): Comma-delimited list of the VLAN ID's allowed
            on the port, or 'all' to permit all VLAN's on the port.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vlan":'vlan',
        "drop_untagged_traffic":'dropUntaggedTraffic',
        "access_policy":'accessPolicy',
        "mtype":'type',
        "enabled":'enabled',
        "allowed_vlans":'allowedVlans'
    }

    def __init__(self,
                 vlan=None,
                 drop_untagged_traffic=None,
                 access_policy=None,
                 mtype=None,
                 enabled=None,
                 allowed_vlans=None):
        """Constructor for the UpdateNetworkAppliancePortModel class"""

        # Initialize members of the class
        self.vlan = vlan
        self.drop_untagged_traffic = drop_untagged_traffic
        self.access_policy = access_policy
        self.mtype = mtype
        self.enabled = enabled
        self.allowed_vlans = allowed_vlans


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
        vlan = dictionary.get('vlan')
        drop_untagged_traffic = dictionary.get('dropUntaggedTraffic')
        access_policy = dictionary.get('accessPolicy')
        mtype = dictionary.get('type')
        enabled = dictionary.get('enabled')
        allowed_vlans = dictionary.get('allowedVlans')

        # Return an object of this model
        return cls(vlan,
                   drop_untagged_traffic,
                   access_policy,
                   mtype,
                   enabled,
                   allowed_vlans)


