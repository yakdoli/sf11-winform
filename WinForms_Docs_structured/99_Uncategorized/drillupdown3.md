---
title: drillupdown3.md
original_path: WinForms_Docs/99_Uncategorized/drillupdown3.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Drill-Up/Down {#drill-updown style="tab-stops: 0pt"}

This is the basic feature of OlapGrid through which the amount of information can be limited. It allows you to drill down to access the detailed level of data, or roll up to see the summarized data using the expander's present in the grid. The expander here refers to the plus/minus sign present in the grid followed by a member.

{border="0"}       -    Drilldown to view data in detail

{border="0"}       -    Collapse to view the summarized data

 

The expanders can be made hidden by setting the **ShowExpanders** property of OlapReport to **false.**

 

+-------------------------------------------------------------------------------------------------------------------+
| \[C#\]                                                                                                            |
|                                                                                                                   |
|                                                                                                                   |
|                                                                                                                   |
| [// Hide Expanders]                                                                         |
|                                                                                                                   |
| [this].OlapGrid1.OlapDataManager.CurrentReport.ShowExpanders = [false]; |
+-------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------+
| \[VB\]                                                                                                         |
|                                                                                                                |
|                                                                                                                |
|                                                                                                                |
| [\' Hide Expanders]                                                                      |
|                                                                                                                |
| [Me].OlapGrid1.OlapDataManager.CurrentReport.ShowExpanders = [False] |
+----------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

