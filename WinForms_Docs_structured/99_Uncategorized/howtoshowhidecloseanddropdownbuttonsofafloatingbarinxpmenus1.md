---
title: howtoshowhidecloseanddropdownbuttonsofafloatingbarinxpmenus1.md
original_path: WinForms_Docs/99_Uncategorized/howtoshowhidecloseanddropdownbuttonsofafloatingbarinxpmenus1.md
created_at: 2025-08-05
---






##### How to show / hide close and dropdown buttons of a floating bar in XPMenus {#how-to-show-hide-close-and-dropdown-buttons-of-a-floating-bar-in-xpmenus style="tab-stops: 0pt"}

[] 

This can be done by using **HideCloseButton** and **HideDropDownButton** properties.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                             |
|                                                                                                                                                                                                                      |
| [//to hide close button]                                                                                                                                           |
|                                                                                                                                                                                                                      |
| [this][.mainFrameBarManager1.GetBarControl([this].bar1).HideCloseButton = [true];]    |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [//to hide dropdown button]                                                                                                                                        |
|                                                                                                                                                                                                                      |
| [this][.mainFrameBarManager1.GetBarControl([this].bar1).HideDropDownButton = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                              |
|                                                                                                                                                                                                                 |
| **[]**                                                                                                                                                        |
|                                                                                                                                                                                                                 |
| [\'to hide close button]                                                                                                                                      |
|                                                                                                                                                                                                                 |
| [Me][.mainFrameBarManager1.GetBarControl([Me].bar1).HideCloseButton = [True]]    |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [\'to hide dropdown button]                                                                                                                                   |
|                                                                                                                                                                                                                 |
| [Me][.mainFrameBarManager1.GetBarControl([Me].bar1).HideDropDownButton = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

See Also

[] 

[Toolbar Properties]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

