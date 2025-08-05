---
title: selecteditem1.md
original_path: WinForms_Docs/99_Uncategorized/selecteditem1.md
created_at: 2025-08-05
---






#### SelectedItem {#selecteditem style="tab-stops: 0pt"}

**SelectedItem** is a property in the TileViewControl that stores the currently selected TileViewItem in it and it is similar to SelectedItem property in ComboBox. This will help you to return the currently selected TileViewItem. Also it allows only one item to be selected at a time.

[] 

Use Case Scenarios

This feature will be very useful who you want to get the SelectedItem.

[] 

Adding SelectedItem to an Application

The SelectedItem can be added to an application by using either XAML or C# code.

The following code example illustrates how to add the MinimizedHeaderTemaplte and MaximizedHeaderTemplate to an application through XAML.

 

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
| [      \<][syncfusion][:][TileViewItem][ x][:][Name][=\"Tile4\"][ Header][=\"TileViewItem 4\" /\>][ ][]                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][syncfusion][:][TileViewControl][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [this][.TileView.SelectedItem = Tile1;]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for properties, methods, and events

Properties

Table 53: SelectedItem Property Table

  -------------- -------------------------------------------- -------------------- ----------- -----------------
  Property       Description                                  Type                 Data Type   Reference links
  SelectedItem   Stores the currently selected TileViewItem   DependencyProperty   Object      
  -------------- -------------------------------------------- -------------------- ----------- -----------------

[] 

Events

Table 54: SelectedItemChanged Table

  Event                 Description                                                        Arguments   Type   Reference links
  --------------------- ------------------------------------------------------------------ ----------- ------ -----------------
  SelectedItemChanged   This event gets fired when the Selected TileViewItem is changed.                      

[] 

Sample Link

To view samples:

[] 

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Select   Run Locally Installed Samples in WPF Button.

3.   Now expand the DragAndDropManagerDemo tree-view item in the Sample Browser.

4.   Choose any one of the samples listed under it to launch.

[] 

[]{#related-topics}

