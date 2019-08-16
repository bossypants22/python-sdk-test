# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.vendor_config_model

class CreateNetworkSmProfileClarityModel(object):

    """Implementation of the 'createNetworkSmProfileClarity' model.

    TODO: type model description here.

    Attributes:
        plugin_bundle_id (string): The bundle ID of the application, defaults
            to com.cisco.ciscosecurity.app
        filter_sockets (bool): Whether or not to enable socket traffic
            filtering (one of true, false). Default true.
        vendor_config (list of VendorConfigModel): The specific VendorConfig
            to be passed to the filtering framework, in the form of an array
            of objects (as JSON).
        scope (string): The scope (one of all, none, withAny, withAll,
            withoutAny, or withoutAll) and a set of tags of the devices to be
            assigned
        name (string): The name to be given to the new profile
        filter_browsers (bool): Whether or not to enable browser traffic
            filtering (one of true, false). Default true.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "vendor_config":'VendorConfig',
        "scope":'scope',
        "name":'name',
        "plugin_bundle_id":'PluginBundleID',
        "filter_sockets":'FilterSockets',
        "filter_browsers":'FilterBrowsers'
    }

    def __init__(self,
                 vendor_config=None,
                 scope=None,
                 name=None,
                 plugin_bundle_id=None,
                 filter_sockets=None,
                 filter_browsers=None):
        """Constructor for the CreateNetworkSmProfileClarityModel class"""

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
        vendor_config = None
        if dictionary.get('VendorConfig') != None:
            vendor_config = list()
            for structure in dictionary.get('VendorConfig'):
                vendor_config.append(meraki.models.vendor_config_model.VendorConfigModel.from_dictionary(structure))
        scope = dictionary.get('scope')
        name = dictionary.get('name')
        plugin_bundle_id = dictionary.get('PluginBundleID')
        filter_sockets = dictionary.get('FilterSockets')
        filter_browsers = dictionary.get('FilterBrowsers')

        # Return an object of this model
        return cls(vendor_config,
                   scope,
                   name,
                   plugin_bundle_id,
                   filter_sockets,
                   filter_browsers)


