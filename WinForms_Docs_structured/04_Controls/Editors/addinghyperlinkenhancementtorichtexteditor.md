---
title: addinghyperlinkenhancementtorichtexteditor.md
original_path: WinForms_Docs/04_Controls/Editors/addinghyperlinkenhancementtorichtexteditor.md
created_at: 2025-08-05
---






##### Adding Hyperlink Enhancement to Rich Text Editor {#adding-hyperlink-enhancement-to-rich-text-editor style="tab-stops: 0pt"}

 

To enable Hyperlink enhancement in your RTE, follow the steps given below:

1.   Create a model in the application.

2.   Create a strongly typed view.

3.   Add the below code snippet in the View page:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [\[ASPX\]][]                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| [\<%][=][Html.Syncfusion().RichTextEditor([\"RTE\"])[%\>]] |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[Razor\]][]                                                                                        |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| [\@{][Html.Syncfusion().RichTextEditor([\"RTE\"])                          ] |
|                                                                                                                                                                                                  |
| [    .Render();]                                                                                                                                             |
|                                                                                                                                                                                                  |
| [       ]                                                                                                                                                    |
|                                                                                                                                                                                                  |
| [   [}]]                                                                                                                         |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
|                                                                                                                                                                                                  |
| []                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

4.   Build and run the application, and you will get the required output.

 

[]{#related-topics}

