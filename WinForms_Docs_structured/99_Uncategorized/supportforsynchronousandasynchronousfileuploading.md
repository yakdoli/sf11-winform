---
title: supportforsynchronousandasynchronousfileuploading.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\supportforsynchronousandasynchronousfileuploading.md
created_at: 2025-07-03
---






##### Support for synchronous and asynchronous file uploading {#support-for-synchronous-and-asynchronous-file-uploading style="tab-stops: 0pt"}

###### 5.29.1.2.3.1        Asynchronous File uploading {#asynchronous-file-uploading style="tab-stops: 0pt"}

This feature allows you to upload and remove files asynchronously.

The following steps guide you in enabling the file upload asynchronously:

1.   In **View,** declare the UploadBox using the helper, and provide the Save and Remove action details (Remove is optional).

[] 

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
| [                .RemoveAction([\"Remove\"], [\"uploadbox\"])]                                                                                                              |
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
| [            .RemoveAction([\"Remove\"], [\"UploadBox\"])]                       |
|                                                                                                                                                                      |
| [            .AutoUpload([true])]                                                                           |
|                                                                                                                                                                      |
| [         )]                                                                                                                     |
|                                                                                                                                                                      |
| [    .AutoFormat([Skins].Sandune).Render();[}]]                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Implement Action methods in the controller:

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[]                                                                                                                                                        |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [  [public] [ActionResult] Save([IEnumerable]\<[HttpPostedFileBase]\> upload)][] |
|                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [            [// \"upload\" gets the attached file documents in the page]]                                                                                                                  |
|                                                                                                                                                                                                                                                       |
| [            [foreach] ([var] file [in] upload)]                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [            {]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [                [// \"file.FileName\" will get the name of the file uploaded. Some browsers send file names with full path ]]                                                              |
|                                                                                                                                                                                                                                                       |
| [                [var] fileName = [Path].GetFileName(file.FileName);]                                                                                                |
|                                                                                                                                                                                                                                                       |
| [                [var] destinationPath = [Path].Combine(Server.MapPath([\"\~/App_Data\"]), fileName);]                                       |
|                                                                                                                                                                                                                                                       |
| [                ]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [                file.SaveAs(destinationPath);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [            }]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [                [// Return an empty string to signify success]]                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [            [return] Content([\"\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [     [public] [ActionResult] Remove([string]\[\] fileNames)]                                                                                   |
|                                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [            [foreach] ([var] fullName [in] fileNames)]                                                                                            |
|                                                                                                                                                                                                                                                       |
| [            {]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [                [var] fileName = [Path].GetFileName(fullName);]                                                                                                     |
|                                                                                                                                                                                                                                                       |
| [                [var] physicalPath = [Path].Combine(Server.MapPath([\"\~/App_Data\"]), fileName);]                                          |
|                                                                                                                                                                                                                                                       |
| [                [if] (System.IO.[File].Exists(physicalPath))]                                                                                                       |
|                                                                                                                                                                                                                                                       |
| [                {]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [                    ]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                       |
| [                    System.IO.[File].Delete(physicalPath);]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [                }]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                       |
| [            }]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                       |
| [            [// Return an empty string to signify success]]                                                                                                                                |
|                                                                                                                                                                                                                                                       |
| [            [return] Content([\"\"]);]                                                                                                                              |
|                                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 


Note: The upload box id and the Save action's argument should have the same name, and the argument in the Remove action method should be named filename.


**[]** 

###### 5.29.1.2.3.2        Synchronous File Uploading {#synchronous-file-uploading style="tab-stops: 0pt"}

The following steps guide you to upload synchronously:

1.   In **View,** declare the UploadBox using the helper, and add the form element and set the controller action. Set the encrypt type to **multipart/form-data.**

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**[]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [   [\<][div] [id][=\"Target\"\>]][]                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<%] [using] (Html.BeginForm([\"SynchronousUpload\"], [\"uploadbox\"],]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                         [FormMethod].Post, [new]]                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                         {]                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                             id = [\"uploadForm\"],]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                             enctype =]                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                                 [\"multipart/form-data\"]]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                         }))]                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [               { [%\>]]                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<%][=]Html.Syncfusion().UploadBox([\"Upload\"]).AutoFormat([Skins].Sandune) [%\>]]                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<][div] [style][=\"][margin][: 20px 0 0 0;\"\>]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][input] [type][=\"submit\"] [class][=\"inputbutton\"] [id][=\"Submit\"] [value][=\"Upload\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [                [\<][input] [type][=\"reset\"] [class][=\"inputbutton\"] [value][=\"Reset\"] [/\>]]                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\</][div][\>]]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [            [\<%] } [%\>]]                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| [        [\</][div][\>]]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**[]                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                        |
| [  [\<][div] [id][=\"Target\"\>]][]                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                        |
| [        [@][using] (Html.BeginForm([\"SynchronousUpload\"], [\"UploadBox\"],]                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                        |
| [                         [FormMethod].Post, [new]]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                        |
| [                         {]                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                        |
| [                             id = [\"uploadForm\"],]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                        |
| [                             enctype =]                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                        |
| [                                 [\"multipart/form-data\"]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                        |
| [                         }))]                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                        |
| [        {]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                        |
| [            Html.Syncfusion().UploadBox([\"Upload\"]).AutoFormat([Skins].Sandune).Render();]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                        |
| [            [\<][div] [style][=\"][margin][: 20px 0 0 0;\"\>]]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                        |
| [                [\<][input] [type][=\"submit\"] [class][=\"inputbutton\"] [value][=\"Upload\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                        |
| [                [\<][input] [type][=\"reset\"] [class][=\"inputbutton\"] [value][=\"Reset\"] [/\>]]   |
|                                                                                                                                                                                                                                                                                                                                        |
| [            [\</][div][\>]]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                        |
| [        }]                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                        |
| [    [\</][div][\>]]                                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

2.   Add submit and reset buttons to the form. 

3.   Implement Action methods in the controller to handle the files:

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Controller\]]**[]                                                                                                                                     |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [   \[[AcceptVerbs]([HttpVerbs].Post)\]][]                                                                 |
|                                                                                                                                                                                                                                    |
| [        [public] [ActionResult] SynchronousUpload([IEnumerable]\<[HttpPostedFileBase]\> Upload)] |
|                                                                                                                                                                                                                                    |
| [        {]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| [            [// \"Upload\" gets the attached file documents in the page]]                                                                                               |
|                                                                                                                                                                                                                                    |
| [            [if](Upload != [null])]                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [            [foreach] ([var] file [in] Upload)]                                                                                |
|                                                                                                                                                                                                                                    |
| [            {]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| [                [// \"file.FileName\" will get the name of the file uploaded. Some browsers send file names with full path ]]                                           |
|                                                                                                                                                                                                                                    |
| [                [var] fileName = [Path].GetFileName(file.FileName);]                                                                             |
|                                                                                                                                                                                                                                    |
| [                [var] destinationPath = [Path].Combine(Server.MapPath([\"\~/App_Data\"]), fileName);]                    |
|                                                                                                                                                                                                                                    |
| [               file.SaveAs(destinationPath);]                                                                                                                                                 |
|                                                                                                                                                                                                                                    |
| [            }]                                                                                                                                                                                |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| [            [// Return to success view page]]                                                                                                                           |
|                                                                                                                                                                                                                                    |
| [            [return] View([\"UploadSuccess\"]);]                                                                                                 |
|                                                                                                                                                                                                                                    |
| [        }]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                    |
| []                                                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[]{#related-topics}

