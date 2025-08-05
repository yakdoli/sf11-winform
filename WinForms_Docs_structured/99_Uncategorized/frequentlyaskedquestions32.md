---
title: frequentlyaskedquestions32.md
original_path: WinForms_Docs/99_Uncategorized/frequentlyaskedquestions32.md
created_at: 2025-08-05
---






##### Frequently Asked Questions {#frequently-asked-questions style="tab-stops: 0pt"}

This section will help you become more familiar in using the FolderBrowser control.

[] 

###### []{#p502}[]{#_What_are_FolderBrowser}3.3.7.1.5.1 What are FolderBrowser Flags? {#what-are-folderbrowser-flags style="tab-stops: 0pt"}

[] 

Flags can be used to set various styles for the FolderBrowser Dialog. Each style has it\'s own behavior and these styles can be added or removed to get the desired style for the FolderBrowser Dialog.

 

Look at the below given snippet to apply \"RestrictToSubfolders\" style and to remove the \"ShowTextBox\" style for the FolderBrowser Dialog.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| []                                                                                                                                        |
|                                                                                                                                                                                             |
| [this][.folderBrowser1.Style &= \~[FolderBrowserStyles].RestrictToSubfolders;] |
|                                                                                                                                                                                             |
| [this][.folderBrowser1.Style \|= [FolderBrowserStyles].ShowTextBox;]           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                  |
| [Me][.folderBrowser1.Style = [Me].folderBrowser1.Style [And] [Not] FolderBrowserStyles.RestrictToSubfolders] |
|                                                                                                                                                                                                                                                                  |
| [Me][.folderBrowser1.Style = [Me].folderBrowser1.Style [Or] FolderBrowserStyles.ShowTextBox]                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

