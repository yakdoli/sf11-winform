---
title: dynamicresizingofribboncontrols1.md
original_path: WinForms_Docs/04_Controls/Ribbon/dynamicresizingofribboncontrols1.md
created_at: 2025-08-05
---






#### Dynamic Resizing of Ribbon Controls {#dynamic-resizing-of-ribbon-controls style="tab-stops: 0pt"}

[] 

Ribbon Control provides **Office 2007 UI**. While resizing the ribbon window, which contains the Ribbon Controls, the ribbon controls automatically resize to fit into the Ribbon layout panel. Note: Further resizing the ribbon window will collapse the ribbon bars containing the ribbon controls.

 

Following property is used to activate the dynamic resizing feature of ribbon controls.

 

**IsAutoSizeFormEnabled** -- Gets or sets a value indicating whether the ribbon controls should dynamically resize to its auto size form or not. This is a dependency property.

[] 

Enabling Dynamic Resizing of Rabin control

**[]** 

Set **IsAutoSizeFormEnabled** to **true** to enable Dynamic Resizing of Rabin control.

The following code illustrates this.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [   \<][syncfusion][:][Ribbon ][Name][=\"MyRibbon\"][ [IsAutoSizeFormEnabled][=\"True\"\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [\</][syncfusion][:][Ribbon][\>]                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                 |
|                                                                                                                                                                                |
| []                                                                                                                                                        |
|                                                                                                                                                                                |
| [  Ribbon][ MyRibbon = [new] [Ribbon]();] |
|                                                                                                                                                                                |
| [MyRibbon.IsAutoSizeFormEnabled = [true];]                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Ribbon items automatically changed its size form when window resized.

[] 

{border="0"}

Figure 895: Ribbon Items Resized

***[]*** 

Small size form buttons automatically changed to extra small buttons when resized.

[] 

{border="0"}

Figure 896: Small Size Form Buttons Resized to Extra Small Buttons

[] 

Large size form buttons changed to small size form buttons when resized.

[] 

{border="0"}

Figure 897: Large Size Form Buttons Resized to Small Size Form Buttons

[] 


[{border="0"}]Note: Size form changed on further resizing of window.


[]{#related-topics}

