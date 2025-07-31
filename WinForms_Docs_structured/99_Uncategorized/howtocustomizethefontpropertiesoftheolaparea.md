---
title: howtocustomizethefontpropertiesoftheolaparea.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtocustomizethefontpropertiesoftheolaparea.md
created_at: 2025-07-03
---






##### How to customize the font properties of the OlapArea? {#how-to-customize-the-font-properties-of-the-olaparea style="tab-stops: 0pt"}

[] 

Typically, the primary axis and the secondary axis font settings will override the font properties applied to their content in the OlapArea. To set the font properties such as Foreground, FontFamily, FontSize, and FontWeight consider using the font properties available in the primary and the secondary axis.

 

###### 1.6.1.1.5.1 FontStyle {#fontstyle style="tab-stops: 0pt"}

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **\[C#\]**                                                                                                              |
|                                                                                                                         |
|                                                                                                                         |
|                                                                                                                         |
| [       this].olapchart1.Series\[0\].Area.FontStyle = [FontStyles].Italic; |
|                                                                                                                         |
|                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------+
| **\[VB\]**                                                                              |
|                                                                                         |
|                                                                                         |
|                                                                                         |
| [      Me].olapchart1.Series(0).Area.FontStyle = FontStyles.Italic |
|                                                                                         |
|                                                                                         |
+-----------------------------------------------------------------------------------------+

[] 

See also:

How to customize PrimaryAxis font properties?

How to customize SecondaryAxis font properties?

[] 

[]{#related-topics}

