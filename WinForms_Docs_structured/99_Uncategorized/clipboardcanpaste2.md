---
title: clipboardcanpaste2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clipboardcanpaste2.md
created_at: 2025-07-03
---






##### ClipboardCanPaste {#clipboardcanpaste style="TEXT-ALIGN: justify; tab-stops: 0pt"}

This event is fired when some grid data is about to be pasted from the clipboard. Inside this event handler, you can check for the data and range of cells going to be pasted and cancel the operation if you don't want to paste the data. It receives an argument of type **GridCutCopyPasteEventArgs** containing data related to this event. The following are the event argument properties.

 

Properties*[]*

  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------
  **[Property]**                         **[Description][]**
  DataObject[]   Data to be pasted.[]
  RangeList                                                    List of cell ranges that are selected for pasting.
  Handled                                                      When true, indicates that the event has been handled and no further processing of the event should happen.
  ------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------

 

[]{#related-topics}

