---
title: improvingperformance2.md
original_path: WinForms_Docs/99_Uncategorized/improvingperformance2.md
created_at: 2025-08-05
---








  









## Improving Performance {#improving-performance style="tab-stops: 0pt"}

 

Essential XlsIO can create large reports in few seconds.

 

{border="0"}**Tips to improve the Performance**

 

, which can be used to apply styles for the whole column instead of having to apply for each cell.

[·      ]Minimize AutoFit manipulations.

[·      ]Get **UsedRange** globally. It is recommended to get the UsedRange in loops as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                              |
|                                                                                                                                                               |
| []                                                                                                          |
|                                                                                                                                                               |
| [for][([int] i = 0;i\<sheet.UsedRange.LastRow;i++)] |
|                                                                                                                                                               |
| []                                                                                                                        |
|                                                                                                                                                               |
| [// Do not use the following method.]                                                                       |
|                                                                                                                                                               |
| [int][ lastRow = sheet.UsedRange.LastRow]                                |
|                                                                                                                                                               |
| [for][([int] i=0;i\<lastRow;i++)]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

 to optimize memory performance while dealing with large strings.

, rather than using different cell styles for each cell/range.

[·      ]Use **Begin** and **End** call while using more than one global style for a worksheet.

[·      ]Use **Value** and **Value2** property only when the data type is unknown. Value/Value2 property checks the data type of the given string and hence this consumes time.

[·      ]Files parsing can be optimized by setting **IApplication.UseFastRecordParsing** = **false** or **true** (true -- fast mode, but less error checks and false -- slower but more reliable).

[·      ]To extract values little faster, use **Unsafe** code option of **IApplication** interface as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                          |
|                                                                                                                           |
| []                                                                      |
|                                                                                                                           |
| [application.DataProviderType = [ExcelDataProviderType].Unsafe;] |
+---------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Make use of **GetText**, **SetText**, **GetNumber** and **SetNumber** methods that enable users to get/set values without range object.

[·      ]Set **IWorkbook.DetectDateTimeInValue** property to **false** with Value2 property, if you are sure that the given value is not of **DateTime** data type which improves time performance.

[·      ]Use of **BeginUpdate** and **EndUpdate** methods for large blocks of Data Validation greatly improves the performance.

[·      ]Use **DataProvider.Unsafe** option to increase performance while deleting large number of rows or columns.

 to reduce the size of the file.

 

[]{#p32} 

[]{#related-topics}

