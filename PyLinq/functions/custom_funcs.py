import logging
from PyLinq.decorator import register_func

__all__ = ['rename_wrap', 'deflate_wrap']


@register_func("rename", is_aggr=True)
def rename_wrap():
    ret = []

    def rename(rename_fields_str, *items):
        nonlocal ret
        res = {}
        try:
            new_name = rename_fields_str.split(',')
            for i, name in enumerate(new_name):
                res[name] = items[i]
        except Exception as e:
            logging.warning("RenameAggr: ", e)
        else:
            ret.append(res)
            return ret
    return rename


@register_func("DEFLATE", is_aggr=True)
def deflate_wrap():
    master_vals = {}
    vals = []
    rename_fields_dict = {}

    def deflate(master_key, master_name, slave_key, rename_field_val, rename_fields_str, default_val=None):
        nonlocal master_vals, vals, rename_fields_dict
        try:
            if not rename_fields_dict:
                for rename_field in rename_fields_str.split(","):
                    old_key, new_key = rename_field.split(":")
                    rename_fields_dict[old_key] = new_key

            if master_key not in master_vals:
                master_val = {
                    master_name: master_key,
                    **{
                        rename_field: default_val
                        for rename_field
                        in rename_fields_dict.values()
                    }
                }
                master_vals[master_key] = master_val
                vals.append(master_val)

            rename_field = rename_fields_dict.get(str(slave_key), None)
            if rename_field:
                master_vals[master_key][rename_field] = rename_field_val
        except Exception as e:
            logging.warning("DeflateAggr: ", e)
        return vals
    return deflate
