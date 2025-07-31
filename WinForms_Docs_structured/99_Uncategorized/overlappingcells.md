---
title: overlappingcells.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\overlappingcells.md
created_at: 2025-07-03
---






#### Overlapping Cells {#overlapping-cells style="tab-stops: 0pt"}

    

Overlapping Cells behavior occurs when the text exceeds the length of the cell and will float to the adjacent cell in non-editing mode. Flooding behavior specifies whether a previous cell can be allowed to float over the corresponding cell even if it is empty. Floating cell is to enable the cell to float over the next cell while editing despite of the flooding or overlapping behavior.

 

To assign the floatingCell behavior to one particular cell or a certain range of cells

The FloatingCell behavior can be assigned to one particular cell or a certain range of cells as follows:

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                            |
|                                                                                                                                                                |
| [C#]                                                                                                          |
|                                                                                                                                                                |
| []                                                                                                            |
|                                                                                                                                                                |
| [//Provided as CellStyle][]                    |
|                                                                                                                                                                |
| [grid.Model\[4, 1\].EnableFloatCell = [true];]                                           |
|                                                                                                                                                                |
| [grid.Model\[4, 1\].FloatCellMode = [GridFloatCellsMode].OnDemandCalculation;]        |
|                                                                                                                                                                |
| [grid.Model\[1, 1\].FloodCell = [false];]                                                |
|                                                                                                                                                                |
| []                                                                                                            |
|                                                                                                                                                                |
| [//Provided as ColumnStyle][]                  |
|                                                                                                                                                                |
| [grid.Model.ColStyles\[2\].EnableFloatCell = [true];]                                    |
|                                                                                                                                                                |
| [grid.Model.ColStyles\[2\].FloatCellMode = [GridFloatCellsMode].OnDemandCalculation;] |
|                                                                                                                                                                |
| [grid.Model.ColStyles\[2\].FloodCell = [false];]                                         |
|                                                                                                                                                                |
| []                                                                                                            |
|                                                                                                                                                                |
| [//Provided as TableStyle][]                   |
|                                                                                                                                                                |
| [grid.Model.Options.EnableFloatCell = [true];]                                           |
|                                                                                                                                                                |
| [grid.Model.Options.FloatCellMode = [GridFloatCellsMode].OnDemandCalculation;]        |
|                                                                                                                                                                |
| [grid.Model.Options.FloodCell = [false];]                                                |
|                                                                                                                                                                |
| []                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 47: Floating Cell

Properties, Methods and Events tables

Properties

+---------------------+-----------------------------------------------------------------------------------------------------+-----------------+--------------------------------+-----------------------------+
| Property            | Description                                                                                         | Type            | Data Type                      | Reference links             |
+---------------------+-----------------------------------------------------------------------------------------------------+-----------------+--------------------------------+-----------------------------+
| **EnableFloatCell** | This allows the user to float the cell while typing.                                                | Static Property | Boolean                        | []  |
|                     |                                                                                                     |                 |                                |                             |
|                     | This floats the cell in non-editing mode.                                                           |                 |                                |                             |
|                     |                                                                                                     |                 |                                |                             |
| **FloatCellMode**   | When the user specifies the property as false it will not allow the previous cell to float over it. | Static Property | GridFloatCellsMode (enum type) |                             |
|                     |                                                                                                     |                 |                                |                             |
|                     |                                                                                                     |                 |                                |                             |
|                     |                                                                                                     |                 |                                |                             |
| **FloodCell**       |                                                                                                     | Static Property | Boolean                        |                             |
|                     |                                                                                                     |                 |                                |                             |
|                     |                                                                                                     |                 |                                |                             |
|                     |                                                                                                     |                 |                                |                             |
|                     |                                                                                                     |                 |                                |                             |
|                     |                                                                                                     |                 |                                |                             |
|                     |                                                                                                     |                 |                                |                             |
+---------------------+-----------------------------------------------------------------------------------------------------+-----------------+--------------------------------+-----------------------------+

More:





