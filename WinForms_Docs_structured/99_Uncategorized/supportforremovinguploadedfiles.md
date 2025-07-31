---
title: supportforremovinguploadedfiles.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\supportforremovinguploadedfiles.md
created_at: 2025-07-03
---






##### Support for removing uploaded files {#support-for-removing-uploaded-files style="tab-stops: 0pt"}

This feature allows you to remove the files that have been uploaded.

**Action Method implemented**

+--------------+---------------------------------------------------------------------------------------------------+----------------------+----------------------+----------------+
| **Name**     | **Description**                                                                                   | **Type of property** | **Value it accepts** | **Dependency** |
+--------------+---------------------------------------------------------------------------------------------------+----------------------+----------------------+----------------+
| RemoveAction | This is the action method that is used to remove the files that have been uploaded to the server. | ActionMethod         | Controller           | NA             |
|              |                                                                                                   |                      |                      |                |
|              |                                                                                                   |                      | Action               |                |
+--------------+---------------------------------------------------------------------------------------------------+----------------------+----------------------+----------------+

[[[]]]{.underline} 

You can remove files that have been uploaded by making use of the following code snippets:

Using Builder

The following steps guide you in configuring the **[RemoveAction ]**through Builder.

1.   In **View**, [invoke the UploadBox helper with the ]UploadBox**[ id]**[ as the first argument followed by the **RemoveAction** in the AsyncUpload.]

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                 |
| [\<%][=][ Html.Syncfusion().UploadBox([\"upload\"])][] |
|                                                                                                                                                                                                                                                                 |
| [    .AllowMultipleFiles([true])]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [    .AsyncUpload(]                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                 |
| [        a =\> ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [            a.SaveAction([\"Save\"],[\"uploadbox\"])]                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| **[                .RemoveAction([\"Remove\"], [\"uploadbox\"])]**                                                                                                          |
|                                                                                                                                                                                                                                                                 |
| [            .AutoUpload([true])]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                 |
| [              ]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                 |
| [         )]                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                 |
| [    .AutoFormat([Skins].Sandune)[%\>]]                                                                                                                                 |
|                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[]                                                                            |
|                                                                                                                                                                      |
| [\@{][Html.Syncfusion().UploadBox([\"upload\"])] |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| [    .AllowMultipleFiles([true])]                                                                           |
|                                                                                                                                                                      |
| [    .AsyncUpload(]                                                                                                              |
|                                                                                                                                                                      |
| [        a =\>]                                                                                                                  |
|                                                                                                                                                                      |
| [            a.SaveAction([\"Save\"], [\"UploadBox\"])]                          |
|                                                                                                                                                                      |
| **[            .RemoveAction([\"Remove\"], [\"UploadBox\"])]**                   |
|                                                                                                                                                                      |
| [            .AutoUpload([true])]                                                                           |
|                                                                                                                                                                      |
| [         )]                                                                                                                     |
|                                                                                                                                                                      |
| [    .AutoFormat([Skins].Sandune).Render();[}]]                              |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| []                                                                                                                               |
|                                                                                                                                                                      |
| []                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   In the controller, define the ActionMethod. This is the code snippet for Action Method:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Controller\]]**[]                                                                                                              |
|                                                                                                                                                                                                              |
| [   [public] [ActionResult] Remove([string]\[\] fileNames)][]      |
|                                                                                                                                                                                                              |
| [        {]                                                                                                                                                              |
|                                                                                                                                                                                                              |
| [            [foreach] ([var] fullName [in] fileNames)]                                                   |
|                                                                                                                                                                                                              |
| [            {]                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [                [var] fileName = [Path].GetFileName(fullName);]                                                            |
|                                                                                                                                                                                                              |
| [                [var] physicalPath = [Path].Combine(Server.MapPath([\"\~/App_Data\"]), fileName);] |
|                                                                                                                                                                                                              |
| [                [if] (System.IO.[File].Exists(physicalPath))]                                                              |
|                                                                                                                                                                                                              |
| [                {]                                                                                                                                                      |
|                                                                                                                                                                                                              |
| [                    ]                                                                                                                                                   |
|                                                                                                                                                                                                              |
| [                    [System.IO.File.Delete(physicalPath);]]                                                                                       |
|                                                                                                                                                                                                              |
| [                }]                                                                                                                                                      |
|                                                                                                                                                                                                              |
| [            }]                                                                                                                                                          |
|                                                                                                                                                                                                              |
| [            [// Return an empty string to signify success]]                                                                                       |
|                                                                                                                                                                                                              |
| [            [return] Content([\"\"]);]                                                                                     |
|                                                                                                                                                                                                              |
| [        }]                                                                                                                                                              |
|                                                                                                                                                                                                              |
| []                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

**[Using Properties Model]**

[The following steps will guide you in setting RemoveAction, through the Properties model:]

1.   In the **Controller**, create an instance of UploadBoxModel, define the **RemoveAction** method and pass the instance through view-specific data to View as given below:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[ \[Controller\]]**[]                                                                           |
|                                                                                                                                                                           |
| [    [public] [ActionResult] Index()][]              |
|                                                                                                                                                                           |
| [        {]                                                                                                                           |
|                                                                                                                                                                           |
| [          ]                                                                                                                          |
|                                                                                                                                                                           |
| [            [UploadBoxModel] model = [new] [UploadBoxModel]();] |
|                                                                                                                                                                           |
| [            [AsyncUpload] async = [new] [AsyncUpload]();]       |
|                                                                                                                                                                           |
| [            async.AutoUpload = [true];]                                                                         |
|                                                                                                                                                                           |
| [            async.SaveAction = [\"Home/Save\"];]                                                             |
|                                                                                                                                                                           |
| [            async.RemoveAction = [\"Home/Remove\"];]                                                         |
|                                                                                                                                                                           |
| [            model.AsyncUpload = async;]                                                                                              |
|                                                                                                                                                                           |
| []                                                                                                                                    |
|                                                                                                                                                                           |
| [            [return] View(model);]                                                                              |
|                                                                                                                                                                           |
| [          ]                                                                                                                          |
|                                                                                                                                                                           |
| [        }]                                                                                                                           |
|                                                                                                                                                                           |
| []                                                                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   [In **View**, invoke the UploadBox helper with the UploadBox id as the first argument followed by the view data of the **UploadBoxModel** class.]

 

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

[] 

[]{#related-topics}

