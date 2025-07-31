---
title: addtheelementstoanaxis.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addtheelementstoanaxis.md
created_at: 2025-07-03
---








  









## Add the elements to an Axis {#add-the-elements-to-an-axis style="tab-stops: 0pt"}

After creating the element, add the element to the specific axis. The **OlapReport** contains the axis as **CategoricalElements**, **SeriesElement** and **SliceElements**. By adding the created elements to any of these elements group, you can specify the axis position of the elements.

The following codes will describe the adding of the elements to categorical, series element:

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]                                                                 ]**                 |
|                                                                                                                                   |
| []                                                                                            |
|                                                                                                                                   |
| [///][Adding Column Members][\ |
| olapReport.CategoricalElements.Add(dimensionElementColumn);\                                                                      |
| [///][Adding Measure Element]\                                                         |
| olapReport.CategoricalElements.Add(measureElementColumn);\                                                                        |
|             \                                                                                                                     |
| [///][Adding Row Members]\                                                             |
| olapReport.SeriesElements.Add(dimensionElementRow);]                                          |
|                                                                                                                                   |
| []                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                       |
|                                                                                                                        |
| []                                                                                 |
|                                                                                                                        |
| [\'\'\'Adding Column Members][]  |
|                                                                                                                        |
| [olapReport.CategoricalElements.Add(dimensionElementColumn)]                       |
|                                                                                                                        |
| [\'\'\'Adding Measure Element][] |
|                                                                                                                        |
| [olapReport.CategoricalElements.Add(measureElementColumn)]                         |
|                                                                                                                        |
| []                                                                                 |
|                                                                                                                        |
| [\'\'\'Adding Row Members][]     |
|                                                                                                                        |
| [olapReport.SeriesElements.Add(dimensionElementRow)]                               |
|                                                                                                                        |
| []                                                                                 |
+------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

