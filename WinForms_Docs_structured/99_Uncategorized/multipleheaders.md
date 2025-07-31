---
title: multipleheaders.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\multipleheaders.md
created_at: 2025-07-03
---






#### Multiple Headers {#multiple-headers style="tab-stops: 0pt"}

[] 

Grid Data Bound Grid supports display of multiple row and column headers. Additional row headers can be added along side the existing header by setting Model.Rows.HeaderCount and additional column headers can be added below the existing column header by setting the Model.Cols.HeaderCount property.

 

The following code example illustrates how to display multiple row and column headers.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                             |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [int][ extraRowHeaders = 1;]                                          |
|                                                                                                                                                            |
| [int][ extraColHeaders = 1;]                                          |
|                                                                                                                                                            |
| []                                                                                                       |
|                                                                                                                                                            |
| [// Initialize extra row and column headers.]                                                            |
|                                                                                                                                                            |
| [this][.gridDataBoundGrid1.Model.Rows.HeaderCount = extraRowHeaders;] |
|                                                                                                                                                            |
| [this][.gridDataBoundGrid1.Model.Cols.HeaderCount = extraColHeaders;] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                        |
|                                                                                                                                                                           |
| **[]**                                                                                                                  |
|                                                                                                                                                                           |
| [Dim][ extraRowHeaders [As] [Integer] = 1] |
|                                                                                                                                                                           |
| [Dim][ extraColHeaders [As] [Integer] = 1] |
|                                                                                                                                                                           |
| []                                                                                                                      |
|                                                                                                                                                                           |
| [\' Initialize extra row and column headers.]                                                                           |
|                                                                                                                                                                           |
| [Me][.gridDataBoundGrid1.Model.Rows.HeaderCount = extraRowHeaders]                   |
|                                                                                                                                                                           |
| [Me][.gridDataBoundGrid1.Model.Cols.HeaderCount = extraColHeaders]                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The resultant output is shown below.

[] 

{border="0"}

[] 

*[Figure ][225][: Multiple Headers]*

 

[]{#p385} 

 

[]{#related-topics}

