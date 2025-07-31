---
title: inlinestylesheet.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\inlinestylesheet.md
created_at: 2025-07-03
---






#### Inline StyleSheet {#inline-stylesheet style="tab-stops: 0pt"}

[] 

The Inline style sheet will be present inside the HTML tag as an attribute named **Style**, for the HTML element. The styles for the contents of the tag will be given as the values for this attribute.

The following snippet shows an inline style, which is applied as an attribute inside the tag to a HTML element, which is inside the document.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                       |
| [File name and location: C:\\MyProjects\\StyleSheets\\inline.html]                                                                                                                               |
|                                                                                                                                                                                                                                                                                       |
| [\<][html][\>]                                                                   |
|                                                                                                                                                                                                                                                                                       |
| [\<][body][\>]                                                                   |
|                                                                                                                                                                                                                                                                                       |
| [\<][p][ [style][=\"background-color: #dae5f5;\"\>]] |
|                                                                                                                                                                                                                                                                                       |
| [Inline style applied to a paragraph.]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                       |
| [\</][p][\>][ ]              |
|                                                                                                                                                                                                                                                                                       |
| [\</][body][\>]                                                                  |
|                                                                                                                                                                                                                                                                                       |
| [\</][html][\>]                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                        |
|                                                                                                                                                       |
| []                                                                  |
|                                                                                                                                                       |
| [htmluiControl.LoadHTML([@\"C:\\MyProjects\\StyleSheets\\inline.html\"]);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                   |
|                                                                                                                                                      |
| []                                                                 |
|                                                                                                                                                      |
| [htmluiControl.LoadHTML(@[\"C:\\MyProjects\\StyleSheets\\inline.html\"])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

