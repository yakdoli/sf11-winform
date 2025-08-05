---
title: uploadboxclientsideevents.md
original_path: WinForms_Docs/99_Uncategorized/uploadboxclientsideevents.md
created_at: 2025-08-05
---






##### UploadBox Client-Side Events {#uploadbox-client-side-events style="tab-stops: 0pt"}

 

Most of the time, it is not possible to know the size of a file before it is uploaded, so that the upload can be stopped if the file size too large. By using the ClientSideOnUploading event of UploadBox, you can perform Business Logic as the upload begins, so there is no need to wait until a file is uploaded to the server to find out its size---thereby saving time and bytes.

Although it is not possible to retrieve the size of a file before the upload process starts, once it does begin, the ClientSideOnUploading event will be triggered. You may then use the GetTotalFileSize() client method to retrieve the size of the file before it is completely uploaded to the server.

This event can be used whenever there is a need to perform business logic before a file is completely uploaded to the server.

First, add UploadBox and a UploadProgress to the page and add the ClientSideOnUploading event to the UploadBox, as seen in the following code snippet.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][syncfusion][:][UploadBox][ [ID][=\"UploadBox1\"] [runat][=\"server\"] [ClientObjectId][=\"upbox\"] [UploadFolder][=\"Upload\"] [PostbackOnUpload][=\"true\"]  ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                        [ShowSubmitButton][=\"true\"]  [ClientSideOnUploading][=\"checkSize()\"]  [/\>]]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [                        [\<][syncfusion][:][UploadProgress] [ID][=\"prog\"] [runat][=\"server\"] [ClosePopup][=\"false\"] [Triggers][=\"UploadBox1\"] [/\>]]                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[                 []]

[] 

In the method invoked by the ClientSideOnUploading event (here it is checkSize() ), check to see whether the file size is greater than a specified size restriction, as measured in bytes, by using the GetTotalFileSize() method of UploadBox. If the file size is greater than the specified size, the upload can be cancelled.

 

+-------------------------------------------------------------------------------------------------------------------+
| [function][ checkSize() {]   |
|                                                                                                                   |
| [            [var] size = upbox.GetTotalFileSize();]     |
|                                                                                                                   |
| [            [if] (size \> 36450000) {]                  |
|                                                                                                                   |
| [                upbox.CancelUploadFile();]                                   |
|                                                                                                                   |
| [                [return] [false];] |
|                                                                                                                   |
| [            }]                                                               |
|                                                                                                                   |
| [        }]                                                                   |
+-------------------------------------------------------------------------------------------------------------------+

 

In the code snippet above, any file greater than 34.7 MB will be filtered and the upload will be cancelled.

[] 

Property Detail

**[]** 

+-----------------------+-------------------------------------------------------+------------------+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Property              | Description                                           | Type of property | Value it accepts                              | Property syntax                                                                                                                                      |
|                       |                                                       |                  |                                               |                                                                                                                                                      |
|                       |                                                       |                  |                                               |                                                                                                                                                      |
+-----------------------+-------------------------------------------------------+------------------+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ClientSideOnUploading | A client-side method triggered when an upload begins. | Client-side      | Name of the client-side method to be invoked. |                                                                                                                                                      |
|                       |                                                       |                  |                                               |                                                                                                                                                      |
|                       |                                                       |                  |                                               |   -------------------------------------------------------------------------------------------------------------------------------------------------- |
|                       |                                                       |                  |                                               |   [ClientSideOnUploading][=\"anyClientMethod()\"]   |
|                       |                                                       |                  |                                               |   -------------------------------------------------------------------------------------------------------------------------------------------------- |
+-----------------------+-------------------------------------------------------+------------------+-----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

Methods

**[]** 

  --------------------- -------------------------- ---------------------------- ---------------------------------------------------------------------------------------- ---------------------------------------------------------------- ---------------------------------------------------------------
  Name of the method    Parameters of the method   Return type                  When is it called?                                                                       Purpose of the method                                            What is the result after the control returns from the method?
  GetTotalFileSize();   NIL                        FileSize in bytes notation   This method can be called after the upload has started and the upload progress begins.   This method is used to retrieve the size of the uploaded file.   The size of a file selected for upload will be retrieved.
  --------------------- -------------------------- ---------------------------- ---------------------------------------------------------------------------------------- ---------------------------------------------------------------- ---------------------------------------------------------------

**[]** 

[]{#p569}[] 

[]{#related-topics}

