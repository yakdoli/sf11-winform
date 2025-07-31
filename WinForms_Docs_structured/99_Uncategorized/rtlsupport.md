---
title: rtlsupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\rtlsupport.md
created_at: 2025-07-03
---






##### RTL Support {#rtl-support style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

RightToLeft

 

Tabs framework allows the tabitems in the TabControlAdv to be drawn from right to left. This can be done by setting the RightToLeft property to Yes.

 

This property aligns the tabs and the text from right to left which proves to be helpful for the Right-To-Left languages.

[] 


  ------------------------ --------------------------------------------------------------------------------------
  TabControlAdv Property   Description
  RightToLeft              Specifies to draw the tabs and the text from right to left. The default value is No.
  ------------------------ --------------------------------------------------------------------------------------


[] 

[ {border="0"}]

**[]** 

Figure 1072: TabControlAdv with Tabs drawn from Left and Right

**[]** 

Rotating Tabs

[] 

**RotateTabsWhenRTL** property can be used to rotate the tabs of the tabcontroladv that are aligned to the left and right of the tabpages. This specifies whether a tab should be drawn from left to right or from right to left. The default value is False.

 

When the RightToLeft mode is activated and RotateTabsWhenRTL property is enabled, tab rotation is allowed.

[] 


  ------------------------ -------------------------------------------------------------------------------------------------------------
  TabControlAdv Property   Description
  RotateTabsWhenRTL        Gets / sets the value that decides whether the tabs can be rotated, when the RightToLeft mode is activated.
  ------------------------ -------------------------------------------------------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 1073: TabControlAdv with RotateTabsWhenRTL set to False and True

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                   |
|                                                                                                                                                                  |
| **[]**                                                                                                         |
|                                                                                                                                                                  |
| [this][.tabControlAdv1.RightToLeft = System.Windows.Forms.RightToLeft.Yes;] |
|                                                                                                                                                                  |
| [this][.tabControlAdv1.RotateTabsWhenRTL = [true];]    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                            |
|                                                                                                                                                               |
| **[]**                                                                                                      |
|                                                                                                                                                               |
| [Me][.tabControlAdv1.RightToLeft = System.Windows.Forms.RightToLeft.Yes] |
|                                                                                                                                                               |
| [Me][.tabControlAdv1.RotateTabsWhenRTL = [True]]    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 


{border="0"} Note: Only VS2005Style, OneNoteStyle and DockingWhidbeyStyle support RotateTabsWhenRTL property.


 

 

 

 

[]{#related-topics}

