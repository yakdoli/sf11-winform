---
title: clipboardcut2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clipboardcut2.md
created_at: 2025-07-03
---






##### ClipboardCut {#clipboardcut style="TEXT-ALIGN: justify; tab-stops: 0pt"}

This event is fired when some grid data is being moved to the clipboard. Inside this event handler, you can check for the data and range of cells being moved and cancel the operation if you don't want to move the data. You can also provide custom formatted data for moving to clipboard. It receives an argument of type **GridCutCopyPasteEventArgs** containing data related to this event. The following are the event argument properties.

 

Properties*[]*

  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------
  **[Property]**                         **[Description][]**
  DataObject[]   Data to be moved.[]
  RangeList                                                    List of cell ranges that are selected for transfer.
  Handled                                                      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------

 

[]{#related-topics}

