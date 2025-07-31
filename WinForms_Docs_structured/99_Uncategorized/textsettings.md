---
title: textsettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\textsettings.md
created_at: 2025-07-03
---






##### Text Settings {#text-settings style="tab-stops: 0pt"}

[] 

This topic discusses how the text settings of the Captcha control can be customized.

 

The text (comprising alphabetic / numeric characters) can be set for the Captcha control using the **CaptchaChars** property. Also, text can be made case-sensitive using the **CaseSensitive** property.

[] 


+-----------------------------------+----------------------------------------------------------------------------------+
| Property                          | Description                                                                      |
+-----------------------------------+----------------------------------------------------------------------------------+
| CaptchaChars                      | Gets / sets the Captcha characters.                                              |
|                                   |                                                                                  |
|                                   |                                                                                  |
|                                   |                                                                                  |
|                                   | Default value is abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789. |
+-----------------------------------+----------------------------------------------------------------------------------+
| CaseSensitive                     | Gets / sets value that indicates whether Captcha is case-sensitive or not.       |
|                                   |                                                                                  |
|                                   |                                                                                  |
|                                   |                                                                                  |
|                                   | Default value is set to False.                                                   |
+-----------------------------------+----------------------------------------------------------------------------------+


[] 

+------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                       |
|                                                                                                                        |
| []                                                    |
|                                                                                                                        |
| [Captcha1.CaptchaChars = [\"abcABC123\"];] |
|                                                                                                                        |
| [Captcha1.CaseSensitive = [true];]            |
+------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                      |
|                                                                                                                       |
| []                                                   |
|                                                                                                                       |
| [Captcha1.CaptchaChars = [\"abcABC123\"]] |
|                                                                                                                       |
| [Captcha1.CaseSensitive = [True]]            |
+-----------------------------------------------------------------------------------------------------------------------+

[] 

Text Length

**[]** 

Number of characters to be displayed by the control can be limited by users using the below given property.

[] 


  ----------- -------------------------------------------------
  Property    Description
  MaxLength   Gets / sets maximum length of the Captcha text.
  ----------- -------------------------------------------------


[] 

+-------------------------------------------------------------------------------+
| **[\[C#\]]**                              |
|                                                                               |
| []           |
|                                                                               |
| [Captcha1.Maxlength = 6;] |
+-------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------+
| **[\[VB\]]**                             |
|                                                                              |
| []          |
|                                                                              |
| [Captcha1.Maxlength = 6] |
+------------------------------------------------------------------------------+

 

[]{#related-topics}

