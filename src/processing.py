def filter_by_state(incoming_data: list[dict], state: str) -> list[dict]:
    """функция возвращает список в зависимости от состояния"""
    result = list(filter(lambda x: x["state"] in state, incoming_data))
    return result



