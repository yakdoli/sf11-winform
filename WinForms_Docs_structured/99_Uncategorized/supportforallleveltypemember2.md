---
title: supportforallleveltypemember2.md
original_path: WinForms_Docs/99_Uncategorized/supportforallleveltypemember2.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Support for \"All\" Level Type Member {#support-for-all-level-type-member style="tab-stops: 0pt"}

This feature enables you to display the "All" level type member across the rows and columns in the OlapGrid. This member behaves as parent to other members in its hierarchy by controlling their visibility through expander.

 

Properties

Table 2: Property Table


  ------------------ ------------------------------------------------------------------------ -------- ----------- -----------------
  Property           Description                                                              Type     Data Type   Reference links
  ShowLevelTypeAll   Specifies whether members with level type as All has to be displayed.    Normal   Boolean     NA
  ------------------ ------------------------------------------------------------------------ -------- ----------- -----------------


[] 

Displaying \"All\" Level Type Member

To display the "All" level type member, set the *ShowLevelTypeAll* property to *true*. By default this is set to *false*.  

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| [OlapDataManager] [ DataManager = [new][OlapDataManager]() { ShowLevelTypeAll = [true]};] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                               |
| **[]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [OlapDataManager] [ DataManager = [New][OlapDataManager]() { ShowLevelTypeAll = [True] }] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 38: Member with Level type "All" is displayed.

**[]**  

Sample Link

A demo of this feature is available in the following location:

 

**Windows XP:**

*..\\Syncfusion\\EssentialStudio\\\<Versionnumber\>\\BI\\WPF\\OlapGrid.WPF\\Samples\\Defining Reports\\Reports-in-code Demo*

 

**Windows 7/Vista:**

*C:\\Users\\\<UserName\>\\AppData\\Local\\Syncfusion\\EssentialStudio\\x.x.x.x\\BI\\ WPF\\OlapGrid.WPF\\Samples\\Defining Reports\\Reports-in-code Demo[]*

***[]***  

 

[]{#related-topics}

