# shodan_data.py

SHODAN_FINDINGS = {

    # Remote access exposure
    "vpn_detected": True,

    "rdp_exposed": True,

    "ssh_exposed": False,

    "telnet_exposed": False,

    # Remote access technologies
    "teamviewer_detected": True,

    "fortinet_detected": True,

    "anydesk_detected": False,

    "citrix_detected": False,

    # Web exposure
    "http_exposed": True,

    "https_exposed": True,

    "admin_portal_detected": True,

    # Security posture indicators
    "weak_tls_detected": False,

    "self_signed_certificate": True,

    "default_login_page_detected": False,

    # Infrastructure indicators
    "windows_host_detected": True,

    "active_directory_exposed": False,

    # Network visibility
    "open_ports": [
        80,
        443,
        3389
    ],

    # Threat indicators
    "known_vulnerabilities_detected": False,

    "cve_matches": [],

    # Metadata
    "last_scan_source": "shodan",

    "last_updated": "2026-05-13T12:00:00Z"
}
