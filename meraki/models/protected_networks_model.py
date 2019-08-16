# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class ProtectedNetworksModel(object):

    """Implementation of the 'ProtectedNetworks' model.

    Set the included/excluded networks from the intrusion engine (optional -
    omitting will leave current config unchanged). This is available only in
    'passthrough' mode

    Attributes:
        included_cidr (list of string): list of IP addresses or subnets being
            protected (required if 'useDefault' is false)
        use_default (bool): true/false whether to use special IPv4 addresses:
            https://tools.ietf.org/html/rfc5735 (required). Default value is
            true if none currently saved
        excluded_cidr (list of string): list of IP addresses or subnets being
            excluded from protection (required if 'useDefault' is false)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "included_cidr":'includedCidr',
        "use_default":'useDefault',
        "excluded_cidr":'excludedCidr'
    }

    def __init__(self,
                 included_cidr=None,
                 use_default=None,
                 excluded_cidr=None):
        """Constructor for the ProtectedNetworksModel class"""

        # Initialize members of the class
        self.included_cidr = included_cidr
        self.use_default = use_default
        self.excluded_cidr = excluded_cidr


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
        included_cidr = dictionary.get('includedCidr')
        use_default = dictionary.get('useDefault')
        excluded_cidr = dictionary.get('excludedCidr')

        # Return an object of this model
        return cls(included_cidr,
                   use_default,
                   excluded_cidr)


