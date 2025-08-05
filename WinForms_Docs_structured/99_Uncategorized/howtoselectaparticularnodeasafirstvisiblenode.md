---
title: howtoselectaparticularnodeasafirstvisiblenode.md
original_path: WinForms_Docs/99_Uncategorized/howtoselectaparticularnodeasafirstvisiblenode.md
created_at: 2025-08-05
---






#### How to select a particular node as a first visible node {#how-to-select-a-particular-node-as-a-first-visible-node style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

**[]** 

This can be done by using the code snippet given below. This will allow the user to make a particular node as the first visible node. The **EnsureVisibleSelectedNode** property will help the user to bring the invisible node into a visible state by scrolling the ScrollBar to the SelectedNode, if necessary.

[] 


  --------------------------- -----------------------------------------------------------------------------------
  TreeViewAdv Properties      Description
  EnsureVisibleSelectedNode   Indicates if the selected node will be brought to view by scrolling if necessary.
  --------------------------- -----------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                  |
| [private void][ Form1_Load(][object][ sender, System.EventArgs e) ]        |
|                                                                                                                                                                                                                                                                                  |
| [{ ]                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [this][.treeViewAdv1.SelectedNode=][this][.treeViewAdv1.LastVisibleNode; ] |
|                                                                                                                                                                                                                                                                                  |
| [this][.treeViewAdv1.SelectedNode=][this][.treeViewAdv1.Nodes\[3\]; ]      |
|                                                                                                                                                                                                                                                                                  |
| [// Setting EnsureVisibleSelectedNode property to true, makes a particular selected node as the first visible node. ]                                                                                                          |
|                                                                                                                                                                                                                                                                                  |
| [this][.treeViewAdv1.EnsureVisibleSelectedNode=][true][; ]                 |
|                                                                                                                                                                                                                                                                                  |
| [} ][]                                                                                                                                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Private Sub][ Form1_Load(][ByVal][ sender][ As Object][, ][ByVal][ e ][As][ System.EventArgs) ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.treeViewAdv1.SelectedNode=][Me][.treeViewAdv1.LastVisibleNode ]                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.treeViewAdv1.SelectedNode=][Me][.treeViewAdv1.Nodes(3) ]                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\' Setting EnsureVisibleSelectedNode property to true, makes a particular selected node as the first visible node. ]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [Me][.treeViewAdv1.EnsureVisibleSelectedNode=][True][ ]                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [End Sub ][]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

