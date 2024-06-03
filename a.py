import os, json

with open(
    os.path.join("vitonhd_test_tagged.json"), "r"
) as file1:
    data1 = json.load(file1)

annotation_list = [
    "sleeveLength",
    "neckLine",
    "item",
]

annotation_pair = {}
for k, v in data1.items():
    for elem in v:
        annotation_str = ""
        for template in annotation_list:
            for tag in elem["tag_info"]:
                if (
                    tag["tag_name"] == template
                    and tag["tag_category"] is not None
                ):
                    annotation_str += tag["tag_category"]
                    annotation_str += " "
        annotation_pair[elem["file_name"]] = annotation_str