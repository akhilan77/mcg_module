from engine import score_question


# ----------------------------------------
# Explain WHY question selected
# ----------------------------------------

def explain_question(
    question,
    state
):

    result = score_question(
        question,
        state
    )

    print("\nWHY THIS QUESTION?")
    print("-" * 40)

    for reason in result["reasons"]:

        print(f"- {reason}")

    print(
        f"\nFINAL SCORE: {result['score']}"
    )

    return result


# ----------------------------------------
# Record decision trace
# ----------------------------------------

def record_decision_trace(
    question,
    state,
    result
):

    trace = {

        "question_id":
            question["id"],

        "question":
            question["text"],

        "score":
            result["score"],

        "reasons":
            result["reasons"],

        "active_flags":
            list(state["flags"]),

        "covered_domains":
            list(
                state["covered_domains"]
            ),

        "osint":
            state["osint"]
    }

    state["decision_trace"].append(
        trace
    )
