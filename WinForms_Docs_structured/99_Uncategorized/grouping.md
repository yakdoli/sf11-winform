---
title: grouping.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\grouping.md
created_at: 2025-07-03
---








  









### Grouping[] {#grouping style="tab-stops: 0pt"}

[] 

A group is a node that acts as a transparent container for other nodes. A group is a composite node that controls a set of child nodes. The bounding rectangle of a group is the union of the bounds of its children. The group renders itself by iterating through its children and rendering them. Child nodes cannot be selected or manipulated individually. Members of the group are added and removed through the ICompositeNode interface.

 

The below code snippet creates a group with two nodes.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [//Node 1]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [Syncfusion.Windows.Forms.Diagram.[Rectangle] nodeRect = [new] Syncfusion.Windows.Forms.Diagram.[Rectangle](50, 100, 125, 75);]                       |
|                                                                                                                                                                                                                                                          |
| [nodeRect.FillStyle.Color = [Color].FromArgb(255, 223, 189);]                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [nodeRect.LineStyle.LineColor = [Color].Orange;]                                                                                                                                                |
|                                                                                                                                                                                                                                                          |
| [Syncfusion.Windows.Forms.Diagram.[Label] lbl = [new] Syncfusion.Windows.Forms.Diagram.[Label](nodeRect, [\"Rectangle\"]);]    |
|                                                                                                                                                                                                                                                          |
| [lbl.FontStyle.Size = 12;]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                          |
| [lbl.FontStyle.Bold = [true];]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [nodeRect.Labels.Add(lbl);]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [//Node 2]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                          |
| [Syncfusion.Windows.Forms.Diagram.[Rectangle] nodeRect1 = [new] Syncfusion.Windows.Forms.Diagram.[Rectangle](150, 100, 125, 75);]                     |
|                                                                                                                                                                                                                                                          |
| [nodeRect1.FillStyle.Color = [Color].FromArgb(255, 223, 189);]                                                                                                                                  |
|                                                                                                                                                                                                                                                          |
| [nodeRect1.LineStyle.LineColor = [Color].Orange;]                                                                                                                                               |
|                                                                                                                                                                                                                                                          |
| [Syncfusion.Windows.Forms.Diagram.[Label] lbl1 = [new] Syncfusion.Windows.Forms.Diagram.[Label](nodeRect1, [\"Rectangle1\"]);] |
|                                                                                                                                                                                                                                                          |
| [lbl1.FontStyle.Size = 12;]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                          |
| [lbl1.FontStyle.Bold = [true];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                          |
| [nodeRect1.Labels.Add(lbl1);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                          |
| [//Grouping Nodes]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                          |
| [Syncfusion.Windows.Forms.Diagram.[Group] grp = [new] [Group]();]                                                                                     |
|                                                                                                                                                                                                                                                          |
| [grp.AppendChild(nodeRect);]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                          |
| [grp.AppendChild(nodeRect1);]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                          |
| [this][.DiagramWebControl1.Model.AppendChild(grp);]                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                            |
| [\'Node 1]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| [Dim][ nodeRect [As] Syncfusion.Windows.Forms.Diagram.Rectangle = [New] Syncfusion.Windows.Forms.Diagram.Rectangle(50, 100, 125, 75)]                       |
|                                                                                                                                                                                                                                                                                            |
| [nodeRect.FillStyle.Color = Color.FromArgb(255, 223, 189)]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [nodeRect.LineStyle.LineColor = Color.Orange]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                            |
| [Dim ][lbl [As] Syncfusion.Windows.Forms.Diagram.Label = [New] Syncfusion.Windows.Forms.Diagram.Label(nodeRect, [\"Rectangle\"])]    |
|                                                                                                                                                                                                                                                                                            |
| [lbl.FontStyle.Size = 12]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                            |
| [lbl.FontStyle.Bold = [True]]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [nodeRect.Labels.Add(lbl)]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [\'Node 2]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| [Dim][ nodeRect1 [As] Syncfusion.Windows.Forms.Diagram.Rectangle = [New] Syncfusion.Windows.Forms.Diagram.Rectangle(150, 100, 125, 75)]                     |
|                                                                                                                                                                                                                                                                                            |
| [nodeRect1.FillStyle.Color = Color.FromArgb(255, 223, 189)]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [nodeRect1.LineStyle.LineColor = Color.Orange]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [Dim][ lbl1 [As] Syncfusion.Windows.Forms.Diagram.Label = [New] Syncfusion.Windows.Forms.Diagram.Label(nodeRect1, [\"Rectangle1\"])] |
|                                                                                                                                                                                                                                                                                            |
| [lbl1.FontStyle.Size = 12]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| [lbl1.FontStyle.Bold = [True]]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| [nodeRect1.Labels.Add(lbl1)]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [\'Grouping Nodes]                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [Dim][ grp [As] Syncfusion.Windows.Forms.Diagram.Group = [New] Syncfusion.Windows.Forms.Diagram.Group()]                                                    |
|                                                                                                                                                                                                                                                                                            |
| [grp.AppendChild(nodeRect)]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [grp.AppendChild(nodeRect1)]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                            |
| [Me][.DiagramWebControl1.Model.AppendChild(grp)]                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 16: Selecting a Group in a Diagram

 

[]{#related-topics}

