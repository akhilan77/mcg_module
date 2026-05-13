# yacht_context.py

YACHT_CONTEXT = {

    # Vessel information
    "vessel_type": "superyacht",

    "loa": 90,

    # Connectivity
    "guest_wifi": True,

    "starlink": True,

    # Operational profile
    "remote_vendor_access": True,

    "satellite_comms": True,

    "internet_exposed_services": True,

    # Network architecture
    "segmented_networks": False,

    "bridge_network_separate": False,

    # Crew environment
    "crew_size": 35,

    "guest_capacity": 12,

    "crew_byod_allowed": True,

    # Security posture
    "vpn_enabled": True,

    "mfa_enabled": False,

    "edr_installed": False,

    # Compliance / governance
    "incident_response_plan": False,

    "security_awareness_training": False,

    # Technology stack hints
    "windows_systems": True,

    "active_directory_present": True,

    "vendor_maintenance_tools": [
        "TeamViewer",
        "Fortinet VPN"
    ],

    # Metadata
    "region": "Mediterranean",

    "assessment_scope": "full_vessel",

    "criticality": "high"
}
