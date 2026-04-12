def schedule_pipeline(tasks, resource_budget):
    time = 0
    completed = set()
    running = []
    result = []

    task_map = {t["name"]: t for t in tasks}

    while len(completed) < len(tasks):
        # Check finished tasks
        finished = [t for t in running if t["end"] <= time]
        for t in finished:
            running.remove(t)
            completed.add(t["name"])

        # Find ready tasks
        ready = []
        for t in tasks:
            if (
                t["name"] not in completed and
                t["name"] not in [r["name"] for r in running] and
                all(dep in completed for dep in t["depends_on"])
            ):
                ready.append(t)

        ready = sorted(ready, key=lambda x: x["name"])

        # Current resource usage
        used = sum(t["resources"] for t in running)

        # Start tasks if enough resource
        for t in ready:
            if used + t["resources"] <= resource_budget:
                running.append({
                    "name": t["name"],
                    "end": time + t["duration"],
                    "resources": t["resources"]
                })
                result.append((t["name"], time))
                used += t["resources"]

        time += 1

    return result
    pass