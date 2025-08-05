---
title: configuringflowlayout.md
original_path: WinForms_Docs/99_Uncategorized/configuringflowlayout.md
created_at: 2025-08-05
---






##### Configuring FlowLayout {#configuring-flowlayout style="tab-stops: 0pt"}

[] 

Layout Mode

[] 

The layout mode dictates the core function of a FlowLayout, whether to layout the Child controls horizontally or vertically. This property will be in effect for both the scenarios.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------+
| FlowLayout Property               | Description                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------+
| LayoutMode                        | Specifies the layout mode of the Child controls. The default value is set to \'Horizontal\'. |
|                                   |                                                                                              |
|                                   |                                                                                              |
|                                   |                                                                                              |
|                                   | The options included are as follows.                                                         |
|                                   |                                                                                              |
|                                   |                                                                                              |
|                                   |                                                                                              |
|                                   | *Horizontal and*                                                                             |
|                                   |                                                                                              |
|                                   | *Vertical.*                                                                                  |
+-----------------------------------+----------------------------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                  |
|                                                                                                                                                                                                       |
| [this][.flowLayout1.LayoutMode = Syncfusion.Windows.Forms.Tools.[FlowLayoutMode].Vertical;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                          |
|                                                                                                                                                                             |
| []                                                                                                                        |
|                                                                                                                                                                             |
| [Me][.flowLayout1.LayoutMode = Syncfusion.Windows.Forms.Tools.FlowLayoutMode.Vertical] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 669: Layout Mode set to \"Vertical\"

[] 

ParticipateInLayout

[] 

Child controls can be prevented from being laid out using the FlowLayout Manager. This can be done using the methods given below.

[] 


  ------------------------ -------------------------------------------------------------
  Method                   Description
  GetParticipateInLayout   Indicates whether the component is in the layout list.
  SetParticipateInLayout   Adds or removes the specified control from the layout list.
  ------------------------ -------------------------------------------------------------


[] 

The following code can be used to add or remove the Child control from the FlowLayout list programmatically.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| []                                                                                                                                                |
|                                                                                                                                                                                                     |
| [this][.flowLayout1.SetParticipateInLayout([this].button1,[false]);] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                             |
|                                                                                                                                                                                                |
| []                                                                                                                                           |
|                                                                                                                                                                                                |
| [Me][.flowLayout1.SetParticipateInLayout([Me].button1,[False])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

HGap and VGap

[] 

The horizontal and the vertical gap between the Child controls can be set using the properties given below.

[] 


  --------------------- ------------------------------------------------------------
  FlowLayout Property   Description
  HGap                  Gets / sets the horizontal spacing between the components.
  VGap                  Gets / sets the vertical spacing between the components.
  --------------------- ------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                       |
|                                                                                                                      |
| []                                                                 |
|                                                                                                                      |
| [this][.flowLayout1.HGap = 20;] |
|                                                                                                                      |
| [this][.flowLayout1.VGap = 20;] |
+----------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                |
|                                                                                                                   |
| []                                                              |
|                                                                                                                   |
| [Me][.flowLayout1.HGap = 20] |
|                                                                                                                   |
| [Me][.flowLayout1.VGap = 20] |
+-------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 670: HGap and VGap Set

[] 

AutoHeight

[] 

The height of the Container control can be automatically increased when there is a lack of sufficient space to show the Child components in the horizontal alignment mode. This is useful to enforce minimum heights on Container controls and forms.

[] 


  --------------------- -----------------------------------------------------------------------------------------------------------
  FlowLayout Property   Description
  AutoHeight            Specifies if the Container\'s height should be enforced to the minimum when in horizontal alignment mode.
  --------------------- -----------------------------------------------------------------------------------------------------------


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                      |
|                                                                                                                                                     |
| []                                                                                                |
|                                                                                                                                                     |
| [this][.flowLayout1.AutoHeight = [true];] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                               |
|                                                                                                                                                  |
| []                                                                                             |
|                                                                                                                                                  |
| [Me][.flowLayout1.AutoHeight = [True]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Layout Direction

[] 

FlowLayout allows you to layout the Child controls in the opposite direction (right to left or bottom to top).

[] 


  --------------------- ------------------------------------------------------------------
  FlowLayout Property   Description
  ReverseRows           Specifies to layout the Child controls in the reverse direction.
  --------------------- ------------------------------------------------------------------


[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                       |
|                                                                                                                                                      |
| []                                                                                                 |
|                                                                                                                                                      |
| [this][.flowLayout1.ReverseRows = [true];] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                |
|                                                                                                                                                   |
| []                                                                                              |
|                                                                                                                                                   |
| [Me][.flowLayout1.ReverseRows = [True]] |
+---------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 671: ReverseRows property set to \"True\"

[] 

Alignment

[] 

The Alignment property is where you specify whether the current layout logic should be simple or constraint-based.

[] 


{border="0"} Note: Alignment is applied only along the direction of flow. For example, if the LayoutMode property is set to \'Horizontal\' and the Alignment property is set to \'Center\', then the rows will be centered horizontally.


[] 


+-----------------------------------+------------------------------------------------------------------------+
| FlowLayout Property               | Description                                                            |
+-----------------------------------+------------------------------------------------------------------------+
| Alignment                         | Specifies the alignment of layout components in the direction of flow. |
|                                   |                                                                        |
|                                   |                                                                        |
|                                   |                                                                        |
|                                   | The options included are as follows.                                   |
|                                   |                                                                        |
|                                   |                                                                        |
|                                   |                                                                        |
|                                   | Center,                                                                |
|                                   |                                                                        |
|                                   | Near,                                                                  |
|                                   |                                                                        |
|                                   | Far and                                                                |
|                                   |                                                                        |
|                                   | ChildConstraints.                                                      |
+-----------------------------------+------------------------------------------------------------------------+


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                  |
|                                                                                                                                                                                                 |
| []                                                                                                                                            |
|                                                                                                                                                                                                 |
| [this][.flowLayout1.Alignment = Syncfusion.Windows.Forms.Tools.[FlowAlignment].Near;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                  |
|                                                                                                                                                                       |
| [Me][.flowLayout1.Alignment = Syncfusion.Windows.Forms.Tools.FlowAlignment.Near] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

***[]*** 

Figure 672: Alignment = \"Near\"

[] 

Once you specify the alignment of a FlowLayout as \'**ChildConstraints\'**, the Layout Manager will use a constraint-based layout logic based on the constraints specified on each Child component. During design time, the constraints can be specified for each Child control through the following extended property.

[] 


  --------------------------- -----------------------------------------------------------------------------------------------------------------------------------
  FlowLayout Property         Description
  Constraints on flowLayout   Specifies the alignment of layout components in the direction of flow when the Alignment property is set to \'ChildConstraints\'.
  --------------------------- -----------------------------------------------------------------------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [this][.flowLayout1.Alignment = Syncfusion.Windows.Forms.Tools.[FlowAlignment].ChildConstraints;] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [Me][.flowLayout1.Alignment = Syncfusion.Windows.Forms.Tools.FlowAlignment.ChildConstraints] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

{border="0"}

[] 

Figure 673: VAlign of Constraints on flowLayout property set to \"Justify\"

[] 


{border="0"} Note: Refer FlowLayout - Configuring Child Controls topic to know about HAlign, VAlign and other options provided by the Constraints on flowLayout property.


[] 

See Also

[] 

[FlowLayout - Configuring Child Controls]{.UGHyperlink}[, ]{.UGHyperlink}[Centering the Child Controls Horizontally and Vertically]{.UGHyperlink}[, ]{.UGHyperlink}[Enabling Constrained FlowLayout on a Container]{.UGHyperlink}[, ]{.UGHyperlink}[Rearranging the Controls laid out by FlowLayout]{.UGHyperlink}[]{.UGHyperlink}

[[]]{.UGHyperlink} 

[]{#p825}[[]]{.UGHyperlink} 

 

[]{#related-topics}

