---
title: multilevelundoandredo.md
original_path: WinForms_Docs/99_Uncategorized/multilevelundoandredo.md
created_at: 2025-08-05
---






##### MultiLevel Undo and Redo {#multilevel-undo-and-redo style="tab-stops: 0pt"}

[] 

Essential Grid has flexible support for **Multilevel Undo/Redo**. This feature enables the user to undo history for most actions that are performed. This feature can be enabled by setting the **CommandStack.Enabled** property to *true*. Using the functions of the **GridModelCommandManager** class, various tasks like undo and redo can be done. You can access this class from a Grid with the **CommandStack** property of a GridModel instance.

 

The Multilevel Undo/Redo feature can be enabled for Essential Grid by using the following code:

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                |
| []                                                                                                           |
|                                                                                                                                                                |
| [this][.gridControl1.CommandStack.Enabled = [true];] |
|                                                                                                                                                                |
| [this][.gridControl1.CommandStack.Undo();]                                |
|                                                                                                                                                                |
| [this][.gridControl1.CommandStack.Redo();]                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [Me][.gridControl1.CommandStack.Enabled = [True]] |
|                                                                                                                                                             |
| [Me][.gridControl1.CommandStack.Undo()]                                |
|                                                                                                                                                             |
| [Me][.gridControl1.CommandStack.Redo()]                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][123][: Multilevel Undo/Redo]*

 

[]{#p113} 

 

[]{#related-topics}

