---
title: draganddrop4.md
original_path: WinForms_Docs/99_Uncategorized/draganddrop4.md
created_at: 2025-08-05
---






##### Drag-and-drop {#drag-and-drop style="tab-stops: 0pt"}

 

The Edit Control fully supports the file drop functionality.**[ ]**Any text file can be dragged onto the Edit Control, which then displays the contents of the file, as if the file had been opened with the Edit Control.

 

The Edit Control also supports the text drag-and-drop**[ ]**functionality. In other words, you can drag a piece of text from one region in the Edit Control to another. You can also drag text from other editor controls like the RichTextBox onto the Edit Control. These features are supported out of the box, and no explicit handling of drag-and-drop operations are required.

 

Make sure to set the **AllowDrop** property of the Edit Control to **True** for this purpose.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                   |
| [// Enable drag and drop.]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                   |
| [this][.editControl1.AllowDrop = ][true][;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                       |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [\' Enable drag and drop.]                                                                                             |
|                                                                                                                                                                          |
| [Me][.[editControl1.]AllowDrop = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p82} 

[]{#related-topics}

