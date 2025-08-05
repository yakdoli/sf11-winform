---
title: externalstylesheet.md
original_path: WinForms_Docs/02_Concepts/externalstylesheet.md
created_at: 2025-08-05
---






#### External StyleSheet {#external-stylesheet style="tab-stops: 0pt"}

[[[]]]{.underline} 

The External style sheets contain style definitions in a separate .css file, for various HTML tags that are in the document. These styles are applied by linking the css file to the HTML document inside the Link tag. The Link tag should be placed in the head section of the HTML document as it contains the information about the cascading style sheet that is to be referred by this document.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------+
| **[\[CSS\]]**                                                                      |
|                                                                                                                                        |
| **[]**                                                                             |
|                                                                                                                                        |
| [FileName and location: C:\\MyProjects\\StyleSheets\\styleSheet.css] |
|                                                                                                                                        |
| []                                                                   |
|                                                                                                                                        |
| [body]                                                              |
|                                                                                                                                        |
| [ {]                                                                               |
|                                                                                                                                        |
| [        [background-color]: [#dae5f5];]  |
|                                                                                                                                        |
| [        [cursor]: [default];        ]    |
|                                                                                                                                        |
| [ }]                                                                               |
|                                                                                                                                        |
| [ [p]]                                                      |
|                                                                                                                                        |
| [ {]                                                                               |
|                                                                                                                                        |
| [        [color]: [Green];]               |
|                                                                                                                                        |
| [ }]                                                                               |
|                                                                                                                                        |
| [ [div]]                                                    |
|                                                                                                                                        |
| [ {]                                                                               |
|                                                                                                                                        |
| [        [color]: [Blue];]                |
|                                                                                                                                        |
| [        [font-family]: [Tahoma];]        |
|                                                                                                                                        |
| [ }]                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------+

[   ]

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[HTML\]]**                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [File name and location: C:\\MyProjects\\StyleSheets\\external.html]                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][html][\>]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][head][\>]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [        [\<][link] [rel][=Stylesheet] [type][=\"text/css\"] [href][=\"C:\\MyProjects\\StyleSheets\\styleSheet.css\"] [/\>]]   |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][head][\>][ ]                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][body][\>]                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][p][\>][Green color for paragraph.[\</][p][\>] ] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][div][\>][Blue color for division[\</][div][\>]] |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][body][\>]                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                |
| [\</][html][\>]                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The HTMLUI control uses two modes of applying styles to the HTML document with the help of the external style sheets.

 

More:







