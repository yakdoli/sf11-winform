---
title: freezeheaders.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\freezeheaders.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Freeze Headers {#freeze-headers style="tab-stops: 0pt"}

OlapGrid for WPF provides built-in support to freeze the Column and Row Headers. This is achieved by setting the **FreezeHeaders** property of **OlapGrid** to true. This feature also enables scrolling through the value cells.

 

+------------------------------------------------------------------------------------+
| \[C#\]                                                                             |
|                                                                                    |
|                                                                                    |
|                                                                                    |
| [// To Freeze Grid Headers]                                  |
|                                                                                    |
| [this].OlapGrid1.FreezeHeaders = [true]; |
|                                                                                    |
|                                                                                    |
+------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------+
| \[VB\]                                                                          |
|                                                                                 |
|                                                                                 |
|                                                                                 |
| [\' To Freeze Grid Headers]                               |
|                                                                                 |
| [Me].OlapGrid1.FreezeHeaders = [True] |
|                                                                                 |
|                                                                                 |
+---------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 30: OlapGrid with Freeze Headers

[] 

Sample Location

A sample demo is available at the following location:

**..\\Syncfusion\\EssentialStudio\\\<Versionnumber\>\\BI\\WPF\\OlapGrid.WPF\\Samples\\Appearance\\Frozen Header Demo**

[]{#related-topics}

