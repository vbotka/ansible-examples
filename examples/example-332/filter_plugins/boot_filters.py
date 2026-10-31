def to_boot_dict(record_list):

    result = {}

    for item in record_list:

        sw_key = item.get("SWITCH_ID")

        current_boot = {
            "config": item.get("CURRENT_BOOT", "").rstrip(";")
        }

        next_boot = {
            "config": item.get("NEXT_BOOT").rstrip(";")
        }
        if item.get("MANUAL_BOOT", ""):
            next_boot["manual_boot"] = item["MANUAL_BOOT"] == "yes"
        if item.get("ENABLE_BREAK", ""):
            next_boot["enable_break"] = item["ENABLE_BREAK"] == "yes"

        result[sw_key] = {
            "id": sw_key,
            "current_boot": current_boot,
            "next_boot": next_boot
        }

    return result


class FilterModule(object):
    def filters(self):
        return {
            "to_boot_dict": to_boot_dict
        }
