---
title: clipboardcopy.md
original_path: WinForms_Docs/99_Uncategorized/clipboardcopy.md
created_at: 2025-08-05
---






#### ClipboardCopy {#clipboardcopy style="tab-stops: 0pt"}

[]{#p230}This event gets fired when some grid data is being copied to the clipboard. Inside this event handler, you can check for the data and range of cells being copied and cancel the operation if you don't want to copy the data. You can also provide custom formatted data for copying to clipboard. It receives an argument of type GridCutCopyPasteEventArgs containing data related to this event. The following are the event argument properties.

 

Table 34: Property


  ------------ ------------------------------------------------------------------------------------------------------------
  Property     Description
  DataObject   Data being copied.
  RangeList    List of cell ranges that are selected for copying.
  Handled      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------ ------------------------------------------------------------------------------------------------------------


 

Example

 

This event can be triggered using the following code:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                   |
|                                                                                                                                                                              |
| **[]**                                                                                                                     |
|                                                                                                                                                                              |
| [gridControl.Model.ClipboardCopy += [new] [GridCutPasteEventHandler](Model_ClipboardCopy);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

The following event handler sets up new data for clipboard copy.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                       |
|                                                                                                                                                                                  |
| **[]**                                                                                                                         |
|                                                                                                                                                                                  |
| [void][ Model_ClipboardCopy([object] sender, GridCutPasteEventArgs e)] |
|                                                                                                                                                                                  |
| [{]                                                                                                                                          |
|                                                                                                                                                                                  |
| [    [if] (e.RangeList.Contains(GridRangeInfo.Row(2)))]                                                                 |
|                                                                                                                                                                                  |
| [    {]                                                                                                                                      |
|                                                                                                                                                                                  |
| [        [string] newData = [\"Data for Row2\"];]                                               |
|                                                                                                                                                                                  |
| [        e.DataObject = [new] DataObject(newData);]                                                                     |
|                                                                                                                                                                                  |
| [        e.Handled = [true];]                                                                                           |
|                                                                                                                                                                                  |
| [    }]                                                                                                                                      |
|                                                                                                                                                                                  |
| [}]                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

