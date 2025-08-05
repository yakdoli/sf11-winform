---
title: howtoclearafilter.md
original_path: WinForms_Docs/99_Uncategorized/howtoclearafilter.md
created_at: 2025-08-05
---








  









## How to Clear a Filter? {#how-to-clear-a-filter style="tab-stops: 0pt"}

[] 

To clear all filters, call the groupingEngine.TableDescriptor.RecordFilters.Clear method.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                 |
|                                                                                                                                                                                                                |
| []                                                                                                                                                           |
|                                                                                                                                                                                                                |
| [// Removes all the filters associated with the table.]                                                                                                      |
|                                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.RecordFilters.Clear();  ]                                                    |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// Removes the Filter associated by sending the argument as RecordFilterDescriptor.name ]                                                                   |
|                                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.RecordFilters.Remove([RecordFilterDescriptor].Name);  ] |
|                                                                                                                                                                                                                |
| []                                                                                                                                                                         |
|                                                                                                                                                                                                                |
| [// Removes the RecordFilter associated by mentioning as index.]                                                                                             |
|                                                                                                                                                                                                                |
| [this][.gridGroupingControl1.TableDescriptor.RecordFilters.RemoveAt(); ]                                                  |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                      |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [\' Removes all the filters associated with the table.]                                                               |
|                                                                                                                                                                         |
| [Me][.gridGroupingControl1.TableDescriptor.RecordFilters.Clear()]    |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [\' Removes the Filter associated by sending the argument as RecordFilterDescriptor.name ]                            |
|                                                                                                                                                                         |
| [Me][.gridGroupingControl1.TableDescriptor.RecordFilters.Remove()]   |
|                                                                                                                                                                         |
| []                                                                                                                    |
|                                                                                                                                                                         |
| [\' Removes the RecordFilter associated by mentioning as index.]                                                      |
|                                                                                                                                                                         |
| [Me][.gridGroupingControl1.TableDescriptor.RecordFilters.RemoveAt()] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: To remove a particular filter, use the groupingEngine.TableDescriptor.RecordFilters.Remove or groupingEngine.TableDescriptor.RecordFilters.RemoveAt. To use Remove, you will need a reference to the RecordFilterDescriptor object that you want to delete or your RecordFilterDescriptor object would have to be named (setting the RecordFilterDescriptor.Name property or by passing a name string into its overloaded constructor).


[]{#related-topics}

