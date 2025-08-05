---
title: usingbuilder79.md
original_path: WinForms_Docs/99_Uncategorized/usingbuilder79.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



##### Using Builder {#using-builder style="tab-stops: 0pt"}

The following steps explain the handling of client side events of the dialog using Builder:

1.   In the **View**, create the contents of the dialog and invoke the dialog helper with the Control ID as the first argument followed by the event handler methods with the desired hanlders as argument.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                    |
|                                                                                                                                       |
| **[]**                                                                                            |
|                                                                                                                                       |
| [            [\<%]{]                                                  |
|                                                                                                                                       |
| [                  Html.MobSyncfusion().Dialog([\"MobDialog\"])]          |
|                                                                                                                                       |
| [                    .AutoFormat([MobSkins].DarkNight)]                   |
|                                                                                                                                       |
| [                    .Title([\"Syncfusion Essential Studio\"])]           |
|                                                                                                                                       |
| [                    .DialogIconUrl([\"\~/Content/Images/favicon.ico\"])] |
|                                                                                                                                       |
| [                    .ClientSideEvents(events =\> events]                                         |
|                                                                                                                                       |
| [                        .ClientSideOnBeforeClose([\"onBeforeClose\"])]   |
|                                                                                                                                       |
| [                        .ClientSideOnClose([\"onClose\"])]               |
|                                                                                                                                       |
| [                        .ClientSideOnCreate([\"onCreate\"])]             |
|                                                                                                                                       |
| [                        .ClientSideOnDrag([\"onDrag\"])]                 |
|                                                                                                                                       |
| [                        .ClientSideOnDragStart([\"onDragStart\"])]       |
|                                                                                                                                       |
| [                        .ClientSideOnDragStop([\"onDragStop\"])]         |
|                                                                                                                                       |
| [                        .ClientSideOnOpen([\"onOpen\"])]                 |
|                                                                                                                                       |
| [                        )]                                                                       |
|                                                                                                                                       |
| [                    .Template(() =\>]                                                            |
|                                                                                                                                       |
| [                      {[%\>]]                                        |
|                                                                                                                                       |
| [            [\<][div][\>]]      |
|                                                                                                                                       |
| [                This is the Syncfusion Mobile Dialog control]                                    |
|                                                                                                                                       |
| [            [\</][div][\>]]     |
|                                                                                                                                       |
| [            [\<%]})]                                                 |
|                                                                                                                                       |
| [            .Render();]                                                                          |
|                                                                                                                                       |
| [              }[%\>]]                                                |
|                                                                                                                                       |
| **[]**                                                                        |
|                                                                                                                                       |
| []                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                   |
|                                                                                                                                       |
| **[]**                                                                                            |
|                                                                                                                                       |
| [            [\<%]{]                                                  |
|                                                                                                                                       |
| [                  Html.MobSyncfusion().Dialog([\"MobDialog\"])]          |
|                                                                                                                                       |
| [                    .AutoFormat([MobSkins].DarkNight)]                   |
|                                                                                                                                       |
| [                    .Title([\"Syncfusion Essential Studio\"])]           |
|                                                                                                                                       |
| [                    .DialogIconUrl([\"\~/Content/Images/favicon.ico\"])] |
|                                                                                                                                       |
| [                    .ClientSideEvents(events =\> events]                                         |
|                                                                                                                                       |
| [                        .ClientSideOnBeforeClose([\"onBeforeClose\"])]   |
|                                                                                                                                       |
| [                        .ClientSideOnClose([\"onClose\"])]               |
|                                                                                                                                       |
| [                        .ClientSideOnCreate([\"onCreate\"])]             |
|                                                                                                                                       |
| [                        .ClientSideOnDrag([\"onDrag\"])]                 |
|                                                                                                                                       |
| [                        .ClientSideOnDragStart([\"onDragStart\"])]       |
|                                                                                                                                       |
| [                        .ClientSideOnDragStop([\"onDragStop\"])]         |
|                                                                                                                                       |
| [                        .ClientSideOnOpen([\"onOpen\"])]                 |
|                                                                                                                                       |
| [                        )]                                                                       |
|                                                                                                                                       |
| [                    .Template(() =\>]                                                            |
|                                                                                                                                       |
| [                      {[%\>]]                                        |
|                                                                                                                                       |
| [            [\<][div][\>]]      |
|                                                                                                                                       |
| [                This is the Syncfusion Mobile Dialog control]                                    |
|                                                                                                                                       |
| [            [\</][div][\>]]     |
|                                                                                                                                       |
| [            [\<%]})]                                                 |
|                                                                                                                                       |
| [            .Render();]                                                                          |
|                                                                                                                                       |
| [              }[%\>]]                                                |
|                                                                                                                                       |
| []                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------+

 

2.   In the **Javascript**, define the handlers as given below:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**                                                                                                                                                                           |
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
| [        [function] onDrag(event, ui) {]                                                                                                                                  |
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
| [      [\</][script][\>]]                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

3.   Build and run the application in emulator.

**[]**  

[]{#related-topics}

