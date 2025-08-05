---
title: disabledrillupdown1.md
original_path: WinForms_Docs/99_Uncategorized/disabledrillupdown1.md
created_at: 2025-08-05
---








  





### Disable Drill Up/Down {#disable-drill-updown style="tab-stops: 0pt"}

The drill up/down functionality can be disabled by hiding the expanders in the OlapGrid control. This can be done by using the following code:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                     |
| [// Hide Expanders][]                                                                         |
|                                                                                                                                                                                     |
| [this][.OlapGrid1.OlapDataManager.CurrentReport.ShowExpanders = [false];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                 |
|                                                                                                                                                                                  |
| [\' Hide Expanders][]                                                                      |
|                                                                                                                                                                                  |
| [Me][.OlapGrid1.OlapDataManager.CurrentReport.ShowExpanders = [False]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Table 11: ShowExpanders Property


  --------------- --------------------------------------- ------------- -----------
  Property        Description                             Type          Data Type
  ShowExpanders   Enables/disables the expander option.   Server side   boolean
  --------------- --------------------------------------- ------------- -----------


 

Sample Link

A sample demo is available at the following link:

[]{#_Toolbar}**..\\Syncfusion\\EssentialStudio\\\<VersionNumber\>\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Appearance\\Appearance Demo**

 

[]{#related-topics}

