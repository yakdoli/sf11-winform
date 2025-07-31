---
title: internalstylesheet.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\internalstylesheet.md
created_at: 2025-07-03
---






#### Internal StyleSheet {#internal-stylesheet style="tab-stops: 0pt"}

[] 

The Internal style sheet is used to define the same styles to all the occurrences of a specific tag in the document. The internal style sheet is defined inside the Style tag, in the head section of the document. The user can create another style definition for other HTML tags with a new name inside the same style tag. The following snippet shows how an internal stylesheet is defined for a specific tag in a HTML document.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [File name and location: C:\\MyProjects\\StyleSheets\\internal.html]                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][html][\>]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][head][\>]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][style][ [type][=\"text/css\"\>]]                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [        [p] {[color]: [blue]}]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [        [div]{[color]: [red]}]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][style][\>]                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][head][\>][ ]                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][body][\>]                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][p][\>][This is a paragraph.[\</][p][\>] ]    |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][div][\>][This is a division.[\</][div][\>]]  |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\<][p][\>][This is a new paragraph.[\</][p][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][body][\>]                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                             |
| [\</][html][\>]                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[   ]

+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                                         |
| []                                                                    |
|                                                                                                                                                         |
| [htmluiControl.LoadHTML([@\"C:\\MyProjects\\StyleSheets\\internal.html\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                     |
|                                                                                                                                                        |
| []                                                                   |
|                                                                                                                                                        |
| [htmluiControl.LoadHTML(@[\"C:\\MyProjects\\StyleSheets\\internal.html\"])] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

