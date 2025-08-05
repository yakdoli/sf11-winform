---
title: clientsideevents7.md
original_path: WinForms_Docs/99_Uncategorized/clientsideevents7.md
created_at: 2025-08-05
---






##### Client-side Events {#client-side-events style="tab-stops: 0pt"}

[] 

The various client-side events of the ColorPicker control are illustrated below.

**[]** 

[·      ]**ClientSideOnBeforePopup**

[] 

Gets the function name to be triggered before the ColorPicker pop-up is opened.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [\<][Syncfusion][:][ColorPicker][ [ID][=\"ColorPicker1\"] [runat][=\"server\"] [ClientSideOnBeforePopup][=\"BeforePopup\"] [/\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                         |
| []                                                                                  |
|                                                                                                                                         |
| [ColorPicker1.ClientSideOnBeforePopup = [\"BeforePopup\"];] |
+-----------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                       |
|                                                                                                                                        |
| []                                                                                 |
|                                                                                                                                        |
| [ColorPicker1.ClientSideOnBeforePopup = [\"BeforePopup\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------+

[] 

[·      ]**ClientSideOnAfterPopup**

[] 

Gets the function name to be triggered after the ColorPicker pop-up is opened.

[] 

[·      ]**ClientSideOnBeforeCloseup[]**

[] 

Gets the function name to be triggered before the ColorPicker pop-up is closed.

[] 

[·      ]**ClientSideOnAfterCloseup**

[] 

Gets the function name to be triggered after the ColorPicker pop-up is closed.

[] 

[·      ]**ClientSideOnColorClick**

[] 

Gets the function name to be triggered when a color from the ColorPicker is selected.

**[]** 

[·      ]**ClientSideOnColorHover**

[] 

Gets the function name to be triggered when the mouse is hovered over a color in the color box of the ColorPicker.

[] 

[·      ]**ClientSideOnColorOut**

[                 ]

Gets the function name to be triggered when the mouse is hovered out of a color in the color box of the ColorPicker.

 

[]{#related-topics}

