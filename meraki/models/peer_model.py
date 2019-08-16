# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.ipsec_policies_model

class PeerModel(object):

    """Implementation of the 'Peer' model.

    TODO: type model description here.

    Attributes:
        network_tags (list of string): A list of network tags that will
            connect with this peer. Use ['all'] for all networks. Use ['none']
            for no networks. If not included, the default is ['all'].
        ipsec_policies_preset (string): One of the following available
            presets: 'default', 'aws', 'azure'. If this is provided, the
            'ipsecPolicies' parameter is ignored.
        name (string): The name of the VPN peer
        public_ip (string): The public IP of the VPN peer
        private_subnets (list of string): The list of the private subnets of
            the VPN peer
        secret (string): The shared secret with the VPN peer
        ipsec_policies (IpsecPoliciesModel): Custom IPSec policies for the VPN
            peer. If not included and a preset has not been chosen, the
            default preset for IPSec policies will be used.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "public_ip":'publicIp',
        "private_subnets":'privateSubnets',
        "secret":'secret',
        "network_tags":'networkTags',
        "ipsec_policies_preset":'ipsecPoliciesPreset',
        "ipsec_policies":'ipsecPolicies'
    }

    def __init__(self,
                 name=None,
                 public_ip=None,
                 private_subnets=None,
                 secret=None,
                 network_tags=None,
                 ipsec_policies_preset=None,
                 ipsec_policies=None):
        """Constructor for the PeerModel class"""

        # Initialize members of the class
        self.network_tags = network_tags
        self.ipsec_policies_preset = ipsec_policies_preset
        self.name = name
        self.public_ip = public_ip
        self.private_subnets = private_subnets
        self.secret = secret
        self.ipsec_policies = ipsec_policies


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
        public_ip = dictionary.get('publicIp')
        private_subnets = dictionary.get('privateSubnets')
        secret = dictionary.get('secret')
        network_tags = dictionary.get('networkTags')
        ipsec_policies_preset = dictionary.get('ipsecPoliciesPreset')
        ipsec_policies = meraki.models.ipsec_policies_model.IpsecPoliciesModel.from_dictionary(dictionary.get('ipsecPolicies')) if dictionary.get('ipsecPolicies') else None

        # Return an object of this model
        return cls(name,
                   public_ip,
                   private_subnets,
                   secret,
                   network_tags,
                   ipsec_policies_preset,
                   ipsec_policies)


