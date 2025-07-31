---
title: nosummarieslayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\nosummarieslayout.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






    


### No Summaries Layout {#no-summaries-layout style="tab-stops: 0pt"}

In this kind of layout, the summary cells were made hidden and the child member appears adjacent to the parent member.

{border="0"}

Figure 25: OlapGrid in No Summaries Layout

[] 

+--------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                           |
|                                                                                                  |
|                                                                                                  |
|                                                                                                  |
| [///] [ No Summaries Grid Layout]                     |
|                                                                                                  |
| [this].OlapGrid1.Layout = [GridLayout].NoSummaries; |
|                                                                                                  |
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------+
| \[VB\]                                                                                        |
|                                                                                               |
|                                                                                               |
|                                                                                               |
| [\' Grid Layout will be Normal]                                         |
|                                                                                               |
| [Me].OlapGrid1.Layout = [GridLayout].NoSummaries |
|                                                                                               |
|                                                                                               |
+-----------------------------------------------------------------------------------------------+

[] 

[] 

Sample Location

A sample demo is available at the following location:

**..\\Syncfusion\\EssentialStudio\\\<Versionnumber\>\\BI\\WPF\\OlapGrid.WPF\\Samples\\Product Showcase\\Grid Layout Demo**

[]{#related-topics}

