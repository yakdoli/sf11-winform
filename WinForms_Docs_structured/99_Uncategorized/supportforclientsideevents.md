---
title: supportforclientsideevents.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\supportforclientsideevents.md
created_at: 2025-07-03
---






##### Support for client-side events {#support-for-client-side-events style="tab-stops: 0pt"}

Refer to the [Client-side events table] to understand the basics of the events used in this Control.

You can handle client-side events using the following two ways-

 

Using Builder

The following steps guide in handling client side events through Builder:

1.   In **View**, [invoke the UploadBox helper with the **UploadBox id** as the first argument followed by the **Client side events**.]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                        |
|                                                                                                                                                                                 |
| [  [\<%][=] Html.Syncfusion().UploadBox(\"upload\")][] |
|                                                                                                                                                                                 |
| [                             .AsyncUpload]                                                                                                 |
|                                                                                                                                                                                 |
| [                             (]                                                                                                            |
|                                                                                                                                                                                 |
| [                                 s =\> s.AutoUpload(true)]                                                                                 |
|                                                                                                                                                                                 |
| [                                     .SaveAction(\"Save\", \"UploadBox\")]                                                                 |
|                                                                                                                                                                                 |
| [                                     .RemoveAction(\"Remove\",\"UploadBox\")]                                                              |
|                                                                                                                                                                                 |
| [                             )]                                                                                                            |
|                                                                                                                                                                                 |
| [                    .ClientSideOnLoad(\"onLoad\") ]                                                                                        |
|                                                                                                                                                                                 |
| [                    .ClientSideOnCancel(\"onCancel\")]                                                                                     |
|                                                                                                                                                                                 |
| [                    .ClientSideOnComplete(\"onComplete\")]                                                                                 |
|                                                                                                                                                                                 |
| [                    .ClientSideOnError(\"onError\")]                                                                                       |
|                                                                                                                                                                                 |
| [                    .ClientSideOnRemove(\"onRemove\") ]                                                                                    |
|                                                                                                                                                                                 |
| [                    .ClientSideOnSelect(\"onSelect\") ]                                                                                    |
|                                                                                                                                                                                 |
| [                    ]                                                                                                                      |
|                                                                                                                                                                                 |
| [                    .ClientSideOnUpload(\"onUpload\")]                                                                                     |
|                                                                                                                                                                                 |
| [                                                    .AutoFormat(Skins.Sandune).ExtensionsAllow(\".zip,.png,.JPEG,.jpeg,.PNG\") ]           |
|                                                                                                                                                                                 |
| [        [%\>]]                                                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Razor\]]**[]                                                                                                                                         |
|                                                                                                                                                                                                                                    |
| [   [\@{]  Html.Syncfusion().UploadBox([\"upload\"])][]                                                |
|                                                                                                                                                                                                                                    |
| [                             .AsyncUpload]                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [                             (]                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [                                 s =\> s.AutoUpload([true])]                                                                                                             |
|                                                                                                                                                                                                                                    |
| [                                     .SaveAction([\"Save\"], [\"UploadBox\"])]                                                                |
|                                                                                                                                                                                                                                    |
| [                                     .RemoveAction([\"Remove\"], [\"UploadBox\"])]                                                            |
|                                                                                                                                                                                                                                    |
| [                             )]                                                                                                                                                               |
|                                                                                                                                                                                                                                    |
| [                             .ClientSideOnLoad([\"onLoad\"])]                                                                                                         |
|                                                                                                                                                                                                                                    |
| [                    .ClientSideOnCancel([\"onCancel\"])]                                                                                                              |
|                                                                                                                                                                                                                                    |
| [                    .ClientSideOnComplete([\"onComplete\"])]                                                                                                          |
|                                                                                                                                                                                                                                    |
| [                    .ClientSideOnError([\"onError\"])]                                                                                                                |
|                                                                                                                                                                                                                                    |
| [                    .ClientSideOnRemove([\"onRemove\"]) ]                                                                                                             |
|                                                                                                                                                                                                                                    |
| [                    .ClientSideOnSelect([\"onSelect\"]) ]                                                                                                             |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [                                .ClientSideOnUpload([\"onUpload\"])]                                                                                                  |
|                                                                                                                                                                                                                                    |
| [                                                    .AutoFormat([Skins].Sandune).ExtensionsAllow([\".zip,.png,.JPEG,.jpeg,.PNG\"]).Render();] |
|                                                                                                                                                                                                                                    |
| [        [}]]                                                                                                                                                      |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   [In Javascript, use the methods to enable and disable an item ]as[ follows:]

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Javascript\]]**[]                                                                            |
|                                                                                                                                                                            |
| [  [function] onLoad(evt) {][]                                                |
|                                                                                                                                                                            |
| [         ]                                                                                                                            |
|                                                                                                                                                                            |
| [          [//ClientSideOnLoad event triggered]]                                                             |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| [        [function] onCancel(evt) {]                                                                              |
|                                                                                                                                                                            |
| [            [//ClientSideOnCancel event triggered]]                                                         |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(evt).each([function] () {]                                                                        |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| [         ]                                                                                                                            |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [return] [false];]                                                              |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| [        [function] onComplete(evt) {]                                                                            |
|                                                                                                                                                                            |
| [            [var] file = evt.files;]                                                                             |
|                                                                                                                                                                            |
| [            [//ClientSideOnComplete event triggered]]                                                       |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(file).each([function] () {]                                                                       |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| **[        [function] onError(evt, control) {]**                                                                  |
|                                                                                                                                                                            |
| **[            [// You can handle the Extension violation in the On Error event]]**                          |
|                                                                                                                                                                            |
| **[]**                                                                                                                                 |
|                                                                                                                                                                            |
| **[            [//On Error event triggered]]**                                                               |
|                                                                                                                                                                            |
| **[            [if] (evt.action == [\"ExtensionsDeny\"]) {]**                              |
|                                                                                                                                                                            |
| **[                alert([\"Denied Extension are \"] + control.get_ExtensionsDeny());]**                        |
|                                                                                                                                                                            |
| **[            }]**                                                                                                                    |
|                                                                                                                                                                            |
| **[            [else] [if] (evt.action == [\"ExtensionsAllow\"]) {]** |
|                                                                                                                                                                            |
| **[                alert([\"Allowed Extension are \"] + control.get_ExtensionsAllow());]**                      |
|                                                                                                                                                                            |
| **[            }]**                                                                                                                    |
|                                                                                                                                                                            |
| **[            [else] [if] (evt.action == [\"Error\"]) {]**           |
|                                                                                                                                                                            |
| **[                [var] file = evt.files;]**                                                                     |
|                                                                                                                                                                            |
| **[                [var] filenames = [\"\"];]**                                            |
|                                                                                                                                                                            |
| **[                \$(file).each([function] () {]**                                                               |
|                                                                                                                                                                            |
| **[                    filenames = filenames + [\"\\nName:\"] + [this].name;]**            |
|                                                                                                                                                                            |
| **[                });]**                                                                                                              |
|                                                                                                                                                                            |
| **[]**                                                                                                                                 |
|                                                                                                                                                                            |
| **[            }]**                                                                                                                    |
|                                                                                                                                                                            |
| **[           ]**                                                                                                                      |
|                                                                                                                                                                            |
| **[        }]**                                                                                                                        |
|                                                                                                                                                                            |
| [        [function] onRemove(evt) {]                                                                              |
|                                                                                                                                                                            |
| [            [//ClientSideOnRemove event triggered]]                                                         |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(evt).each([function] () {]                                                                        |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [return] [false];]                                                              |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| [        [function] onSelect(evt) {]                                                                              |
|                                                                                                                                                                            |
| [            [//ClientSideOnSelect event triggered]]                                                         |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(evt).each([function] () {]                                                                        |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [return] [false];]                                                              |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [        [function] onUpload(evt) {]                                                                              |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [//ClientSideOnUpload event triggered]]                                                         |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(evt).each([function] () {]                                                                        |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| [          ]                                                                                                                           |
|                                                                                                                                                                            |
| [            [return] [false];]                                                              |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Using Properties Model

[The following steps guide in handling client side events through the Properties model.]

1.   [In Controller, create an object for the **UploadBoxModel** class and set the **ClientSide Events**. Assign this model class to view data.][ ]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Controller\]]**[]                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [     [public] [ActionResult] Index()][]             |
|                                                                                                                                                                           |
| [        {]                                                                                                                           |
|                                                                                                                                                                           |
| [          ]                                                                                                                          |
|                                                                                                                                                                           |
| [            [UploadBoxModel] model = [new] [UploadBoxModel]();] |
|                                                                                                                                                                           |
| [            model.ClientSideOnCancel = [\"onLoad\"];]                                                        |
|                                                                                                                                                                           |
| [            \...\...]                                                                                                                |
|                                                                                                                                                                           |
| [            [return] View(model);]                                                                              |
|                                                                                                                                                                           |
| [          ]                                                                                                                          |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[2.   [In **View**, invoke the UploadBox helper with the UploadBox id as the first argument followed by the view data of the **UploadBoxModel** class.]]

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                             |
| [    [\<%][=] Html.Syncfusion().UploadBox([\"uploadbox\"], ([UploadBoxModel])Model) [%\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                    |
| [     [@(] [new] [HtmlString](Html.Syncfusion().UploadBox([\"upload\"],([UploadBoxModel])Model).ToString())[)]][] |
|                                                                                                                                                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

3.   [In **Javascript**, define the function to handle the specified events.]

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Javascript\]]**[]                                                                             |
|                                                                                                                                                                            |
| [  [function] onLoad(evt) {][]                                                |
|                                                                                                                                                                            |
| [         ]                                                                                                                            |
|                                                                                                                                                                            |
| [          [//ClientSideOnLoad event triggered]]                                                             |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| [        [function] onCancel(evt) {]                                                                              |
|                                                                                                                                                                            |
| [            [//ClientSideOnCancel event triggered]]                                                         |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(evt).each([function] () {]                                                                        |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| [         ]                                                                                                                            |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [return] [false];]                                                              |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| [        [function] onComplete(evt) {]                                                                            |
|                                                                                                                                                                            |
| [            [var] file = evt.files;]                                                                             |
|                                                                                                                                                                            |
| [            [//ClientSideOnComplete event triggered]]                                                       |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(file).each([function] () {]                                                                       |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| **[        [function] onError(evt, control) {]**                                                                  |
|                                                                                                                                                                            |
| **[            [// You can handle the Extension violation in the On Error event]]**                          |
|                                                                                                                                                                            |
| **[]**                                                                                                                                 |
|                                                                                                                                                                            |
| **[            [//On Error event triggered]]**                                                               |
|                                                                                                                                                                            |
| **[            [if] (evt.action == [\"ExtensionsDeny\"]) {]**                              |
|                                                                                                                                                                            |
| **[                alert([\"Denied Extension are \"] + control.get_ExtensionsDeny());]**                        |
|                                                                                                                                                                            |
| **[            }]**                                                                                                                    |
|                                                                                                                                                                            |
| **[            [else] [if] (evt.action == [\"ExtensionsAllow\"]) {]** |
|                                                                                                                                                                            |
| **[                alert([\"Allowed Extension are \"] + control.get_ExtensionsAllow());]**                      |
|                                                                                                                                                                            |
| **[            }]**                                                                                                                    |
|                                                                                                                                                                            |
| **[            [else] [if] (evt.action == [\"Error\"]) {]**           |
|                                                                                                                                                                            |
| **[                [var] file = evt.files;]**                                                                     |
|                                                                                                                                                                            |
| **[                [var] filenames = [\"\"];]**                                            |
|                                                                                                                                                                            |
| **[                \$(file).each([function] () {]**                                                               |
|                                                                                                                                                                            |
| **[                    filenames = filenames + [\"\\nName:\"] + [this].name;]**            |
|                                                                                                                                                                            |
| **[                });]**                                                                                                              |
|                                                                                                                                                                            |
| **[]**                                                                                                                                 |
|                                                                                                                                                                            |
| **[            }]**                                                                                                                    |
|                                                                                                                                                                            |
| **[           ]**                                                                                                                      |
|                                                                                                                                                                            |
| **[        }]**                                                                                                                        |
|                                                                                                                                                                            |
| [        [function] onRemove(evt) {]                                                                              |
|                                                                                                                                                                            |
| [            [//ClientSideOnRemove event triggered]]                                                         |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(evt).each([function] () {]                                                                        |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [return] [false];]                                                              |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| [        [function] onSelect(evt) {]                                                                              |
|                                                                                                                                                                            |
| [            [//ClientSideOnSelect event triggered]]                                                         |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(evt).each([function] () {]                                                                        |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [return] [false];]                                                              |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [        [function] onUpload(evt) {]                                                                              |
|                                                                                                                                                                            |
| []                                                                                                                                     |
|                                                                                                                                                                            |
| [            [//ClientSideOnUpload event triggered]]                                                         |
|                                                                                                                                                                            |
| [            [var] filenames = [\"\"];]                                                    |
|                                                                                                                                                                            |
| [            \$(evt).each([function] () {]                                                                        |
|                                                                                                                                                                            |
| [                filenames = filenames + [\"\\nName:\"] + [this].name;]                    |
|                                                                                                                                                                            |
| [            });]                                                                                                                      |
|                                                                                                                                                                            |
| [          ]                                                                                                                           |
|                                                                                                                                                                            |
| [            [return] [false];]                                                              |
|                                                                                                                                                                            |
| [        }]                                                                                                                            |
|                                                                                                                                                                            |
| []                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

