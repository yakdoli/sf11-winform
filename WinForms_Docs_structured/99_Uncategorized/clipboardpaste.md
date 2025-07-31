---
title: clipboardpaste.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clipboardpaste.md
created_at: 2025-07-03
---






#### ClipboardPaste {#clipboardpaste style="tab-stops: 0pt"}

This event gets fired when some grid data is being pasted from the clipboard. Inside this event handler, you can check for the data and range of cells being pasted and cancel the operation if you don't want to paste the data. You can also provide custom formatted data for saving into grid cells. It receives an argument of type GridCutCopyPasteEventArgs containing data related to this event. The following are the event argument properties.

**[]** 

Table 36: Property


  ------------ ------------------------------------------------------------------------------------------------------------
  Property     Description
  DataObject   Data being pasted.
  RangeList    List of cell ranges that are selected for pasting.
  Handled      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------ ------------------------------------------------------------------------------------------------------------


[] 

Example

 

This event can be triggered using the following code:    

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                     |
|                                                                                                                                                                                |
| **[]**                                                                                                                       |
|                                                                                                                                                                                |
| [gridControl.Model.ClipboardPaste += [new] [GridCutPasteEventHandler](Model_ClipboardPaste);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Event Handler

[] 

The following event handler sets up new data for clipboard paste.

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                        |
|                                                                                                                                                                                   |
| []                                                                                                                                            |
|                                                                                                                                                                                   |
| [void][ Model_ClipboardPaste([object] sender, GridCutPasteEventArgs e)] |
|                                                                                                                                                                                   |
| [{]                                                                                                                                           |
|                                                                                                                                                                                   |
| [    [if] (e.RangeList.Contains(GridRangeInfo.Row(2)))]                                                                  |
|                                                                                                                                                                                   |
| [    {]                                                                                                                                       |
|                                                                                                                                                                                   |
| [        [string] newData = [\"Data for Row2\"];]                                                |
|                                                                                                                                                                                   |
| [        e.DataObject = [new] DataObject(newData);]                                                                      |
|                                                                                                                                                                                   |
| [        e.Handled = [true];]                                                                                            |
|                                                                                                                                                                                   |
| [    }]                                                                                                                                       |
|                                                                                                                                                                                   |
| [}]                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

