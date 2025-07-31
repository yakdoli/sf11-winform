---
title: recordfilterdescriptor.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\recordfilterdescriptor.md
created_at: 2025-07-03
---








  









### RecordFilterDescriptor {#recordfilterdescriptor style="tab-stops: 0pt"}

[] 

Filtering in GridGroupingControl indicates adding filter condition to the Grid. **RecordFilterDescriptor** is used to add filter conditions to the TableDescriptor of the GridGroupingControl. Refer to the below code snippet to add filter conditions to the Grid.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [FilterCondition][ fc = [new] [FilterCondition](FilterCompareOperator.Like, id);]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [RecordFilterDescriptor][ rfd = [new] [RecordFilterDescriptor]([this].GridGroupingControl1.TableDescriptor.Columns.FindByMappingName([\"CategoryID\"]).ToString(), FilterLogicalOperator.Or, [new] Syncfusion.Grouping.FilterCondition\[\] { fc });] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [this][.GridGroupingControl1.TableDescriptor.RecordFilters.Add(rfd);]                                                                                                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ id [As] Int = 4]                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ fc [As] FilterCondition = [New] FilterCondition(FilterCompareOperator.Like, id)]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Dim][ rfd [As] RecordFilterDescriptor = [New] RecordFilterDescriptor([Me].GridGroupingControl1.TableDescriptor.Columns.FindByMappingName([\"CategoryID\"]).ToString(), FilterLogicalOperator.Or, [New] Syncfusion.Grouping.FilterCondition() {fc})] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [Me][.GridGroupingControl1.TableDescriptor.RecordFilters.Add(rfd)]                                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 83: Filtering records with CategoryID set to 4

[]{#related-topics}

