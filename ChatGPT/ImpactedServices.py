from collections import defaultdict, deque


def find_impacted_services(dependencies, failed_service):
    reverse_graph = defaultdict(list)
    for service, dependency in dependencies.items():
        for dep in dependency:
            reverse_graph[dep].append(service)

    impacted_services = []
    queue = deque([failed_service])

    while queue:
        current = queue.popleft()
        for dependent in reverse_graph.get(current, []):
            if dependent not in impacted_services:
                impacted_services.append(dependent)
                queue.append(dependent)

    return sorted(impacted_services)


dependencies = {
    "search": ["ads", "auth"],
    "ads": ["tracking"],
    "auth": ["core-auth"],
    "tracking": [],
    "core-auth": [],
    "review": ["search"],
    "notifications": ["auth"],
}

print(find_impacted_services(dependencies, "core-auth"))
