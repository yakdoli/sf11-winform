---
title: paintevent.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\paintevent.md
created_at: 2025-07-03
---






#### Paint Event {#paint-event style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

This event occurs when a TabControlAdv needs re-painting.

 

**Event Data**

 

This Event Handler receives an argument of type **EditEventArgs** containing data related to this event. The following EditEventArgs property provides information specific to this event.

[] 


  --------------- ---------------------------------------
  Members         Description
  ClipRectangle   Gets the rectangle in which to paint.
  Graphics        Gets the graphics used to paint.
  --------------- ---------------------------------------


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| **[]**                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [private][ [void] tabControlAdv1_Paint([object] sender, System.Windows.Forms.[PaintEventArgs] e)]                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [if][([this].ClientRectangle.Width \> 0 && [this].ClientRectangle.Height \> 0)]                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [LinearGradientBrush][ lgb = [new] [LinearGradientBrush]([this].ClientRectangle, [SystemColors].Control, [SystemColors].ControlDark, [LinearGradientMode].Horizontal);] |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [e.Graphics.FillRectangle(lgb, [this].ClientRectangle);]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                             |
| [Private][ [Sub] tabControlAdv1_Paint([ByVal] sender [As] [Object], [ByVal] e [As] System.Windows.Forms.PaintEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                             |
| [If][ [Me].ClientRectangle.Width \> 0 [AndAlso] [Me].ClientRectangle.Height \> 0 [Then]]                                                                           |
|                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ lgb [As] LinearGradientBrush = [New] LinearGradientBrush([Me].ClientRectangle, SystemColors.Control, SystemColors.ControlDark, LinearGradientMode.Horizontal)]                   |
|                                                                                                                                                                                                                                                                                                                                             |
| [e.Graphics.FillRectangle(lgb, [Me].ClientRectangle)]                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                             |
| [End][ [If]]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                             |
| [End][ [Sub]]                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

 

[]{#related-topics}

