---
title: basiccelltypes.md
original_path: WinForms_Docs/99_Uncategorized/basiccelltypes.md
created_at: 2025-08-05
---






##### Basic Cell Types {#basic-cell-types style="tab-stops: 0pt"}

[]{#p19}This section elaborates you on how to employ basic controls like Check Box, Radio Button and more in a grid cell. The list of cell types and their usages are described below. The table also lists the format string for the individual cell types.

 

Table 5: Cell Type[]


  ----------- ------------------ -------------------------------------------------------------------------
  Cell Type   Cell Type String   Usage
  Header      "Header"           Used as row and column headers
  Static      "Static"           Cannot be edited
  Check Box   "CheckBox"         Used for toggling options
  Button      "Button"           Provides Click event, which can be triggered to perform required action
  Image       "ImageCell"        Used to display pictures
  ----------- ------------------ -------------------------------------------------------------------------


[] 

To set up desired cell type, the Style.CellType property must be assigned with the corresponding format string. For instance, if you want to display a Check box control in the cell (2, 2), then you have to use the code below.

 

Displaying a Check Box Control in a cell

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                    |
|                                                                                                                                               |
| []                                                                                          |
|                                                                                                                                               |
| [GridStyleInfo][ style = gridControl1.Model\[2, 2\];] |
|                                                                                                                                               |
| [style.CellType = [\"CheckBox\"];]                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Likewise, you can also add other controls from the table above. A sample output is displayed below.

 

{border="0"}

Figure 15: Basic Cell Types

A check box is created in the grid.


{border="0"}Note: For complete code, please refer to the following browser sample:


[] 

***\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Basic Cell Type Demo***

[]{#related-topics}

