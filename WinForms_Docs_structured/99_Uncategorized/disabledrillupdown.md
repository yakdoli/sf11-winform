---
title: disabledrillupdown.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\disabledrillupdown.md
created_at: 2025-07-03
---








  





### Disable Drill Up/Down {#disable-drill-updown style="tab-stops: 0pt"}

The Drill Up/Down can be disabled by hiding the expanders in the OlapChart. This can be done by using the following code:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                      |
| [// Hide Expanders][]                                                                          |
|                                                                                                                                                                                      |
| [this][.OlapChart1.OlapDataManager.CurrentReport.ShowExpanders = [false];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                  |
|                                                                                                                                                                                   |
| [\' Hide Expanders][]                                                                       |
|                                                                                                                                                                                   |
| [Me][.OlapChart1.OlapDataManager.CurrentReport.ShowExpanders = [False]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

Table 12: ShowExpandersProperty


  --------------- --------------------------------------- ------------- ----------- ----------------
  Property        Description                             Type          Data type   Reference link
  ShowExpanders   Enables/disables the expander option.   Server side   boolean     \-
  --------------- --------------------------------------- ------------- ----------- ----------------


 

Sample Link

A sample demo is available at the following link:

[]{#_Toolbar}**..\\Syncfusion\\EssentialStudio\\\<VersionNumber\>\\BI\\Web\\OlapChart.Web\\Samples\\3.5\\Appearance\\** **Expanders Visibility Demo**

 

[]{#related-topics}

