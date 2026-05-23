"""
HNS-36 PoC Replication
Replicates the 50-Turn Blind Experiment from the EVA-HNS book.
Requires: pip install anthropic hns36
"""

import hns36
from dataclasses import dataclass


@dataclass
class TurnResult:
    turn: int
    question: str
    standard_errors: int
    hns_errors: int
    standard_stability: float
    hns_stability: float


def run_case(case_name: str, questions: list[str]) -> list[TurnResult]:
    """Run a single case with 5 turns comparing Standard vs HNS-36 conditions."""
    print(f"\n{'='*60}")
    print(f"CASE: {case_name}")
    print('='*60)

    results = []
    for i, question in enumerate(questions, 1):
        print(f"\n  Turn {i}: {question[:60]}...")

        # Generate standard response
        import anthropic
        client = anthropic.Anthropic()

        standard = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=500,
            system="You are a helpful and honest AI assistant. Answer the user's questions clearly and naturally.",
            messages=[{"role": "user", "content": question}]
        ).content[0].text

        # Generate HNS-36 constrained response
        hns_response = hns36.constrain(question)

        # Evaluate both
        std_analysis = hns36.analyze(standard, question=question)
        hns_analysis = hns36.analyze(hns_response, question=question)

        result = TurnResult(
            turn=i,
            question=question,
            standard_errors=std_analysis.total_errors,
            hns_errors=hns_analysis.total_errors,
            standard_stability=std_analysis.structural_stability or 0,
            hns_stability=hns_analysis.structural_stability or 0,
        )
        results.append(result)

        print(f"    Standard: {result.standard_errors} errors, stability={result.standard_stability:.1f}")
        print(f"    HNS-36:   {result.hns_errors} errors, stability={result.hns_stability:.1f}")

    return results


def print_summary(all_results: list[TurnResult]) -> None:
    """Print aggregate summary across all cases and turns."""
    total_std_errors = sum(r.standard_errors for r in all_results)
    total_hns_errors = sum(r.hns_errors for r in all_results)
    avg_std_stability = sum(r.standard_stability for r in all_results) / len(all_results)
    avg_hns_stability = sum(r.hns_stability for r in all_results) / len(all_results)

    print("\n" + "="*60)
    print("AGGREGATE RESULTS")
    print("="*60)
    print(f"{'Metric':<30} {'Standard':>10} {'HNS-36':>10}")
    print("-"*52)
    print(f"{'Total structural errors':<30} {total_std_errors:>10} {total_hns_errors:>10}")
    print(f"{'Avg structural stability':<30} {avg_std_stability:>10.2f} {avg_hns_stability:>10.2f}")
    print("-"*52)
    print(f"\nError reduction: {total_std_errors} → {total_hns_errors}")
    if total_std_errors > 0:
        reduction_pct = (1 - total_hns_errors / total_std_errors) * 100
        print(f"Reduction rate: {reduction_pct:.1f}%")


if __name__ == "__main__":
    # Replicate Case 1: Digital Fatigue (5 turns)
    case1_questions = [
        "Why do people feel exhausted by digital interfaces even when they enjoy using them?",
        "Is this mainly a psychological or a physical problem?",
        "How does social media specifically contribute to this?",
        "What role does the design of the interface play?",
        "Is this a personal problem or a societal problem?",
    ]

    # Replicate Case 3: Workplace Burnout (5 turns)
    case3_questions = [
        "Why does workplace burnout happen even in well-paid jobs?",
        "What is the difference between stress and burnout?",
        "How does management style contribute to burnout?",
        "Why do some people burn out and others don't in the same environment?",
        "Is burnout a personal failure or an organizational failure?",
    ]

    all_results = []
    all_results.extend(run_case("Digital Fatigue", case1_questions))
    all_results.extend(run_case("Workplace Burnout", case3_questions))

    print_summary(all_results)

    print("\n[Original PoC result for reference: Standard=37 errors, HNS-36=0 errors]")
