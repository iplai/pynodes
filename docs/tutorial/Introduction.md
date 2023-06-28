# Introduction
```{admonition} About the name of the module
Although this module is derived from[`geonodes`](https://github.com/al1brn/geonodes), But the implementation logic and usage are completely different.

For `geonodes`, only geometry nodes are supported, while `pynodes` supports almost all of blender's node trees, including geometry nodes and material nodes.
```

```{admonition} Prerequisities
:class: tip
Before using **`pynodes`**, you must first know:
- How to use `Blender` Node editor
- `Python` language
- How to run `Python` script in `Blender`
```

```{admonition} Basic Concepts
:class: important
Nodes are created by a series of chain calls in a python function decrorated by `@tree` which represents a node group in blender.
- Operations on nodes are based on the output port(data socket), not on the node itself.
- A decorated `Python` function (`@tree`) corresponds to a tree of nodes. Calling the function means creating a group node in the current node tree.
- Data in a data flow has strict type checking, what methods are available for the data socket, and what is provided by its type.
- Good IDE support，e.g. [`VS Code`](https://code.visualstudio.com/)，All exposed methods have built-in documentation, including images of the nodes involved, optional enumeration parameters, and links to official documentation.
```

```{toctree}
:maxdepth: 4
GeometryNodes
```