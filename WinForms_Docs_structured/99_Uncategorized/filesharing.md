---
title: filesharing.md
original_path: WinForms_Docs/99_Uncategorized/filesharing.md
created_at: 2025-08-05
---








  









### File Sharing {#file-sharing style="tab-stops: 0pt"}

[] 

By default, Edit Control locks the file currently loaded into it, and does not allow access to the same by any external application. To enable file sharing, set the **SharedFileMode** property of the Edit Control to **True**.

[] 


  ----------------------- ----------------------------------------------------------------------------
  Edit Control Property   Description
  SharedFileMode          Gets / sets value indicating whether file should be opened in shared mode.
  ----------------------- ----------------------------------------------------------------------------


 

+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                           |
|                                                                                                                                                          |
| []                                                                                                     |
|                                                                                                                                                          |
| [// Enable file sharing.]                                                                              |
|                                                                                                                                                          |
| [this][.editControl1.SharedFileMode = [true];] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                    |
|                                                                                                                                                       |
| []                                                                                                  |
|                                                                                                                                                       |
| [\' Enable file sharing.]                                                                           |
|                                                                                                                                                       |
| [Me][.editControl1.SharedFileMode = [True]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p90} 

[]{#related-topics}

