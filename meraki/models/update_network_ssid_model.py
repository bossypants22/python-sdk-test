# -*- coding: utf-8 -*-

"""
    meraki

    This file was automatically generated for meraki by APIMATIC v2.0 ( https://apimatic.io ).
"""

import meraki.models.radius_accounting_server_model
import meraki.models.ap_tags_and_vlan_id_model
import meraki.models.radius_server_model

class UpdateNetworkSsidModel(object):

    """Implementation of the 'updateNetworkSsid' model.

    TODO: type model description here.

    Attributes:
        band_selection (BandSelectionEnum): The client-serving radio
            frequencies. ('Dual band operation', '5 GHz band only' or 'Dual
            band operation with Band Steering')
        min_bitrate (float): The minimum bitrate in Mbps. ('1', '2', '5.5',
            '6', '9', '11', '12', '18', '24', '36', '48' or '54')
        radius_accounting_servers (list of RadiusAccountingServerModel): The
            RADIUS accounting 802.1x servers to be used for authentication.
            This param is only valid if the authMode is 'open-with-radius' or
            '8021x-radius' and radiusAccountingEnabled is 'true'
        psk (string): The passkey for the SSID. This param is only valid if
            the authMode is 'psk'
        wpa_encryption_mode (WpaEncryptionModeEnum): The types of WPA
            encryption. ('WPA1 and WPA2' or 'WPA2 only')
        enabled (bool): Whether or not an SSID is enabled
        radius_failover_policy (RadiusFailoverPolicyEnum): This policy
            determines how authentication requests should be handled in the
            event that all of the configured RADIUS servers are unreachable
            ('Deny access' or 'Allow access')
        default_vlan_id (int): The default VLAN ID used for 'all other APs'.
            This param is only valid with 'Bridge mode' and 'Layer 3 roaming'
        splash_page (SplashPageEnum): The type of splash page for the SSID
            ('None', 'Click-through splash page', 'Billing',
            'Password-protected with Meraki RADIUS', 'Password-protected with
            custom RADIUS', 'Password-protected with Active Directory',
            'Password-protected with LDAP', 'SMS authentication', 'Systems
            Manager Sentry', 'Facebook Wi-Fi', 'Google OAuth' or 'Sponsored
            guest'). This attribute is not supported for template children.
        ap_tags_and_vlan_ids (list of ApTagsAndVlanIdModel): The list of tags
            and VLAN IDs used for VLAN tagging. This param is only valid with
            'Bridge mode', 'Layer 3 roaming'
        encryption_mode (EncryptionModeEnum): The psk encryption mode for the
            SSID ('wpa', 'wep' or 'wpa-eap')
        concentrator_network_id (string): The concentrator to use for 'Layer 3
            roaming with a concentrator' or 'VPN'.
        radius_servers (list of RadiusServerModel): The RADIUS 802.1x servers
            to be used for authentication. This param is only valid if the
            authMode is 'open-with-radius' or '8021x-radius'
        radius_coa_enabled (bool): If true, Meraki devices will act as a
            RADIUS Dynamic Authorization Server and will respond to RADIUS
            Change-of-Authorization and Disconnect messages sent by the RADIUS
            server.
        per_client_bandwidth_limit_down (int): The download bandwidth limit in
            Kbps. (0 represents no limit.)
        radius_accounting_enabled (bool): Whether or not RADIUS accounting is
            enabled. This param is only valid if the authMode is
            'open-with-radius' or '8021x-radius'
        vlan_id (int): The VLAN ID used for VLAN tagging. This param is only
            valid with 'Layer 3 roaming with a concentrator' and 'VPN'
        ip_assignment_mode (IpAssignmentModeEnum): The client IP assignment
            mode ('NAT mode', 'Bridge mode', 'Layer 3 roaming', 'Layer 3
            roaming with a concentrator' or 'VPN')
        auth_mode (AuthModeEnum): The association control method for the SSID
            ('open', 'psk', 'open-with-radius', '8021x-meraki' or
            '8021x-radius')
        use_vlan_tagging (bool): Direct trafic to use specific VLANs. This
            param is only valid with 'Bridge mode' and 'Layer 3 roaming'
        per_client_bandwidth_limit_up (int): The upload bandwidth limit in
            Kbps. (0 represents no limit.)
        radius_load_balancing_policy (RadiusLoadBalancingPolicyEnum): This
            policy determines which RADIUS server will be contacted first in
            an authentication attempt and the ordering of any necessary retry
            attempts ('Strict priority order' or 'Round robin')
        name (string): The name of an SSID
        walled_garden_enabled (bool): Allow access to a configurable list of
            IP ranges, which users may access prior to sign-on.
        walled_garden_ranges (string): Specify your walled garden by entering
            space-separated addresses, ranges using CIDR notation, domain
            names, and domain wildcards (e.g. 192.168.1.1/24 192.168.37.10/32
            www.yahoo.com *.google.com). Meraki's splash page is automatically
            included in your walled garden.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "band_selection":'bandSelection',
        "min_bitrate":'minBitrate',
        "radius_accounting_servers":'radiusAccountingServers',
        "psk":'psk',
        "wpa_encryption_mode":'wpaEncryptionMode',
        "enabled":'enabled',
        "radius_failover_policy":'radiusFailoverPolicy',
        "default_vlan_id":'defaultVlanId',
        "splash_page":'splashPage',
        "ap_tags_and_vlan_ids":'apTagsAndVlanIds',
        "encryption_mode":'encryptionMode',
        "concentrator_network_id":'concentratorNetworkId',
        "radius_servers":'radiusServers',
        "radius_coa_enabled":'radiusCoaEnabled',
        "per_client_bandwidth_limit_down":'perClientBandwidthLimitDown',
        "radius_accounting_enabled":'radiusAccountingEnabled',
        "vlan_id":'vlanId',
        "ip_assignment_mode":'ipAssignmentMode',
        "auth_mode":'authMode',
        "use_vlan_tagging":'useVlanTagging',
        "per_client_bandwidth_limit_up":'perClientBandwidthLimitUp',
        "radius_load_balancing_policy":'radiusLoadBalancingPolicy',
        "name":'name',
        "walled_garden_enabled":'walledGardenEnabled',
        "walled_garden_ranges":'walledGardenRanges'
    }

    def __init__(self,
                 band_selection=None,
                 min_bitrate=None,
                 radius_accounting_servers=None,
                 psk=None,
                 wpa_encryption_mode=None,
                 enabled=None,
                 radius_failover_policy=None,
                 default_vlan_id=None,
                 splash_page=None,
                 ap_tags_and_vlan_ids=None,
                 encryption_mode=None,
                 concentrator_network_id=None,
                 radius_servers=None,
                 radius_coa_enabled=None,
                 per_client_bandwidth_limit_down=None,
                 radius_accounting_enabled=None,
                 vlan_id=None,
                 ip_assignment_mode=None,
                 auth_mode=None,
                 use_vlan_tagging=None,
                 per_client_bandwidth_limit_up=None,
                 radius_load_balancing_policy=None,
                 name=None,
                 walled_garden_enabled=None,
                 walled_garden_ranges=None):
        """Constructor for the UpdateNetworkSsidModel class"""

        # Initialize members of the class
        self.band_selection = band_selection
        self.min_bitrate = min_bitrate
        self.radius_accounting_servers = radius_accounting_servers
        self.psk = psk
        self.wpa_encryption_mode = wpa_encryption_mode
        self.enabled = enabled
        self.radius_failover_policy = radius_failover_policy
        self.default_vlan_id = default_vlan_id
        self.splash_page = splash_page
        self.ap_tags_and_vlan_ids = ap_tags_and_vlan_ids
        self.encryption_mode = encryption_mode
        self.concentrator_network_id = concentrator_network_id
        self.radius_servers = radius_servers
        self.radius_coa_enabled = radius_coa_enabled
        self.per_client_bandwidth_limit_down = per_client_bandwidth_limit_down
        self.radius_accounting_enabled = radius_accounting_enabled
        self.vlan_id = vlan_id
        self.ip_assignment_mode = ip_assignment_mode
        self.auth_mode = auth_mode
        self.use_vlan_tagging = use_vlan_tagging
        self.per_client_bandwidth_limit_up = per_client_bandwidth_limit_up
        self.radius_load_balancing_policy = radius_load_balancing_policy
        self.name = name
        self.walled_garden_enabled = walled_garden_enabled
        self.walled_garden_ranges = walled_garden_ranges


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
        band_selection = dictionary.get('bandSelection')
        min_bitrate = dictionary.get('minBitrate')
        radius_accounting_servers = None
        if dictionary.get('radiusAccountingServers') != None:
            radius_accounting_servers = list()
            for structure in dictionary.get('radiusAccountingServers'):
                radius_accounting_servers.append(meraki.models.radius_accounting_server_model.RadiusAccountingServerModel.from_dictionary(structure))
        psk = dictionary.get('psk')
        wpa_encryption_mode = dictionary.get('wpaEncryptionMode')
        enabled = dictionary.get('enabled')
        radius_failover_policy = dictionary.get('radiusFailoverPolicy')
        default_vlan_id = dictionary.get('defaultVlanId')
        splash_page = dictionary.get('splashPage')
        ap_tags_and_vlan_ids = None
        if dictionary.get('apTagsAndVlanIds') != None:
            ap_tags_and_vlan_ids = list()
            for structure in dictionary.get('apTagsAndVlanIds'):
                ap_tags_and_vlan_ids.append(meraki.models.ap_tags_and_vlan_id_model.ApTagsAndVlanIdModel.from_dictionary(structure))
        encryption_mode = dictionary.get('encryptionMode')
        concentrator_network_id = dictionary.get('concentratorNetworkId')
        radius_servers = None
        if dictionary.get('radiusServers') != None:
            radius_servers = list()
            for structure in dictionary.get('radiusServers'):
                radius_servers.append(meraki.models.radius_server_model.RadiusServerModel.from_dictionary(structure))
        radius_coa_enabled = dictionary.get('radiusCoaEnabled')
        per_client_bandwidth_limit_down = dictionary.get('perClientBandwidthLimitDown')
        radius_accounting_enabled = dictionary.get('radiusAccountingEnabled')
        vlan_id = dictionary.get('vlanId')
        ip_assignment_mode = dictionary.get('ipAssignmentMode')
        auth_mode = dictionary.get('authMode')
        use_vlan_tagging = dictionary.get('useVlanTagging')
        per_client_bandwidth_limit_up = dictionary.get('perClientBandwidthLimitUp')
        radius_load_balancing_policy = dictionary.get('radiusLoadBalancingPolicy')
        name = dictionary.get('name')
        walled_garden_enabled = dictionary.get('walledGardenEnabled')
        walled_garden_ranges = dictionary.get('walledGardenRanges')

        # Return an object of this model
        return cls(band_selection,
                   min_bitrate,
                   radius_accounting_servers,
                   psk,
                   wpa_encryption_mode,
                   enabled,
                   radius_failover_policy,
                   default_vlan_id,
                   splash_page,
                   ap_tags_and_vlan_ids,
                   encryption_mode,
                   concentrator_network_id,
                   radius_servers,
                   radius_coa_enabled,
                   per_client_bandwidth_limit_down,
                   radius_accounting_enabled,
                   vlan_id,
                   ip_assignment_mode,
                   auth_mode,
                   use_vlan_tagging,
                   per_client_bandwidth_limit_up,
                   radius_load_balancing_policy,
                   name,
                   walled_garden_enabled,
                   walled_garden_ranges)


