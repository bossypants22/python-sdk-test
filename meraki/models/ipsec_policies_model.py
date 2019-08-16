# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""


class IpsecPoliciesModel(object):

    """Implementation of the 'IpsecPolicies' model.

    Custom IPSec policies for the VPN peer. If not included and a preset has
    not been chosen, the default preset for IPSec policies will be used.

    Attributes:
        ike_auth_algo (list of string): This is the authentication algorithm
            to be used in Phase 1. The value should be an array with one of
            the following algorithms: 'sha1', 'md5'
        ike_diffie_hellman_group (list of string): This is the Diffie-Hellman
            group to be used in Phase 1. The value should be an array with one
            of the following algorithms: 'group5', 'group2', 'group1'
        child_lifetime (int): The lifetime of the Phase 2 SA in seconds.
        child_cipher_algo (list of string): This is the cipher algorithms to
            be used in Phase 2. The value should be an array with one or more
            of the following algorithms: 'aes256', 'aes192', 'aes128',
            'tripledes', 'des', 'null'
        ike_lifetime (int): The lifetime of the Phase 1 SA in seconds.
        ike_cipher_algo (list of string): This is the cipher algorithm to be
            used in Phase 1. The value should be an array with one of the
            following algorithms: 'aes256', 'aes192', 'aes128', 'tripledes',
            'des'
        child_auth_algo (list of string): This is the authentication
            algorithms to be used in Phase 2. The value should be an array
            with one of the following algorithms: 'sha1', 'md5'
        child_pfs_group (list of string): This is the Diffie-Hellman group to
            be used for Perfect Forward Secrecy in Phase 2. The value should
            be an array with one of the following values: 'disabled',
            'group5', 'group2', 'group1'

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ike_auth_algo":'ikeAuthAlgo',
        "ike_diffie_hellman_group":'ikeDiffieHellmanGroup',
        "child_lifetime":'childLifetime',
        "child_cipher_algo":'childCipherAlgo',
        "ike_lifetime":'ikeLifetime',
        "ike_cipher_algo":'ikeCipherAlgo',
        "child_auth_algo":'childAuthAlgo',
        "child_pfs_group":'childPfsGroup'
    }

    def __init__(self,
                 ike_auth_algo=None,
                 ike_diffie_hellman_group=None,
                 child_lifetime=None,
                 child_cipher_algo=None,
                 ike_lifetime=None,
                 ike_cipher_algo=None,
                 child_auth_algo=None,
                 child_pfs_group=None):
        """Constructor for the IpsecPoliciesModel class"""

        # Initialize members of the class
        self.ike_auth_algo = ike_auth_algo
        self.ike_diffie_hellman_group = ike_diffie_hellman_group
        self.child_lifetime = child_lifetime
        self.child_cipher_algo = child_cipher_algo
        self.ike_lifetime = ike_lifetime
        self.ike_cipher_algo = ike_cipher_algo
        self.child_auth_algo = child_auth_algo
        self.child_pfs_group = child_pfs_group


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
        ike_auth_algo = dictionary.get('ikeAuthAlgo')
        ike_diffie_hellman_group = dictionary.get('ikeDiffieHellmanGroup')
        child_lifetime = dictionary.get('childLifetime')
        child_cipher_algo = dictionary.get('childCipherAlgo')
        ike_lifetime = dictionary.get('ikeLifetime')
        ike_cipher_algo = dictionary.get('ikeCipherAlgo')
        child_auth_algo = dictionary.get('childAuthAlgo')
        child_pfs_group = dictionary.get('childPfsGroup')

        # Return an object of this model
        return cls(ike_auth_algo,
                   ike_diffie_hellman_group,
                   child_lifetime,
                   child_cipher_algo,
                   ike_lifetime,
                   ike_cipher_algo,
                   child_auth_algo,
                   child_pfs_group)


