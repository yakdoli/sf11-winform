---
title: stylesheetscss.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\stylesheetscss.md
created_at: 2025-07-03
---








  









## []Style Sheets CSS {#style-sheets-css style="tab-stops: 0pt"}

[[[]]]{.underline} 

The support for style sheets is enabled in HTMLUI. This lets the user to define styles for HTML elements and decide the appearance of the HTML elements in the application. HTMLUI supports three types of style sheets.

[] 

[·      ]External Style sheets

[·      ]Internal Style sheets

[·      ]Inline Style sheets

[] 

External style sheets are linked to the file through the **Link** tag. While the internal style sheets are applied with the help of the **Style** tag inside the head section, inline style sheets are applied as the values of the style attributes of the specific HTML element.

The following HTML code illustrates the above concepts.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][html][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][head][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][link][ ][type][=\"text/css\" rel=\"stylesheet\" ][href][=\"ExternalCSS.CSS\"\>\<][/link][\>]      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][style][\>.div{\"background-color: #dae5f5;\"}\<][/style][\>]                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][/head][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][body][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][p][ ][style][=\"background-color: #ffffff;\"\> ][This is an inline styled element][ \<][/p][\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][div][ ][class][=\"div\"\> ][The Internal style sheet is applied for this element[ \<][/div][\>]]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][/body][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][/html][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

HTMLUI also supports updation of styles to the HTML document at run time. This can be done in two modes, either by changing the value of the style attribute for internal style or the class attribute for the inline style sheet.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [if][([this].textBox.Attributes.Contains([\"style\"]) = = [false]) ] |
|                                                                                                                                                                                                                                                             |
| [this][.textBox.Attributes.Add([\"style\"]); ]                                                                 |
|                                                                                                                                                                                                                                                             |
| [this][.textBox.Attributes\[[\"style\"]\].Value = [\"background-color:red;\"]; ]       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                   |
| [If][ [Me].textBox.Attributes.Contains([\"style\"]) = [False] [Then]] |
|                                                                                                                                                                                                                                                                                   |
| [Me][.textBox.Attributes.Add([\"style\"])]                                                                                           |
|                                                                                                                                                                                                                                                                                   |
| [End][ [If]]                                                                                                                            |
|                                                                                                                                                                                                                                                                                   |
| [Private][ [Me].textBox.Attributes([\"style\"]).Value = [\"background-color:red;\"] ]   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

More:









