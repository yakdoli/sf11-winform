---
title: howtoexportcellcommenttipstoexcelusinggridexcelconvertercontrol.md
original_path: WinForms_Docs/04_Controls/Grid/howtoexportcellcommenttipstoexcelusinggridexcelconvertercontrol.md
created_at: 2025-08-05
---








  









### How to export CellCommentTips to Excel using GridExcelConverterControl {#how-to-export-cellcommenttips-to-excel-using-gridexcelconvertercontrol style="tab-stops: 0pt"}

[] 

You can achieve this by handling the **QueryImportExportCellInfo** event handler. In the event, check the GridExcelTipStyleProperties for ExcelTip properties, and accordingly add the comment to the IRange.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [Syncfusion.GridExcelConverter.GridExcelConverterControl gecc = [new] Syncfusion.GridExcelConverter.GridExcelConverterControl();]                                            |
|                                                                                                                                                                                                                                       |
| [gecc.QueryImportExportCellInfo += [new] Syncfusion.GridExcelConverter.GridImportExportCellInfoEventHandler(gecc_QueryImportExportCellInfo);]                                |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [void][ gecc_QueryImportExportCellInfo([object] sender, Syncfusion.GridExcelConverter.GridImportExportCellInfoEventArgs e)] |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [ExcelTip.GridExcelTipStyleProperties style = [new] ExcelTip.GridExcelTipStyleProperties(e.GridCell);]                                                                       |
|                                                                                                                                                                                                                                       |
| [if][ (style.HasExcelTipText)]                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [e.ExcelCell.AddComment().Text = style.ExcelTipText;]                                                                                                                                             |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[  ]

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ gecc [As] [New] Syncfusion.GridExcelConverter.GridExcelConverterControl()]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [AddHandler][ gecc.QueryImportExportCellInfo, [AddressOf] gecc_QueryImportExportCellInfo]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Private][ [Sub] gecc_QueryImportExportCellInfo([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.GridExcelConverter.GridImportExportCellInfoEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [Dim][ style [As] [New] ExcelTipDLL.GridExcelTipStyleProperties(e.GridCell)]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [If][ style.HasExcelTipText [Then]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [e.ExcelCell.AddComment().Text = style.ExcelTipText]                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                   |
| [End][ [Sub] [\'gecc_QueryImportExportCellInfo]]                                                                                                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p619} 

 

[]{#related-topics}

