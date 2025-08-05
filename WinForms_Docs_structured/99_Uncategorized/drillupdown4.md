---
title: drillupdown4.md
original_path: WinForms_Docs/99_Uncategorized/drillupdown4.md
created_at: 2025-08-05
---








  





## Drill-Up/Down {#drill-updown style="tab-stops: 0pt"}

This is the basic feature of **OLAP Chart** through which the amount of information can be limited (for a better view). It allows you to drill down to access the detailed level of data, or roll up to see the summarized data using the expander's present in the chart. The expander here refers to the plus/minus sign present in the chart label followed by a member name.

 

Drill Up/Down can be done is two different ways. They are

[·      ]Drill Member

[·      ]Drill Position

 

This can be selected based on our analysis requirements.

 

**Event Support**

*Table 11: DrillUpDownClick Event*


+------------------+---------------------------------------------------------------+---------------------+-------------------+
|                  |                                                               |                     |                   |
|                  |                                                               |                     |                   |
| Event            | Description                                                   | Arguments           |  Type             |
|                  |                                                               |                     |                   |
|                  |                                                               |                     |                   |
+------------------+---------------------------------------------------------------+---------------------+-------------------+
| AfterDrillUpDown | Handles the Drill-Up/Down event when the expander is clicked. | PivotCellDescriptor | DrillDownEventArg |
+------------------+---------------------------------------------------------------+---------------------+-------------------+


 

Sample Link

A sample is available in the following locations:

 

Windows XP:

..\\Syncfusion\\EssentialStudio\\ x.x.x.x \\BI\\Web\\OlapChart.Web\\Samples\\3.5\\Data Relation\\Drill Types Demo

 

Windows 7/Vista:

C:\\Users\\\<UserName\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\x.x.x.x\\BI\\Web\\ OlapChart.Web\\Samples\\3.5\\Data Relation\\Drill Types Demo

 

More:











