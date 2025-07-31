---
title: clipboardcancut.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clipboardcancut.md
created_at: 2025-07-03
---






#### ClipboardCanCut[]{#p228} {#clipboardcancut style="tab-stops: 0pt"}

This event is triggered when some grid data is about to be moved to the clipboard. Inside this event handler, you can check for the data and range of cells going to be moved and cancel the operation if you do not want to move the data. It receives an argument of type GridCutCopyPasteEventArgs containing data related to this event. The following are the event argument properties.

 

Table 32: Property


  ------------ ------------------------------------------------------------------------------------------------------------
  Property     Description
  DataObject   Data to be moved.
  RangeList    List of cell ranges that are selected for moving.
  Handled      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------ ------------------------------------------------------------------------------------------------------------


 

Example

 

This event can be triggered using the following code:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                       |
|                                                                                                                                                                                  |
| **[]**                                                                                                                         |
|                                                                                                                                                                                  |
| [gridControl.Model.ClipboardCanCut += [new] [GridCutPasteEventHandler](Model_ClipboardCanCut);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

The following event handler prevents the data in row 2 from getting cut.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                         |
|                                                                                                                                                                                    |
| []                                                                                                                                             |
|                                                                                                                                                                                    |
| [void][ Model_ClipboardCanCut([object] sender, GridCutPasteEventArgs e)] |
|                                                                                                                                                                                    |
| [{]                                                                                                                                            |
|                                                                                                                                                                                    |
| [    [if] (e.RangeList.Contains(GridRangeInfo.Row(2)))]                                                                   |
|                                                                                                                                                                                    |
| [    {]                                                                                                                                        |
|                                                                                                                                                                                    |
| [        e.Handled = [true];]                                                                                             |
|                                                                                                                                                                                    |
| [    }]                                                                                                                                        |
|                                                                                                                                                                                    |
| [}]                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

