---
title: newlinestyles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\newlinestyles.md
created_at: 2025-07-03
---








  









### New Line Styles {#new-line-styles style="tab-stops: 0pt"}

 

Edit Control allows you to specify a new line style, or get the currently used new line style in the text.

 

**SetNewLineStyle** method sets the current new line style in the Edit Control. SetNewLineStyle method accepts values from the **NewLineStyle** enumerator which has values like Windows, Mac, Unix and Control, which correspond to new line styles \"\\r\\n\", \"\\r\", \"\\n\\r\" and \"\\n\\r\" respectively.

 

Similarly, the **GetNewLineStyle** method returns a NewLineStyle enumerator value which indicates the currently used new line stye in the Edit Control.

 


{border="0"}Note: The default new line style value is set to \'Control\'. This value can be changed according to the needs of the user using the DefaultNewLineStyle property.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [// Change the current new line style in the Edit Control.]                                                                               |
|                                                                                                                                                                                             |
| [this][.editControl1.SetNewLineStyle(Syncfusion.IO.[NewLineStyle].Control);]      |
|                                                                                                                                                                                             |
| [this][.editControl1.GetNewLineStyle();]                                                               |
|                                                                                                                                                                                             |
| []                                                                                                                                                      |
|                                                                                                                                                                                             |
| [//][ [Specify the default new line style.]]                                    |
|                                                                                                                                                                                             |
| [this][.editControl1.DefaultNewLineStyle = Syncfusion.IO.[NewLineStyle].Windows;] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                |
|                                                                                                                                                                   |
| []                                                                                                              |
|                                                                                                                                                                   |
| [\' Change the current new line style in the Edit Control.]                                                     |
|                                                                                                                                                                   |
| [Me][.editControl1.SetNewLineStyle(Syncfusion.IO.NewLineStyle.Control)]      |
|                                                                                                                                                                   |
| [Me][.editControl1.GetNewLineStyle()]                                        |
|                                                                                                                                                                   |
| []                                                                                                                            |
|                                                                                                                                                                   |
| [\' Specify the default new line style.]                                                                        |
|                                                                                                                                                                   |
| [Me][.editControl1.DefaultNewLineStyle = Syncfusion.IO.NewLineStyle.Windows] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p22} 

[]{#related-topics}

