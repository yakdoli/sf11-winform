---
title: drillupdown5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\drillupdown5.md
created_at: 2025-07-03
---








  





## Drill Up/Down {#drill-updown style="tab-stops: 0pt"}

This is the basic feature of the OlapGrid control through which the amount of information can be limited. It allows you to drill down to access the detailed level of data, or drill up to see the summarized data using the expanders present in the grid. The expander here refers to the plus/minus sign present in the grid followed by a member.

       {border="0"}  or {border="0"} Drill down to view data in detail

       {border="0"}  or {border="0"} Collapse to view the summarized data

 

Drill up/down can be done in two different ways. They are:

1.   Drill Member

2.   Drill Position

 

This can be selected based on our analysis requirements.

 

**Event Support**

Table 10: DrillUpDownClick Event


+------------------+---------------------------------------------------------------------------------------------------+---------------------+---------------------+
| Event            | Description                                                                                       | Arguments           |  Type               |
|                  |                                                                                                   |                     |                     |
|                  |                                                                                                   |                     |                     |
+------------------+---------------------------------------------------------------------------------------------------+---------------------+---------------------+
| DrillUpDownClick | Handles the Drill-Up/Down event when the **IsAsyncReqData** property of OLAP Grid is set to False | PivotCellDescriptor | DrillUpDownEventArg |
+------------------+---------------------------------------------------------------------------------------------------+---------------------+---------------------+


 

Sample Link

A sample is available in the following locations:

Windows XP:

..\\Syncfusion\\EssentialStudio\\\<VersionNumber\>\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Data Relation\\Drill Types Demo

Windows 7/Vista:

C:\\Users\\\<UserName\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\x.x.x.x\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Data Relation\\Drill Types Demo

 

More:











