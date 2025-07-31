---
title: namedsetelement.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\namedsetelement.md
created_at: 2025-07-03
---








  









### NamedSet Element {#namedset-element style="tab-stops: 0pt"}

A named set is a collection of tuples and members, which can be defined and saved as a part of the cube definition. Named set records reside inside the sets folder, which is under a dimension element. These elements can be dragged to Categories/Series/Slicer axis of Axes Element Builder. To help make working with a lengthy, complex, or commonly used expression easier, Multidimensional Expressions (MDX) lets you to define a named set.

The following code will describe the creation of a Named set Element:

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]                    ]**                                                                                                                                      |
|                                                                                                                                                                                                           |
| [NamedSetElement][ dimensionElementRow = [new] [NamedSetElement]();] |
|                                                                                                                                                                                                           |
| [// Specifying the dimension name]                                                                                                                      |
|                                                                                                                                                                                                           |
| [dimensionElementRow.Name = [\"Negative Margin Products\"];][]                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                          |
|                                                                                                                                                                                                           |
| [Dim][ dimensionElementRow [As] NamedSetElement = [New] NamedSetElement()] |
|                                                                                                                                                                                                           |
| [\' Specifying the dimension name]                                                                                                                      |
|                                                                                                                                                                                                           |
| [dimensionElementRow.Name = [\"Negative Margin Products\"]][]                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

