# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class UpdateNetworkSmAppPolarisModel(object):

    """Implementation of the 'updateNetworkSmAppPolaris' model.

    TODO: type model description here.

    Attributes:
        uses_vpp (bool): optional: Whether or not the app should use VPP by
            device assignment (one of true or false)
        prevent_auto_install (bool): optional: Whether or not SM should
            auto-install this app (one of true or false)
        scope (string): optional: The scope (one of all, none, automatic,
            withAny, withAll, withoutAny, or withoutAll) and a set of tags of
            the devices to be assigned

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uses_vpp":'usesVPP',
        "prevent_auto_install":'preventAutoInstall',
        "scope":'scope'
    }

    def __init__(self,
                 uses_vpp=None,
                 prevent_auto_install=None,
                 scope=None):
        """Constructor for the UpdateNetworkSmAppPolarisModel class"""

        # Initialize members of the class
        self.uses_vpp = uses_vpp
        self.prevent_auto_install = prevent_auto_install
        self.scope = scope


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
        uses_vpp = dictionary.get('usesVPP')
        prevent_auto_install = dictionary.get('preventAutoInstall')
        scope = dictionary.get('scope')

        # Return an object of this model
        return cls(uses_vpp,
                   prevent_auto_install,
                   scope)


