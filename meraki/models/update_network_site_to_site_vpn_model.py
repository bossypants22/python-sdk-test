# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.subnet_model
import meraki.models.hub_model

class UpdateNetworkSiteToSiteVpnModel(object):

    """Implementation of the 'updateNetworkSiteToSiteVpn' model.

    TODO: type model description here.

    Attributes:
        mode (string): The site-to-site VPN mode: hub, spoke, or none
        subnets (list of SubnetModel): The list of subnets and their VPN
            presence.
        hubs (list of HubModel): The list of VPN hubs, in order of preference.
            In spoke mode, at least 1 hub is required.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mode":'mode',
        "subnets":'subnets',
        "hubs":'hubs'
    }

    def __init__(self,
                 mode=None,
                 subnets=None,
                 hubs=None):
        """Constructor for the UpdateNetworkSiteToSiteVpnModel class"""

        # Initialize members of the class
        self.mode = mode
        self.subnets = subnets
        self.hubs = hubs


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
        mode = dictionary.get('mode')
        subnets = None
        if dictionary.get('subnets') != None:
            subnets = list()
            for structure in dictionary.get('subnets'):
                subnets.append(meraki.models.subnet_model.SubnetModel.from_dictionary(structure))
        hubs = None
        if dictionary.get('hubs') != None:
            hubs = list()
            for structure in dictionary.get('hubs'):
                hubs.append(meraki.models.hub_model.HubModel.from_dictionary(structure))

        # Return an object of this model
        return cls(mode,
                   subnets,
                   hubs)


