---
title: buttonedit.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\buttonedit.md
created_at: 2025-07-03
---






##### Button Edit {#button-edit style="tab-stops: 0pt"}

[] 

The Button Edit cell type will allow you to add images to the button which can be embedded into the grid cells. This Button Edit cell type can be added by registering its cell model to the corresponding grid by using the **RegisterCellModel** class. There are some in-built images which will be added to the button by providing the button type, and also custom images can be added by specifying the button type as image and providing the location of the image. These Button Edit types can be used by initializing the **ButtonEditStyleProperties** class for the corresponding cell. The Button Edit types provided by grid control are listed as follows.

[] 

[·      ]Browse

[·      ]Check

[·      ]Down

[·      ]Left

[·      ]Leftend

[·      ]Redo

[·      ]Right

[·      ]Rightend

[·      ]Undo

[·      ]Up

[·      ]Image

[] 

You can also add custom buttons that you have created to the grid cells. This enables you to add custom buttons like split button to the grid.

[] 

The following code examples illustrate how to set the cell type to ButtonEdit.

[] 

1.   Using C#

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| []                                                                                                                                                         |
|                                                                                                                                                                                                              |
| [RegisterCellModel][.GridCellType(gridControl1, [CustomCellTypes].ButtonEdit);]              |
|                                                                                                                                                                                                              |
| [ButtonEditStyleProperties][ sp;]                                                                                    |
|                                                                                                                                                                                                              |
| [this][.gridControl1\[rowIndex, colIndex\].CellType = [CustomCellTypes].ButtonEdit.ToString();] |
|                                                                                                                                                                                                              |
| [sp = [new] [ButtonEditStyleProperties]([this].gridControl1\[rowIndex, colIndex\]);]                   |
|                                                                                                                                                                                                              |
| [sp.ButtonEditInfo.ButtonEditType = [ButtonType].Browse;]                                                                                        |
|                                                                                                                                                                                                              |
| [sp.ButtonEditInfo.Width = 50;]                                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                       |
|                                                                                                                                                                                          |
| []                                                                                                                                     |
|                                                                                                                                                                                          |
| [RegisterCellModel.GridCellType(gridControl1, CustomCellTypes.ButtonEdit)]                                                                           |
|                                                                                                                                                                                          |
| [Private][ sp [As] ButtonEditStyleProperties]                                  |
|                                                                                                                                                                                          |
| [Me][.gridControl1\[rowIndex += 1, colIndex\].CellType = [\"ButtonEdit\"];] |
|                                                                                                                                                                                          |
| [Me][.gridControl1(rowIndex, colIndex).CellType = CustomCellTypes.ButtonEdit.ToString()]            |
|                                                                                                                                                                                          |
| [sp = [New] ButtonEditStyleProperties([Me].gridControl1(rowIndex, colIndex))]                              |
|                                                                                                                                                                                          |
| [sp.ButtonEditInfo.ButtonEditType = ButtonType.Browse]                                                                                               |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][105][: Button Edit Cells]*

 

[]{#p94} 

 

[]{#related-topics}

