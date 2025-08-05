---
title: uploadingandinsertingimages.md
original_path: WinForms_Docs/99_Uncategorized/uploadingandinsertingimages.md
created_at: 2025-08-05
---






##### [Uploading and Inserting Images] {#uploading-and-inserting-images style="tab-stops: 0pt"}

[] 

Uploading Images

[] 

The **UploadImagesPath** property lets you specify the path where users can upload their images. By default, this property is set to **String.Empty**, which will disable the \'Upload Images\' command in the toolbar. Specify a proper value to enable this feature.

[] 


{border="0"}Note: Provide appropriate write permission to the target folder.


[] 

Programmatically this could be set as follows.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [RichTextEditor1.UploadImagesPath = \"..\"; [//Specifies the application folder]]                                                                                |
|                                                                                                                                                                                                                                            |
| [RichTextEditor1.UploadImagesPath = \"ClientData/UploadedImages\";[//Specifies a sub-folder called \"ClientData/UploadedImages\" within the application folder]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                       |
| [Private][ RichTextEditor1.UploadImagesPath = \"..\" [\'Specifies the application folder]]                                                                                 |
|                                                                                                                                                                                                                                                                                                                       |
| [Private][ RichTextEditor1.UploadImagesPath = \"ClientData/UploadedImages\" [\'Specifies a sub-folder called \"ClientData/UploadedImages\" within the application folder]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Also note that for the above feature to work, you will have to add the following **httpModule** to your application\'s **web.config** file.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[web.config\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][httpModules][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [  \<][add][ ][name][=][\"[UploadModule]\"[ ][type][=]\"[Syncfusion.Web.UI.WebControls.Tools.UploadControl.UploadModule, Syncfusion.Tools.Web, Version=x.x.x.x, Culture=neutral, PublicKeyToken=3D67ED1F87D44C89]\"[/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\</][httpModules][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: You might have to change the version number in the tags to whatever version you are linking to.


[] 

With this feature turned on users can upload custom images into the server using the Upload dialog as shown below.

[] 

{border="0"}

**[]** 

Figure 79: RichTextEditor with Upload dialog to upload custom image into the target folder

[] 

Inserting Images

[] 

The **InsertImagesPath** property lets you specify the path containing the image files to which users can insert links to. By default, this property is set to **String.Empty**, which will disable the \'Insert Images\' command in the toolbar. Specify a proper value to enable this feature.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                            |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                                            |
| [RichTextEditor1.InsertImagesPath = \"..\"; [//Specifies the application folder]]                                                                                |
|                                                                                                                                                                                                                                            |
| [RichTextEditor1.InsertImagesPath = \"ClientData/UploadedImages\";[//Specifies a sub-folder called \"ClientData/UploadedImages\" within the application folder]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                       |
| [Private][ RichTextEditor1.InsertImagesPath = \"..\" [\'Specifies the application folder]]                                                                                 |
|                                                                                                                                                                                                                                                                                                                       |
| [Private][ RichTextEditor1.InsertImagesPath = \"ClientData/UploadedImages\" [\'Specifies a sub-folder called \"ClientData/UploadedImages\" within the application folder]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

With this feature turned on users can insert links to images into the server by using the **Open** **Image** dialog box as shown below.

[] 

{border="0"}

**[]** 

Figure 80: Open Image dialog box to insert image into RichTextEditor

 

[]{#related-topics}

