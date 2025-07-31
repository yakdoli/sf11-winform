---
title: howtocontrolwhetheroledraganddropissupportedinthegrid.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\howtocontrolwhetheroledraganddropissupportedinthegrid.md
created_at: 2025-07-03
---








  









### How to Control Whether OLE Drag-and-Drop is Supported in the Grid {#how-to-control-whether-ole-drag-and-drop-is-supported-in-the-grid style="tab-stops: 0pt"}

[] 

Introduction

[] 

Whether a grid is an OLE drop target which, is controlled by the **DragDropTargetFlags** in the grids **Model.Options** class. These flags control things like the clipboard format, the type of the data, whether columns or rows can be appended to accommodate the dropped data and whether auto scrolling is supported. Check the enums for **GridDragDropFlags** to see the full set of options.

[] 

Example

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
| []                                                                                                                                   |
|                                                                                                                                                            |
| [// Turn off being a drop target.        ]                                                               |
|                                                                                                                                                            |
| [gridControl1.Model.Options.DragDropDropTargetFlags = GridDragDropFlags.Disabled;        ]               |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [// Turn on accepting text.         ]                                                                    |
|                                                                                                                                                            |
| [gridControl1.Model.Options.DragDropDropTargetFlags = GridDragDropFlags.Text;        ]                   |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [// Accept both text and styles.        ]                                                                |
|                                                                                                                                                            |
| [gridControl1.Model.Options.DragDropDropTargetFlags = GridDragDropFlags.Text \| GridDragDropFlags.Text;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| [\' Turn off being a drop target. ]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                  |
| [gridControl1.Model.Options.DragDropDropTargetFlags = GridDragDropFlags.Disabled]                                                                                                                              |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [\' Turn on accepting text. ]                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
| [gridControl1.Model.Options.DragDropDropTargetFlags = GridDragDropFlags.Text]                                                                                                                                  |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [\' Accept both text and styles. ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [gridControl1.Model.Options.DragDropDropTargetFlags = GridDragDropFlags.Text ][Or][ GridDragDropFlags.Text] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p615} 

 

[]{#related-topics}

