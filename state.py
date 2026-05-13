# state.py

STATE = {

    # User answers
    "answers": {},

    # Triggered risk flags
    "flags": set(),

    # Domains touched during assessment
    "covered_domains": set(),

    # Domain risk scores
    "scores": {},

    # Question order/history
    "question_history": [],

    # Current role/persona
    "role": "eto",

    # OSINT findings
    "osint": {

        "rdp_exposed": True,

        "teamviewer_detected": True,

        "fortinet_detected": True
    },

    # Assessment metadata
    "metadata": {

        "assessment_version": "1.0",

        "assessment_type": "yacht_cybersecurity",

        "started": None,

        "completed": None
    }
}
