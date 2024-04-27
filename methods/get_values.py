def try_parse_to_float_value(value: str) -> float:
    try:
        return_value = float(value)
        if return_value < 0 or return_value > 200:
            raise ValueError
        return return_value
    except ValueError:
        raise ValueError