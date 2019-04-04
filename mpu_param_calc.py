import os
import math
import json

out = {"Main Power Up":{}}
for file in os.listdir("."):
    if ".txt" in file:
        with open(file, 'r') as f:
            d = f.readlines()
            name = d[0].strip()
            desc = d[1].strip()
            d = d[2:]
            if "Damage Up" in desc:
                _min_min = float(d[0].split(' ')[3].split('-')[0].strip())
                _min_max = float(d[-1].split(' ')[3].split('-')[0].strip())
                _min_mid = float((_min_min + _min_max) / 2)
                min_params = [_min_max, _min_mid, _min_min]
                
                _max_min = float(d[0].split(' ')[3].split('-')[1].strip())
                _max_max = float(d[-1].split(' ')[3].split('-')[1].strip())
                _max_mid = float((_max_min + _max_max) / 2)
                max_params = [_max_max, _max_mid, _max_min]
                out["Main Power Up"][name] = {"desc": desc, "min_params":min_params, "max_params":max_params}
                
            else:
                _max = float(d[-1].split(' ')[3].strip())
                _min = float(d[0].split(' ')[3].strip())
                _mid = float((_max + _min) / 2)
                params = [_max,_mid,_min]
                out["Main Power Up"][name] = {"desc": desc, "params":params}

with open("mpu_params.json", 'w') as f:
    f.write(json.dumps(out, indent=2))
