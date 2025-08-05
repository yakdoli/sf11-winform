---
title: isselected1.md
original_path: WinForms_Docs/99_Uncategorized/isselected1.md
created_at: 2025-08-05
---






#### IsSelected {#isselected style="tab-stops: 0pt"}

**IsSelected** is a boolean property in the TileViewItem which is used to select a particular TileViewItem. If the IsSelected property of a TileViewItem is set to True, the set TileViewItems opacity is set to 1 and the remaining TileViewItems opacity will be reduced to show the difference.

[] 

Use Case Scenarios

This feature will be very useful when you who want to select a particular TileViewItem.

[] 

Adding IsSelected to an Application

IsSelected can be added to an application by using either XAML or C# code.

The following code example illustrates how to add the IsSelected to an application.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][syncfusion][:][TileViewControl][ x][:][Name][=\"TileView\"][ Height][=\"600\"][ Width][=\"800\"\>][] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [      ][\<][syncfusion][:][TileViewItem][ x][:][Name][=\"Tile1\"][ Header][=\"TileViewItem 1\" /\>]                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [      \<][syncfusion][:][TileViewItem][ x][:][Name][=\"Tile2\"][ Header][=\"TileViewItem 2\" /\>][]                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [      \<][syncfusion][:][TileViewItem][ x][:][Name][=\"Tile3\"][ Header][=\"TileViewItem 3\" /\>]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [      \<][syncfusion][:][TileViewItem][ x][:][Name][=\"Tile4\"][ Header][=\"TileViewItem 4\" ]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [                               ][IsSelected][=\"True\" /\>][ ][]                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][syncfusion][:][TileViewControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                             |
| [      [TileViewControl] Tile = [new] [TileViewControl]();]                        |
|                                                                                                                                                                                             |
| [      TileViewItem][ item1 = [new] [TileViewItem]();] |
|                                                                                                                                                                                             |
| [      item1.IsSelected = true;]                                                                                                                        |
|                                                                                                                                                                                             |
| [      ]                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Properties

Table 55: IsSelected Property Table

  ------------ --------------------------------------------- -------------------- ----------- -----------------
  Property     Description                                   Type                 Data Type   Reference links
  IsSelected   Allows to select a particular TileViewItem.   DependencyProperty   False       
  ------------ --------------------------------------------- -------------------- ----------- -----------------

**[]** 

Sample Link

To view samples:

[] 

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Select   Run Locally Installed Samples in WPF Button.

3.   Now expand the DragAndDropManagerDemo tree-view item in the Sample Browser.

4.   Choose any one of the samples listed under it to launch.

 

[]{#related-topics}

