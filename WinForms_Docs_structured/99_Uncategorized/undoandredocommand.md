---
title: undoandredocommand.md
original_path: WinForms_Docs/99_Uncategorized/undoandredocommand.md
created_at: 2025-08-05
---








  









### Undo and Redo Command {#undo-and-redo-command style="tab-stops: 0pt"}

**Undo** command reverses the last action performed. For example: Some of the basic operations like translation, rotation, resizing, grouping, ungrouping, changing z-order, addition, deletion etc., which are performed on diagram objects (Nodes and Line Connectors) can be reversed. **Redo** command undoes the last Undo action. Alternatively these commands can be executed using the keyboard shortcuts; **Ctrl +Z** for Undo command and **Ctrl+Y** for Redo command.

[] 

Undo Command can be specified in the following way.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [DiagramCommandManager][.Undo.Execute(diagramView.Page, diagramView);]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                  |
|                                                                                                                                                                                           |
| [DiagramCommandManager][.Undo.Execute(diagramView.Page, diagramView)**[]**] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

Redo Command can be specified in the following way.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [DiagramCommandManager][.Redo.Execute(diagramView.Page, diagramView);]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| **[]**                                                                                                                                  |
|                                                                                                                                                                                           |
| [DiagramCommandManager][.Redo.Execute(diagramView.Page, diagramView)**[]**] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#p91} 

[]{#_How_to_disable}Disable Undo and Redo[]

Disabling Undo and Redo is helpful when the Diagram control has large number of nodes and line connectors where insertion and deletion are very frequently used. This property can be disabled so that all the references are removed for the stack. This implies that deleted nodes will lose their references and Garbage collected.

 

Table 73: Property Table

  ----------------- ---------------------------------------------------------------------- ---------------------- --------------------- ---------------------------------------------------
  Property          Description                                                            Type of the property   Value it accepts      Any other dependencies/ sub properties associated
  UndoRedoEnabled   Gets or sets a value indicating whether undo redo is enabled or not.   Dependency property    Boolean(True/False)   No
  ----------------- ---------------------------------------------------------------------- ---------------------- --------------------- ---------------------------------------------------

[] 

The following code snippet to shows how to disable Undo Redo operation.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        \<][sfdiagram][:][DiagramControl][ IsSymbolPaletteEnabled][=\"True\" \>]                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\<][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][sfdiagram][:][DiagramModel][ x][:][Name][=\"diagramModel\" \>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\</][sfdiagram][:][DiagramModel][\>]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\</][sfdiagram][:][DiagramControl.Model][\>]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\<][sfdiagram][:][DiagramControl.View][ \>]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\<][sfdiagram][:][DiagramView][ UndoRedoEnabled][=\"False\"][ ]                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [ ShowHorizontalGridLine][=\"True\"][ ShowVerticalGridLine][=\"True\"\>]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [                ][\</][sfdiagram][:][DiagramView][\>]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [            ][\</][sfdiagram][:][DiagramControl.View][\>]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [        ][\</][sfdiagram][:][DiagramControl][\>]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [DiagramView][ diagramView = [new] [DiagramView]();] |
|                                                                                                                                                                                           |
| [diagramView.UndoRedoEnabled = [false];]                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [Dim][ diagramView [As] [New] [DiagramView]()] |
|                                                                                                                                                                                                       |
| [diagramView.UndoRedoEnabled = [False]][]                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Clearing Undo Redo Stack

The following code snippet illustrates how to clear Undo Redo stack.

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [DiagramView][ diagramView = [new] [DiagramView]();] |
|                                                                                                                                                                                           |
| [diagramView.ClearUndoRedoStack();]                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [Dim][ diagramView [As] [New] [DiagramView]()] |
|                                                                                                                                                                                                       |
| [diagramView.ClearUndoRedoStack()][]                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[]{#related-topics}

