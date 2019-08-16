# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class CreateNetworkSmAppPolarisModel(object):

    """Implementation of the 'createNetworkSmAppPolaris' model.

    TODO: type model description here.

    Attributes:
        uses_vpp (bool): (optional) Whether or not the app should use VPP by
            device assignment (one of true or false). False by default.
        prevent_auto_install (bool): (optional) Whether or not SM should
            auto-install this app (one of true or false). False by default.
        manifest_url (string): The manifest URL of the Polaris app (one of
            manifestUrl and bundleId must be provided)
        scope (string): The scope (one of all, none, automatic, withAny,
            withAll, withoutAny, or withoutAll) and a set of tags of the
            devices to be assigned
        bundle_id (string): The bundleId of the Polaris app (one of
            manifestUrl and bundleId must be provided)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "scope":'scope',
        "uses_vpp":'usesVPP',
        "prevent_auto_install":'preventAutoInstall',
        "manifest_url":'manifestUrl',
        "bundle_id":'bundleId'
    }

    def __init__(self,
                 scope=None,
                 uses_vpp=None,
                 prevent_auto_install=None,
                 manifest_url=None,
                 bundle_id=None):
        """Constructor for the CreateNetworkSmAppPolarisModel class"""

        # Initialize members of the class
        self.uses_vpp = uses_vpp
        self.prevent_auto_install = prevent_auto_install
        self.manifest_url = manifest_url
        self.scope = scope
        self.bundle_id = bundle_id


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
        scope = dictionary.get('scope')
        uses_vpp = dictionary.get('usesVPP')
        prevent_auto_install = dictionary.get('preventAutoInstall')
        manifest_url = dictionary.get('manifestUrl')
        bundle_id = dictionary.get('bundleId')

        # Return an object of this model
        return cls(scope,
                   uses_vpp,
                   prevent_auto_install,
                   manifest_url,
                   bundle_id)


