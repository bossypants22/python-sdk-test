# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.network_model
import meraki.models.tag_model

class CreateOrganizationSamlRoleModel(object):

    """Implementation of the 'createOrganizationSamlRole' model.

    TODO: type model description here.

    Attributes:
        role (string): The role of the SAML administrator
        org_access (string): The privilege of the SAML administrator on the
            organization
        networks (list of NetworkModel): The list of networks that the SAML
            administrator has privileges on
        tags (list of TagModel): The list of tags that the SAML administrator
            has privileges on

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "role":'role',
        "org_access":'orgAccess',
        "networks":'networks',
        "tags":'tags'
    }

    def __init__(self,
                 role=None,
                 org_access=None,
                 networks=None,
                 tags=None):
        """Constructor for the CreateOrganizationSamlRoleModel class"""

        # Initialize members of the class
        self.role = role
        self.org_access = org_access
        self.networks = networks
        self.tags = tags


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
        role = dictionary.get('role')
        org_access = dictionary.get('orgAccess')
        networks = None
        if dictionary.get('networks') != None:
            networks = list()
            for structure in dictionary.get('networks'):
                networks.append(meraki.models.network_model.NetworkModel.from_dictionary(structure))
        tags = None
        if dictionary.get('tags') != None:
            tags = list()
            for structure in dictionary.get('tags'):
                tags.append(meraki.models.tag_model.TagModel.from_dictionary(structure))

        # Return an object of this model
        return cls(role,
                   org_access,
                   networks,
                   tags)


