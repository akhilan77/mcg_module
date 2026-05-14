# engine.py

from questions import QUESTIONS


# ----------------------------------------
# Evaluate conditions
# ----------------------------------------

def evaluate_conditions(question, state):

    conditions = question.get(
        "conditions",
        []
    )

    for cond in conditions:

        actual = state["answers"].get(
            cond["question"]
        )

        operator = cond["operator"]

        expected = cond["value"]

        if operator == "equals":

            if actual != expected:
                return False

    return True


# ----------------------------------------
# OSINT filtering
# ----------------------------------------

def osint_relevant(question, state):

    required = question.get(
        "osint_required"
    )

    if not required:
        return True

    return state["osint"].get(
        required,
        False
    )


# ----------------------------------------
# Generic scoring engine
# ----------------------------------------

def score_question(question, state):

    score = question.get(
        "base_weight",
        0
    )

    reasons = []

    # ----------------------------------------
    # Base priority
    # ----------------------------------------

    reasons.append(
        f"Base priority: +{score}"
    )

    # ----------------------------------------
    # Missing domain coverage
    # ----------------------------------------

    if (
        question["domain"]
        not in state["covered_domains"]
    ):

        score += 20

        reasons.append(
            "Uncovered domain: +20"
        )

    # ----------------------------------------
    # Information gain
    # ----------------------------------------

    ig = question.get(
        "information_gain",
        0
    )

    score += ig

    reasons.append(
        f"Information gain: +{ig}"
    )

    # ----------------------------------------
    # Dynamic score modifiers
    # ----------------------------------------

    for mod in question.get(
        "score_modifiers",
        []
    ):

        # ----------------------------------------
        # Flag boosts
        # ----------------------------------------

        if (
            "if_flag" in mod
            and mod["if_flag"]
            in state["flags"]
        ):

            score += mod["boost"]

            reasons.append(
                f"Flag '{mod['if_flag']}' matched: +{mod['boost']}"
            )

        # ----------------------------------------
        # OSINT boosts
        # ----------------------------------------

        if (
            "if_osint" in mod
            and state["osint"].get(
                mod["if_osint"]
            )
        ):

            score += mod["boost"]

            reasons.append(
                f"OSINT '{mod['if_osint']}' matched: +{mod['boost']}"
            )

    # ----------------------------------------
    # Role relevance
    # ----------------------------------------

    role = state.get("role")

    tags = question.get(
        "tags",
        []
    )

    if role == "eto":

        technical_tags = [

            "remote_access",

            "authentication",

            "rdp",

            "credentials",

            "vpn",

            "segmentation",

            "endpoint"
        ]

        for tag in technical_tags:

            if tag in tags:

                score += 15

                reasons.append(
                    f"ETO technical relevance ({tag}): +15"
                )

    elif role == "captain":

        operational_tags = [

            "vendor",

            "incident_response"
        ]

        for tag in operational_tags:

            if tag in tags:

                score += 10

                reasons.append(
                    f"Captain operational relevance ({tag}): +10"
                )

    # ----------------------------------------
    # Final result
    # ----------------------------------------

    return {

        "score": score,

        "reasons": reasons
    }


# ----------------------------------------
# Get valid questions
# ----------------------------------------

def get_valid_questions(state):

    valid_questions = []

    for question in QUESTIONS:

        # ----------------------------------------
        # Already answered
        # ----------------------------------------

        if (
            question["id"]
            in state["answers"]
        ):

            continue

        # ----------------------------------------
        # Conditions
        # ----------------------------------------

        if not evaluate_conditions(
            question,
            state
        ):

            continue

        # ----------------------------------------
        # OSINT filtering
        # ----------------------------------------

        if not osint_relevant(
            question,
            state
        ):

            continue

        valid_questions.append(
            question
        )

    return valid_questions


# ----------------------------------------
# Rank questions
# ----------------------------------------

def rank_questions(state):

    valid_questions = get_valid_questions(
        state
    )

    ranked = sorted(

        valid_questions,

        key=lambda q:
            score_question(
                q,
                state
            )["score"],

        reverse=True
    )

    return ranked


