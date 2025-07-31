---
title: statusbaradvpanel.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\statusbaradvpanel.md
created_at: 2025-07-03
---






##### StatusBarAdvPanel {#statusbaradvpanel style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

 

StatusBarAdvPanels can also be added to the StatusBarAdv control using the **Panels** property. On clicking the Panels property, the **StatusBarAdvPanel Collection Editor** pops up. Using this window, the user can add any number of panels to the control and customize them according to their requirements.

[] 


  ----------------------- -------------------------------------------------------------------------
  StatusBarAdv Property   Description
  Panels                  Indicates the StatusBarAdvPanel controls contained in the StatusBarAdv.
  ----------------------- -------------------------------------------------------------------------


[] 

[{border="0"}][]

[] 

Figure 1012: StatusBarAdvPanel Collection Editor

[] 

Spacing

[] 

The space between the panels can be set using the property given below.

[] 


  ----------------------- ---------------------------------------------
  StatusBarAdv Property   Description
  Spacing                 Gets / sets the spacing between the panels.
  ----------------------- ---------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                     |
|                                                                                                                                                                                                    |
| []                                                                                                                                               |
|                                                                                                                                                                                                    |
| [this][.statusBarAdv1.Spacing = [new] System.Drawing.[Size](5, 5);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                       |
|                                                                                                                                                                          |
| []                                                                                                                     |
|                                                                                                                                                                          |
| [Me][.statusBarAdv1.Spacing = [New] System.Drawing.Size(5, 5)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[{border="0"}][]

[] 

Figure 1013: Spacing property Set

[] 

Panel Size

 

 The rectangle that is used to display the panels can be customized using the property given below.

[] 


  ----------------------- ------------------------------------------------------------------------------
  StatusBarAdv Property   Description
  CustomLayoutBounds      Indicates a custom rectangle that the layout will use to display the panels.
  ----------------------- ------------------------------------------------------------------------------


[] 

It can be set programmatically through the below code snippet.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [this][.statusBarAdv1.CustomLayoutBounds = [new] System.Drawing.[Rectangle](5, 2, 100, 20);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                                          |
| [Me][.statusBarAdv1.CustomLayoutBounds = [New] System.Drawing.[Rectangle](5, 2, 100, 20)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 1014: StatusBarAdv with CustomLayoutBounds property Set

 

 

 

 

[]{#related-topics}

