---
title: memberproperties1.md
original_path: WinForms_Docs/99_Uncategorized/memberproperties1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Member Properties {#member-properties style="tab-stops: 0pt"}

 

**OlapGrid** allows binding of **Dimension Members** along with their properties. Member properties cover the basic information about each member in each tuple. This basic information includes the member name, parent level, the number of children, and so on. Member properties are available for all members at a given level. In order to display member properties along with the dimension member, **OlapReport** requires member properties to be defined in the concerned dimension element. Also, the grid layout should be set to **ExcelLikeLayoutWithMemberProperties**.

[Click here for Sample Report with Member Properties]{.UGHyperlink} []{.UGHyperlink}

[] 

{border="0"}

Figure 26: OlapGrid with Member Properties

 

To display member properties via header tooltip, the following property of **OlapGrid** should be set to true.

+--------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                           |
|                                                                                                  |
|                                                                                                  |
|                                                                                                  |
| [// To Display Member Properties in ToolTip]                               |
|                                                                                                  |
| [this].OlapGrid1.ShowMemberPropertiesToolTip = [true]; |
|                                                                                                  |
|                                                                                                  |
+--------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------+
| \[VB\]                                                                                        |
|                                                                                               |
|                                                                                               |
|                                                                                               |
| [\' To Display Member Properties in ToolTip]                            |
|                                                                                               |
| [Me].OlapGrid1.ShowMemberPropertiesToolTip = [True] |
|                                                                                               |
|                                                                                               |
+-----------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 27: OlapGrid displaying Member Properties via Header Tooltip

 

Sample Location

A sample demo is available at the following location:

**..\\Syncfusion\\EssentialStudio\\\<Versionnumber\>\\BI\\WPF\\OlapGrid.WPF\\Samples\\Application Scenario\\Member Properties Demo**

[]{#related-topics}

