---
title: memberpropertiestool.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\memberpropertiestool.md
created_at: 2025-07-03
---








  





### Member Properties Tooltip {#member-properties-tooltip style="tab-stops: 0pt"}

To display member properties through the header ToolTip, the following property of the OLAP grid should be set to **true**:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                    |
| [// To Display Member Properties in ToolTip]                                                                     |
|                                                                                                                                                                    |
| [this][.OlapGrid1.ShowMemberPropertiesToolTip = [true];] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                |
|                                                                                                                                                                 |
| [\' To Display Member Properties in ToolTip]                                                                  |
|                                                                                                                                                                 |
| [Me][.OlapGrid1.ShowMemberPropertiesToolTip = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

 

Figure 29: OLAP Grid Displaying Member Properties through the Header ToolTip

 

Table16: Properties


  ----------------------------- ------------------------------------------------------------------------------------------------------ ------------- ----------------
  Property                      Description                                                                                            Type          Data Type
  MemberProperty                On passing the member name as a string, it renders the control accordingly with the respective data.   Server side   MemberProperty
  ShowMemberPropertiesToolTip   Gets or sets a value to include member properties on the header ToolTip.                               Server side   boolean
  ----------------------------- ------------------------------------------------------------------------------------------------------ ------------- ----------------


 

[]{#related-topics}

