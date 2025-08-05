---
title: outlines.md
original_path: WinForms_Docs/99_Uncategorized/outlines.md
created_at: 2025-08-05
---








  









### Outlines {#outlines style="tab-stops: 0pt"}

**[]** 

Microsoft Excel has grouping and outlining features, which allows you to group large quantities of data. You can group/ungroup a range of rows and columns. To do this, go to the **Data** menu, point to **Group and Outline**, and select **Group/UnGroup** in Excel.

 

{border="0"}

Figure 137: Grouping from Data Menu[]

[] 

 

**Grouping and Ungrouping in Essential XlsIO**

 

Essential XlsIO provides support to group and ungroup rows and columns by using the **Group** and **UnGroup** methods of **IRange.** You can also collapse or expand groups through one of its overload.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                                 |
| [    ]                                                                                                                                     |
|                                                                                                                                                                                                 |
| [// Grouping by Rows.]                                                                                                       |
|                                                                                                                                                                                                 |
| [sheet.Range\[[\"A1:A3\"]\].Group([ExcelGroupBy].ByRows, [true]);]    |
|                                                                                                                                                                                                 |
| [sheet.Range\[[\"A4:A6\"]\].Group([ExcelGroupBy].ByRows);]                                 |
|                                                                                                                                                                                                 |
| []                                                                                                                                         |
|                                                                                                                                                                                                 |
| [// Grouping by Columns.]                                                                                                    |
|                                                                                                                                                                                                 |
| [sheet.Range\[[\"A1:B1\"]\].Group([ExcelGroupBy].ByColumns, [true]);] |
|                                                                                                                                                                                                 |
| [sheet.Range\[[\"C1:F1\"]\].Group([ExcelGroupBy].ByColumns);]                              |
|                                                                                                                                                                                                 |
| []                                                                                                                                         |
|                                                                                                                                                                                                 |
| [//UnGroup by Rows]                                                                                                          |
|                                                                                                                                                                                                 |
| [sheet.Range\[[\"A1:A3\"]\].UnGroup([ExcelGroupBy].ByRows);]                               |
|                                                                                                                                                                                                 |
| []                                                                                                                                         |
|                                                                                                                                                                                                 |
| [//Ungroup by columns]                                                                                                       |
|                                                                                                                                                                                                 |
| [sheet.Range\[[\"C1:F1\"]\].UnGroup([ExcelGroupBy].ByColumns);]                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                            |
| **[]**                                                                                                                |
|                                                                                                                                                                            |
| [\' Grouping by Rows.]                                                                                  |
|                                                                                                                                                                            |
| [sheet.Range( [\"A1:A3\"] ).Group(ExcelGroupBy.ByRows, [True])        ]   |
|                                                                                                                                                                            |
| [sheet.Range( [\"A4:A6\"] ).Group(ExcelGroupBy.ByRows)]                                        |
|                                                                                                                                                                            |
| []                                                                                                                    |
|                                                                                                                                                                            |
| [\' Grouping by Columns.]                                                                               |
|                                                                                                                                                                            |
| [sheet.Range( [\"A1:B1\"] ).Group(ExcelGroupBy.ByColumns, [True])       ] |
|                                                                                                                                                                            |
| [sheet.Range( [\"C1:F1\"] ).Group(ExcelGroupBy.ByColumns)]                                     |
|                                                                                                                                                                            |
| []                                                                                                                    |
|                                                                                                                                                                            |
| [\' UnGroup by Rows]                                                                                    |
|                                                                                                                                                                            |
| [sheet.Range( [\"A1:A3\"] ).UnGroup(ExcelGroupBy.ByRows)       ]                               |
|                                                                                                                                                                            |
| []                                                                                                                    |
|                                                                                                                                                                            |
| [\' Ungroup by columns]                                                                                 |
|                                                                                                                                                                            |
| [sheet.Range( [\"C1:F1\"] ).UnGroup(ExcelGroupBy.ByColumns)]                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

{border="0"}

Figure 138: Grouping in XlsIO[]

[] 

 

Excel has options to customize the Grouping settings through the **Settings** dialog box. You can show the Summary details row below or right of the column, by using the options provided in the Settings dialog box.

 

{border="0"}

Figure 139: Grouping Settings Dialog in MS Excel[]

[] 

 

In **XlsIO**, this is set by using the **IsSummaryRowBelow** and **IsSummaryColumnRight** properties of **IPageSetup** class.

 

Following screenshot shows the disabled state of summary settings.

 

{border="0"}

Figure 140: Summary Settings Disabled[]

***[]*** 

 

XlsIO also has options to check the existence of a group, and the level at which it exists. This can be done through the **IsGroupedByColumn/IsGroupedByRow** and **RowGroupLevel/ColumnGroupLevel** properties of IRange**.**

 

**Expand/Collapse Groups**

 

Essential XlsIO supports Expand and Collapse features for existing groups. Expand group comes with overloads that will allow to expand the entire parent including child groups. The Expand and Collapse features are available for both Column and Row groups[.]

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                  |
| [    ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                  |
| [// Expand group with flag set to expand parent.]                                                                                                             |
|                                                                                                                                                                                                                                  |
| [worksheet.Range\[[\"A11:A19\"]\].ExpandGroup([ExcelGroupBy].ByRows, [ExpandCollapseFlags].ExpandParent);] |
|                                                                                                                                                                                                                                  |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [// Collapse group.]                                                                                                                                          |
|                                                                                                                                                                                                                                  |
| [worksheet.Range\[[\"A61:A114\"]\].CollapseGroup([ExcelGroupBy].ByRows);]                                                       |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                           |
|                                                                                                                                                                                 |
| **[]**                                                                                                                     |
|                                                                                                                                                                                 |
| [\' Expand group with flag set to expand parent.]                                                            |
|                                                                                                                                                                                 |
| [worksheet.Range([\"A11:A19\"]).ExpandGroup(ExcelGroupBy.ByRows, ExpandCollapseFlags.ExpandParent)] |
|                                                                                                                                                                                 |
| []                                                                                                           |
|                                                                                                                                                                                 |
| [\' Collapse group.]                                                                                         |
|                                                                                                                                                                                 |
| [worksheet.Range([\"A61:A114\"]).CollapseGroup(ExcelGroupBy.ByRows)]                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

For More Information Refer:

 

[, ][[Grouping and Ungrouping]{.UGHyperlink}]()[]

**[]** 

[]{#p112} 

[]{#related-topics}

