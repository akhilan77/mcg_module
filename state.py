# state.py

STATE = {

    # ----------------------------------------
    # Vessel identity
    # ----------------------------------------

    "imo": None,

    # ----------------------------------------
    # Vessel profile/context
    # Filled from IMO enrichment
    # ----------------------------------------

    "vessel_profile": {

        "vessel_type": None,

        "loa": None,

        "build_year": None,

        "flag_state": None,

        "operator": None
    },

    # ----------------------------------------
    # User answers
    # ----------------------------------------

    "answers": {},

    # ----------------------------------------
    # Triggered risk flags
    # ----------------------------------------

    "flags": set(),

    # ----------------------------------------
    # Domains touched during assessment
    # ----------------------------------------

    "covered_domains": set(),

    # ----------------------------------------
    # Domain risk scores
    # ----------------------------------------

    "scores": {},

    # ----------------------------------------
    # Question order/history
    # ----------------------------------------

    "question_history": [],

    # ----------------------------------------
    # Explainability / decision tracking
    # ----------------------------------------

    "decision_trace": [],

    # ----------------------------------------
    # Current role/persona
    # ----------------------------------------

    "role": "eto",

    # ----------------------------------------
    # OSINT findings
    # Populated dynamically from IMO
    # ----------------------------------------

    "osint": {

        "rdp_exposed": False,

        "teamviewer_detected": False,

        "fortinet_detected": False
    },

    # ----------------------------------------
    # Assessment metadata
    # ----------------------------------------

    "metadata": {

        "assessment_version": "1.0",

        "assessment_type":
            "yacht_cybersecurity",

        "started": None,

        "completed": None
    }
}
