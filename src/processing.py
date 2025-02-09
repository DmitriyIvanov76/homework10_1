def filter_by_state(incoming_data: list[dict], state: str) -> list[dict]:
    """функция возвращает список в зависимости от состояния"""
    result = list(filter(lambda x: x["state"] in state, incoming_data))
    return result


def sort_by_date (incoming_data: list[dict], sorted_parameter=True) -> list[dict]:
    """функция сортировки данных по дате"""
    result = list(sorted(incoming_data, key=lambda x: x['date'], reverse=sorted_parameter))
    return result

