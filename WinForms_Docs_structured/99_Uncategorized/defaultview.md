---
title: defaultview.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\defaultview.md
created_at: 2025-07-03
---








  









## Default View {#default-view style="tab-stops: 0pt"}

ChartView

 

Loads the OLAP Client by setting the OLAP Chart as a default control to view. The following code snippet will illustrate how to load the control setting OLAP Chart as a default control.

 

 

+---------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                            |
|                                                                                             |
| [this.OlapClient1.DefaultView = DefaultView.ChartView;] |
+---------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                         |
|                                                                                          |
| [Me.OlapClient1.DefaultView = DefaultView.ChartView] |
+------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 48: ChartView

GridView

Loads the OLAP Client by setting the OLAP Grid as a default control to view. The following code snippet will illustrate how to load the control setting OLAP Grid as a default control.

 

+--------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                           |
|                                                                                            |
| [this.OlapClient1.DefaultView = DefaultView.GridView;] |
+--------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                         |
|                                                                                          |
| [Me.OlapClient1.DefaultView = DefaultView. GridView] |
+------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 49: Grid View

 

Table 21: DefaultView Property

 


  ------------- ------------------------------------------------------------------------------------------------------------------------------- ------------- ---------------------------------------------------- ---------------------------------------------------------
  Property      Description                                                                                                                     Type          [Data type]   [Reference link]
  DefaultView   This option would allow user to set the control to view on OLAP Client load. The default control may be either chart or grid.   Server side   enum                                                 \-
  ------------- ------------------------------------------------------------------------------------------------------------------------------- ------------- ---------------------------------------------------- ---------------------------------------------------------


 

Sample Link

A sample demo is available at the following link:

**..\\Syncfusion\\EssentialStudio\\\<Version Number\>\\BI\\Web\\OlapClient.Web\\Samples\\3.5\\OlapClient\\ DefaultViewDemo**

[]{#related-topics}

