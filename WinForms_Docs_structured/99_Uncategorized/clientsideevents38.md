---
title: clientsideevents38.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\clientsideevents38.md
created_at: 2025-07-03
---






#### Client Side Events {#client-side-events style="tab-stops: 0pt"}

 

Rich text editor supports client side event handling.

Events

 

  ------------------- ------------------------------------------------------------------------------------------------ ----------- ----------------
  Name                Description                                                                                      Arguments   Reference Link
  ClientSideOnLoded   This event is raised immediately when the rich text editor gets loaded                           inst,args   \-
  ClientSideKeyUp     This event is raised when the user releases a key on the keyboard within the content area        inst,args   \-
  ClientSideKeyDown   This event is raised when the user first presses a key on the keyboard within the content area   inst,args   \-
  ------------------- ------------------------------------------------------------------------------------------------ ----------- ----------------

 

Using Builder

 

The following steps explain you how to handle the client side events raised by the rich text editor through builder.

1.   In **View**, call the rich text editor helper, followed by the **ClientSideOnLoaded, ClientSideKeyUp** and **ClientSideKeyDown** methods with the desired handlers as:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                |
| [\<%][=][Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"])] |
|                                                                                                                                                                                                                                                                                |
| [               .**ClientSideOnLoaded([\"OnLoaded\"])**]                                                                                                                                              |
|                                                                                                                                                                                                                                                                                |
| **[               .ClientSideKeyUp([\"OnKeyUp\"])]**                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                |
| **[               .ClientSideKeyDown([\"OnKeyDown\"])]**[%\>][]                 |
|                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                           |
| [\@{][ Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"])]                                                                                                            |
|                                                                                                                                                                                                                                                                                                                           |
| [               .**ClientSideOnLoaded([\"OnLoaded\"])**]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                           |
| **[               .ClientSideKeyUp([\"OnKeyUp\"])]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                           |
| **[               .ClientSideKeyDown([\"OnKeyDown\"])]**[.Render();][}][] |
|                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

2.   In the Javascirpt, define the handlers as below.

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Javascript\]**                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [\<][script][ [type][=\"text/javascript\"\>]] |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnLoaded(inst, args) {            ]                                                                                                                                         |
|                                                                                                                                                                                                                                                                       |
| [            [//inst                  - instance of rich text editor client side object]]                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            [//args: HtmlText        - current content of the editor as raw HTML]]                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [            [//      innerText       - current content of the editor as text]]                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [            [//      selectedFormats - array of the selected formats           ]]                                                                                                         |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnKeyUp(inst, args) {]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                       |
| [            [//inst                  - instance of rich text editor client side object]]                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            [//args: HtmlText        - current content of the editor as raw HTML]]                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [            [//      innerText       - current content of the editor as text]]                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [            [//      selectedFormats - array of the selected formats ]]                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [        [function] OnKeyDown(inst, args) {]                                                                                                                                                    |
|                                                                                                                                                                                                                                                                       |
| [            [//inst                  - instance of rich text editor client side object]]                                                                                                  |
|                                                                                                                                                                                                                                                                       |
| [            [//args: HtmlText        - current content of the editor as raw HTML]]                                                                                                        |
|                                                                                                                                                                                                                                                                       |
| [            [//      innerText       - current content of the editor as text]]                                                                                                            |
|                                                                                                                                                                                                                                                                       |
| [            [//      selectedFormats - array of the selected formats ]]                                                                                                                   |
|                                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| [       [\</][script][\>]]                                                                                                                          |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   Build and run the application.

**[]** 

Using Properties Model

The following steps explain you how to handle the client side events raised by the rich text editor through properties model.

1.   In the Controller, create an instance of RichTextEditorModel, define the **ClientSideOnLoaded, ClientSideKeyUp** and **ClientSideKeyDown** properties and pass the instance through view-specific data to the view as below.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\[Controller\]**                                                                                                                                                                                 |
|                                                                                                                                                                                                    |
| [public][ [ActionResult] Index()]                           |
|                                                                                                                                                                                                    |
| [        {]                                                                                                                                       |
|                                                                                                                                                                                                    |
| [            [RichTextEditorModel] myModel = [new] [RichTextEditorModel]();] |
|                                                                                                                                                                                                    |
| [            **myModel.ClientSideOnLoaded = [\"OnLoaded\"];**]                                                            |
|                                                                                                                                                                                                    |
| **[            myModel.ClientSideKeyUp = [\"OnKeyUp\"];]**                                                                |
|                                                                                                                                                                                                    |
| **[            myModel.ClientSideKeyDown = [\"OnKeyDown\"];]**[]         |
|                                                                                                                                                                                                    |
| []                                                                                                                                                |
|                                                                                                                                                                                                    |
| [            [//pass the model through view data to the view]]                                                              |
|                                                                                                                                                                                                    |
| [            ViewData\[[\"myRichTextEditor\"]\] = myModel; [return] View();]                         |
|                                                                                                                                                                                                    |
| [        }]                                                                                                                                       |
|                                                                                                                                                                                                    |
| []                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In **View**, call the rich text editor helper passing the view data key as control id.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[ASPX\]**                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                 |
| [\<%][=][Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"])[%\>]] |
|                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **View\[cshtml\]**                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                         |
| [\@{][ Html.Syncfusion().RichTextEditor([\"myRichtextEditor\"]).Render();[}]] |
|                                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

3.   Build and run the application.

You can observer the hanlders getting invoked when the corresponding events are triggered.

 

[]{#related-topics}

