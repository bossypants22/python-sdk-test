# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.network1_model
import meraki.models.tag1_model

class UpdateOrganizationAdminModel(object):

    """Implementation of the 'updateOrganizationAdmin' model.

    TODO: type model description here.

    Attributes:
        name (string): The name of the dashboard administrator
        org_access (string): The privilege of the dashboard administrator on
            the organization (full, read-only, none)
        networks (list of Network1Model): The list of networks that the
            dashboard administrator has privileges on
        email (string): The email of the dashboard administrator. This
            attribute can not be updated.
        tags (list of Tag1Model): The list of tags that the dashboard
            administrator has privileges on

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name":'name',
        "org_access":'orgAccess',
        "networks":'networks',
        "email":'email',
        "tags":'tags'
    }

    def __init__(self,
                 name=None,
                 org_access=None,
                 networks=None,
                 email=None,
                 tags=None):
        """Constructor for the UpdateOrganizationAdminModel class"""

        # Initialize members of the class
        self.name = name
        self.org_access = org_access
        self.networks = networks
        self.email = email
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
        name = dictionary.get('name')
        org_access = dictionary.get('orgAccess')
        networks = None
        if dictionary.get('networks') != None:
            networks = list()
            for structure in dictionary.get('networks'):
                networks.append(meraki.models.network1_model.Network1Model.from_dictionary(structure))
        email = dictionary.get('email')
        tags = None
        if dictionary.get('tags') != None:
            tags = list()
            for structure in dictionary.get('tags'):
                tags.append(meraki.models.tag1_model.Tag1Model.from_dictionary(structure))

        # Return an object of this model
        return cls(name,
                   org_access,
                   networks,
                   email,
                   tags)


