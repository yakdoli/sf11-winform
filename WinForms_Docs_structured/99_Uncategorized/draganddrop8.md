---
title: draganddrop8.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\draganddrop8.md
created_at: 2025-07-03
---






#### Drag--and-Drop {#dragand-drop style="tab-stops: 0pt"}

Drag-and-Drop enables you to drag the TileViewItems in TileViewControl in a normal state. Once the TileViewItem is dragged, the other items in the TileViewControl moves to the corresponding positions in accordance to the dragging item. This can be enabled and disabled by using the **AllowItemsRepositioning** property.

[] 

Adding Dragging Items to an Application

The Dragging items can be added to an application by using either XAML or C# code.

[] 

Adding through XAML

The following code example illustrates how to add the Dragging Items to an application through XAML.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][TileViewControl][ Name][=\"tileViewCntrl\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [                            AllowItemRepositioning][=\"True\"/\>]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [              ]                                                                                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Adding through C#

The following code example illustrates how to add the Dragging Items to an application through C#.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                          |
|                                                                                                                                                           |
| **[]**                                                                                                                |
|                                                                                                                                                           |
| [tileViewCntrl.AllowItemRepositioning = true;][   ] |
|                                                                                                                                                           |
| [           ]                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Tables for properties, methods, and events

Properties

Table 48: MinimizedItemTemplate / MaximizedItemTemplate Properties Table

  ------------------------ ------------------------------------------------------ -------------------- ----------- -----------------
  Property                 Description                                            Type                 Data Type   Reference links
  AllowItemRepositioning   Enables or disables the TileViewItems from dragging.   DependencyProperty   True        
  ------------------------ ------------------------------------------------------ -------------------- ----------- -----------------

[] 

Events

Table 49: AllowItemRepositioningChanged Table

  Event                           Description                                                                    Arguments   Type   Reference links
  ------------------------------- ------------------------------------------------------------------------------ ----------- ------ -----------------
  AllowItemRepositioningChanged   The event gets fired when the dragging items feature is enabled or disabled.                      

[] 

Sample Link

To view samples:

[] 

1.   Select Start -\> Programs -\> Syncfusion -\> Essential Studio x.x.xx -\> Dashboard.

2.   Select   Run Locally Installed Samples in WPF Button.

3.   Now expand the DragAndDropManagerDemo tree-view item in the Sample Browser.

4.   Choose any one of the samples listed under it to launch.

 

[]{#related-topics}

