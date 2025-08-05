---
title: enablingresizingpivotgrid1.md
original_path: WinForms_Docs/04_Controls/Grid/enablingresizingpivotgrid1.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Enabling Resizing Pivot Grid {#enabling-resizing-pivot-grid style="tab-stops: 0pt"}

Users can enable or disable this feature by using the **AllowRowHeaderAreaAutoSizing***[]*property. To show the **Computation** button (**Show Fields** button) and to restrict the row header items from being stretched when more items are added to the computation area, set this property to **false**. To hide the **Computation** button (**Show Fields** Button) and to allow the row header items to stretch when more items are added to the computation area, set this property to **true**. By default the property is set to **true**.

 

The following code illustrates how to restrict the items from stretching and how to show the **Computation List** window through **Computation** button click:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                |
|                                                                                                                                                                                                                                 |
| [this] [.pivotGrid1.AllowRowHeaderAreaAutoSizing =[ false];] [] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                              |
| [Me] [.pivotGrid1.AllowRowHeaderAreaAutoSizing = [False]] [] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 28: ComputationButton, ComputationList Shown, and RowHeader Item displayed with fixed size

 

The following code illustrates how to allow the items to stretch and how to hide the **Computation** button:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                               |
|                                                                                                                                                                                                                                |
| [this] [.pivotGrid1.AllowRowHeaderAreaAutoSizing = [true];] [] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [Me] [.pivotGrid1.AllowRowHeaderAreaAutoSizing = [True]] [ [] ] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 29: ComputationButton Hidden and RowHeader Item stretched

 

 

[]{#related-topics}

