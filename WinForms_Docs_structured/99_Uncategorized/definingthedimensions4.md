---
title: definingthedimensions4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\definingthedimensions4.md
created_at: 2025-07-03
---






#### Defining the dimensions {#defining-the-dimensions style="tab-stops: 0pt"}

 

Rich text editor support customizing the dimensions to make it fit under any scenario.

**[]** 

Properties

 


  -------- --------------------------------------------------- ------------------ -------------------------------- ------------
  Name     Description                                         Type of property   Value it accepts                 Dependency
  Height   Sets the height of the rich text editor in pixels   Unit               numeric                          NA
  Width    Sets the width of the rich text editor in pixels    Unit               numeric[]   NA
  -------- --------------------------------------------------- ------------------ -------------------------------- ------------


*[[]]{.underline}* 

Using Builder

 

The following steps explain how to set the dimensions through properties model.

1.   In **View**, call the rich text editor helper, enabling the **Height** and **Width** methods passing the desired dimensions as arguments.

**[]** 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                               |
| [\<%][=][Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"])\ |
|        .**Height(100)**]                                                                                                                                                     |
|                                                                                                                                                                                                                               |
| [              .**Width(370)**[%\>]]                                                                                                             |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                  |
| [\@{][ ][Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"])\ |
|        .**Height(100)**]                                                                                                                                        |
|                                                                                                                                                                                                                  |
| [              .**Width(370)**][]                                                                              |
|                                                                                                                                                                                                                  |
| [      .Render();[}]]                                                                                                               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                          |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

2.   Buid and run the application

**[]** 

Using Properties Model

 

1.   In the Controller, create an instance of RichTextEditorModel, define the **Height** and **Width** properties and pass the instance through view-specific data to the view as below.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| [public][ [ActionResult] Index()]                                                        |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [RichTextEditorModel][ myModel = [new] [RichTextEditorModel]();] |
|                                                                                                                                                                                                                                 |
| **[myModel.Height = 100;]**                                                                                                                                                    |
|                                                                                                                                                                                                                                 |
| **[myModel.Width = 370;]**                                                                                                                                                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                                                 |
| [//pass the model through view data to the view][]                                                              |
|                                                                                                                                                                                                                                 |
| [ViewData\[[\"myRichtextEditor\"]\] = myModel;]                                                                                                        |
|                                                                                                                                                                                                                                 |
| [return][ View();]                                                                                               |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

[] 

3.   Build and run the application.

The output is shown in the following screenshot.

 

{border="0"}

Figure 204:  Rich text editor with customized dimensions

[]{#related-topics}

