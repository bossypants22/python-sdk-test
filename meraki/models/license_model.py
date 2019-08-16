# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class LicenseModel(object):

    """Implementation of the 'License' model.

    TODO: type model description here.

    Attributes:
        mode (Mode1Enum): Either 'renew' or 'addDevices'. 'addDevices' will
            increase the license limit, while 'renew' will extend the amount
            of time until expiration. Please see <a target='_blank'
            href='https://documentation.meraki.com/zGeneral_Administration/Lice
            nsing/Adding_an_Enterprise_license_to_an_existing_Dashboard_account
            '>this article</a> for more information.
        key (string): The key of the license

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mode":'mode',
        "key":'key'
    }

    def __init__(self,
                 mode=None,
                 key=None):
        """Constructor for the LicenseModel class"""

        # Initialize members of the class
        self.mode = mode
        self.key = key


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
        key = dictionary.get('key')

        # Return an object of this model
        return cls(mode,
                   key)


