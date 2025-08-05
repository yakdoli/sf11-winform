---
title: triggers.md
original_path: WinForms_Docs/99_Uncategorized/triggers.md
created_at: 2025-08-05
---






##### Triggers {#triggers style="tab-stops: 0pt"}

[] 

Triggers in Uploads contains list of Ids to trigger upload. The triggers will work when **PostBackOnUpload** property is set to **False**.

 

When UploadBox has it\'s **Trigger** property set, on form submit if form \_EventTarget value is not in UploadBox\'s Trigger value, then UploadBox\'s \<input type=\"file\"\> should be cleared to prevent upload process. If UploadBox has PostBackOnUpload set to False, upload process will not be done on form submit, because Uploadbox\'s \<input type=\"file\"/\> is rendered in individual frame element.

[] 

In this case user can call client side **UploadFile** method to call UploadBox\'s child frame form submit. UploadFile method only calls submit of UploadBox\'s frame form. This method should be called without any parameters and file will be uploaded, that are entered into UploadBox\'s \<input type=\"file\"/\> element.

[] 

Triggers property of UploadProgress

[] 

UploadProgress allows you to specify the target UploadBox controls, for which the progress control should be triggered displaying details of the process. Triggers property of UploadProgress specifies a comma-delimited list of the UploadBox controls Ids to trigger the UploadProgress control.

 

The following sample demonstrates how to show summary of both files uploading process, when two files are uploading asynchronously (UploadBox\'s PostbackOnUpload set to False).

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][UploadBox][ [ID][=\"UploadBox1\"] **[PostbackOnUpload][=\"false\"]** [runat][=\"server\"] [/\>]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][UploadBox][ [ID][=\"UploadBox2\"] **[PostbackOnUpload][=\"false\"]** [runat][=\"server\"] [/\>]]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [\<][cc1][:][UploadProgress][ [ID][=\"SummaryProgress\"] [runat][=\"server\"] **[Triggers][=\"UploadBox1, UploadBox2\"]** [Inline][=\"True\"\>\</][cc1][:][UploadProgress][\>]] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

If files are uploading synchronously (UploadBox\'s PostbackOnUpload set to True), all triggered UploadProgresses display summary process, because all files are uploaded simultaneously in one request to the server and this process cannot be divided.

[] 

For more details, see [Multiple File Uploads]{.UGHyperlink}[.]

[] 

Triggers property of UploadBox

 

Triggers property of UploadBox is a comma-delimited list of the controls Ids, to trigger the UploadBox. You can hide UploadBox\'s Upload button and start to upload file on postback from some controls. For this, you need add these controls Ids to Triggers property of UploadBox. If Page\'s postback will be sent from any other controls, then UploadBox\'s value will be cleared to prevent upload process.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [The following sample demonstrates how to trigger UploadBoxes controls:]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][cc1][:][UploadBox][ [ID][=\"UploadBox1\"] **[Triggers][=\"SubmitButton, WebButton\"]** [runat][=\"server\"] [ShowSubmitButton][=\"false\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][cc1][:][UploadBox][ [ID][=\"UploadBox2\"] **[Triggers][=\"SubmitButton, WebButton\"]** [runat][=\"server\"] [/\>]]                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][input][ [type][=\"submit\"] **[id][=\"SubmitButton\"]** [value][=\"Upload files  synchronously\"/\>]]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][asp][:][Button][ **[ID][=\"WebButton\"]** [Text][=\"Upload files  synchronously\"] [runat][=\"server\"/\>]]                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Triggers property  of the UploadBox works when the PostbackOnUpload property of the UploadBox is set to True. In other case, for triggering UploadBox with PostbackOnUpload is set to False, you can call client side UploadFile method of UploadBox script object to start file uploading and file will be uploaded that are entered into UploadBox control.

 

The following sample demonstrates how to trigger UploadBox control, when PostbackOnUpload is set to False.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][cc1][:][UploadBox][ [ID][=\"UploadBox1\"] [ClientObjectId][=\"\_sfUploadBox1\"] **[PostbackOnUpload][=\"false\"]** [runat][=\"server\"] [ShowSubmitButton][=\"false\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<][input][ [type][=\"button\"] [id][=\"SubmitButton\"] [value][=\"Upload file\"] **[onclick][=\"\_sfUploadBox1.UploadFile()\"]**[/\>]]                                                                                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

