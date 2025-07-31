---
title: performance2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\performance2.md
created_at: 2025-07-03
---








  









## Performance {#performance style="tab-stops: 0pt"}

 

This section discusses the fast load mode of the Edit Control.

 

**Quick File Loading**

[] 

The Edit Control loads files extremely quick, and hence its performance is unmatched by any of our competitors or the Visual Studio.NET IDE.

 

The **ConvertOnLoad[ ]**property of the Edit Control should be set to **False** to enable the fast load mode. By default, this property is set to **True**.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                           |
|                                                                                                                                                          |
| []                                                                                                     |
|                                                                                                                                                          |
| [// Enable the fast load mode.]                                                                        |
|                                                                                                                                                          |
| [this][.editControl1.ConvertOnLoad = [false];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                    |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [\' Enable the fast load mode.]                                                                     |
|                                                                                                                                                       |
| [Me][.editControl1.ConvertOnLoad = [False]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p108} 

[]{#related-topics}

