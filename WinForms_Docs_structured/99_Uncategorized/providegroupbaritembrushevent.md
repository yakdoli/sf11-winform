---
title: providegroupbaritembrushevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\providegroupbaritembrushevent.md
created_at: 2025-07-03
---






##### ProvideGroupBarItemBrush Event {#providegroupbaritembrush-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

It occurs when a GroupBar Item is about to be drawn. The event handler receives an argument of type ProvideGroupBarItemBrushEventArgs.

 

The event properties associated with the **ProvideGroupBarItemBrushEventArgs** are given below.

[] 


  ----------------- -----------------------------------------------------------------------
  Members           Description
  BackgroundBrush   Gets / sets the brush that will be used to draw the specified bounds.
  Bounds            Returns the bounds for which a brush is requested.
  Item              Returns the index of the GroupBar Item being drawn.
  ----------------- -----------------------------------------------------------------------


[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                             |
| [private][ [void] gbOutlook_ProvideGroupBarItemBrush([object] sender, Syncfusion.Windows.Forms.Tools.[ProvideGroupBarItemBrushEventArgs] args)]                                                         |
|                                                                                                                                                                                                                                                                                                                                                             |
| [{]                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                             |
| [System.Drawing.Drawing2D.[Blend] blend = [new] System.Drawing.Drawing2D.[Blend]();]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                             |
| [blend.Factors = [new] [float]\[\] { 0.0f, 0.0f, 1.0f };]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                             |
| [blend.Positions = [new] [float]\[\] { 0.0F, 0.5f, 1.0F };]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                             |
| [// Estimate the GroupBar Item bounds.]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                             |
| [Rectangle][ rcgroupbaritem = args.Bounds;]                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                             |
| [// Create and initialize the LinearGradientBrush.]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                             |
| [System.Drawing.Drawing2D.[LinearGradientBrush] lgbrush = [new] System.Drawing.Drawing2D.[LinearGradientBrush](rcgroupbaritem, gbOutlook.GroupBarItems\[0\].BackColor, [SystemColors].ScrollBar, 90, [true]);] |
|                                                                                                                                                                                                                                                                                                                                                             |
| [lgbrush.Blend = blend;]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                             |
| [args.BackgroundBrush = lgbrush;]                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                             |
| [}][     ]                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Private][ [Sub] gbOutlook_ProvideGroupBarItemBrush([ByVal] sender [As] [Object], [ByVal] args [As] Syncfusion.Windows.Forms.Tools.ProvideGroupBarItemBrushEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ blend [As] [New] System.Drawing.Drawing2D.Blend()]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [blend.Factors = [New] [Single]() {0.0F, 0.0F, 1.0F}]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [blend.Positions = [New] [Single]() {0.0F, 0.5F, 1.0F}]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Estimate the GroupBar Item bounds. ]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ rcgroupbaritem [As] Rectangle = args.Bounds]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [\' Create and initialize the LinearGradientBrush. ]                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [Dim][ lgbrush [As] [New] System.Drawing.Drawing2D.LinearGradientBrush(rcgroupbaritem, gbOutlook.GroupBarItems(0).BackColor, SystemColors.ScrollBar, 90, [True])]                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [lgbrush.Blend = blend]                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [args.BackgroundBrush = lgbrush]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                           |
| [End][ [Sub]]                                                                                                                                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Refer[ ][[How to apply Gradient Rendering for the GroupBar?]{.UGHyperlink}](../../../../../../../../Documents%20and%20Settings/sylviap/Desktop/Tools%20-%20Part%202.docx#_How_to_apply)[ ]for further information on this event.[]

 

 

[]{#p625} 

 

[]{#related-topics}

