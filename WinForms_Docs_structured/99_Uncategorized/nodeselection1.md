---
title: nodeselection1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nodeselection1.md
created_at: 2025-07-03
---








  









### Node Selection {#node-selection style="tab-stops: 0pt"}

 

A selected node is indicated using a rectangular resizer over the node's border. Many interactions using keyboard, mouse will affect elements that is currently selected.

 

Properties

 

  ------------- ------------------------------------------------------------------------------------------------------------ ---------------------- ----------------------- -----------------------------------------------------
  Property      Description                                                                                                  Type of the property   Value it Accept         Any other dependencies/ sub properties associated
  AllowSelect   Gets or sets a value indicating whether the node can be selected or not. The default value is set to true.   Dependency property    Boolean (true/ false)   No[]
  IsSelected    Gets or sets a value indicating whether this instance is selected.                                           Dependency property    Boolean (true/ false)   No[]
  ------------- ------------------------------------------------------------------------------------------------------------ ---------------------- ----------------------- -----------------------------------------------------

 

A node can be selected in two ways namely:

 

[·      ]At run time

[·      ]Through code

 

A Node can be selected at run time just by clicking on the node.

 

{border="0"}

Figure 43: Node before Selection**[]**

 

 

{border="0"}

Figure 44: Node after Selection**[]**

 

 

 

The above two images differentiates the appearance of the node before and after selection.

 

The Node can also be selected using the IsSelected property of the Node.

 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\                                                                                                                                                                                                                                                                                                                                                                                                 |
| ][Node][ n = ][new][ ][Node][();] |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [n.Shape = [Shapes].FlowChart_Card;]                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [n.IsSelected = [true];]                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                    |
| [diagramModel.Nodes.Add(n);]                                                                                                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                          |
|                                                                                                                                                                                                                                         |
| [\                                                                                                                                                                                                                                      |
| ][Dim][ n [As] [New] [Node]()] |
|                                                                                                                                                                                                                                         |
| [n.Shape = Shapes.FlowChart_Card]                                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [n.IsSelected = [True]]                                                                                                                                                        |
|                                                                                                                                                                                                                                         |
| [diagramModel.Nodes.Add(n)][]                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#p28} 

[]{#_How_to_Specify_6}[]{#_How_to_Edit}[]{#_How_to_Specify_7}[]{#_How_to_Specify_8}[]{#_How_to_Specify_9}[]{#_How_to_Specify_11}[]{#_How_to_Specify_10}AllowSelect

[] 

The **AllowSelect** property can be used to enable/disable the node selection.\
\
When this property is set to **true**, it is possible to select the node. Otherwise the node cannot be selected.\
The default value is **true**.

 

The AllowSelect property can be set in the following way:

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| [\                                                                                                                                                                                                                            |
| ][Node][ nodeobject = [new] [Node]();] |
|                                                                                                                                                                                                                               |
| [nodeobject.AllowSelect = [false];]                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                  |
| [\                                                                                                                                                                                                                                               |
| ][Dim][ nodeobject [As] [New] [Node]()] |
|                                                                                                                                                                                                                                                  |
| [nodeobject.AllowSelect = [False]][]                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p36}See Also:

\
[Select Nodes and Connectors]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

