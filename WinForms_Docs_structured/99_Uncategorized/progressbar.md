---
title: progressbar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\progressbar.md
created_at: 2025-07-03
---








  









### ProgressBar {#progressbar style="tab-stops: 0pt"}

 

 

The ProgressBar control is ideal to show the progress of a lengthy operation on the server with a live progress bar on the client.

[·      ]Uses asynchronous callbacks.

[·      ]Fires a callback event called UpdateProgress that the user can listen to and update the ProgressPercentage.

[·      ]Frequency property indicates the time interval at which progress should be updated.

[·      ]ProgressBar control can be hosted in Safari browser too.

   

Limitations in using the ProgressBar

 

The ProgressBar control relies on being able to trigger asynchronous callbacks to update the progress state. But, such calls are prevented by the framework when Session states are used in an application. If you use Session state in your application you will notice that the progress does not update smoothly. It would go from 0 to 100% directly.

So, the workaround is to not use Session state in your application or isolate the ProgressBar using logic in a separate application that does not use Session state.

[]{#p585} 

More:









