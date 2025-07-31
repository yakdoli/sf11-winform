---
title: clientsideprogramming.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideprogramming.md
created_at: 2025-07-03
---






##### Client-side Programming {#client-side-programming style="tab-stops: 0pt"}

[] 

The various client-side events of the Slider control are illustrated below.

[] 

[·      ]CurrentValue()

[] 

Gets the current value of the slider.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                        |
|                                                                                                                                 |
| []                                                                          |
|                                                                                                                                 |
| [function currentvalue()]                                                   |
|                                                                                                                                 |
| [{]                                                                         |
|                                                                                                                                 |
| [var track= \$find([\"\<%=Slider1.ClientID%\>\"]);] |
|                                                                                                                                 |
| [alert(track.get_currentValue());]                                          |
|                                                                                                                                 |
| [}]                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]Disable(bool val)

[] 

Enables / disables the track handle. Default Value is set to **False**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                         |
|                                                                                                                                  |
| []                                                                           |
|                                                                                                                                  |
| [function disable()]                                                         |
|                                                                                                                                  |
| [{]                                                                          |
|                                                                                                                                  |
| [var track = \$find([\"\<%=Slider1.ClientID%\>\"]);] |
|                                                                                                                                  |
| [track.set_disable([true]);]                            |
|                                                                                                                                  |
| [}]                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]ShowHandle(bool val)

[] 

Shows / hides the track handle. Default Value is set to **True**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                         |
|                                                                                                                                  |
| []                                                                           |
|                                                                                                                                  |
| [function hideTrackHandle()]                                                 |
|                                                                                                                                  |
| [{]                                                                          |
|                                                                                                                                  |
| [var track = \$find([\"\<%=Slider1.ClientID%\>\"]);] |
|                                                                                                                                  |
| [track.set_showHandle([false]);]                        |
|                                                                                                                                  |
| [}]                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------+

[] 

Client-side Event

[] 

The **ClientSideOnValueChange** event is triggered when the Slider value changes.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[JavaScript\]]**                                                                                           |
|                                                                                                                                                    |
| []                                                                                             |
|                                                                                                                                                    |
| [function ValueChange(sender,args)]                                                            |
|                                                                                                                                                    |
| [{]                                                                                            |
|                                                                                                                                                    |
| [document.getElementById([\"Label1\"]).value= args.get_SliderValue();] |
|                                                                                                                                                    |
| [}]                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

