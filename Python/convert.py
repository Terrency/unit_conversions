# 合并后的单位转换表
conversion_table = {
    "speed": {
        "base_unit": "meter_per_second",
        "meter_per_second": {
            "display": "m/s",
            "to_base": "value",
            "from_base": "value"
        },
        "kilometer_per_hour": {
            "display": "km/h",
            "to_base": "value / 3.6",
            "from_base": "value * 3.6"
        },
        "mile_per_hour": {
            "display": "mph",
            "to_base": "value / 2.23694",
            "from_base": "value * 2.23694"
        }
    },
    "distance": {
        "base_unit": "meter",
        "meter": {
            "display": "m",
            "to_base": "value",
            "from_base": "value"
        },
        "kilometer": {
            "display": "km",
            "to_base": "value * 1000",
            "from_base": "value / 1000"
        },
        "mile": {
            "display": "mi",
            "to_base": "value * 1609.344",
            "from_base": "value / 1609.344"
        }
    }
}

def convert(value, from_unit, to_unit, category):
    unit_category = conversion_table[category]
    base_unit = unit_category["base_unit"]

    from_unit_def = unit_category["units"][from_unit]
    to_unit_def = unit_category["units"][to_unit]

    # 转换为基本单位
    base_value = eval(from_unit_def["to_base"].replace("value", str(value)))

    # 从基本单位转换为目标单位
    result = eval(to_unit_def["from_base"].replace("value", str(base_value)))

    return result

# 示例调用
result = convert(36, "kilometer_per_hour", "meter_per_second", "speed")
print(result)  # 输出 10
def convert(value, from_unit, to_unit, category):
    unit_category = conversion_table[category]
    base_unit = unit_category["base_unit"]

    from_unit_def = unit_category["units"][from_unit]
    to_unit_def = unit_category["units"][to_unit]

    # 转换为基本单位
    base_value = eval(from_unit_def["to_base"].replace("value", str(value)))

    # 从基本单位转换为目标单位
    result = eval(to_unit_def["from_base"].replace("value", str(base_value)))

    return result