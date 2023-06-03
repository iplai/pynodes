import requests, re, json
from bs4 import BeautifulSoup


prefix_official = "https://docs.blender.org/manual/en/latest/"
prefix_local = "http://127.0.0.1:8090/blender_manual_v350_en/"

data = []


def parse_geometry_nodes_index():
    html_doc = requests.get(f"{prefix_local}modeling/geometry_nodes/index.html").content
    soup = BeautifulSoup(html_doc, "html.parser")
    section = soup.find(id="node-types")
    for level1 in section.find_all("li", {"class": "toctree-l1"}):
        level1_name = level1.contents[0].string
        if level1_name.endswith(" Nodes"):
            level1_name = level1_name[:-6]
        if level1_name == "Group":
            continue
        for level2 in level1.find_all("li", {"class": "toctree-l2"}):
            level2_name = level2.contents[0].string
            if len(level2.contents) == 1:
                path = f"{level1_name} > {level2_name}"
                link = level2.contents[0].get("href")
                parse_geometry_nodes_detail(link, path)
            else:
                for level3 in level2.find_all("li", {"class": "toctree-l3"}):
                    level3_name = level3.contents[0].string
                    path = f"{level1_name} > {level2_name} > {level3_name}"
                    link = level3.contents[0].get("href")
                    parse_geometry_nodes_detail(link, path)


def parse_geometry_nodes_detail(link, path):
    doc_url = f"{prefix_local}modeling/geometry_nodes/{link}"
    html_doc = requests.get(doc_url).content
    soup = BeautifulSoup(html_doc, "html.parser")
    article = soup.find(itemprop="articleBody")
    description = article.section.find("p", recursive=False).get_text()
    description = description.replace('\n', " ")
    image = article.img
    if image is not None:
        image_url = article.img.get("src")
        image_url = re.search(r"(_images/.*)", image_url).group(1)
        image_url = f"{prefix_official}{image_url}"
    else:
        image_url = ""
    if image_url == "":
        return
    class_name = image_url.split("_")[-1].split(".")[0]
    # print(path, description, image_url, class_name, sep="\n")
    if path == "Material > Material Selection Node":
        class_name = "GeometryNodeMaterialSelection"
    if path == "Utilities > Math > Mix Node":
        class_name = "ShaderNodeMix"

    data.append({
        "bl_idname": class_name,
        "path": path,
        "documentation": description,
        "url1": doc_url.replace(prefix_local, prefix_official),
        "url2": image_url,
    })

    # file.write(f"class {class_name}:\n")
    # file.write(f"    \"\"\"{description}\"\"\"\n")
    # file.write(f"    url1 = \"{doc_url.replace(prefix_local, prefix_official)}\"\n")
    # file.write(f"    url2 = \"{image_url}\"\n\n")


if __name__ == "__main__":
    parse_geometry_nodes_index()
    json.dump(data, open(r"E:\blender-3.4.1-windows-x64\3.4\scripts\addons\modules\pynodes\nodes_doc_url.json", "w", encoding="utf-8"), indent=2)
