def filter_by_state(incoming_data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """the function returns a list depending on the state"""
    result = list(filter(lambda x: x["state"] in state, incoming_data))
    return result


def sort_by_date(
    incoming_data: list[dict], sorted_parameter: bool = True
) -> list[dict]:
    """function to sort data by date"""
    result = list(
        sorted(incoming_data, key=lambda x: x["date"], reverse=sorted_parameter)
    )
    return result
