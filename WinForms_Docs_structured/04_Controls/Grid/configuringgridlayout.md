---
title: configuringgridlayout.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\04_Controls\Grid\configuringgridlayout.md
created_at: 2025-07-03
---






##### Configuring GridLayout {#configuring-gridlayout style="tab-stops: 0pt"}

[] 

Rows and Columns

[] 

The GridLayout simply divides the available space into a number of rows and columns based on the number of Child controls. The number of rows and columns can be specified using the properties given below.

[] 


  --------------------- ----------------------------------------------
  GridLayout Property   Description
  Rows                  Specifies the number of rows in the grid.
  Columns               Specifies the number of columns in the grid.
  --------------------- ----------------------------------------------


[] 

The **Rows** property usually dictates the number of columns (overriding the Columns property setting) based on the number of Child controls, unless the Rows property is set to \'Null\' or less, in which case the **Columns** property will dictate the number of rows.

 

The following code snippet arranges the Child controls in one column and two rows.

[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                         |
|                                                                                                                        |
| []                                                                   |
|                                                                                                                        |
| [this][.gridLayout1.Rows = 2;]    |
|                                                                                                                        |
| [this][.gridLayout1.Columns = 1;] |
+------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                  |
|                                                                                                                     |
| []                                                                |
|                                                                                                                     |
| [Me][.gridLayout1.Rows = 2]    |
|                                                                                                                     |
| [Me][.gridLayout1.Columns = 1] |
+---------------------------------------------------------------------------------------------------------------------+

[] 

HGap and VGap

[] 

The horizontal and the vertical gap between the Child controls can be set using the properties given below.

[] 


  --------------------- ------------------------------------------------------------
  GridLayout Property   Description
  HGap                  Gets / sets the horizontal spacing between the components.
  VGap                  Gets / sets the vertical spacing between the components.
  --------------------- ------------------------------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                     |
|                                                                                                                    |
| []                                                               |
|                                                                                                                    |
| [this][.gridLayout1.HGap=10;] |
|                                                                                                                    |
| [this][.gridLayout1.VGap=10;] |
+--------------------------------------------------------------------------------------------------------------------+

**[]** 

+-----------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                              |
|                                                                                                                 |
| []                                                            |
|                                                                                                                 |
| [Me][.gridLayout1.HGap=10] |
|                                                                                                                 |
| [Me][.gridLayout1.VGap=10] |
+-----------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 688: GridLayout with Rows, Columns, HGap and VGap properties Set

[] 


{border="0"} Note: To include some margin space along the borders, refer Margin Settings.


[] 

See Also

[] 

[GridLayout - Configuring Child Controls]{.UGHyperlink}[, ]{.UGHyperlink}[Rearranging the Controls laid out by GridLayout]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

