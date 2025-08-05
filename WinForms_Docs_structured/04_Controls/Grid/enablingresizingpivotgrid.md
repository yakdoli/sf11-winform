---
title: enablingresizingpivotgrid.md
original_path: WinForms_Docs/04_Controls/Grid/enablingresizingpivotgrid.md
created_at: 2025-08-05
---








  









### Enabling Resizing Pivot Grid {#enabling-resizing-pivot-grid style="tab-stops: 0pt"}

The user can enable or disable this feature using the **AllowRowHeaderAreaAutoSizing***[ ]*property.  To show the computation button (**Show Fields** button) and to restrict the row header items getting stretched when more items are added to the computation area, set this property to **false**. To hide the computation button (**Show Fields** button) and to allow the row header items getting stretched when more items are added to the computation area, set this property to **true**. By default the property is set to true.

The following code illustrates how to restrict the items from stretching and how to show the **Computation List** window through **ComputationButton** click:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| [this][.pivotGridControl1.AllowRowHeaderAreaAutoSizing = [false];][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                         |
| [Me][.pivotGridControl1.AllowRowHeaderAreaAutoSizing = [False]][ ][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 29: ComputationButton, ComputationList Shown, and RowHeader Item Displayed with Fixed Size

 

The following code illustrates how to allow the items stretching and how to hide the computation button:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                     |
| [this][.pivotGridControl1.AllowRowHeaderAreaAutoSizing = [true];][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                              |
|                                                                                                                                                                                                                                               |
| [Me][.pivotGridControl1.AllowRowHeaderAreaAutoSizing = [True]][] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 30: ComputationButton Hidden and RowHeader Item Stretched

 

 

[]{#related-topics}

