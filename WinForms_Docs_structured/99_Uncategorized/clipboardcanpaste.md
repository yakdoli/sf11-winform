---
title: clipboardcanpaste.md
original_path: WinForms_Docs/99_Uncategorized/clipboardcanpaste.md
created_at: 2025-08-05
---






#### ClipboardCanPaste {#clipboardcanpaste style="tab-stops: 0pt"}

[]{#p229}This event gets fired when some grid data is about to be pasted from the clipboard. Inside this event handler, you can check for the data and range of cells going to be pasted and cancel the operation if you don't want to paste the data. It receives an argument of type GridCutCopyPasteEventArgs containing data related to this event. The following are the event argument properties.

 

Table 33: Property


  ------------ ------------------------------------------------------------------------------------------------------------
  Property     Description
  DataObject   Data to be pasted.
  RangeList    List of cell ranges that are selected for pasting.
  Handled      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------ ------------------------------------------------------------------------------------------------------------


 

Example

 

This event can be triggered using the following code:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                           |
|                                                                                                                                                                                      |
| **[]**                                                                                                                             |
|                                                                                                                                                                                      |
| [gridControl.Model.ClipboardCanPaste += [new] [GridCutPasteEventHandler](Model_ClipboardCanPaste);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Event Handler

 

The following event handler prevents the data in row 2 from getting pasted.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                                           |
|                                                                                                                                                                                      |
| **[]**                                                                                                                             |
|                                                                                                                                                                                      |
| [void][ Model_ClipboardCanPaste([object] sender, GridCutPasteEventArgs e)] |
|                                                                                                                                                                                      |
| [{]                                                                                                                                              |
|                                                                                                                                                                                      |
| [    [if] (e.RangeList.Contains(GridRangeInfo.Row(2)))]                                                                     |
|                                                                                                                                                                                      |
| [    {]                                                                                                                                          |
|                                                                                                                                                                                      |
| [        e.Handled = [true];]                                                                                               |
|                                                                                                                                                                                      |
| [    }]                                                                                                                                          |
|                                                                                                                                                                                      |
| [}]                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#_ClipboardCopy} 

[]{#related-topics}

