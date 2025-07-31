---
title: grouping6.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\grouping6.md
created_at: 2025-07-03
---








  









### Grouping {#grouping style="tab-stops: 0pt"}

[] 

A group is a node that acts as a transparent container for other nodes. A group is a composite node that controls a set of child nodes. The bounding rectangle of a group is the union of the bounds of its children. The group renders itself by iterating through its children and rendering them. Child nodes cannot be selected or manipulated individually. Members of the group are added and removed through the ICompositeNode interface.

 

There are two ways available to add a Group in diagram control:

 

1\. Add the children to the group manually with the help of Group class methods. The below code snippet creates a group with two nodes.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [//Node 1]                                                                                                                                                |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [Syncfusion.Windows.Forms.Diagram.Rectangle nodeRect = [new] Syncfusion.Windows.Forms.Diagram.Rectangle(50, 100, 125, 75);]                        |
|                                                                                                                                                                                                                             |
| [nodeRect.FillStyle.Color = Color.FromArgb(255, 223, 189);]                                                                                                             |
|                                                                                                                                                                                                                             |
| [nodeRect.LineStyle.LineColor = Color.Orange;]                                                                                                                          |
|                                                                                                                                                                                                                             |
| [Syncfusion.Windows.Forms.Diagram.Label lbl = [new] Syncfusion.Windows.Forms.Diagram.Label(nodeRect, [\"Rectangle\"]);]    |
|                                                                                                                                                                                                                             |
| [lbl.FontStyle.Size = 12;]                                                                                                                                              |
|                                                                                                                                                                                                                             |
| [lbl.FontStyle.Bold = [true];]                                                                                                                     |
|                                                                                                                                                                                                                             |
| [nodeRect.Labels.Add(lbl);]                                                                                                                                             |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [//Node 2]                                                                                                                                                |
|                                                                                                                                                                                                                             |
| [Syncfusion.Windows.Forms.Diagram.Rectangle nodeRect1 = [new] Syncfusion.Windows.Forms.Diagram.Rectangle(150, 100, 125, 75);]                      |
|                                                                                                                                                                                                                             |
| [nodeRect1.FillStyle.Color = Color.FromArgb(255, 223, 189);]                                                                                                            |
|                                                                                                                                                                                                                             |
| [nodeRect1.LineStyle.LineColor = Color.Orange;]                                                                                                                         |
|                                                                                                                                                                                                                             |
| [Syncfusion.Windows.Forms.Diagram.Label lbl1 = [new] Syncfusion.Windows.Forms.Diagram.Label(nodeRect1, [\"Rectangle1\"]);] |
|                                                                                                                                                                                                                             |
| [lbl1.FontStyle.Size = 12;]                                                                                                                                             |
|                                                                                                                                                                                                                             |
| [lbl1.FontStyle.Bold = [true];]                                                                                                                    |
|                                                                                                                                                                                                                             |
| [nodeRect1.Labels.Add(lbl1);]                                                                                                                                           |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [//Grouping Nodes]                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [Syncfusion.Windows.Forms.Diagram.Group grp = [new] Group();]                                                                                      |
|                                                                                                                                                                                                                             |
| [grp.AppendChild(nodeRect);]                                                                                                                                            |
|                                                                                                                                                                                                                             |
| [grp.AppendChild(nodeRect1);]                                                                                                                                           |
|                                                                                                                                                                                                                             |
| [this][.DiagramWebControl1.Model.AppendChild(grp);]                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2\. Diagram control support two direct methods for Grouping and UnGrouping as follows.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [this][.diagram1.Controller.Group();     [//Method to Group the nodes]]   |
|                                                                                                                                                                                                                      |
| [this][.diagram1.Controller.UnGroup();   [//Method to UnGroup the nodes]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

How to access the child nodes in a Group, and how to delete / remove the node

**[]** 

The first step is to check whether the node is a Group.

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                                    |
| **[]**                                                                           |
|                                                                                                                                    |
| [if][ (node [is] Group)] |
|                                                                                                                                    |
| [{]                                                                                            |
|                                                                                                                                    |
| [    [// Your code here]]                                                |
|                                                                                                                                    |
| [}]                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

If the node is a Group, then following are some special methods.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [public][ Node GetChild([int] childIndex);]                                       |
|                                                                                                                                                                                             |
| [public][ Node GetChildByName([string] childName);]                               |
|                                                                                                                                                                                             |
| [public][ [void] RemoveAllChildren();]                                            |
|                                                                                                                                                                                             |
| [public][ [bool] RemoveChild([int] childIndex);]             |
|                                                                                                                                                                                             |
| [public][ [bool] RemoveChild(Node nodeToRemove);]                                 |
|                                                                                                                                                                                             |
| [public][ [void] InsertChild(Node child, [int] childIndex);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Also, Group has an int **ChildCount** property, which returns the child count in a Group. To delete the first element in a Group, use the below code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                              |
|                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                             |
| [foreach][ (Node node [in] Diagram1.Model.Nodes)] |
|                                                                                                                                                             |
| [{]                                                                                                                     |
|                                                                                                                                                             |
| [    [if] (node [is] Group) [// Check for Group]]       |
|                                                                                                                                                             |
| [    {]                                                                                                                 |
|                                                                                                                                                             |
| [        Group groupNode = (Group)node;]                                                                                |
|                                                                                                                                                             |
| [        [if] (groupNode.ChildCount \> 0) [// Group has sub nodes]]          |
|                                                                                                                                                             |
| [        {]                                                                                                             |
|                                                                                                                                                             |
| [            Node nodeToRemove = groupNode.GetChild(0);]                                                                |
|                                                                                                                                                             |
| [            groupNode.RemoveChild(nodeToRemove);]                                                                      |
|                                                                                                                                                             |
| []                                                                                                                      |
|                                                                                                                                                             |
| [        }]                                                                                                             |
|                                                                                                                                                             |
| [    }]                                                                                                                 |
|                                                                                                                                                             |
| [}]                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 85: Group Node

More:





