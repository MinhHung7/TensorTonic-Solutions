def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """

    # Write code here
    
    top_k = recommended[:k]

    relevant_set = set(relevant)

    top_k_in_relevant = relevant_set.intersection(top_k)

    top_k_in_relevant_size = len(top_k_in_relevant)

    return [top_k_in_relevant_size / k, top_k_in_relevant_size / len(relevant)]