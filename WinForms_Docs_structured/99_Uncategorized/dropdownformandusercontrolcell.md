---
title: dropdownformandusercontrolcell.md
original_path: WinForms_Docs/99_Uncategorized/dropdownformandusercontrolcell.md
created_at: 2025-08-05
---






##### Drop-Down Form and User Control Cell {#drop-down-form-and-user-control-cell style="tab-stops: 0pt"}

[] 

A custom control cell that displays a drop-down form or a user control in a grid cell can be created.

 

You can create:

[] 

[·      ]A drop-down form in a grid cell by deriving **GridStaticCellModel**/**GridStaticCellRenderer** classes.

[·      ]Adrop-down User control in a grid cell by deriving **GridDropDownCellModel**/**GridDropDownCellRender** classes.

[] 

The actions mentioned can be performed by using the following code example.

[] 

1.   Using C#

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [// Register your custom cell type.]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [this][.gridControl1.CellModels.Add([\"DropDownForm\"], [new] DropDownFormCellModel([this].gridControl1.Model, [new] DropDownForm()));]        |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [// Set the style.CellType for the cells.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| [this][.gridControl1\[2, 2\].CellType = [\"DropDownForm\"];]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                            |
| [// Register your custom cell type.]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [this][.gridControl1.CellModels.Add([\"DropDownUserControl\"], [new] DropDownUserCellModel([this].gridControl1.Model, [new] DropDownUser()));] |
|                                                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                            |
| [// Set the style.CellType for the cells.]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                            |
| [this][.gridControl1\[6, 2\].CellType = [\"DropDownUserControl\"];]                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Using VB.NET

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [\' Register your custom cell type.]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.gridControl1.CellModels.Add([\"DropDownForm\"], [New] DropDownFormCellModel([Me].gridControl1.Model, [New] DropDownForm()))]        |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [\' Set the style.CellType for the cells.]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.gridControl1(2, 2).CellType = [\"DropDownForm\"]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                       |
| [\' Register your custom cell type.]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.gridControl1.CellModels.Add([\"DropDownUserControl\"], [New] DropDownUserCellModel([Me].gridControl1.Model, [New] DropDownUser()))] |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                       |
| [\' Set the style.CellType for the cells.]                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                       |
| [Me][.gridControl1(6, 2).CellType = [\"DropDownUserControl\"]]                                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

*[Figure ][117][: Drop-Down Grid Form]*

 

[]{#p106} 

 

[]{#related-topics}

