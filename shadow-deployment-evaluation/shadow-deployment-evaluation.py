from math import ceil

def evaluate_shadow(production_log, shadow_log, criteria):
    """
    Evaluate whether a shadow model is ready for promotion.
    """
    # Write code here
    n = len(shadow_log)

    production_number_matching = sum(1 for d in production_log if d["actual"] == d["prediction"])
    shadow_number_matching = sum(1 for d in shadow_log if d["actual"] == d["prediction"]) 

    production_accuracy = production_number_matching / n
    shadow_accuracy = shadow_number_matching / n

    accuracy_gain = shadow_accuracy - production_accuracy

    index = ceil(0.95 * n) - 1

    shadow_latencies_ascending = sorted([d["latency_ms"] for d in shadow_log])
    shadow_latency_p95 = shadow_latencies_ascending[index]
    
    production_prediction_set = {(d["input_id"], d["prediction"]) for d in production_log}
    shadow_prediction_set = {(d["input_id"], d["prediction"]) for d in shadow_log}

    agreement_rate = len(production_prediction_set & shadow_prediction_set) / n

    min_accuracy_gain = criteria["min_accuracy_gain"]
    max_latency_p95 = criteria["max_latency_p95"]
    min_agreement_rate = criteria["min_agreement_rate"]
    
    return {
        "promote": (accuracy_gain >= min_accuracy_gain) and (shadow_latency_p95 <= max_latency_p95) and (agreement_rate >= min_agreement_rate),
        "metrics": {
            "shadow_accuracy": shadow_accuracy,
            "production_accuracy": production_accuracy,
            "accuracy_gain": accuracy_gain,
            "shadow_latency_p95": shadow_latency_p95,
            "agreement_rate": agreement_rate
        }
    }
    pass