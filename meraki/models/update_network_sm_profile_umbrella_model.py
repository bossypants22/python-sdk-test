# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.provider_configuration_model

class UpdateNetworkSmProfileUmbrellaModel(object):

    """Implementation of the 'updateNetworkSmProfileUmbrella' model.

    TODO: type model description here.

    Attributes:
        uses_cert (bool): optional: Whether the certificate should be attached
            to this profile (one of true, false)
        scope (string): optional: A new scope for the profile (one of all,
            none, withAny, withAll, withoutAny, or withoutAll) and a set of
            tags of the devices to be assigned
        app_bundle_identifier (string): optional: The bundle ID of the
            application
        name (string): optional: A new name for the profile
        provider_bundle_identifier (string): optional: The bundle ID of the
            provider
        provider_configuration (list of ProviderConfigurationModel): optional:
            The specific ProviderConfiguration to be passed to the filtering
            framework, in the form of an array of objects (as JSON).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uses_cert":'usesCert',
        "scope":'scope',
        "app_bundle_identifier":'AppBundleIdentifier',
        "name":'name',
        "provider_bundle_identifier":'ProviderBundleIdentifier',
        "provider_configuration":'ProviderConfiguration'
    }

    def __init__(self,
                 uses_cert=None,
                 scope=None,
                 app_bundle_identifier=None,
                 name=None,
                 provider_bundle_identifier=None,
                 provider_configuration=None):
        """Constructor for the UpdateNetworkSmProfileUmbrellaModel class"""

        # Initialize members of the class
        self.uses_cert = uses_cert
        self.scope = scope
        self.app_bundle_identifier = app_bundle_identifier
        self.name = name
        self.provider_bundle_identifier = provider_bundle_identifier
        self.provider_configuration = provider_configuration


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
        uses_cert = dictionary.get('usesCert')
        scope = dictionary.get('scope')
        app_bundle_identifier = dictionary.get('AppBundleIdentifier')
        name = dictionary.get('name')
        provider_bundle_identifier = dictionary.get('ProviderBundleIdentifier')
        provider_configuration = None
        if dictionary.get('ProviderConfiguration') != None:
            provider_configuration = list()
            for structure in dictionary.get('ProviderConfiguration'):
                provider_configuration.append(meraki.models.provider_configuration_model.ProviderConfigurationModel.from_dictionary(structure))

        # Return an object of this model
        return cls(uses_cert,
                   scope,
                   app_bundle_identifier,
                   name,
                   provider_bundle_identifier,
                   provider_configuration)


