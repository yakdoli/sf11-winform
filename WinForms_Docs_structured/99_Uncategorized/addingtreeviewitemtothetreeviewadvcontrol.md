---
title: addingtreeviewitemtothetreeviewadvcontrol.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingtreeviewitemtothetreeviewadvcontrol.md
created_at: 2025-07-03
---






#### Adding TreeView Item to the TreeViewAdv Control {#adding-treeview-item-to-the-treeviewadv-control style="tab-stops: 0pt"}

[] 

The TreeviewItem is added to a TreeViewAdv control either by using XAML or Procedural code. The following code example lets you to create and add treeview items to the TreeViewAdv.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<!\-- Adding TreeViewAdv \--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\<][syncfusion][:][TreeViewAdv][ Name][=\"treeView1\"\>]                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<!\-- Adding TreeViewItemAdv \--\>]                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [    ][\<][syncfusion][:][TreeViewItemAdv][ Header][=\"Marital Status\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][syncfusion][:][TreeViewAdv][\>]                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Creating an instance of TreeViewAdv]                                                                                                                            |
|                                                                                                                                                                                                                                       |
| [TreeViewAdv][ treeViewAdv = [new] [TreeViewAdv]();]             |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Creating an instance of TreeViewItem]                                                                                                                           |
|                                                                                                                                                                                                                                       |
| [TreeViewItemAdv][ treeViewItemAdv = [new] [TreeViewItemAdv]();] |
|                                                                                                                                                                                                                                       |
| [treeViewItemAdv.Header = [\"TreeViewItem\"];]                                                                                                            |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Adding treeviewitem to treeview]                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [treeViewAdv.Items.Add(treeViewItemAdv);]                                                                                                                                         |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [// Adding content to the window]                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [this][.Content = treeViewAdv;]                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: To display the TreeViewItem, you must already have a TreeViewAdv in which you are going to add the TreeViewItem.


[]{#p576} 

[]{#related-topics}

