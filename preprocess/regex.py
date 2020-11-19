import re
import types

def get_int_value(in_str):
    return int(in_str.replace(',', '.'))

regex_pattern = {
    "Kind": {
        "patterns": ["(CCMN|[Cc]hung cư)", "[Hh]omestay"],
        "values" : ["Chung cư", "Homestay"],
        "default": "Phòng trọ"
    },
    "Price": {
        "patterns": ["([0-9]+,[0-9]+|[0-9]+)"],
        "values" : [get_int_value],
        "default": None
    },
    "Size": {
        "patterns": ["[0-9]+"],
        "values" : [get_int_value],
        "default": None
    },
    "Parking_slot": {
        "patterns": ["[Đđ]ể xe"],
        "values" : [1],
        "default": None,
    },
    "Air_condition": {
        "patterns": ["[Đđ]iều hòa"],
        "values" : [1],
        "default": None
    },
    "Heater_shower": {
        "patterns": ["[Nn]óng lạnh"],
        "values" : [1],
        "default": None
    },
    "Furnish": {
        "patterns": ["([Tt]ủ|[Ff]ull đồ|tivi|nội thất đầy đủ)"],
        "values" : [1],
        "default": None
    },
    "Inner_toilet": {
        "patterns": ["khép kín"],
        "values" : [1],
        "default": None
    },
    "Size_total_bool": {
        "patterns": ["[Tt]ổng diện tích"],
        "values" : [1],
        "default": None
    }
}

def reg(prop_type, data):
    
    patterns = regex_pattern[prop_type]["patterns"]
    values = regex_pattern[prop_type]["values"]
    default_value = regex_pattern[prop_type]["default"]

    for idx, pattern in enumerate(patterns):
        result = re.findall(pattern, data)
        if result:
            if isinstance(values[idx], types.FunctionType):
                return values[idx](result[0])
            return values[idx]
    return default_value

if __name__ == "__main__":
    # print(regex_pattern["Size_total_bool"])
    print(reg("Parking_slot", "vai ca dai"))
    print(reg("Size", "vai ca dai"))