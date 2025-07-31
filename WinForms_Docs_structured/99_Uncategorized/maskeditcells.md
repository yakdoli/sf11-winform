---
title: maskeditcells.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\maskeditcells.md
created_at: 2025-07-03
---






##### Mask Edit Cells {#mask-edit-cells style="tab-stops: 0pt"}

MaskEdit cell type allows you to create specially formatted text cells that confirm to an edit mask that you specify. The Style.MaskEdit.Mask property holds the mask string, which will control the format of the input text being entered. The Mask Edit cells are useful when the user wants to display some formatted text such as Social Security Number (SSN), telephone number etc.

**[]** 

Example

Setting up Mask Edit cells with different mask string.

 

+---------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                            |
|                                                                                                                                       |
| **[]**                                                                              |
|                                                                                                                                       |
| [var maskStyleInfo = [this].grid.Model\[6, 2\];]                             |
|                                                                                                                                       |
| [maskStyleInfo.CellType = [\"MaskEdit\"];]                                |
|                                                                                                                                       |
| [maskStyleInfo.MaskEdit = GridMaskEditInfo.Default;]                                              |
|                                                                                                                                       |
| [maskStyleInfo.MaskEdit.Mask = [\"00/00/0000\"];]                         |
|                                                                                                                                       |
| [maskStyleInfo.CellValue = 1232313;]                                                              |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [var maskStyleInfo1 = [this].grid.Model\[8, 2\];]                            |
|                                                                                                                                       |
| [maskStyleInfo1.CellType = [\"MaskEdit\"];]                               |
|                                                                                                                                       |
| [maskStyleInfo1.MaskEdit = GridMaskEditInfo.Default;]                                             |
|                                                                                                                                       |
| [maskStyleInfo1.MaskEdit.Mask = [\"00:00:00\"];]                          |
|                                                                                                                                       |
| [maskStyleInfo1.CellValue = 1232313;]                                                             |
|                                                                                                                                       |
| []                                                                                                |
|                                                                                                                                       |
| [var maskStyleInfo2 = [this].grid.Model\[10, 2\];]                           |
|                                                                                                                                       |
| [maskStyleInfo2.CellType = [\"MaskEdit\"];]                               |
|                                                                                                                                       |
| [maskStyleInfo2.MaskEdit = GridMaskEditInfo.Default;]                                             |
|                                                                                                                                       |
| [maskStyleInfo2.MaskEdit.Mask = [\"00/00/0000\"];]                        |
|                                                                                                                                       |
| [maskStyleInfo2.CellValue = [\"12012007\"];[\"];] |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

Output

The following output is generated using the code above.

 

{border="0"}

Figure 31: Mask Edit Cell


{border="0"}Note: For complete code, please refer to the following browser sample.


**[]** 

\...\\My Documents\\Syncfusion\\EssentialStudio\\\<Version Number\>\\WPF\\Grid.WPF\\Samples\\3.5\\WindowsSamples\\Cell Types\\Mask Edit Cell Demo

[]{#related-topics}

