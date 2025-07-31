---
title: disablingtheformattingoptions.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\disablingtheformattingoptions.md
created_at: 2025-07-03
---






#### Disabling the formatting options {#disabling-the-formatting-options style="tab-stops: 0pt"}

 

Rich text editor has two major editing options viz., toolbar with rich set of commands and font options comprising the font-style and font-size variations.Rich text editor supports to enable and disable these options

 

Properties

 


+----------------+----------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------+
| Name           | Description                                                          | Type of property                                                                               | Value it accepts                                                                                       | Dependency  |
+----------------+----------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------+
| ShowToolBar    | When set to false, the editor will be rendered without a toolbar     | [[bool]]{.UGHyperlink} | [[true / false]]{.UGHyperlink} | NA          |
|                |                                                                      |                                                                                                |                                                                                                        |             |
|                |                                                                      |                                                                                                |                                                                                                        |             |
+----------------+----------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------+
| ShowFontOption | When set to false, the editor will be rendered with the font options | [[bool]]{.UGHyperlink} | [[true / false]]{.UGHyperlink} | NA          |
|                |                                                                      |                                                                                                |                                                                                                        |             |
|                |                                                                      |                                                                                                |                                                                                                        |             |
+----------------+----------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-------------+


 

Using Builder

The following steps explain you how to render rich text editor without toolbar and font-option through builder.

 

1.   In **View**, call the rich text editor helper with control id as first argument, followed by the **ShowToolbar** and **ShowFontOption** methods with argument set to 'false'.

 

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"])] |
|                                                                                                                                                                                                                                                                                |
| [.**ShowFontOption([false])**]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                |
| [.**ShowToolBar([false])**[%\>]]                                                                                                                                             |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                |
| [\@{][ Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"])] |
|                                                                                                                                                                                                                |
| [.**ShowFontOption([false])**]                                                                                                           |
|                                                                                                                                                                                                                |
| [       .**ShowToolBar([false])**]                                                                                                       |
|                                                                                                                                                                                                                |
| [.Render();[}]]                                                                                                                   |
|                                                                                                                                                                                                                |
| []                                                                                                                                        |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   Build and run the application

 

 

Using Properties Model

 

The following steps explain you how to render rich text editor without toolbar and font-option through properties model.

1.   In the **Controller**, create an instance of **RichTextEditorModel**, set the **ShowToolbar** and **ShowFontOption** properties to 'false' and pass the instance through view-specific data to the view as below.

**[]** 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                 |
|                                                                                                                                                                                                    |
| [public][ [ActionResult] Index()]                           |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                       |
|                                                                                                                                                                                                    |
| [            [RichTextEditorModel] myModel = [new] [RichTextEditorModel]();] |
|                                                                                                                                                                                                    |
| [            myModel.ShowToolBar = [false];]                                                                                 |
|                                                                                                                                                                                                    |
| [            myModel.ShowFontOption = [false];]                                                                              |
|                                                                                                                                                                                                    |
| []                                                                                                                                                |
|                                                                                                                                                                                                    |
| [            [//pass the model through view data to the view]]                                                              |
|                                                                                                                                                                                                    |
| [            ViewData\[[\"myRichTextEditor\"]\] = myModel;]                                                               |
|                                                                                                                                                                                                    |
| [            [return] View();]                                                                                               |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                       |
|                                                                                                                                                                                                    |
| []                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In **View**, call the rich text editor helper passing the view data key as control id.

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"])[%\>]] |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                         |
| [\@{][ Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"]).Render();[}]] |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

The rich text editor will be rendered without a toolbar and font-options.

 

[]{#related-topics}

