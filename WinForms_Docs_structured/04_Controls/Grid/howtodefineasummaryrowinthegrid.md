---
title: howtodefineasummaryrowinthegrid.md
original_path: WinForms_Docs/04_Controls/Grid/howtodefineasummaryrowinthegrid.md
created_at: 2025-08-05
---






#### How to define a summary row in the grid {#how-to-define-a-summary-row-in-the-grid style="tab-stops: 0pt"}

[] 

This can be done using the below code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                     |
| [// Defining a summary column descriptor.]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [GridSummaryColumnDescriptor sd = [new] GridSummaryColumnDescriptor();]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| [// Summary for Col2 ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                     |
| [sd.DataMember= [\"Col2\"];]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [// Setting under which column you need to see the total.]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [sd.DisplayColumn = [\"Col2\"];]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                     |
| [// Here you specify the format of the field to be displayed.]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                     |
| [sd.Format = [\"{Count}\"];]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                     |
| [// Here you set the type of the summary i.e totalling or average or count etc\...]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                     |
| [sd.SummaryType = SummaryType.DistinctCount;]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [// Here \"Total\" is the text that occurs as the header.]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                     |
| [// Create a new SummaryRowDescriptor and add it to the SummaryRows collection]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                     |
| [this][.gridGroupingControl1.TableDescriptor.SummaryRows.Add([new] GridSummaryRowDescriptor([\"Col2\"], [\"Total\"], sd));] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [\' Defining a summary column descriptor.]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [Private][ sd [As] GridSummaryColumnDescriptor = [New] GridSummaryColumnDescriptor()]                                                             |
|                                                                                                                                                                                                                                                                                  |
| [\' Summary for Col2 ]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                  |
| [sd.DataMember= [\"Col2\"]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [\' Setting under which column you need to see the total.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [sd.DisplayColumn = [\"Col2\"]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                  |
| [\' Here you specify the format of the field to be displayed.]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                  |
| [sd.Format = [\"{Count}\"]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                  |
| [\' Here you set the type of the summary i.e totalling or average or count etc\...]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                  |
| [sd.SummaryType = SummaryType.DistinctCount]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                  |
| [\' Here \"Total\" is the text that occurs as the header.]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                  |
| [\' Create a new SummaryRowDescriptor and add it to the SummaryRows collection]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                  |
| [Me][.gridGroupingControl1.TableDescriptor.SummaryRows.Add([New] GridSummaryRowDescriptor([\"Col2\"], [\"Total\"], sd))] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p667} 

 

[]{#related-topics}

