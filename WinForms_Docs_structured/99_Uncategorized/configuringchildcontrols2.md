---
title: configuringchildcontrols2.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\configuringchildcontrols2.md
created_at: 2025-07-03
---






##### Configuring Child Controls[] {#configuring-child-controls style="tab-stops: 0pt"}

Constraints on FlowLayout

[] 

Constrained FlowLayout is typically useful when creating resizable data entry forms filled with textboxes, checkboxes, and so on. During design time, the constraints can be specified for each Child control through its extended **Constraints on flowLayout** property. The constraints in the FlowLayout are described below in detail.

[] 

Setting the Constraints Through Designer

[] 

HAlign and VAlign

[] 

The alignment of the Child controls that have been placed within a row can be set using the properties given below. The alignment is done based upon the layout modes of the Child controls.

[] 


+-----------------------------------+-----------------------------------------------------------------------------------+
| Child Control Constraints         | Description                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------+
| HAlign                            | Specifies the mode in which the Child control should be laid out within a row.    |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   | The options includes are as follows.                                              |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   | *Left,*                                                                           |
|                                   |                                                                                   |
|                                   | *Right,*                                                                          |
|                                   |                                                                                   |
|                                   | *Center and*                                                                      |
|                                   |                                                                                   |
|                                   | *Justify.*                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------+
| VAlign                            | Specifies the mode in which the Child control should be laid out within a column. |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   | The options includes are as follows.                                              |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   |                                                                                   |
|                                   | *Top,*                                                                            |
|                                   |                                                                                   |
|                                   | *Bottom,*                                                                         |
|                                   |                                                                                   |
|                                   | *Center and*                                                                      |
|                                   |                                                                                   |
|                                   | *Justify.*                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------+


[] 

When the alignment is set to \'Justify\', any extra space will be equally distributed across the other Child controls that have been justified differently within that same row. However, when there is a lack of sufficient space, the justified Child controls are shrunk proportionally based on their minimum size and preferred size settings (specifically, the difference between the two sizes).

[] 


{border="0"} Note:[ ]The Alignment property should be set to \'True\' for the above properties to take effect.


[] 

{border="0"}

[] 

Figure 674: Children with different HAlign Settings

[] 


{border="0"} Note: In the figure above, the textboxes have autolabels associated with them.


[] 

Layout Participation

[] 

You can prevent a Child control from participating in the layout using the below given property.

[] 


  -------------------------- -------------------------------------------------------------------------------------------------------------
  Child Control Constraint   Description
  Active                     Specifies whether the Child control should participate in the layout. The default value is set to \'True\'.
  -------------------------- -------------------------------------------------------------------------------------------------------------


[] 

Line Beginner

[] 

You can force a Child control to always start at a new row by setting the below given property.

[] 


  -------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  Child Control Constraint   Description
  NewLine                    Specifies whether the Child control should always be moved to the beginning of a new line. The default value is set to \'False\'.
  -------------------------- -----------------------------------------------------------------------------------------------------------------------------------


[] 

Row Height and Column Width

[] 

By default, rows are not adjusted to take into account the remaining vertical space in the horizontal layout mode or horizontal space in the vertical layout mode. This can be done using the properties given below.

[] 


  -------------------------- -----------------------------------------------------------------------------------------------------------------------
  Child Control Constraint   Description
  ProportionalColWidth       Specifies if proportional column widths should be used in the vertical layout. The default value is set to \'False\'.
  ProportionalRowHeight      Specifies if proportional row heights should be used in the horizontal layout. The default value is set to \'False\'.
  -------------------------- -----------------------------------------------------------------------------------------------------------------------


[] 

{border="0"}

[] 

Figure 675: Two Proportionally Aligned Rows Split the Extra Horizontal Space Between Them

[] 

The methods associated with the above properties are given below.

[] 


  ------------------- -------------------------------------------------------------------------------
  Methods             Description
  GetConstraints      Returns the constraints associated with the specified control.
  GetConstraintsRef   Returns a reference to the constraints associated with the specified control.
  SetConstraints      Specifies the constraints associated with the specified control.
  ------------------- -------------------------------------------------------------------------------


[] 

In code, you can specify constraints through the **SetConstraints()** method. The **FlowLayoutConstraints** type defines the constraint that can be specified on a Child component.

[] 

Setting the Constraints Programmatically

[] 

In the coding given below, the constraints are set to the particular control along with the constraint values like Active, HAlign, VAlign, NewLine, ProportionalColWidth and ProportionalRowHeight.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [this][.flowLayout1.SetConstraints([this].textBox1, [new] Syncfusion.Windows.Forms.Tools.[FlowLayoutConstraints]([true], Syncfusion.Windows.Forms.Tools.[HorzFlowAlign].Justify, Syncfusion.Windows.Forms.Tools.[VertFlowAlign].Center, [false], [false], [false]));] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Me][.flowLayout1.SetConstraints([Me].textBox1, [New] Syncfusion.Windows.Forms.Tools.FlowLayoutConstraints([True], Syncfusion.Windows.Forms.Tools.HorzFlowAlign.Justify, Syncfusion.Windows.Forms.Tools.VertFlowAlign.Center, [False], [False], [False]))] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

See Also

[] 

[Configuring FlowLayout]{.UGHyperlink}[, ]{.UGHyperlink}[Centering the Child Controls Horizontally and Vertically]{.UGHyperlink}[, ]{.UGHyperlink}[Enabling Constrained FlowLayout on a Container]{.UGHyperlink}[, ]{.UGHyperlink}[Rearranging the Controls laid out by FlowLayout]{.UGHyperlink}[, ]{.UGHyperlink}[Child Control Settings]{.UGHyperlink}[]{.UGHyperlink}

[]{#related-topics}

