# Home


[![LICENSE](https://img.shields.io/github/license/iplai/pynodes)](https://github.com/iplai/pynodes/blob/main/LICENSE)
[![Python 3.10 +](https://img.shields.io/badge/python-3.10_+-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Blender](https://img.shields.io/badge/Blender-_3.5.1~3.6.0_-blue)](http://www.blender.org)

*[Pynodes](https://github.com/iplai/pynodes/) is ia a module as well as an addon for blender to create all kinds of nodes in node editor with python sciprts.*

---

#### About the birth of this module

Although this module is derived from [`geonodes`](https://github.com/al1brn/geonodes), But the implementation logic and usage are completely different.

For [`geonodes`](https://github.com/al1brn/geonodes), only geometry nodes are supported, while `pynodes` supports almost all of blender's node trees, including geometry nodes and material nodes.

#### Prerequisities

```{admonition} Before using pynodes, you must first know:
:class: tip
- How to use `Blender` Node editor
- `Python` language
- How to run `Python` script in `Blender`
```

```{admonition} Basic Concepts
:class: important
Nodes are created by a series of chain calls in a python function decrorated by {class}`pynodes.core.tree` which represents a node group in blender.
- Operations on nodes are based on the output port(data socket), not on the node itself.
- A decorated `Python` function (`@tree`) corresponds to a tree of nodes. Calling the function means creating a group node in the current node tree.
- Data in a data flow has strict type checking, what methods are available for the data socket, and what is provided by its type.
- Good IDE support，e.g. [`VS Code`](https://code.visualstudio.com/)，All exposed methods have built-in documentation, including images of the nodes involved, optional enumeration parameters, and links to official documentation.
```

---

#### Content

```{toctree}
:hidden:
self
```

```{toctree}
:maxdepth: 4
quick_start
gallery/index
socket_types
apidocs/index
```