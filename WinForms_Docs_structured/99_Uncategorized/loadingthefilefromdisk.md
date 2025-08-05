---
title: loadingthefilefromdisk.md
original_path: WinForms_Docs/99_Uncategorized/loadingthefilefromdisk.md
created_at: 2025-08-05
---






#### Loading the File From Disk {#loading-the-file-from-disk style="tab-stops: 0pt"}

 

The HTML file that is located in the user\'s disk can be loaded into the HTMLUIControl. It is loaded by specifying the location of the file in the disk.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                    |
|                                                                                                                                                                                                                   |
| **[]**                                                                                                                                          |
|                                                                                                                                                                                                                   |
| [// Load the specified HTML Document from user\'s drive.]                                                                                       |
|                                                                                                                                                                                                                   |
| [string][ filepath = [@\"C:\\MyProjects\\LoadHTML\\FromDisk.htm\"];] |
|                                                                                                                                                                                                                   |
| [this][.htmluiControl1.LoadHTML(filePath);]                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                          |
| **[]**                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                          |
| [\'Load the specified HTML Document from user\'s drive.]                                                                                                                                               |
|                                                                                                                                                                                                                                                                          |
| [Private][ filepath [As] [String] = [\"C:\\MyProjects\\LoadHTML\\FromDisk.htm\"]] |
|                                                                                                                                                                                                                                                                          |
| [Me][.HtmluiControl1.LoadHTML(filepath)]                                                                                                            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image shows file loaded from the User\'s Drive.

 

                {border="0"}

[] 

Figure 15: [Loading HTML document from the User\'s Drive into the HTMLUI Control]**[]**

[]{#p22} 

More:





