---
title: howtoreturnthenodeataspecifiedlocation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoreturnthenodeataspecifiedlocation.md
created_at: 2025-07-03
---






#### How to return the node at a specified location {#how-to-return-the-node-at-a-specified-location style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

**GetNodeAtPoint** method will get or returns the node at the specified location. There are three overloads for this method. This method can be called inside DragOver event. The parameters are as follows. To return the node at the specified point, **GetNodeAtPointEx** method can be called.

[] 


  ------------------- -----------------------------------------------------------------------------------------------------------------
  Parameter           Description
  pt                  Indicates the location.
  textbounds          Indicates whether testing will be done using the bounds of text and not the whole bounds of the node.
  textOrImageBounds   Indicates whether testing will be done using the bounds of image and text and not the whole bounds of the node.
  ------------------- -----------------------------------------------------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| **[]**                                                                                                                                             |
|                                                                                                                                                                                                      |
| [Point][ ptInTree = treeView.PointToClient([new] [Point](e.X, e.Y));] |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [//Gets the node point at the specified location]                                                                                                  |
|                                                                                                                                                                                                      |
| [this][.treeViewAdv1.GetNodeAtPoint(ptInTree);]                                                                 |
|                                                                                                                                                                                                      |
| [//Gets the node point at the specified location, uses the bounds of text]                                                                         |
|                                                                                                                                                                                                      |
| [this][.treeViewAdv1.GetNodeAtPoint(ptInTree, [true]);]                                    |
|                                                                                                                                                                                                      |
| [//Gets the node point at the specified location, uses the bounds of text and bounds of image and text]                                            |
|                                                                                                                                                                                                      |
| [this][.treeViewAdv1.GetNodeAtPoint(ptInTree, [true], [true]);]       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [//Gets the node point at the specified Point]                                                                                                     |
|                                                                                                                                                                                                      |
| [this][.treeViewAdv1.GetNodeAtPointEx(ptInTree);][]                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                  |
|                                                                                                                                                                                                     |
| **[]**                                                                                                                                            |
|                                                                                                                                                                                                     |
| [Point][ ptInTree = treeView.PointToClient([new] [Point](e.X, e.Y))] |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [\'Gets the node point at the specified location]                                                                                                 |
|                                                                                                                                                                                                     |
| [Me][.treeViewAdv1.GetNodeAtPoint(ptInTree)]                                                                   |
|                                                                                                                                                                                                     |
| [\'Gets the node point at the specified location, uses the bounds of text]                                                                        |
|                                                                                                                                                                                                     |
| [Me][.treeViewAdv1.GetNodeAtPoint(ptInTree, [True])]                                      |
|                                                                                                                                                                                                     |
| [\'Gets the node point at the specified location, uses the bounds of text and bounds of image and text]                                           |
|                                                                                                                                                                                                     |
| [Me][.treeViewAdv1.GetNodeAtPoint(ptInTree, [True], [True])]         |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [Gets the node point at the specified Point]                                                                                                      |
|                                                                                                                                                                                                     |
| [Me][.treeViewAdv1.GetNodeAtPointEx(ptInTree)][]                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[[Drag and Drop]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_Drag_And_Drop)[]{.UGHyperlink}

 

 

[]{#related-topics}