# ----------------------------------------
# Get next question
# ----------------------------------------

def get_next_question(state):

    ranked = rank_questions(state)

    if not ranked:
        return None

    return ranked[0]


# ----------------------------------------
# Generic flag processor
# ----------------------------------------

def process_flags(
    question,
    answer,
    state
):

    triggered_flags = []

    for rule in question.get(
        "flags",
        []
    ):

        if answer == rule["answer"]:

            flag = rule["flag"]

            state["flags"].add(
                flag
            )

            triggered_flags.append(
                flag
            )

    return triggered_flags


# ----------------------------------------
# Update coverage + scoring
# ----------------------------------------

def update_coverage(
    question,
    state
):

    domain = question["domain"]

    state["covered_domains"].add(
        domain
    )

    # ----------------------------------------
    # Initialize score
    # ----------------------------------------

    if domain not in state["scores"]:

        state["scores"][domain] = 0

    # ----------------------------------------
    # Accumulate weighted score
    # ----------------------------------------

    state["scores"][domain] += question.get(
        "base_weight",
        0
    )


# ----------------------------------------
# Track question flow
# ----------------------------------------

def record_question_history(
    question,
    answer,
    state
):

    state["question_history"].append({

        "question_id":
            question["id"],

        "question":
            question["text"],

        "answer":
            answer,

        "domain":
            question["domain"]
    })


# ----------------------------------------
# Correlation engine
# ----------------------------------------

def process_correlations(state):

    correlations = []

    flags = state["flags"]

    # ----------------------------------------
    # Remote compromise path
    # ----------------------------------------

    if (
        "vendor_remote_access" in flags
        and
        "weak_authentication" in flags
    ):

        correlations.append(
            "high_remote_compromise_probability"
        )

    # ----------------------------------------
    # Internet-facing attack path
    # ----------------------------------------

    if (
        "critical_remote_access_risk" in flags
        and
        "vpn_weak_authentication" in flags
    ):

        correlations.append(
            "internet_facing_attack_path"
        )

    # ----------------------------------------
    # Lateral movement risk
    # ----------------------------------------

    if (
        "credential_sharing" in flags
        and
        "unmanaged_devices" in flags
    ):

        correlations.append(
            "high_lateral_movement_risk"
        )

    # ----------------------------------------
    # OT exposure
    # ----------------------------------------

    if (
        "critical_network_segmentation_risk"
        in flags
        and
        "no_endpoint_detection"
        in flags
    ):

        correlations.append(
            "critical_operational_technology_exposure"
        )

    return correlations


# ----------------------------------------
# Final assessment summary
# ----------------------------------------

def finalize_assessment(state):

    correlations = process_correlations(
        state
    )

    assessment = {

        "answers":
            state["answers"],

        "flags":
            list(state["flags"]),

        "covered_domains":
            list(state["covered_domains"]),

        "risk_scores":
            state["scores"],

        "question_history":
            state["question_history"],

        "correlations":
            correlations,

        "decision_trace":
            state["decision_trace"],

        "total_flags":
            len(state["flags"])
    }

    return assessment


# ----------------------------------------
# Debug state
# ----------------------------------------

def print_state(state):

    print("\n========== STATE ==========")

    print("\nAnswers:")

    for k, v in state["answers"].items():

        print(f"{k}: {v}")

    print("\nFlags:")

    for flag in state["flags"]:

        print(flag)

    print("\nCovered Domains:")

    for d in state["covered_domains"]:

        print(d)

    print("\nScores:")

    for domain, score in state[
        "scores"
    ].items():

        print(
            f"{domain}: {score}"
        )

    print("\nQuestion History:")

    for q in state[
        "question_history"
    ]:

        print(
            f'{q["question_id"]} '
            f'-> {q["answer"]}'
        )

    print("\nDecision Trace Count:")

    print(
        len(
            state["decision_trace"]
        )
    )

    print("\n===========================")
