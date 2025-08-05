---
title: thebasics.md
original_path: WinForms_Docs/99_Uncategorized/thebasics.md
created_at: 2025-08-05
---






##### The Basics {#the-basics style="tab-stops: 0pt"}

[] 

Essential Grid[ ]has a **GridCommandStack** class that implements support for the Undo/Redo commands in a grid. Depending upon the grid settings, as a user makes changes to the grid these changes will be tracked in stack structures which, will be found in the GridCommandStack class. This class has methods that will allow you to undo the last action, redo the last undone action and batch transactions so that a series of actions can be undone or redone in a single step.

 

The **CommandStack** property of the **GridControl** class will return a reference to the GridCommandStack object  that is associated with a grid. It is through this property that you can access the Undo/Redo support in an Essential Grid. For example, you can use the enabled property of the CommandStack to control whether or not the grid is supporting an Undo/Redo at any given moment. Here are the code samples that show you some CommandStack properties.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [// Turn off the Undo buffer. ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                               |
| [this][.gridControl1.CommandStack.Enabled = ][false][;] |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [// Turn on the Undo buffer.]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                               |
| [this][.gridControl1.CommandStack.Enabled = ][true][;]  |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [// Clear the Undo buffer.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [this][.gridControl1.CommandStack.UndoStack.Clear();]                                                                                                      |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [// Clear the Redo buffer.]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                               |
| [this][.gridControl1.CommandStack.RedoStack.Clear();]                                                                                                      |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                               |
| [// Clear both the Undo and Redo buffers.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                               |
| [this][.gridControl1.CommandStack.Clear();]                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\' Turn off the Undo buffer.  ]                                                                                                                     |
|                                                                                                                                                                                                        |
| [Me][.gridControl1.CommandStack.Enabled = ][False] |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\' Turn on the Undo buffer.]                                                                                                                        |
|                                                                                                                                                                                                        |
| [Me][.gridControl1.CommandStack.Enabled = ][True]  |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\' Clear the Undo buffer.]                                                                                                                          |
|                                                                                                                                                                                                        |
| [Me][.gridControl1.CommandStack.UndoStack.Clear()]                                                  |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\' Clear the Redo buffer.]                                                                                                                          |
|                                                                                                                                                                                                        |
| [Me][.gridControl1.CommandStack.RedoStack.Clear()]                                                  |
|                                                                                                                                                                                                        |
| []                                                                                                                                                   |
|                                                                                                                                                                                                        |
| [\' Clear both the Undo and Redo buffers.]                                                                                                           |
|                                                                                                                                                                                                        |
| [Me][.gridControl1.CommandStack.Clear()]                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p296} 

 

[]{#related-topics}

