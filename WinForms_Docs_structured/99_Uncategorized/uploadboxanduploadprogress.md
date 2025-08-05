---
title: uploadboxanduploadprogress.md
original_path: WinForms_Docs/99_Uncategorized/uploadboxanduploadprogress.md
created_at: 2025-08-05
---








  









### UploadBox and UploadProgress {#uploadbox-and-uploadprogress style="tab-stops: 0pt"}

 

The UploadBox and UploadProgress controls are integrated with each other. Hence to achieve the best usage, whenever the files are being uploaded using UploadBox control, the UploadProgress can be used to display the transfer progress of the corresponding files. This feature supports Classic and Integrated pipeline mode for IIS7 -- it is useful when the user wants to host the application in Integrated Pipeline mode of IIS7 with the upload control . 

[] 

UploadBox

[] 

[·      ]Flexible and easy to use.

[·      ]Destination folder can be set to upload the files anywhere on the server or to any physical location in your system.

[·      ]Support to upload multiple files at the same time.

[·      ]UploadBox permits the user to either allow or deny files with certain extensions.

[·      ]The size of files to be uploaded can be easily set.

[] 

UploadProgress

[] 

The UploadProgress displays the progress of the file transfer service. Also, progress control indicates the user with the total size of all the transferred files after completion of the file transfer.

Any control can be set to trigger the uploadprogress, that responds by displaying the progress rate of the upload process.

The progress bar can be made to either popup when it is triggered or can be made visible by default. Also it can be set to close when the upload function is complete.

 

More:









