---
title: clipboardcancopy.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clipboardcancopy.md
created_at: 2025-07-03
---






#### ClipboardCanCopy {#clipboardcancopy style="tab-stops: 0pt"}

[]{#p227}This event is triggered when some grid data is about to be copied to the clipboard. Inside this event handler, you can check for the data and range of cells that are going to be copied, and cancel the operation if you don't want to copy those data.

 

1.   The grid cell data and range of cells that is going to be moved to the clipboard can be accessed by DataObject and RangeList properties ( refer to the Table below).

2.   If you don't want to move the data to the clipboard, you can cancel the operation by setting e.Cancel to true.

 

It receives an argument of type GridCutCopyPasteEventArgs containing data related to this event. The following are the event argument properties.

 

Table 31: Property


  ------------ ------------------------------------------------------------------------------------------------------------
  Property     Description
  DataObject   Data to be copied.
  RangeList    List of cell ranges that are selected for copying.
  Handled      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------ ------------------------------------------------------------------------------------------------------------


 

Example

 

This event can be triggered using the following code:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                         |
|                                                                                                                                                                                    |
| **[]**                                                                                                                           |
|                                                                                                                                                                                    |
| [gridControl.Model.ClipboardCanCopy += [new] [GridCutPasteEventHandler](Model_ClipboardCanCopy);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

The following event handler prevents the data in row 2 from getting copied.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                          |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [void][ Model_ClipboardCanCopy([object] sender, GridCutPasteEventArgs e)] |
|                                                                                                                                                                                     |
| [{]                                                                                                                                             |
|                                                                                                                                                                                     |
| [    [if](e.RangeList.Contains(GridRangeInfo.Row(2)))]                                                                     |
|                                                                                                                                                                                     |
| [    {]                                                                                                                                         |
|                                                                                                                                                                                     |
| [        e.Handled = [true];]                                                                                              |
|                                                                                                                                                                                     |
| [    }]                                                                                                                                         |
|                                                                                                                                                                                     |
| [}]                                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

