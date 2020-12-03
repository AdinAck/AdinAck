d = {
    "disks": {
        "xvda": {
            "size": "2.00 GiB",
            "size_bytes": 2147483648
        },
        "xvdb": {
            "size": "70.00 GiB",
            "size_bytes": 75161927680
        },
        "xvdc": {
            "size": "32.00 GiB",
            "size_bytes": 34359738368
        },
        "xvdf": {
            "size": "8.14 TiB",
            "size_bytes": 8950024649728
        },
        "xvdg": {
            "size": "3.00 TiB",
            "size_bytes": 3298534883328
        }
    }
}
["disks", ":", "size"]
for key in d["disks"]:
    print(d["disks"][key]["size"])
