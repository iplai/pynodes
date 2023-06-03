import requests, re, json
from bs4 import BeautifulSoup


prefix_official = "https://docs.blender.org/manual/en/latest/"
prefix_local = "http://127.0.0.1:8090/blender_manual_v350_en/"

data = []


def parse_shader_nodes_index():
    html_doc = requests.get(f"{prefix_local}render/shader_nodes/index.html").content
    soup = BeautifulSoup(html_doc, "html.parser")
    section = soup.find(id="shader-nodes")
    for level1 in section.find_all("li", {"class": "toctree-l1"}):
        level1_name = level1.contents[0].string
        if level1_name in ["Introduction", "Group", "Open Shading Language"]:
            continue
        for level2 in level1.find_all("li", {"class": "toctree-l2"}):
            level2_name = level2.contents[0].string
            if len(level2.contents) == 1:
                path = f"{level1_name} > {level2_name}"
                link = level2.contents[0].get("href")
                parse_shader_nodes_detail(link, path)


def parse_shader_nodes_detail(link, path):
    doc_url = f"{prefix_local}render/shader_nodes/{link}"
    html_doc = requests.get(doc_url).content
    soup = BeautifulSoup(html_doc, "html.parser")
    article = soup.find(itemprop="articleBody")
    description = article.section.find("p", recursive=False)
    if description is not None:
        description = description.get_text()
        description = description.replace('\n', " ")
    else:
        description = ""
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
    print(path, description, image_url, class_name, sep="\n")

    data.append({
        "bl_idname": class_name,
        "path": path,
        "documentation": description,
        "url1": doc_url.replace(prefix_local, prefix_official),
        "url2": image_url,
    })


parse_shader_nodes_index()
json.dump(data, open("pynodes_builder/nodes_doc_url_shader.json", "w", encoding="utf-8"), indent=2)
