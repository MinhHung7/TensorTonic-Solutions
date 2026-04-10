def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    Strategies:
        - "first": keep the first record in each group
        - "last": keep the last record in each group
        - "most_complete": keep the record with the fewest None values
                           ties broken by first occurrence
    """
    # Group records by key columns
    groups = {}
    for record in records:
        key = tuple(record[col] for col in key_columns)
        groups.setdefault(key, []).append(record)

    deduped = []

    for key, recs in groups.items():
        if strategy == "first":
            deduped.append(recs[0])

        elif strategy == "last":
            deduped.append(recs[-1])

        elif strategy == "most_complete":
            # Count None values per record
            def none_count(rec):
                return sum(v is None for v in rec.values())

            # Choose record with fewest None values
            best = min(recs, key=none_count)
            deduped.append(best)

        else:
            raise ValueError(f"Unknown strategy: {strategy}")

    return deduped
