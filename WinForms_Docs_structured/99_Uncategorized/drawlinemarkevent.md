---
title: drawlinemarkevent.md
original_path: WinForms_Docs/99_Uncategorized/drawlinemarkevent.md
created_at: 2025-08-05
---






#### DrawLineMark Event {#drawlinemark-event style="tab-stops: 0pt"}

 

This event occurs when a custom line mark should be drawn.

 

The event handler receives an argument of type **DrawLineMarkEventArgs**. The following DrawLineMarkEventArgs members provide information specific to this event.

 


  -------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------
  Member                                                                                                   Description
  [[CustomDraw]]{.UGHyperlink}     [[If set to True, user handles drawing of the bookmark.]]{.UGHyperlink}
  [[Graphics]]{.UGHyperlink}       [[Graphics object.]]{.UGHyperlink}
  [[MarkRect]]{.UGHyperlink}       [[Rectangle where line mark should be drawn.]]{.UGHyperlink}
  [[PhysicalLine]]{.UGHyperlink}   [[Virtual line number.]]{.UGHyperlink}
  [[VirtualLine]]{.UGHyperlink}    [[Physical line number.]]{.UGHyperlink}
  -------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------


[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                            |
| [private][ [void] editControl1_DrawLineMark([object] sender, Syncfusion.Windows.Forms.Edit.[DrawLineMarkEventArgs] e)] |
|                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [if][( e.VirtualLine % 2 == 0 )]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                            |
| [Brush][ brush = [new] LinearGradientBrush(e.MarkRect, [Color].Red, [Color].Yellow, LinearGradientMode.Vertical);]     |
|                                                                                                                                                                                                                                                                            |
| [e.Graphics.FillRectangle(brush, e.MarkRect);]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [e.Graphics.DrawRectangle([Pens].IndianRed, e.MarkRect);]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                            |
| [} ]                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Private][ [Sub] editControl1_DrawLineMark([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Edit.DrawLineMarkEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [If][ e.VirtualLine [Mod] 2 = 0 [Then]]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ brush [As] Brush = [New] Drawing2D.LinearGradientBrush(e.MarkRect, Color.Red, Color.Yellow, LinearGradientMode.Vertical)]                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [e.Graphics.FillRectangle(brush, e.MarkRect)]                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [e.Graphics.DrawRectangle(Pens.IndianRed, e.MarkRect)]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [If]]                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                  |
| [End][ [Sub]]                                                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 82: Custom Indicators in the Indicator Margin

[]{#p143} 

[]{#related-topics}

