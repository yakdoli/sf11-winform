---
title: howtocleartheundobufferinessentialedit.md
original_path: WinForms_Docs/99_Uncategorized/howtocleartheundobufferinessentialedit.md
created_at: 2025-08-05
---








  









## How To Clear the Undo Buffer In Essential Edit {#how-to-clear-the-undo-buffer-in-essential-edit style="tab-stops: 0pt"}

[   ]

You can use the **ResetUndoInfo** method to clear the undo buffer, and save the changes to the underlying stream. This is done to make sure that the changes on the contents/actions recently performed cannot be undone.

[] 

The Following code snippet illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                               |
|                                                                                                                              |
| []                                                                         |
|                                                                                                                              |
| [// Code to clear the Undo buffer]                                         |
|                                                                                                                              |
| [this][.editcontrol1.ResetUndoInfo();]  |
|                                                                                                                              |
| []                                                                                       |
|                                                                                                                              |
| [// Code to discard all the Unsaved changes]                               |
|                                                                                                                              |
| [this][.editControl1.DiscardChanges();] |
+------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                        |
|                                                                                                                           |
| []                                                                      |
|                                                                                                                           |
| [\' Code to clear the Undo buffer]                                      |
|                                                                                                                           |
| [Me][.editcontrol1.ResetUndoInfo()]  |
|                                                                                                                           |
| []                                                                                    |
|                                                                                                                           |
| [\' Code to discard all the Unsaved changes]                            |
|                                                                                                                           |
| [Me][.editControl1.DiscardChanges()] |
+---------------------------------------------------------------------------------------------------------------------------+

[]{#p185} 

[]{#related-topics}

