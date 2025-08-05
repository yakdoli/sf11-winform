---
title: theme.md
original_path: WinForms_Docs/02_Concepts/theme.md
created_at: 2025-08-05
---








  









### Theme {#theme style="tab-stops: 0pt"}

[] 

All the controls require the jQuery UI V7.1 style sheet to be linked to the page, in order to view the controls at run time with appropriate styles. You can download the Styles directly from the [[jQuery UI]{.UGHyperlink}](http://jqueryui.com/download/) website, or use the themes available with the Syncfusion samples.

[] 

The documentation for \"[[Theming jQuery UI]{.UGHyperlink}](http://jqueryui.com/docs/Theming)\" is available in the jQuery UI website. You can download the themes with or without scoping. If you download the themes with scoping, then you must specify the name in the **CssClass** property. Scoping enables to use more than one theme in a single page.

[] 

The jQueryUIDatePicker styles cannot be applied with scoping while it is in the PopUp / Inline False mode.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [\<][syncfusion][:][jQueryUISlider][ [ID][=\"JQueryUISlider1\"] [runat][=\"server\"] [CssClass][=\"uilightness\"\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+-------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                            |
|                                                                                                             |
| []                                                         |
|                                                                                                             |
| [jQueryUISlider1.CssClass = [\"uilightness\"];] |
+-------------------------------------------------------------------------------------------------------------+

**[]** 

+------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                           |
|                                                                                                            |
| []                                                        |
|                                                                                                            |
| [jQueryUISlider1.CssClass = [\"uilightness\"]] |
+------------------------------------------------------------------------------------------------------------+

 

[]{#p621} 

[]{#related-topics}

