---
title: managingclipboardoperationswithgridmodelcutpaste.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\managingclipboardoperationswithgridmodelcutpaste.md
created_at: 2025-07-03
---






##### Managing Clipboard Operations with GridModelCutPaste {#managing-clipboard-operations-with-gridmodelcutpaste style="tab-stops: 0pt"}

[] 

The **GridModelCutPaste** class manages Cut, Copy and Paste operations for a grid. You can access this class from a grid with the **Grid.Model.CutPaste** property. This class provides many properties and functions.

 

Here is the list of properties and methods:

[] 

[·      ]**ClipboardFlags**-This property gets or sets various properties of GridDragDropFlags class, which specifies how the clipboard operations like cut, copy, and paste should be handled.

The following code examples illustrate how to set ClipboardFlags by using the GridDragDropFlags.Styles property:

[] 

[o  ]Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [this][.gridControl1.Model.CutPaste.ClipboardFlags = [GridDragDropFlags].Styles;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [Me][.gridControl1.Model.CutPaste.ClipboardFlags = GridDragDropFlags.Styles] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**CanCopy**-This method checks whether there are selected ranges of cells that can be copied to clipboard or if the current cell\'s contents can be copied. The return type of this method is Boolean. If it returns true, it indicates that the selected range of cells or the current cell\'s contents can be copied to the clipboard. If it is false, it indicates that the selected range of cells or the current cell\'s contents cannot be copied to the clipboard.


{border="0"}Note: Any content copied is pasted to the Clipboard by default.


 

The following code examples are used to call the CanCopy method:

[] 

[o  ]Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                                      |
| []                                                                                 |
|                                                                                                                                      |
| [this][.gridControl1.Model.CutPaste.CanCopy();] |
+--------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                |
|                                                                                                                                   |
| []                                                                              |
|                                                                                                                                   |
| [Me][.gridControl1.Model.CutPaste.CanCopy()] |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**Copy**-This method copies the contents of selected cells and the current cell\'s contents to the clipboard.

The following code examples are used to call the Copy method:

[] 

[o  ]Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                                   |
| []                                                                              |
|                                                                                                                                   |
| [this][.gridControl1.Model.CutPaste.Copy();] |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                             |
|                                                                                                                                |
| []                                                                           |
|                                                                                                                                |
| [Me][.gridControl1.Model.CutPaste.Copy()] |
+--------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**CopyRange(GridRangeInfo range)**-This method copies the contents of a specified range of cells to the clipboard. The range of cells to be copied is given to the method as a parameter. For example, if the range is specified to be (2,2), the selection is restricted to the cell with row index 2 and column index 2 of the grid.

The following code examples show how to call this method:

[] 

[o  ]Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                           |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [this][.gridControl1.Model.CutPaste.CopyRange([GridRangeInfo].Cell(2, 2));] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                          |
|                                                                                                                                                             |
| []                                                                                                        |
|                                                                                                                                                             |
| [Me][.gridControl1.Model.CutPaste.CopyRange(GridRangeInfo.Cell(2, 2))] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**CopyTextToClipboard(GridRangeInfo range)**-This method copies the formatted text of a specified range of cells to clipboard. The range of cells to be copied is given to the method as a parameter. For example, if the range is specified to be (1,2,1,4), the selection starts from the cell (1,2) -- with row index 1 and column index 2 to the cell (1,4) -- with row index 1 and column index 4 of the grid.

The following code examples show how to call this method:

[] 

[o  ]Using C#

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                           |
| []                                                                                                                                                      |
|                                                                                                                                                                                                           |
| [this][.gridControl1.Model.CutPaste.CopyTextToClipboard([GridRangeInfo].Cells(1, 2, 1, 4));] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                              |
| []                                                                                                                         |
|                                                                                                                                                                              |
| [Me][.gridControl1.Model.CutPaste.CopyTextToClipboard(GridRangeInfo.Cells(1, 2, 1, 4))] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**CopyCellsToClipboard(GridRangeInfoList list, bool bLoadBaseStyles)**-This method copies the style information of a specified range of cells to clipboard. The range of cells to be copied is given to the method as the first parameter. The second parameter represents a Boolean value. The base style will be copied along with default settings, if it is set to true. Only the default settings that were initialized to the cell are copied if it is set to false.

 

The following code examples show how to call this method:

[] 

[o  ]Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [GridRangeInfoList][ list = [new] [GridRangeInfoList]();] |
|                                                                                                                                                                                                |
| [list.Add([GridRangeInfo].Cell(2, 2));]                                                                                            |
|                                                                                                                                                                                                |
| [this][.gridControl1.Model.CutPaste.CopyCellsToClipboard(list, [true]);]             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                              |
|                                                                                                                                                                                 |
| []                                                                                                                            |
|                                                                                                                                                                                 |
| [Dim][ list [As] [New] GridRangeInfoList()]      |
|                                                                                                                                                                                 |
| [list.Add(GridRangeInfo.Cell(2, 2))]                                                                                                        |
|                                                                                                                                                                                 |
| [Me][.gridControl1.Model.CutPaste.CopyCellsToClipboard(list, [True])] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**CanCut**-This method checks if there are selected ranges that can be cut or if the current cell\'s contents can be cut. The return type of this method is Boolean. If it returns true, it indicates that the content in the selected range of cells or the current cell\'s content can be cut. This method returns false, when no selected range is available to cut.


{border="0"}Note: Any content cut is pasted to the clipboard by default.


[] 

The following code examples show how to call this method:

[] 

[o  ]Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                      |
|                                                                                                                                     |
| []                                                                                |
|                                                                                                                                     |
| [this][.gridControl1.Model.CutPaste.CanCut();] |
+-------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                               |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [Me][.gridControl1.Model.CutPaste.CanCut()] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**Cut**-This method cuts the content of the selected cells and the current cell, and pastes them to the clipboard.

The following code examples show how to call this method:

[] 

[o  ]Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                   |
|                                                                                                                                  |
| []                                                                             |
|                                                                                                                                  |
| [this][.gridControl1.Model.CutPaste.Cut();] |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+-------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                            |
|                                                                                                                               |
| []                                                                          |
|                                                                                                                               |
| [Me][.gridControl1.Model.CutPaste.Cut()] |
+-------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**CutRange(GridRangeInfo rangelist)**-This method cuts the content of a specified range of cells and pastes it to the clipboard. The range of cells to be cut is specified as a parameter.

The following code examples show how to call this method:

[] 

[o  ]Using C#

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [this][.gridControl1.Model.CutPaste.CutRange([GridRangeInfo].Row(4), [false]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                   |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [Me][.gridControl1.Model.CutPaste.CutRange(GridRangeInfo.Row(4), [False])] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**CanPaste**-This method checks for the most recent content in the clipboard that can be pasted into the grid. The return type of this method is Boolean. If it returns true, it indicates that the contents in the clipboard can be pasted into the grid. If there is no content available in the clipboard to paste, this method returns false.

The following code examples show how to call this method:

[] 

[o  ]Using C#

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                                       |
| []                                                                                  |
|                                                                                                                                       |
| [this][.gridControl1.Model.CutPaste.CanPaste();] |
+---------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                 |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [Me][.gridControl1.Model.CutPaste.CanPaste()] |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[·      ]**Paste**-This method pastes the content from the clipboard into the grid at the current selected range or current cell.


{border="0"}Note: It is not mandatory to call this method after CanPaste method. If there is no content in the clipboard to be pasted, this method will not respond.


 

The following code examples show how to call this method:

[] 

[o  ]Using C#

[] 

+------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                     |
|                                                                                                                                    |
| []                                                                               |
|                                                                                                                                    |
| [this][.gridControl1.Model.CutPaste.Paste();] |
+------------------------------------------------------------------------------------------------------------------------------------+

[] 

[o  ]Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                              |
|                                                                                                                                 |
| []                                                                            |
|                                                                                                                                 |
| [Me][.gridControl1.Model.CutPaste.Paste()] |
+---------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p352} 

 

[]{#related-topics}

