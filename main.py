# main.py

import json
import csv
import uuid
import os

from datetime import datetime

from engine import (

    get_next_question,

    process_flags,

    update_coverage,

    record_question_history,

    finalize_assessment,

    print_state
)

from explainability import (

    explain_question,

    record_decision_trace
)

from state import STATE


# ----------------------------------------
# Export folders
# ----------------------------------------

JSON_EXPORT_DIR = "exports/json"

CSV_EXPORT_DIR = "exports/csv"

os.makedirs(
    JSON_EXPORT_DIR,
    exist_ok=True
)

os.makedirs(
    CSV_EXPORT_DIR,
    exist_ok=True
)


# ----------------------------------------
# Export JSON
# ----------------------------------------

def export_json(assessment):

    filename = (
        f'{assessment["assessment_id"]}.json'
    )

    filepath = os.path.join(
        JSON_EXPORT_DIR,
        filename
    )

    with open(
        filepath,
        "w"
    ) as f:

        json.dump(
            assessment,
            f,
            indent=4
        )

    print(
        f"\nJSON exported: {filepath}"
    )


# ----------------------------------------
# Export answers CSV
# ----------------------------------------

def export_answers_csv(assessment):

    filename = (
        f'{assessment["assessment_id"]}_answers.csv'
    )

    filepath = os.path.join(
        CSV_EXPORT_DIR,
        filename
    )

    with open(
        filepath,
        "w",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "question_id",
            "answer"
        ])

        for qid, answer in assessment[
            "answers"
        ].items():

            writer.writerow([
                qid,
                answer
            ])

    print(
        f"Answers CSV exported: {filepath}"
    )


# ----------------------------------------
# Export flags CSV
# ----------------------------------------

def export_flags_csv(assessment):

    filename = (
        f'{assessment["assessment_id"]}_flags.csv'
    )

    filepath = os.path.join(
        CSV_EXPORT_DIR,
        filename
    )

    with open(
        filepath,
        "w",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "flag"
        ])

        for flag in assessment[
            "flags"
        ]:

            writer.writerow([
                flag
            ])

    print(
        f"Flags CSV exported: {filepath}"
    )


# ----------------------------------------
# Export domains CSV
# ----------------------------------------

def export_domains_csv(assessment):

    filename = (
        f'{assessment["assessment_id"]}_domains.csv'
    )

    filepath = os.path.join(
        CSV_EXPORT_DIR,
        filename
    )

    with open(
        filepath,
        "w",
        newline=""
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "domain",
            "score"
        ])

        for domain, score in assessment[
            "risk_scores"
        ].items():

            writer.writerow([
                domain,
                score
            ])

    print(
        f"Domains CSV exported: {filepath}"
    )


# ----------------------------------------
# Main
# ----------------------------------------

print(
    "\n=== Yacht Cyber Questionnaire ==="
)

STATE["metadata"]["started"] = (
    datetime.utcnow().isoformat()
)

while True:

    # ----------------------------------------
    # Get next question
    # ----------------------------------------

    question = get_next_question(
        STATE
    )

    # ----------------------------------------
    # Assessment complete
    # ----------------------------------------

    if not question:

        print(
            "\nAssessment Complete."
        )

        break

    # ----------------------------------------
    # Explain WHY selected
    # ----------------------------------------

    result = explain_question(
        question,
        STATE
    )

    # ----------------------------------------
    # Record decision trace
    # ----------------------------------------

    record_decision_trace(
        question,
        STATE,
        result
    )

    # ----------------------------------------
    # Ask question
    # ----------------------------------------

    print("\n" + question["text"])

    print(
        "Options:",
        ", ".join(
            question["options"]
        )
    )

    answer = input("> ").strip().lower()

    # ----------------------------------------
    # Save answer
    # ----------------------------------------

    STATE["answers"][
        question["id"]
    ] = answer

    # ----------------------------------------
    # Process flags
    # ----------------------------------------

    process_flags(
        question,
        answer,
        STATE
    )

    # ----------------------------------------
    # Update coverage/scoring
    # ----------------------------------------

    update_coverage(
        question,
        STATE
    )

    # ----------------------------------------
    # Track question history
    # ----------------------------------------

    record_question_history(
        question,
        answer,
        STATE
    )

    # ----------------------------------------
    # Debug state
    # ----------------------------------------

    print_state(STATE)


# ----------------------------------------
# Complete metadata
# ----------------------------------------

STATE["metadata"]["completed"] = (
    datetime.utcnow().isoformat()
)


# ----------------------------------------
# Final assessment
# ----------------------------------------

assessment = finalize_assessment(
    STATE
)


# ----------------------------------------
# Build export object
# ----------------------------------------

export_data = {

    "assessment_id":
        str(uuid.uuid4()),

    "timestamp":
        datetime.utcnow().isoformat(),

    "metadata":
        STATE["metadata"],

    "answers":
        assessment["answers"],

    "flags":
        assessment["flags"],

    "covered_domains":
        assessment[
            "covered_domains"
        ],

    "risk_scores":
        assessment[
            "risk_scores"
        ],

    "question_history":
        assessment[
            "question_history"
        ],

    "decision_trace":
        assessment[
            "decision_trace"
        ],

    "correlations":
        assessment[
            "correlations"
        ],

    "total_flags":
        assessment[
            "total_flags"
        ]
}


# ----------------------------------------
# Export files
# ----------------------------------------

export_json(export_data)

export_answers_csv(export_data)

export_flags_csv(export_data)

export_domains_csv(export_data)


print(
    "\nAll exports completed successfully."
)
