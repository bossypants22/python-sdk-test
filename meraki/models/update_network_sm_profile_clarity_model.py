# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.vendor_config_model

class UpdateNetworkSmProfileClarityModel(object):

    """Implementation of the 'updateNetworkSmProfileClarity' model.

    TODO: type model description here.

    Attributes:
        plugin_bundle_id (string): optional: The new bundle ID of the
            application
        filter_sockets (bool): optional: Whether or not to enable socket
            traffic filtering (one of true, false).
        vendor_config (list of VendorConfigModel): optional: The specific
            VendorConfig to be passed to the filtering framework, in the form
            of an array of objects (as JSON).
        scope (string): optional: A new scope for the profile (one of all,
            none, withAny, withAll, withoutAny, or withoutAll) and a set of
            tags of the devices to be assigned
        name (string): optional: A new name for the profile
        filter_browsers (bool): optional: Whether or not to enable browser
            traffic filtering (one of true, false).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "plugin_bundle_id":'PluginBundleID',
        "filter_sockets":'FilterSockets',
        "vendor_config":'VendorConfig',
        "scope":'scope',
        "name":'name',
        "filter_browsers":'FilterBrowsers'
    }

    def __init__(self,
                 plugin_bundle_id=None,
                 filter_sockets=None,
                 vendor_config=None,
                 scope=None,
                 name=None,
                 filter_browsers=None):
        """Constructor for the UpdateNetworkSmProfileClarityModel class"""

        # Initialize members of the class
        self.plugin_bundle_id = plugin_bundle_id
        self.filter_sockets = filter_sockets
        self.vendor_config = vendor_config
        self.scope = scope
        self.name = name
        self.filter_browsers = filter_browsers


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
        plugin_bundle_id = dictionary.get('PluginBundleID')
        filter_sockets = dictionary.get('FilterSockets')
        vendor_config = None
        if dictionary.get('VendorConfig') != None:
            vendor_config = list()
            for structure in dictionary.get('VendorConfig'):
                vendor_config.append(meraki.models.vendor_config_model.VendorConfigModel.from_dictionary(structure))
        scope = dictionary.get('scope')
        name = dictionary.get('name')
        filter_browsers = dictionary.get('FilterBrowsers')

        # Return an object of this model
        return cls(plugin_bundle_id,
                   filter_sockets,
                   vendor_config,
                   scope,
                   name,
                   filter_browsers)


