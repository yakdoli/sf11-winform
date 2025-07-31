---
title: autoexecute.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\autoexecute.md
created_at: 2025-07-03
---








  









## AutoExecute {#autoexecute style="tab-stops: 0pt"}

By default, on dragging and dropping a node from cube dimension browser into an axis element builder, the grid and chart controls would be updated immediately. Instead of updating the grid and chart controls immediately, we can update it on-demand just by setting the "AutoExecute" property to "False".

On setting the "AutoExecute" property to "False", an icon appears in the OLAP Client Toolbar as well as on dragging and dropping a node from cube dimension browser; the grid and chart controls won't be updated. Whenever the user wants to update the grid and chart controls, he/she can just click the "AutoExecute" button available in the toolbar (Binding the data into grid and chart control on-demand).

 

The below code snippet would enable the AutoExecute option:

+-----------------------------------------------------------------------+
| **[\[C#\]]**                      |
|                                                                       |
| [this.OlapClient1.AutoExecute = false;\                               |
| this.OlapClient1.DataBind();]     |
+-----------------------------------------------------------------------+

 

+--------------------------------------------------------------------------+
| **[\[VB\]]**                         |
|                                                                          |
| [Me.OlapClient1.AutoExecute = False] |
|                                                                          |
| [Me.OlapClient1.DataBind()]          |
+--------------------------------------------------------------------------+

 

{border="0"}

 

Figure 47: AutoExecute button in OLAP Client Toolbar

 

Table 20: AutoExecute Property

 


  ------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ----------- ----------------
  Property      Description                                                                                                                                                          Type          Data type   Reference link
  AutoExecute   Instead of updating the grid and chart controls immediately after drag and drop, we can update it on-demand just by setting the "AutoExecute" property to "False".   Server side   boolean     \-
  ------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------- ----------- ----------------


 

Sample Link

A sample demo is available at the following link:

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapClient.Web\\Samples\\3.5\\OlapClient\\ AutoExecuteDemo**

 

[]{#related-topics}

