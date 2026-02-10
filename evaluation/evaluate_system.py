import json
from evaluation.run_on_text import run_on_text

TEST_PATH = "data/contracts/test_contracts.json"

def load_tests():
    with open(TEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def evaluate():
    tests = load_tests()

    total = 0
    correct = 0
    false_positive = 0
    false_negative = 0

    print("\n===== SYSTEM EVALUATION =====\n")

    for t in tests:
        print(f"Contract ID: {t['id']}")
        predicted = run_on_text(t["text"])
        expected = t["expected"]

        for obligation, exp_value in expected.items():
            pred_value = predicted.get(obligation, "MISSING")
            total += 1

            if pred_value == exp_value:
                correct += 1
                status = "✅ CORRECT"
            elif pred_value == "PRESENT" and exp_value == "MISSING":
                false_positive += 1
                status = "❌ FALSE POSITIVE"
            elif pred_value == "MISSING" and exp_value == "PRESENT":
                false_negative += 1
                status = "❌ FALSE NEGATIVE"
            else:
                status = "⚠️ AMBIGUOUS"

            print(f"  {obligation}: expected={exp_value}, predicted={pred_value} → {status}")

        print("-" * 50)

    print("\n===== SUMMARY =====")
    print(f"Total checks       : {total}")
    print(f"Correct detections : {correct}")
    print(f"False positives    : {false_positive}")
    print(f"False negatives    : {false_negative}")

if __name__ == "__main__":
    evaluate()
