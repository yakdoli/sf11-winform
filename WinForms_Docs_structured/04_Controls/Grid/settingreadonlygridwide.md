---
title: settingreadonlygridwide.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\settingreadonlygridwide.md
created_at: 2025-07-03
---






##### Setting ReadOnly Grid Wide {#setting-readonly-grid-wide style="tab-stops: 0pt"}

[] 

The property **GridControl.ReadOnly** or **GridDataBoundGrid.Model.ReadOnly** will allow you to set the ReadOnly behavior on a grid-wide basis.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                        |
| [// Changes cannot be made to the Grid control.]                                                                                                                                                     |
|                                                                                                                                                                                                                                                        |
| [this][.gridControl1.ReadOnly = ][true][;  ]     |
|                                                                                                                                                                                                                                                        |
| [        ]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                        |
| [// Changes cannot be made to the Grid Data Bound Grid.]                                                                                                                                             |
|                                                                                                                                                                                                                                                        |
| [this][.gridDataBoundGrid1.ReadOnly = ][true][;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                  |
| [\' Changes cannot be made to the Grid control.]                                                                                                                                               |
|                                                                                                                                                                                                                                                  |
| [Me][.GridControl1.ReadOnly = ][True][   ] |
|                                                                                                                                                                                                                                                  |
| [        ]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                  |
| [\' Changes cannot be made to the Grid Data Bound Grid.]                                                                                                                                       |
|                                                                                                                                                                                                                                                  |
| [Me][.GridDataBoundGrid1.ReadOnly = ][True]                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p292} 

 

[]{#related-topics}

