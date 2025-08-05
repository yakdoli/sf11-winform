---
title: misspelledwordstyles.md
original_path: WinForms_Docs/02_Concepts/misspelledwordstyles.md
created_at: 2025-08-05
---






##### Misspelled word Styles {#misspelled-word-styles style="MARGIN-LEFT: 1.8pt; tab-stops: 1.8pt"}

[] 

The control comes with a built-in rich dialog form with support for customizing the style of misspelled words through style properties. Just set the properties, which reflects the style settings for the misspelled words in the SpellCheck dialog box.

[] 


+-----------------------------------+----------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                          |
|                                   |                                                                                                          |
| Property                          | Description                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+
| MisspelledWordCss                 | Specifies a collection of style properties, that allows to customize the styles of the misspelled words. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------+


[] 

{border="0"}

[] 

Figure 92: CSS styles applied for the misspelled word

[] 

Programmatic settings of few misspelled style properties are given below.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                   |
|                                                                                                                                                    |
| **[]**                                                                                         |
|                                                                                                                                                    |
| [SpellCheck.MisspelledWordCss.BackColor = System.Drawing.[Color].Orange;] |
|                                                                                                                                                    |
| [SpellCheck.MisspelledWordCss.ForeColor = System.Drawing.[Color].Brown;]  |
|                                                                                                                                                    |
| [SpellCheck.MisspelledWordCss.Font = System.Drawing.[FontStyle].Bold;]    |
+----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                      |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                            |
|                                                                                                                                                                                                       |
| [Private][ SpellCheck.MisspelledWordCss.BackColor = System.Drawing.Color.Orange] |
|                                                                                                                                                                                                       |
| [Private][ SpellCheck.MisspelledWordCss.ForeColor = System.Drawing.Color.Brown]  |
|                                                                                                                                                                                                       |
| [Private][ SpellCheck.MisspelledWordCss.Font = System.Drawing.FontStyle.Bold]    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p152} 

[]{#related-topics}

