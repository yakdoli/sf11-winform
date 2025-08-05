---
title: usingthememorystream1.md
original_path: WinForms_Docs/02_Concepts/usingthememorystream1.md
created_at: 2025-08-05
---






##### Using the Memory Stream {#using-the-memory-stream style="LINE-HEIGHT: 115%; TEXT-INDENT: -50.4pt; MARGIN: 10pt 0pt 0pt 50.4pt; tab-stops: 50.4pt"}

The following code snippet illustrates the implementation of loading the diagram page using a memory stream.


+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**[]                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [DiagramPropertiesModel][ serializeModel = [new] [DiagramPropertiesModel]();]                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [public][ [ActionResult] Serialization()]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [{]                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                  |
| [    serializeModel.Load(savedStream);]                                                                                                                                                                                                                                                                                     |
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

Figure 146: Load Diagram Using a Memory Stream

 

[]{#related-topics}

