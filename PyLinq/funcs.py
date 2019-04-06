import logging
from PyLinq.decorator import register_func

__all__ = ['avg_warp', 'max_wrap', 'min_wrap', 'count_wrap', 'sum_wrap']


@register_func("avg", is_aggr=True)
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


@register_func("max", is_aggr=True)
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


@register_func("min", is_aggr=True)
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
            logging.warning(f'MinAggr: {e}')
        return min_val

    return my_min


@register_func("count", is_aggr=True)
def count_wrap():
    count_val = 0

    def count(val):
        nonlocal count_val
        count_val += len(val) if isinstance(val, list) else 1
        return count_val
    return count


@register_func("rename", is_aggr=True)
def rename_wrap():
    val = []
    rename_fields_dict = {}

    def rename(items, rename_fields_str):
        nonlocal val, rename_fields_dict
        if not items:
            return val
        try:
            item = next(iter(items.values()))

            if not rename_fields_dict:
                for rename_field in rename_fields_str.split(","):
                    old_key, new_key = rename_field.split(":")
                    rename_fields_dict[old_key] = new_key

            for old_key, new_key in rename_fields_dict.items():
                if old_key in item:
                    item[new_key] = item.pop(old_key)

        except Exception as e:
            logging.warning("RenameAggr: ", e)
        else:
            val.append(item)
        return val
    return rename


# @register_func("DEFLATE", is_aggr=True)
# def deflate_wrap():
#     master_vals = {}
#     vals = []
#     rename_fields_dict = {}
#
#     def deflate(master_key, master_name, slave_key, rename_field_val, rename_fields_str, default_val=None):
#         nonlocal master_vals, vals, rename_fields_dict
#         try:
#             if not rename_fields_dict:
#                 for rename_field in rename_fields_str.split(","):
#                     old_key, new_key = rename_field.split(":")
#                     rename_fields_dict[old_key] = new_key
#
#             if master_key not in master_vals:
#                 master_val = {
#                     master_name: master_key,
#                     **{
#                         rename_field: default_val
#                         for rename_field
#                         in rename_fields_dict.values()
#                     }
#                 }
#                 master_vals[master_key] = master_val
#                 vals.append(master_val)
#
#             rename_field = rename_fields_dict.get(str(slave_key), None)
#             if rename_field:
#                 master_vals[master_key][rename_field] = rename_field_val
#         except Exception as e:
#             logging.warning("DeflateAggr: ", e)
#         return vals
#     return deflate


@register_func("sum", is_aggr=True)
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
