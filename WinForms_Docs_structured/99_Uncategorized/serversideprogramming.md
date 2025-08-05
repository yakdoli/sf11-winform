---
title: serversideprogramming.md
original_path: WinForms_Docs/99_Uncategorized/serversideprogramming.md
created_at: 2025-08-05
---






##### Server-side Programming {#server-side-programming style="tab-stops: 0pt"}

[] 

The **ValueChanged** event is triggered when the user changes the Slider value with the mouse or mouse wheel. You should set the **Autopostback** property to **True**, to raise this event when the Slider value is changed on the client-side. You can retrieve the current Slider value using the **SliderValue** property.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [protected][ [void] Slider1_ValueChanged([object] sender, [EventArgs] e)] |
|                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                  |
| [this][.TextBox1.Text = [this].Slider1.SliderValue.ToString();]                                                        |
|                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Protected][ [Sub] Slider1_ValueChanged([ByVal] sender [As] [Object], [ByVal] e [As] EventArgs)] |
|                                                                                                                                                                                                                                                                                                                                                     |
| [Me][.TextBox1.Text = [Me].Slider1.SliderValue.ToString()]                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                     |
| [End][ [Sub]]                                                                                                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

