__all__ = [
    'update_network_syslog_servers_model',
    'server_model',
    'update_network_traffic_analysis_settings_model',
    'custom_pie_chart_item_model',
    'update_organization_vpn_firewall_rules_model',
    'rule_model',
    'create_network_switch_stack_model',
    'update_network_port_forwarding_rules_model',
    'rule1_model',
    'update_network_site_to_site_vpn_model',
    'subnet_model',
    'hub_model',
    'update_network_sm_app_polaris_model',
    'provision_network_clients_model',
    'update_network_switch_port_schedule_model',
    'port_schedule_model',
    'sunday_model',
    'saturday_model',
    'tuesday_model',
    'wednesday_model',
    'thursday_model',
    'friday_model',
    'monday_model',
    'update_organization_saml_role_model',
    'network_model',
    'tag_model',
    'create_network_group_policy_model',
    'vlan_tagging_model',
    'content_filtering_model',
    'blocked_url_patterns_model',
    'allowed_url_patterns_model',
    'blocked_url_categories_model',
    'bonjour_forwarding_model',
    'rule2_model',
    'bandwidth_model',
    'bandwidth_limits_model',
    'scheduling_model',
    'firewall_and_traffic_shaping_model',
    'traffic_shaping_rule_model',
    'per_client_bandwidth_limits_model',
    'bandwidth_limits1_model',
    'definition_model',
    'l3_firewall_rule_model',
    'l7_firewall_rule_model',
    'update_network_one_to_one_nat_rules_model',
    'rule3_model',
    'clone_organization_model',
    'update_network_vlan_model',
    'dhcp_option_model',
    'reserved_ip_range_model',
    'create_organization_action_batch_model',
    'action_model',
    'blink_network_device_leds_model',
    'update_network_ssid_traffic_shaping_model',
    'rule4_model',
    'update_organization_action_batch_model',
    'update_organization_admin_model',
    'network1_model',
    'tag1_model',
    'update_network_l7_firewall_rules_model',
    'rule5_model',
    'add_network_sm_profile_umbrella_model',
    'provider_configuration_model',
    'update_network_sm_profile_umbrella_model',
    'update_network_group_policy_model',
    'update_network_bluetooth_settings_model',
    'update_network_l3_firewall_rules_model',
    'rule7_model',
    'update_network_switch_settings_model',
    'power_exception_model',
    'update_network_security_malware_settings_model',
    'allowed_url_model',
    'allowed_file_model',
    'add_network_sm_profile_clarity_model',
    'vendor_config_model',
    'update_network_sm_profile_clarity_model',
    'update_network_appliance_port_model',
    'update_network_firewalled_service_model',
    'update_network_ssids_plash_settings_model',
    'create_network_http_server_model',
    'update_network_sm_devices_tags_model',
    'update_network_device_model',
    'combine_organization_networks_model',
    'update_network_cellular_firewall_rules_model',
    'update_network_uplink_settings_model',
    'bandwidth_limits5_model',
    'update_network_client_policy_model',
    'claim_network_devices_model',
    'update_organization_snmp_model',
    'update_network_netflow_settings_model',
    'update_device_switch_port_model',
    'create_network_static_route_model',
    'create_network_sm_profile_clarity_model',
    'update_organization_model',
    'create_organization_admin_model',
    'generate_network_camera_snapshot_model',
    'create_network_sm_app_polaris_model',
    'update_network_snmp_settings_model',
    'user_model',
    'create_network_pii_request_model',
    'create_network_vlan_model',
    'update_network_model',
    'create_network_switch_port_schedule_model',
    'claim_organization_model',
    'license_model',
    'update_network_ssid_l3_firewall_rules_model',
    'rule9_model',
    'update_network_device_management_interface_settings_model',
    'wan2_model',
    'wan1_model',
    'update_network_ssid_model',
    'radius_accounting_server_model',
    'ap_tags_and_vlan_id_model',
    'radius_server_model',
    'create_organization_network_model',
    'update_network_vlans_enabled_state_model',
    'create_network_sm_bypass_activation_lock_attempt_model',
    'update_network_one_to_many_nat_rules_model',
    'rule10_model',
    'update_network_security_intrusion_settings_model',
    'protected_networks_model',
    'create_network_http_servers_webhook_test_model',
    'checkin_network_sm_devices_model',
    'add_network_switch_stack_model',
    'update_network_http_server_model',
    'move_network_sm_devices_model',
    'update_network_sm_target_group_model',
    'update_network_sm_device_fields_model',
    'device_fields_model',
    'create_organization_model',
    'update_network_device_wireless_radio_settings_model',
    'create_network_sm_target_group_model',
    'update_network_content_filtering_model',
    'create_organization_saml_role_model',
    'update_network_static_route_model',
    'remove_network_switch_stack_model',
    'update_organization_third_party_vpn_peers_model',
    'peer_model',
    'ipsec_policies_model',
    'bind_network_model',
    'update_network_client_splash_authorization_status_model',
    'ssids_model',
    'wipe_network_sm_device_model',
    'update_organization_security_intrusion_settings_model',
    'whitelisted_rule_model',
    'create_network_sm_profile_umbrella_model',
    'update_network_alert_settings_model',
    'alert_model',
    'default_destinations_model',
    'update_network_traffic_shaping_model',
    'rule11_model',
    'lock_network_sm_devices_model',
    'mode_enum',
    'type_enum',
    'settings_enum',
    'settings1_enum',
    'settings3_enum',
    'settings4_enum',
    'service_enum',
    'settings5_enum',
    'splash_auth_settings_enum',
    'settings6_enum',
    'type1_enum',
    'type2_enum',
    'policy_enum',
    'type4_enum',
    'policy1_enum',
    'power_type_enum',
    'access_enum',
    'v3_auth_mode_enum',
    'v3_priv_mode_enum',
    'access1_enum',
    'type7_enum',
    'mode1_enum',
    'wan_enabled_enum',
    'band_selection_enum',
    'wpa_encryption_mode_enum',
    'radius_failover_policy_enum',
    'splash_page_enum',
    'encryption_mode_enum',
    'ip_assignment_mode_enum',
    'auth_mode_enum',
    'radius_load_balancing_policy_enum',
    'ssid_number_enum',
]