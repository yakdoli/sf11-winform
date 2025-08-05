---
title: providelayoutinformationevent.md
original_path: WinForms_Docs/99_Uncategorized/providelayoutinformationevent.md
created_at: 2025-08-05
---






#### ProvideLayoutInformation Event {#providelayoutinformation-event style="tab-stops: 0pt"}

[] 

This event is triggered to obtain the preferred size information for a Child control during layout.

 

The event handler receives an argument of type **ProvideLayoutInformationEventArgs** containing data related to this event. The ProvideLayoutInformationEventArgs members provide information specific to this event.

[] 


  ----------- -----------------------------------------------------------------------
  Members     Description
  Control     Specifies whether the child controls should be automatically aligned.
  Handle      Specifies whether this event was handled and a value provided.
  Requested   Returns the type of information requested.
  Size        Gets / sets the size to be returned.
  ----------- -----------------------------------------------------------------------


[] 

You can handle this event to autosize the Label control when you increase / decrease the form width.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                    |
| [private][ [void] flowLayout1_ProvideLayoutInformation([object] sender, Syncfusion.Windows.Forms.Tools.[ProvideLayoutInformationEventArgs] e)] |
|                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                    |
| [if][ (e.Control == [this].label1 && e.Requested == LayoutInformationType.PreferredSize)]                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                    |
| [Graphics][ g = [this].CreateGraphics();]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                    |
| [SizeF][ szPref = g.MeasureString([this].label1.Text, [this].label1.Font, [this].ClientRectangle.Width);]                                      |
|                                                                                                                                                                                                                                                                                                    |
| [e.Size = [new] [Size]([this].ClientRectangle.Width-20, ([int])szPref.Height + 5);     ]                                                                                   |
|                                                                                                                                                                                                                                                                                                    |
| [e.Handled = [true];]                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                    |
| [g.Dispose();]                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [Private][ [Sub] flowLayout1_ProvideLayoutInformation([ByVal] sender [As] [Object], [ByVal] e [As] Syncfusion.Windows.Forms.Tools.ProvideLayoutInformationEventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [If][ e.Control = [Me].label1 [AndAlso] e.Requested = LayoutInformationType.PreferredSize [Then]]                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ g [As] Graphics = [Me].CreateGraphics()]                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [Dim][ szPref [As] SizeF = g.MeasureString([Me].label1.Text, [Me].label1.Font, [Me].ClientRectangle.Width)]                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [e.Size = [New] Size([Me].ClientRectangle.Width - 20, [CInt](szPref.Height) + 5)]                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [e.Handled = [True]]                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [g.Dispose()]                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [End][ [If]]                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                          |
| [End][ [Sub]]                                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

