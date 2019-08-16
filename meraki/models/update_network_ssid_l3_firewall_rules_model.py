# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.rule9_model

class UpdateNetworkSsidL3FirewallRulesModel(object):

    """Implementation of the 'updateNetworkSsidL3FirewallRules' model.

    TODO: type model description here.

    Attributes:
        allow_lan_access (bool): Allow wireless client access to local LAN
            (boolean value - true allows access and false denies access)
            (optional)
        rules (list of Rule9Model): An ordered array of the firewall rules for
            this SSID (not including the local LAN access rule or the default
            rule)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "allow_lan_access":'allowLanAccess',
        "rules":'rules'
    }

    def __init__(self,
                 allow_lan_access=None,
                 rules=None):
        """Constructor for the UpdateNetworkSsidL3FirewallRulesModel class"""

        # Initialize members of the class
        self.allow_lan_access = allow_lan_access
        self.rules = rules


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
        allow_lan_access = dictionary.get('allowLanAccess')
        rules = None
        if dictionary.get('rules') != None:
            rules = list()
            for structure in dictionary.get('rules'):
                rules.append(meraki.models.rule9_model.Rule9Model.from_dictionary(structure))

        # Return an object of this model
        return cls(allow_lan_access,
                   rules)


