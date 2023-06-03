# Introduction
```{admonition} 关于模块的名字
虽然本模块脱胎自[`geonodes`](https://github.com/al1brn/geonodes)，但实现逻辑和使用方法已完全不同。

`geonodes`仅支持几何节点，而`pynodes`几乎支持blender所有的节点树，包括几何节点和材质节点。
```

```{admonition} 先备条件
:class: tip
在使用 **`pynodes`** 前，你必须先了解：
- `Blender` 节点编辑器的使用
- `Python` 语言
- 如何在 `blender` 中执行 `Python` 脚本
```

```{admonition} 基本理念
:class: important
- 对几何节点的操作是基于输出端口的，而非节点本身
- 一个`Python`函数对应一个节点树，调用`Python`函数，就是在当前的节点树中，创建一个组节点。
- 数据流中的数据有严格的类型检查，数据有哪些方法，由它的类型提供。
- 良好的IDE支持，比如在`VSCODE`中，所有暴露的方法都有内置文档说明，包括涉及的节点图片，可选枚举参数，以及官方文档链接。
```