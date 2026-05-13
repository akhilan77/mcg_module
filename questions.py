# questions.py

QUESTIONS = [

    # -------------------------------------------------
    # Vendor Remote Access
    # -------------------------------------------------

    {
        "id": "vendor_access",

        "text":
        "Do vendors remotely access yacht systems?",

        "domain":
        "vendor",

        "severity":
        "high",

        "tags": [
            "vendor",
            "remote_access"
        ],

        "base_weight":
        30,

        "options": [
            "yes",
            "no"
        ],

        "flags": [
            {
                "answer": "yes",
                "flag": "vendor_remote_access"
            }
        ],

        "mitre_attack": [
            "T1133"
        ],

        "compliance": [
            "IMO 2021",
            "NIST AC-17"
        ],

        "remediation":
        "Restrict and monitor all vendor remote access.",

        "information_gain":
        20
    },

    # -------------------------------------------------
    # Vendor MFA
    # -------------------------------------------------

    {
        "id": "vendor_mfa",

        "text":
        "Do vendors use MFA for remote access?",

        "domain":
        "authentication",

        "severity":
        "critical",

        "tags": [
            "authentication",
            "vendor",
            "remote_access"
        ],

        "base_weight":
        50,

        "options": [
            "yes",
            "no"
        ],

        "conditions": [
            {
                "question":
                "vendor_access",

                "operator":
                "equals",

                "value":
                "yes"
            }
        ],

        "flags": [
            {
                "answer":
                "no",

                "flag":
                "weak_authentication"
            }
        ],

        "score_modifiers": [

            {
                "if_flag":
                "vendor_remote_access",

                "boost":
                40
            },

            {
                "if_osint":
                "rdp_exposed",

                "boost":
                20
            }
        ],

        "mitre_attack": [
            "T1078"
        ],

        "compliance": [
            "NIST IA-2"
        ],

        "remediation":
        "Enforce MFA for all vendor remote access.",

        "information_gain":
        30
    },

    # -------------------------------------------------
    # RDP Exposure
    # -------------------------------------------------

    {
        "id": "rdp_access",

        "text":
        "Why is RDP exposed publicly?",

        "domain":
        "remote_access",

        "severity":
        "critical",

        "tags": [
            "rdp",
            "remote_access"
        ],

        "base_weight":
        70,

        "options": [
            "intentional",
            "temporary",
            "unknown"
        ],

        "osint_required":
        "rdp_exposed",

        "flags": [
            {
                "answer":
                "unknown",

                "flag":
                "critical_remote_access_risk"
            }
        ],

        "mitre_attack": [
            "T1021"
        ],

        "compliance": [
            "CIS Control 12"
        ],

        "remediation":
        "Remove public RDP exposure or restrict via VPN.",

        "information_gain":
        35
    },

    # -------------------------------------------------
    # Shared Accounts
    # -------------------------------------------------

    {
        "id": "shared_accounts",

        "text":
        "Are shared administrator accounts used onboard?",

        "domain":
        "identity_access",

        "severity":
        "high",

        "tags": [
            "identity",
            "credentials"
        ],

        "base_weight":
        60,

        "options": [
            "yes",
            "no",
            "sometimes"
        ],

        "flags": [

            {
                "answer":
                "yes",

                "flag":
                "credential_sharing"
            },

            {
                "answer":
                "sometimes",

                "flag":
                "credential_sharing"
            }
        ],

        "mitre_attack": [
            "T1078"
        ],

        "compliance": [
            "NIST AC-2"
        ],

        "remediation":
        "Implement unique administrator accounts.",

        "information_gain":
        25
    },

    # -------------------------------------------------
    # Incident Response
    # -------------------------------------------------

    {
        "id": "incident_response",

        "text":
        "Is there a documented cyber incident response process onboard?",

        "domain":
        "incident_response",

        "severity":
        "high",

        "tags": [
            "incident_response"
        ],

        "base_weight":
        65,

        "options": [
            "yes",
            "no",
            "partial"
        ],

        "flags": [
            {
                "answer":
                "no",

                "flag":
                "no_incident_response"
            }
        ],

        "compliance": [
            "NIST IR-1"
        ],

        "remediation":
        "Develop and document a cyber incident response plan.",

        "information_gain":
        20
    },

    # -------------------------------------------------
    # VPN Usage
    # -------------------------------------------------

    {
        "id": "vpn_usage",

        "text":
        "Is VPN used for remote yacht access?",

        "domain":
        "remote_access",

        "severity":
        "high",

        "tags": [
            "vpn",
            "remote_access"
        ],

        "base_weight":
        45,

        "options": [
            "yes",
            "no",
            "unknown"
        ],

        "flags": [
            {
                "answer":
                "no",

                "flag":
                "no_secure_remote_access"
            }
        ],

        "mitre_attack": [
            "T1133"
        ],

        "compliance": [
            "NIST SC-7"
        ],

        "remediation":
        "Require VPN for all remote administrative access.",

        "information_gain":
        20
    },

    # -------------------------------------------------
    # VPN MFA
    # -------------------------------------------------

    {
        "id": "vpn_mfa",

        "text":
        "Is MFA enforced on VPN access?",

        "domain":
        "authentication",

        "severity":
        "critical",

        "tags": [
            "vpn",
            "authentication"
        ],

        "base_weight":
        60,

        "options": [
            "yes",
            "no",
            "partial"
        ],

        "conditions": [
            {
                "question":
                "vpn_usage",

                "operator":
                "equals",

                "value":
                "yes"
            }
        ],

        "flags": [
            {
                "answer":
                "no",

                "flag":
                "vpn_weak_authentication"
            }
        ],

        "score_modifiers": [
            {
                "if_flag":
                "critical_remote_access_risk",

                "boost":
                50
            }
        ],

        "mitre_attack": [
            "T1078"
        ],

        "compliance": [
            "NIST IA-2"
        ],

        "remediation":
        "Enable MFA for all VPN users.",

        "information_gain":
        35
    },

    # -------------------------------------------------
    # Crew Devices
    # -------------------------------------------------

    {
        "id": "crew_personal_devices",

        "text":
        "Are crew personal devices allowed on internal yacht networks?",

        "domain":
        "endpoint_security",

        "severity":
        "medium",

        "tags": [
            "byod",
            "endpoint"
        ],

        "base_weight":
        40,

        "options": [
            "yes",
            "no",
            "guest_only"
        ],

        "flags": [
            {
                "answer":
                "yes",

                "flag":
                "unmanaged_devices"
            }
        ],

        "compliance": [
            "CIS Control 4"
        ],

        "remediation":
        "Restrict personal devices from operational networks.",

        "information_gain":
        15
    },

    # -------------------------------------------------
    # Network Segmentation
    # -------------------------------------------------

    {
        "id": "bridge_network_isolation",

        "text":
        "Is the bridge/navigation network isolated from guest networks?",

        "domain":
        "network_segmentation",

        "severity":
        "critical",

        "tags": [
            "segmentation",
            "bridge_systems"
        ],

        "base_weight":
        75,

        "options": [
            "yes",
            "no",
            "partially"
        ],

        "flags": [
            {
                "answer":
                "no",

                "flag":
                "critical_network_segmentation_risk"
            }
        ],

        "compliance": [
            "IEC 62443"
        ],

        "remediation":
        "Implement strict network segmentation for bridge systems.",

        "information_gain":
        40
    },

    # -------------------------------------------------
    # EDR/XDR
    # -------------------------------------------------

    {
        "id": "edr_solution",

        "text":
        "Is an EDR/XDR security solution deployed onboard?",

        "domain":
        "endpoint_security",

        "severity":
        "high",

        "tags": [
            "edr",
            "endpoint"
        ],

        "base_weight":
        50,

        "options": [
            "yes",
            "no",
            "unknown"
        ],

        "flags": [
            {
                "answer":
                "no",

                "flag":
                "no_endpoint_detection"
            }
        ],

        "compliance": [
            "NIST SI-4"
        ],

        "remediation":
        "Deploy endpoint detection and response tooling.",

        "information_gain":
        20
    }

]
