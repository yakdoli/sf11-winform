---
title: clipboardcut.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clipboardcut.md
created_at: 2025-07-03
---






#### ClipboardCut {#clipboardcut style="tab-stops: 0pt"}

[]{#p231}This event gets fired when some grid data is being moved to the clipboard. Inside this event handler, you can check for the data and range of cells being moved and cancel the operation if you don't want to move the data. You can also provide custom formatted data for moving to clipboard. It receives an argument of type GridCutCopyPasteEventArgs containing data related to this event. The following are the event argument properties.

 

Table 35: Property


  ------------ ------------------------------------------------------------------------------------------------------------
  Property     Description
  DataObject   Data being moved.
  RangeList    List of cell ranges that are selected for transfer.
  Handled      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------ ------------------------------------------------------------------------------------------------------------


**[]** 

Example

 

This event can be triggered[ ]using the following code:**[]**

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                 |
|                                                                                                                                                                            |
| **[]**                                                                                                                   |
|                                                                                                                                                                            |
| [gridControl.Model.ClipboardCut += [new] [GridCutPasteEventHandler](Model_ClipboardCut);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

**[]** 

The following event handler sets up new data for clipboard cut operation.

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                      |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [void][ Model_ClipboardCut([object] sender, GridCutPasteEventArgs e)] |
|                                                                                                                                                                                 |
| [{]                                                                                                                                         |
|                                                                                                                                                                                 |
| [    [if] (e.RangeList.Contains(GridRangeInfo.Row(2)))]                                                                |
|                                                                                                                                                                                 |
| [    {]                                                                                                                                     |
|                                                                                                                                                                                 |
| [        [string] newData = [\"Data for Row2\"];]                                              |
|                                                                                                                                                                                 |
| [        e.DataObject = [new] DataObject(newData);]                                                                    |
|                                                                                                                                                                                 |
| [        e.Handled = [true];]                                                                                          |
|                                                                                                                                                                                 |
| [    }]                                                                                                                                     |
|                                                                                                                                                                                 |
| [}]                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

