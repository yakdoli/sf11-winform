---
title: gridfolderbrowser.md
original_path: WinForms_Docs/04_Controls/Grid/gridfolderbrowser.md
created_at: 2025-08-05
---






##### Grid Folder Browser {#grid-folder-browser style="tab-stops: 0pt"}

[] 

The Essential Grid can be used to develop a powerful **TreeView** control owing to its flexibility. The tree nodes can be created through a custom **TreeCell** cell type. The **GridStaticCellModel** class is inherited to create this cell type. The plus/minus buttons of the tree nodes are selected by using the **ImageIndex** property.

 

**Example**

 

Let us consider the Grid Folder Browser sample which is available under the following installation path.

 

***\<Install Location\>\\Syncfusion\\EssentialStudio\\\[Version Number\]\\Windows\\Grid.Windows\\Samples\\2.0\\Product Showcase\\Grid Folder Browser Demo***

 

This sample operates the grid in virtual mode in order to populate the data dynamically on demand, i.e., when the tree is expanded. The QueryCellInfo, QueryColCount and QueryRowCount events must be handled in order to implement a virtual grid. These events provide basic information about the number of rows and columns and the values of the data.

 

The following code examples illustrates how to set the data from the data source.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [void][ GridQueryCellInfo([object] sender, [GridQueryCellInfoEventArgs] e) ] |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [if][ (e.RowIndex \> 0 && e.ColIndex \> 0) ]                                                                              |
|                                                                                                                                                                                                                |
| [{ ]                                                                                                                                                                       |
|                                                                                                                                                                                                                |
| [e.Style.CellValue = externalData\[e.RowIndex - 1\].Items\[e.ColIndex - 1\]; ]                                                                                             |
|                                                                                                                                                                                                                |
| [if][ (e.ColIndex == 1) ]                                                                                                 |
|                                                                                                                                                                                                                |
| [{]                                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [e.Style.CellType = [\"TreeCell\"]; ]                                                                                                              |
|                                                                                                                                                                                                                |
| [e.Style.Tag = externalData\[e.RowIndex - 1\].IndentLevel; ]                                                                                                               |
|                                                                                                                                                                                                                |
| [e.Style.ImageIndex = ([int]) externalData\[e.RowIndex - 1\].ExpandState; ]                                                                           |
|                                                                                                                                                                                                                |
| [} ]                                                                                                                                                                       |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                                        |
|                                                                                                                                                                                                                |
| [e.Handled = [true];]                                                                                                                                 |
|                                                                                                                                                                                                                |
| [}]                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                 |
| [Private][ [Sub] GridQueryCellInfo([ByVal] sender [As] [Object], [ByVal] e [As] GridQueryCellInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                 |
| [If][ e.RowIndex \> 0 [AndAlso] e.ColIndex \> 0 [Then]]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [e.Style.CellValue = externalData(e.RowIndex - 1).Items(e.ColIndex - 1)]                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                 |
| [If][ e.ColIndex = 1 [Then]]                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [e.Style.CellType = [\"TreeCell\"]]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                 |
| [e.Style.Tag = externalData(e.RowIndex - 1).IndentLevel]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                 |
| [e.Style.ImageIndex = [CInt](Fix(externalData(e.RowIndex - 1).ExpandState))]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [If]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [If]]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                 |
| [e.Handled = [True]]                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                 |
| [End][ [Sub]]                                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The implementation uses a CollapsibleDataSource class. This class makes use of a custom collection to hold a list of SampleData objects (Consider each of these objects as a row in the underlying grid). Each row carries information on a specific folder. Each SampleData object has an IndentValue property, an ExpandState property, and an Items string array that holds the different column values for this row. The column values display the folder details like the name of the folder, folder size and so on. This class also contains the InsertData method which retrieves the data of the inner subtree and inserts the data into the collection when a node is expanded.

[] 

{border="0"}

[] 

*[Figure ][192][: Grid Folder Browser Demo]*

 

[]{#p349} 

 

[]{#related-topics}

