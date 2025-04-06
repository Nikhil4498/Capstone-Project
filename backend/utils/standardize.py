def standardize_cost(provider, service, date, cost, usage):
    return {
        "provider": provider,
        "service": service,
        "date": date,
        "cost": cost,
        "resource_usage": usage
    }
