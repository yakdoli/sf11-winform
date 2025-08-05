---
title: howtomodifythebuiltinstyles.md
original_path: WinForms_Docs/02_Concepts/howtomodifythebuiltinstyles.md
created_at: 2025-08-05
---








  









## How to modify the Built-in styles? {#how-to-modify-the-built-in-styles style="tab-stops: 0pt"}

 

You can use the **CreateBuiltinStyle** method of the Style class, to override the built-in styles.

 

The following code illustrates how to modify the Heading1 style.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                   |
| [Style][ style = [Style].CreateBuiltinStyle([BuiltinStyle].Heading1, doc) [as] [Style];] |
|                                                                                                                                                                                                                                                                   |
| [style.CharacterFormat.Italic = [true];]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                   |
| [style.CharacterFormat.UnderlineStyle = [UnderlineStyle].DotDash;]                                                                                                                                       |
|                                                                                                                                                                                                                                                                   |
| [doc.Styles.Add(style);]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                   |
| [para.ApplyStyle(style.Name);]                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                  |
| [Dim][ style [As] Style = [TryCast](Style.CreateBuiltinStyle(BuiltinStyle.Heading1, doc), Style)] |
|                                                                                                                                                                                                                                  |
| [style.CharacterFormat.Italic = [True]]                                                                                                                                 |
|                                                                                                                                                                                                                                  |
| [style.CharacterFormat.UnderlineStyle = UnderlineStyle.DotDash]                                                                                                                              |
|                                                                                                                                                                                                                                  |
| [doc.Styles.Add(style)]                                                                                                                                                                      |
|                                                                                                                                                                                                                                  |
| [para.ApplyStyle(style.Name)]                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

