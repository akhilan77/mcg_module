# rules.py

FLAG_RULES = {

    # Vendor remote access
    ("vendor_access", "yes"):
        "vendor_remote_access",

    # Weak MFA on vendor access
    ("vendor_mfa", "no"):
        "weak_authentication",

    # Public RDP risk
    ("rdp_access", "unknown"):
        "critical_remote_access_risk",

    # Shared admin accounts
    ("shared_accounts", "yes"):
        "credential_sharing",

    ("shared_accounts", "sometimes"):
        "credential_sharing",

    # Incident response weakness
    ("incident_response", "no"):
        "no_incident_response",

    # No secure remote access
    ("vpn_usage", "no"):
        "no_secure_remote_access",

    # Weak VPN MFA
    ("vpn_mfa", "no"):
        "vpn_weak_authentication",

    # Unmanaged devices
    ("crew_personal_devices", "yes"):
        "unmanaged_devices",

    # Critical segmentation failure
    ("bridge_network_isolation", "no"):
        "critical_network_segmentation_risk",

    # No endpoint detection
    ("edr_solution", "no"):
        "no_endpoint_detection"
}


# Optional advanced correlations

CORRELATION_RULES = [

    {

        "if_flags": [
            "vendor_remote_access",
            "weak_authentication"
        ],

        "trigger":
            "high_remote_compromise_probability"
    },

    {

        "if_flags": [
            "critical_remote_access_risk",
            "vpn_weak_authentication"
        ],

        "trigger":
            "internet_facing_attack_path"
    },

    {

        "if_flags": [
            "credential_sharing",
            "unmanaged_devices"
        ],

        "trigger":
            "high_lateral_movement_risk"
    },

    {

        "if_flags": [
            "critical_network_segmentation_risk",
            "no_endpoint_detection"
        ],

        "trigger":
            "critical_operational_technology_exposure"
    }
]
