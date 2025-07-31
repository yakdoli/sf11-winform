---
title: howtoaccesstheobjectinagroupanddeleteremovethenode.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoaccesstheobjectinagroupanddeleteremovethenode.md
created_at: 2025-07-03
---








  









## How to access the object in a Group and delete / remove the node?[] {#how-to-access-the-object-in-a-group-and-delete-remove-the-node style="tab-stops: 0pt"}

[]{#p64}[] 

The first step is to check whether the node is a Group.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                           |
| []                                                                                                       |
|                                                                                                                                                           |
| [if][ (node [is] [Group])] |
|                                                                                                                                                           |
| [{]                                                                                                                   |
|                                                                                                                                                           |
| [// Your code here]                                                                                     |
|                                                                                                                                                           |
| [}]                                                                                                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                          |
|                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                             |
| [\' Your code here ]                                                                                                                      |
|                                                                                                                                                                                             |
| [If][ [TypeOf] node [Is] Group [Then] ] |
|                                                                                                                                                                                             |
| [End][ [If]]                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

If the node is a Group, then there are some special methods for it which are as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                             |
| [public][ [Node] GetChild([int] childIndex);]                |
|                                                                                                                                                                                             |
| [public][ [Node] GetChildByName([string] childName);]        |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [public][ [void] RemoveAllChildren();]                                            |
|                                                                                                                                                                                             |
| [public][ [bool] RemoveChild([int] childIndex);]             |
|                                                                                                                                                                                             |
| [public][ [bool] RemoveChild(Node nodeToRemove);]                                 |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [public][ [void] InsertChild(Node child, [int] childIndex);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Function] GetChild([ByVal] childIndex [As] [Integer]) [As] Syncfusion.Windows.Forms.Diagram.Node]                                   |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Function]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Function] GetChildByName([ByVal] childName [As] [String]) [As] Syncfusion.Windows.Forms.Diagram.Node]                               |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Function]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Sub] RemoveAllChildren()]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Function] RemoveChild([ByVal] childIndex [As] [Integer]) [As] [Boolean]]                                       |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Function]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Function] RemoveChild([ByVal] nodeToRemove [As] Syncfusion.Windows.Forms.Diagram.Node) [As] [Boolean]]                              |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Function]]                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                              |
| [Public][ [Sub] InsertChild([ByVal] child [As] Syncfusion.Windows.Forms.Diagram.Node, [ByVal] childIndex [As] [Integer])] |
|                                                                                                                                                                                                                                                                                                                                              |
| [End][ [Sub]]                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Also, Group has an int **ChildCount** property which returns the child count in a Group.

The below code will show how to delete the first element in a Group.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                          |
|                                                                                                                                                                                              |
| [foreach][ ([Node] node [in] DiagramWebControl1.Model.Nodes)] |
|                                                                                                                                                                                              |
| [{]                                                                                                                                                      |
|                                                                                                                                                                                              |
| [      [if] (node [is] [Group]) [// Check for Group]]               |
|                                                                                                                                                                                              |
| [      {]                                                                                                                                                |
|                                                                                                                                                                                              |
| [            [Group] groupNode = ([Group])node;]                                                               |
|                                                                                                                                                                                              |
| [      ]                                                                                                                                                 |
|                                                                                                                                                                                              |
| [            [if] (groupNode.ChildCount \> 0) [// Group has sub nodes]]                                       |
|                                                                                                                                                                                              |
| [            {]                                                                                                                                          |
|                                                                                                                                                                                              |
| [                  [Node] nodeToRemove = groupNode.GetChild(0);]                                                                    |
|                                                                                                                                                                                              |
| [                  groupNode.RemoveChild(nodeToRemove);]                                                                                                 |
|                                                                                                                                                                                              |
| [            }]                                                                                                                                          |
|                                                                                                                                                                                              |
| [      }]                                                                                                                                                |
|                                                                                                                                                                                              |
| [}]                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                     |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                    |
|                                                                                                                                                                                                                        |
| [For][ [Each] node [As] Node [In] DiagramWebControl1.Model.Nodes ] |
|                                                                                                                                                                                                                        |
| [    [If] [TypeOf] node [Is] Group [Then] ]                                                    |
|                                                                                                                                                                                                                        |
| [    [\' Check for Group ]]                                                                                                                                  |
|                                                                                                                                                                                                                        |
| [    [Dim] groupNode [As] Text.RegularExpressions.Group = [DirectCast](node, Group)]                                |
|                                                                                                                                                                                                                        |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [If] groupNode.ChildCount \> 0 [Then] ]                                                                                         |
|                                                                                                                                                                                                                        |
| [    [\' Group has sub nodes ]]                                                                                                                              |
|                                                                                                                                                                                                                        |
| [    [Dim] nodeToRemove [As] Syncfusion.Windows.Forms.Diagram.Node = groupNode.GetChild(0)]                                              |
|                                                                                                                                                                                                                        |
| [            groupNode.RemoveChild(nodeToRemove) ]                                                                                                                                 |
|                                                                                                                                                                                                                        |
| [        [End] [If] ]                                                                                                                    |
|                                                                                                                                                                                                                        |
| [    [End] [If] ]                                                                                                                        |
|                                                                                                                                                                                                                        |
| [Next]                                                                                                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

