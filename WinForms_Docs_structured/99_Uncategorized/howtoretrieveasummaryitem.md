---
title: howtoretrieveasummaryitem.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtoretrieveasummaryitem.md
created_at: 2025-07-03
---






#### How to retrieve a summary item {#how-to-retrieve-a-summary-item style="tab-stops: 0pt"}

[] 

The following code shows how to retrieve a summary item.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [// sd is GridSummaryColumnDescriptor ]                                                                                                               |
|                                                                                                                                                                                                         |
| [string][ item=GridEngine.GetSummaryText([this].gridGroupingControl1.Table.TopLevelGroup,sd)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                               |
| [\'sd is GridSummaryColumnDescriptor ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                               |
| [Dim][ item [As] [String] = GridEngine.GetSummaryText([Me].gridGroupingControl1.Table.TopLevelGroup, sd)] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p669} 

 

[]{#related-topics}

