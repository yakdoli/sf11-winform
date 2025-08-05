---
title: howtouseacommaasadecimalseparatorinformula1.md
original_path: WinForms_Docs/99_Uncategorized/howtouseacommaasadecimalseparatorinformula1.md
created_at: 2025-08-05
---








  









### How to Use a Comma as a Decimal Separator in Formula? {#how-to-use-a-comma-as-a-decimal-separator-in-formula style="tab-stops: 0pt"}

 

Local settings may require the use of a different decimal separator than the period character that Essential Calculate uses by default. For example, many Local settings use a comma as the decimal separator.

 

To manage this problem, Essential Calculate exposes two static (Shared in VB.NET) members, which, you can set to specify the character that is recognized as the decimal separator and the character that is recognized as the list separator. The default values of these members are a period and a comma, respectively. You can set these static members at any point in your code before you use any Essential Calculate objects.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [public string][ Form_Load(][object][ sender, ][EventArgs][ e)] |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [{ ]                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [    // Comma]                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [    CalcEngine.ParseDecimalSeparator = \',\'; ]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [    // Semicolon\                                                                                                                                                                                                                                                                                                                                                       |
| ][    CalcEngine.ParseArgumentSeparator = \';\'; ]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [    //\.... More code]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [}]                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [Public Sub][ Form_Load(sender as ][object][, e As ][EventArgs][)] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [     // Comma]                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [     CalcEngine.ParseDecimalSeparator = \",\" ]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [     // Semicolon\                                                                                                                                                                                                                                                                                                                                                         |
| ][     CalcEngine.ParseArgumentSeparator = \";\" ]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [     \'\..... More code ]                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [End Function ]                                                                                                                                                                                                                                                                                                            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

