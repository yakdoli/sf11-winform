---
title: drillfromalllevel.md
original_path: WinForms_Docs/99_Uncategorized/drillfromalllevel.md
created_at: 2025-08-05
---








  





### Drill from All Level {#drill-from-all-level style="tab-stops: 0pt"}

This feature enables you to display the "All" level type member in the OlapChart. This member behaves as parent to other members in its hierarchy by controlling their visibility through expander.

 

Properties

Table 13: Property Table


  ------------------ ------------------------------------------------------------------------ ------------- ----------- -----------------
  Property           Description                                                              Type          Data Type   Reference links
  ShowLevelTypeAll   Specifies whether members with level type as All has to be displayed.    Server Side   Boolean     NA
  ------------------ ------------------------------------------------------------------------ ------------- ----------- -----------------


[] 

Displaying \"All\" Level Type Member

To display the "All" level type member, set the *ShowLevelTypeAll* property to *true*. By default this is set to *false*.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [OlapDataManager][ DataManager = [new] [OlapDataManager]() { ShowLevelTypeAll = [true]};] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [OlapDataManager][ DataManager = [New] [OlapDataManager]() { ShowLevelTypeAll = [True] }] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 37: Member with Level type as All is displayed.

 

Sample Link

 

A demo of this feature is available in the following location:

 

**Windows XP:**

*..\\Syncfusion\\EssentialStudio\\x.x.x.x\\BI\\Web\\OlapChart.Web\\Samples\\3.5\\Defining Reports\\Reports In Code*

 

**Windows 7/Vista:**

*C:\\Users\\\<UserName\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\x.x.x.x\\BI\\Web\\* *OlapChart.Web\\Samples\\3.5\\Defining Reports\\Reports In Code[]*

 

[]{#related-topics}

