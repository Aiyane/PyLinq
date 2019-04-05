import logging
from decorator import register_func


@register_func("avg")
def avg_warp():
    size = s = 0

    def avg(val):
        nonlocal s, size
        if isinstance(val, list):
            try:
                s += sum(map(float, val))
            except TypeError as e:
                logging.warning(f"AvgAggr: {e}")
            else:
                size += len(val)
        else:
            try:
                s += float(val)
            except TypeError as e:
                logging.warning(f"AvgAggr: {e}")
            else:
                size += 1
        return 0 if 0 == size else s / size

    return avg


@register_func("max")
def max_wrap():
    max_val = float('-inf')

    def my_max(val):
        nonlocal max_val
        if isinstance(val, list):
            try:
                val = max(val)
            except TypeError as e:
                logging.warning(f'MaxAggr: {e}')
                return max_val
        try:
            if val > max_val:
                max_val = val
        except TypeError as e:
            logging.warning(f'MaxAggr: {e}')
        return max_val

    return my_max


@register_func("min")
def min_wrap():
    min_val = float('inf')

    def my_min(val):
        nonlocal min_val
        if isinstance(val, list):
            try:
                val = min(val)
            except TypeError as e:
                logging.warning(f'MinAggr: {e}')
                return min_val
        try:
            if val < min_val:
                min_val = val
        except TypeError as e:
            logging.warning('MinAggr: {e}')
        return min_val

    return my_min


@register_func("count")
def count_wrap():
    count_val = 0

    def count(val):
        nonlocal count_val
        count_val += len(val) if isinstance(val, list) else 1
        return count_val
    return count


@register_func("sum")
def sum_wrap():
    s = 0

    def my_sum(val):
        nonlocal s
        try:
            s += sum(map(float, val)) if isinstance(val, list) else float(val)
        except TypeError as e:
            logging.warning(f"SumAggr: {e}")
        return s
    return my_sum
