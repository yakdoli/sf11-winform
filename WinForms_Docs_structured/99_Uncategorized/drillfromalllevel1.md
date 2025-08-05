---
title: drillfromalllevel1.md
original_path: WinForms_Docs/99_Uncategorized/drillfromalllevel1.md
created_at: 2025-08-05
---








  





### Drill from All Level {#drill-from-all-level style="tab-stops: 0pt"}

This feature enables you to display the "All" level type member across the rows and columns in the OlapGrid. This member behaves as a parent to other members in its hierarchy by controlling their visibility through an expander.

 

Properties

Table 12: Property Table


  ------------------ ------------------------------------------------------------------------ ------------- -----------
  Property           Description                                                              Type          Data Type
  ShowLevelTypeAll   Specifies whether members with level type as All has to be displayed.    Server side   Boolean
  ------------------ ------------------------------------------------------------------------ ------------- -----------


[] 

Displaying \"All\" Level Type Member

To display the "All" level type member, set the **ShowLevelTypeAll** property to **true**. By default this is set to **false**.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [OlapDataManager][ DataManager = [new] [OlapDataManager]() { ShowLevelTypeAll = [true]};] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                     |
| [OlapDataManager][ DataManager = [New] [OlapDataManager]() { ShowLevelTypeAll = [True] }] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 20: Member with "All" Level Type Displayed

 

Sample Link

A demo of this feature is available in the following location:

**Windows XP:**

*..\\Syncfusion\\EssentialStudio\\\<Versionnumber\>\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Defining Reports\\Reports In Code*

**Windows 7/Vista:**

*C:\\Users\\\<UserName\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\x.x.x.x\\BI\\Web\\OlapGrid.Web\\Samples\\3.5\\Defining Reports\\Reports In Code[]*

**[]** 

[]{#related-topics}

