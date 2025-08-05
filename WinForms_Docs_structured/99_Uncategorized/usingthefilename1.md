---
title: usingthefilename1.md
original_path: WinForms_Docs/99_Uncategorized/usingthefilename1.md
created_at: 2025-08-05
---






##### Using the File Name {#using-the-file-name style="LINE-HEIGHT: 115%; TEXT-INDENT: -50.4pt; MARGIN: 10pt 0pt 0pt 50.4pt; tab-stops: 50.4pt"}

The [following code snippets illustrate the implementation of loading the diagram page using]{.BodyText1Char} file name:


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [DiagramPropertiesModel][ serializeModel = [new] [DiagramPropertiesModel]();]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [public][ [ActionResult] Serialization()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    serializeModel.**[Load]**(LoadFileName);]                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    serializeModel][.DiagramMode = ][DiagramMode][.SVG;][] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    ViewData\[[\"Serialization\"]\] = serializeModel;]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [return] View();]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 


Note: The code snippet above is used to load diagram from MVC. To load diagram from Silverlight, replace the highlighted method name, with LoadCommonDiagram, as shown in the following code snippet:

 



+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [DiagramPropertiesModel][ serializeModel = [new] [DiagramPropertiesModel]();]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [public][ [ActionResult] Serialization()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    serializeModel.**[LoadCommonDiagram]**(LoadFileName);]                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    serializeModel][.DiagramMode = ][DiagramMode][.SVG;][] |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    ViewData\[[\"Serialization\"]\] = serializeModel;]                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    [return] View();]                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [}]                                                                                                                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 

+-------------------------------------------------------------------------------------------------------------------------+
| **[View]**[]                              |
|                                                                                                                         |
| [    [\<%]{]                           |
|                                                                                                                         |
| [          Html.Syncfusion().Diagram(\"Serialization\")]           |
|                                                                                                                         |
| [              .Render();]                                         |
|                                                                                                                         |
| [      }]                                                          |
|                                                                                                                         |
| [    [%\>]][] |
+-------------------------------------------------------------------------------------------------------------------------+

{border="0"}

Figure 145: Load Diagram Using File Name

 

[]{#related-topics}

