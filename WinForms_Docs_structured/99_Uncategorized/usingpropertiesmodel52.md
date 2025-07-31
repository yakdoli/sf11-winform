---
title: usingpropertiesmodel52.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\usingpropertiesmodel52.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Properties Model {#using-properties-model style="tab-stops: 0pt"}

The following steps explain the handling of the client side events of the dialog through the Properties model:

1.   In the **Controller**, create an instance of **MobDialogModel**, define the the event handler properties and pass the instance through **View Specific Data** to **View** as given below:**

**[]**  

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[]**                                                                                                          |
|                                                                                                                                                                         |
| **[\[Controller\]]**                                                                                                                |
|                                                                                                                                                                         |
| **[]**                                                                                                                              |
|                                                                                                                                                                         |
| [        [public][ActionResult] Dialog()]                                              |
|                                                                                                                                                                         |
| [        {]                                                                                                                         |
|                                                                                                                                                                         |
| [            [//create an instance of MobDialogModel]]                                                        |
|                                                                                                                                                                         |
| [            [MobDialogModel] model = [new][MobDialogModel]()] |
|                                                                                                                                                                         |
| [            {]                                                                                                                     |
|                                                                                                                                                                         |
| [                AutoFormat = [MobSkins].DarkNight,]                                                        |
|                                                                                                                                                                         |
| [                ClientSideEvents = [new][DialogEvents]()]                             |
|                                                                                                                                                                         |
| [                {]                                                                                                                 |
|                                                                                                                                                                         |
| [                    ClientSideOnBeforeClose = [\"onBeforeClose\"],]                                        |
|                                                                                                                                                                         |
| [                    ClientSideOnClose = [\"onClose\"],]                                                    |
|                                                                                                                                                                         |
| [                    ClientSideOnCreate = [\"onCreate\"],]                                                  |
|                                                                                                                                                                         |
| [                    ClientSideOnDrag = [\"onDrag\"],]                                                      |
|                                                                                                                                                                         |
| [                    ClientSideOnDragStart = [\"onDragStart\"],]                                            |
|                                                                                                                                                                         |
| [                    ClientSideOnDragStop = [\"onDragStop\"],]                                              |
|                                                                                                                                                                         |
| [                    ClientSideOnOpen = [\"onOpen\"]]                                                       |
|                                                                                                                                                                         |
| [                },]                                                                                                                |
|                                                                                                                                                                         |
| [                Title = [\"Syncfusion Essential Studio\"],]                                                |
|                                                                                                                                                                         |
| [                DialogIconUrl = [\"\~/Content/Images/favicon.ico\"]]                                       |
|                                                                                                                                                                         |
| [            };]                                                                                                                    |
|                                                                                                                                                                         |
| [            ViewData\[[\"MobDialog\"]\] = model;]                                                          |
|                                                                                                                                                                         |
| [            [return] View();]                                                                                 |
|                                                                                                                                                                         |
| [        }]                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

 

2.   In **View**, create the dialog contents and invoke the dialog helper with the view data key as the first argument.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                   |
|                                                                                                                                                                      |
| **[]**                                                                                                                           |
|                                                                                                                                                                      |
| [\<%] [{]                                                                |
|                                                                                                                                                                      |
| [          Html.MobSyncfusion().Dialog([\"MobDialog\"])]                                                 |
|                                                                                                                                                                      |
| [              .Template(() =\>]                                                                                                 |
|                                                                                                                                                                      |
| [              {[%\>][\<][div][\>]] |
|                                                                                                                                                                      |
| [                  This is the Syncfusion Mobile Dialog control]                                                                 |
|                                                                                                                                                                      |
| [              [\</][div][\>]]                                  |
|                                                                                                                                                                      |
| [    [\<%]})]                                                                                        |
|                                                                                                                                                                      |
| [            .Render();]                                                                                                         |
|                                                                                                                                                                      |
| [      }[%\>]]                                                                                       |
|                                                                                                                                                                      |
| [ [] ]                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| []                                                                                                                                    |
|                                                                                                                                                                           |
| **[\[Razor\]]**                                                                                                                       |
|                                                                                                                                                                           |
| **[]**                                                                                                                                |
|                                                                                                                                                                           |
| [    [\@{]]                                                                                               |
|                                                                                                                                                                           |
| [        Html.MobSyncfusion().Dialog([\"MobDialog\"])]                                                        |
|                                                                                                                                                                           |
| [            .Template([@][\<][div][\>]] |
|                                                                                                                                                                           |
| [                This is the Syncfusion Mobile Dialog control]                                                                        |
|                                                                                                                                                                           |
| [            [\</][div][\>]]                                         |
|                                                                                                                                                                           |
| [).Render();]                                                                                                                         |
|                                                                                                                                                                           |
| [    [}]]                                                                                                 |
|                                                                                                                                                                           |
| []                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   In Javascript, define the handlers as given below:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascirpt\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                    |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [\<] [script] [ [type] [=\"text/javascript\"\>] ] |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [        [function] onOpen(event) {]                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] onClose(event) {]                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] onDragStart(event,ui) {]                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [            [//ui:]]                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// position         - current position of the dialog]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [            [// size             - current size of the dialog]]                                                                                                     |
|                                                                                                                                                                                                                                    |
| [            [// originalPosition - original position of the dialog]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// originalSize     - original size of the dialog]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] onDrag(event, ui) {]                                                                                                                                  |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [            [//ui:]]                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// position         - current position of the dialog]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [            [// size             - current size of the dialog]]                                                                                                     |
|                                                                                                                                                                                                                                    |
| [            [// originalPosition - original position of the dialog]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// originalSize     - original size of the dialog]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] onDragStop(event, ui) {]                                                                                                                              |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [            [//ui:]]                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// position         - current position of the dialog]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [            [// size             - current size of the dialog]]                                                                                                     |
|                                                                                                                                                                                                                                    |
| [            [// originalPosition - original position of the dialog]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// originalSize     - original size of the dialog]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] onCreate(event) {]                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.]]                                                                                           |
|                                                                                                                                                                                                                                    |
| [            [//ui:]]                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// position         - current position of the dialog]]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [            [// size             - current size of the dialog]]                                                                                                     |
|                                                                                                                                                                                                                                    |
| [            [// originalPosition - original position of the dialog]]                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [// originalSize     - original size of the dialog]]                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [        [function] onBeforClose(event) {]                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [            [//event             - object send by jQuery event trigger.        ]]                                                                                   |
|                                                                                                                                                                                                                                    |
| [        }       ]                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [      [\</][script][\>][]]                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

4.   Build and run the application in emulator.

You can observe the handlers getting invoked when the corresponding event is triggered.

[]{#related-topics}

