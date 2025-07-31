---
title: howtochangethecaptiontext.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\howtochangethecaptiontext.md
created_at: 2025-07-03
---






#### How to change the caption text {#how-to-change-the-caption-text style="tab-stops: 0pt"}

[] 

This can be done using the below code.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                            |
|                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                                           |
| [// Set the caption text]                                                                                                                                                               |
|                                                                                                                                                                                                                                           |
| [// {TableName} - Displays the CaptionSection.ParentTableDescriptor.Name]                                                                                                               |
|                                                                                                                                                                                                                                           |
| [//{CategoryName} - Displays the CaptionSection.ParentGroup.Name]                                                                                                                       |
|                                                                                                                                                                                                                                           |
| [//{Category} - Displays the CaptionSection.ParentGroup.Category]                                                                                                                       |
|                                                                                                                                                                                                                                           |
| [//{RecordCount} - Displays the CaptionSection.ParentGroup.GetFilteredRecordCount()]                                                                                                    |
|                                                                                                                                                                                                                                           |
| [this][.gridGroupingControl1.TopLevelGroupOptions.CaptionText = [\"Tablename is {TableName} : {Category} : {RecordCount}\"];] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [\' Set the caption text]                                                                                                                                                            |
|                                                                                                                                                                                                                                        |
| [\' {TableName} - Displays the CaptionSection.ParentTableDescriptor.Name]                                                                                                            |
|                                                                                                                                                                                                                                        |
| [\'{CategoryName} - Displays the CaptionSection.ParentGroup.Name]                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [\'{Category} - Displays the CaptionSection.ParentGroup.Category]                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [\'{RecordCount} - Displays the CaptionSection.ParentGroup.GetFilteredRecordCount()]                                                                                                 |
|                                                                                                                                                                                                                                        |
| [Me][.gridGroupingControl1.TopLevelGroupOptions.CaptionText = [\"Tablename is {TableName} : {Category} : {RecordCount}\"]] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p646} 

 

[]{#related-topics}

