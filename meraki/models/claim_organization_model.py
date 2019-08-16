# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.license_model

class ClaimOrganizationModel(object):

    """Implementation of the 'claimOrganization' model.

    TODO: type model description here.

    Attributes:
        serials (list of string): The serials of the devices that should be
            claimed
        licenses (list of LicenseModel): The licenses that should be claimed
        orders (list of string): The numbers of the orders that should be
            claimed

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "serials":'serials',
        "licenses":'licenses',
        "orders":'orders'
    }

    def __init__(self,
                 serials=None,
                 licenses=None,
                 orders=None):
        """Constructor for the ClaimOrganizationModel class"""

        # Initialize members of the class
        self.serials = serials
        self.licenses = licenses
        self.orders = orders


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
        serials = dictionary.get('serials')
        licenses = None
        if dictionary.get('licenses') != None:
            licenses = list()
            for structure in dictionary.get('licenses'):
                licenses.append(meraki.models.license_model.LicenseModel.from_dictionary(structure))
        orders = dictionary.get('orders')

        # Return an object of this model
        return cls(serials,
                   licenses,
                   orders)


