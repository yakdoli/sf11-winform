---
title: selectselecttag.md
original_path: WinForms_Docs/99_Uncategorized/selectselecttag.md
created_at: 2025-08-05
---








  









### SELECT - Select Tag {#select---select-tag style="tab-stops: 0pt"}

[] 

The **Select** tag is used to create a drop-down list of options that can be selected by the user to give some input to the application. The select tag in HTMLUI supports the following attributes that improve the usage of the application.

[] 

[·      ]**size**: Specifies the number of items to be displayed in the select control in the document

[·      ]**disabled**: Displays a disabled list box in which no items can be selected

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                  |
| [File Location and Name:  C:\\MyProjects\\select\\select.html]                                                                                                                                 |
|                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                  |
| [\<][html][\>]                                              |
|                                                                                                                                                                                                                                                                  |
| [\<][body][\>]                                              |
|                                                                                                                                                                                                                                                                  |
| [\<][p][\>]                                                 |
|                                                                                                                                                                                                                                                                  |
| [Essential Studio includes ten component libraries in one great package. Each of these products has a unique and useful feature set.]                                                                        |
|                                                                                                                                                                                                                                                                  |
| [\</][p][\>]                                                |
|                                                                                                                                                                                                                                                                  |
| [\<][select][ [size][=\"2\"\>]] |
|                                                                                                                                                                                                                                                                  |
| [  [\<][option][\>]Essential Tools[\</][option][\>]]                       |
|                                                                                                                                                                                                                                                                  |
| [  [\<][option][\>]Essential Chart[\</][option][\>]]                       |
|                                                                                                                                                                                                                                                                  |
| [  [\<][option][\>]Essential Grid[\</][option][\>]]                        |
|                                                                                                                                                                                                                                                                  |
| [  [\<][option][\>]Essential HTMLUI[\</][option][\>]]                      |
|                                                                                                                                                                                                                                                                  |
| [\</][select][\>]                                           |
|                                                                                                                                                                                                                                                                  |
| [\</][body][\>]                                             |
|                                                                                                                                                                                                                                                                  |
| [\</][html][\>]                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [this][.htmluiControl.LoadHTML([@\"C:\\MyProjects\\select\\select.html\"]);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                     |
|                                                                                                                                                                                                                        |
| **[]**                                                                                                                                               |
|                                                                                                                                                                                                                        |
| [Me][.htmluiControl.LoadHTML(@[\"C:\\MyProjects\\select\\select.html\"])] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p95} 

[]{#related-topics}

