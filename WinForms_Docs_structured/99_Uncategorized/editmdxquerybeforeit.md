---
title: editmdxquerybeforeit.md
original_path: WinForms_Docs/99_Uncategorized/editmdxquerybeforeit.md
created_at: 2025-08-05
---








  





## Edit MDX Query before Its Execution {#edit-mdx-query-before-its-execution style="tab-stops: 0pt"}

MDX Query can be edited before its execution to retrieve the CellSet through handling the **BeforeMdxQueryExecute** event of **OlapDataManager**. The following code example illustrates this.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                   |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [olapDataManager.BeforeMdxQueryExecute += [new] [QueryExecuteEventHandler](olapDataManager_BeforeMdxQueryExecute);]                               |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [void][ olapDataManager_BeforeMdxQueryExecute([object] sender, [QueryExecutingEventArgs] e)    ] |
|                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| [     e.MdxQuery = [\"Edit MDX query here\"];]                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ olapDataManager.BeforeMdxQueryExecute += [New] QueryExecuteEventHandler([AddressOf] olapDataManager_BeforeMdxQueryExecute)]                                                                            |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] olapDataManager_BeforeMdxQueryExecute([ByVal] sender [As] [Object], [ByVal] e [As] QueryExecutingEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                  |
| [        e.MdxQuery = [\"Edit MDX query here\"]]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]**[]**                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

