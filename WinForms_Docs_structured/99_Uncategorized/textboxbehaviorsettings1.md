---
title: textboxbehaviorsettings1.md
original_path: WinForms_Docs/99_Uncategorized/textboxbehaviorsettings1.md
created_at: 2025-08-05
---






##### [TextBox Behavior settings] {#textbox-behavior-settings style="tab-stops: 0pt"}

[] 

Editing the text

[] 

The text can be displayed in the generic textbox, on selecting from the drop down and it can be edited at run time only by enabling the **AllowTextEditing** property.

[] 


  ------------------ ---------------------------------------------------------------------
  Property           Description
  AllowTextEditing   Specifies whether to allow editing the text. Default value is True.
  ------------------ ---------------------------------------------------------------------


[] 

Postback

[] 

When the text is edited, a postback can be optionally can be triggered, by setting the **AutoPostBackOnTextChanged** property.

[] 


  --------------------------- -------------------------------------------------------------------------------------------
  Property                    Description
  AuotPostBackOnTextChanged   Specifies whether to postback the page, when the text is changed. Default value is False.
  --------------------------- -------------------------------------------------------------------------------------------


[] 

Programmatically the text editing and page postback can be set as follows.

[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                                 |
| []                                                             |
|                                                                                                                                 |
| [genericdropdown1.AllowTextEditing = [true];]          |
|                                                                                                                                 |
| [genericdropdown1.AutoPostBackOnTextChanged = [true];] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                                           |
| [Private][ genericdropdown1.AllowTextEditing = [True]]          |
|                                                                                                                                                                                                           |
| [Private][ genericdropdown1.AutoPostBackOnTextChanged = [True]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Customizing dropdown image

[] 

The button image of the generic control can be customized by setting the image name to the **ButtonImageSrc** property. Make sure to add the image to the application.

[] 

{border="0"}

[] 

Figure 98: Custom Button Settings

[] 


  ---------------- -----------------------------------------------------------
  Property         Description
  ButtonImageSrc   Specifies name of the custom image to use for the button.
  ---------------- -----------------------------------------------------------


[] 

+---------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                |
|                                                                                                                                 |
| []                                                             |
|                                                                                                                                 |
| [genericdropdown3.ButtonImageSrc = [\"buton.gif\"];] |
+---------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                          |
|                                                                                                                                                                                                           |
| []                                                                                                                                       |
|                                                                                                                                                                                                           |
| [Private][ genericdropdown3.ButtonImageSrc = [\"buton.gif\"]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

