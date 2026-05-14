# imo_enrichment.py

"""
IMO Enrichment Engine

Purpose:
- Build vessel profile from IMO
- Generate OSINT context
- Pre-seed risk flags
- Provide vessel-aware intelligence
"""


# ----------------------------------------
# Simulated vessel database
# Replace later with real APIs
# ----------------------------------------

VESSEL_DATABASE = {

    "9876543": {

        "vessel_type":
            "charter_yacht",

        "loa":
            95,

        "build_year":
            2018,

        "flag_state":
            "Cayman Islands",

        "operator":
            "Oceanic Charter Group"
    },

    "1234567": {

        "vessel_type":
            "sailing_yacht",

        "loa":
            42,

        "build_year":
            2006,

        "flag_state":
            "Malta",

        "operator":
            "Private Owner"
    },

    "7654321": {

        "vessel_type":
            "explorer_yacht",

        "loa":
            110,

        "build_year":
            2014,

        "flag_state":
            "Marshall Islands",

        "operator":
            "Northern Expedition Holdings"
    }
}


# ----------------------------------------
# Simulated OSINT database
# Replace later with:
# - Shodan
# - Censys
# - AIS
# - Satcom discovery
# ----------------------------------------

OSINT_DATABASE = {

    "9876543": {

        "rdp_exposed": True,

        "teamviewer_detected": True,

        "fortinet_detected": True
    },

    "1234567": {

        "rdp_exposed": False,

        "teamviewer_detected": False,

        "fortinet_detected": False
    },

    "7654321": {

        "rdp_exposed": True,

        "teamviewer_detected": False,

        "fortinet_detected": True
    }
}


# ----------------------------------------
# Generate pre-seeded flags
# ----------------------------------------

def generate_preseeded_flags(
    vessel_profile,
    osint
):

    flags = set()

    # ----------------------------------------
    # Large yacht complexity
    # ----------------------------------------

    loa = vessel_profile.get(
        "loa",
        0
    )

    if loa >= 80:

        flags.add(
            "large_attack_surface"
        )

        flags.add(
            "high_vendor_dependency"
        )

    # ----------------------------------------
    # Older vessel risk
    # ----------------------------------------

    build_year = vessel_profile.get(
        "build_year",
        2025
    )

    if build_year <= 2010:

        flags.add(
            "legacy_systems"
        )

    # ----------------------------------------
    # Charter yacht exposure
    # ----------------------------------------

    vessel_type = vessel_profile.get(
        "vessel_type"
    )

    if vessel_type == "charter_yacht":

        flags.add(
            "high_guest_exposure"
        )

    # ----------------------------------------
    # Explorer yachts
    # ----------------------------------------

    if vessel_type == "explorer_yacht":

        flags.add(
            "complex_satcom_environment"
        )

    # ----------------------------------------
    # OSINT-driven flags
    # ----------------------------------------

    if osint.get(
        "rdp_exposed"
    ):

        flags.add(
            "internet_exposed_rdp"
        )

    if osint.get(
        "teamviewer_detected"
    ):

        flags.add(
            "remote_management_detected"
        )

    if osint.get(
        "fortinet_detected"
    ):

        flags.add(
            "enterprise_firewall_detected"
        )

    return flags


# ----------------------------------------
# Main enrichment function
# ----------------------------------------

def enrich_vessel(imo):

    # ----------------------------------------
    # Lookup vessel profile
    # ----------------------------------------

    vessel_profile = VESSEL_DATABASE.get(

        imo,

        {

            "vessel_type":
                "unknown",

            "loa":
                0,

            "build_year":
                0,

            "flag_state":
                "unknown",

            "operator":
                "unknown"
        }
    )

    # ----------------------------------------
    # Lookup OSINT
    # ----------------------------------------

    osint = OSINT_DATABASE.get(

        imo,

        {

            "rdp_exposed": False,

            "teamviewer_detected": False,

            "fortinet_detected": False
        }
    )

    # ----------------------------------------
    # Generate intelligent flags
    # ----------------------------------------

    flags = generate_preseeded_flags(

        vessel_profile,

        osint
    )

    # ----------------------------------------
    # Final enrichment package
    # ----------------------------------------

    return {

        "imo":
            imo,

        "vessel_profile":
            vessel_profile,

        "osint":
            osint,

        "flags":
            flags
    }


# ----------------------------------------
# Debug testing
# ----------------------------------------

if __name__ == "__main__":

    imo = input(
        "Enter IMO: "
    )

    result = enrich_vessel(
        imo
    )

    print("\n=== ENRICHMENT RESULT ===\n")

    print("IMO:")
    print(result["imo"])

    print("\nVESSEL PROFILE:")
    print(
        result["vessel_profile"]
    )

    print("\nOSINT:")
    print(
        result["osint"]
    )

    print("\nFLAGS:")
    print(
        result["flags"]
    )
