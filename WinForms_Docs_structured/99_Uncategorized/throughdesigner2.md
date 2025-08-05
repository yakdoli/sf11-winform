---
title: throughdesigner2.md
original_path: WinForms_Docs/99_Uncategorized/throughdesigner2.md
created_at: 2025-08-05
---






##### [Through Designer] {#through-designer style="tab-stops: 0pt"}

[] 

To create RichTextEditor control, follow the below given steps.

[] 

1.   Create a new ASP.NET Web application. For details, see [Creating ASP.NET Web Application]{.UGHyperlink}.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][cc1][:][RichTextEditor][ [ID][=\"RichTextEditor1\"] [runat][=\"server\"] [Height][=\"420\"] [Width][=\"620\"] [/\>]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Refer to the [Concepts and Features]{.UGHyperlink} section, to customize the various settings of the controls.

[] 

{border="0"}

***[]*** 

Figure 76: RichTextEditor Control

[] 

3.   Build and run the application. Enter text inside the editor and use the built-in toolbars to format the text. Listen to Update button click by subscribing to the **UpdateClick** event, retrieve editor content via **Html** or **Text** methods and save the contents in your data store.

[] 

Smart Tag

[] 

Smart tag is used to add or remove toolbars in RichTextEditor through Designer.

[] 

{border="0"}

***[]*** 

Figure 77: RichTextEditor Smart Tag Options

[] 

See Also

[] 

[Concepts and Features]{.UGHyperlink}[]{.UGHyperlink}

 

[]{#related-topics}

