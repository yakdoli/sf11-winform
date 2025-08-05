---
title: performance.md
original_path: WinForms_Docs/99_Uncategorized/performance.md
created_at: 2025-08-05
---








  









## Performance {#performance style="tab-stops: 0pt"}

[] 

The Syncfusion Essential Studio makes use of the class named ScriptResourceAttribute, to define a resource in an assembly, to be used from a client script file.

 

Then, the resource files which are all used in the Syncfusion controls will be gzipped and served over the network. The following screenshot shows this.

[] 

{border="0"}[]

Figure 115[]

[] 

In order to achieve this, you need to set the following attributes in the project\'s web.config file.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][configuration][ [system.web.extensions][/\>]]                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [. . .]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [      [\<][scripting][\>]]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                   |
| [            [\<][ScriptResourceHandler] [enableCompression][=\"true\"] [enableCaching][=\"true\"] [/\>]] |
|                                                                                                                                                                                                                                                                                                   |
| [      [\</][scripting][\>]]                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                   |
| [. . .]                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                   |
| [\</][system.web.extensions][\>]                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

As the resource files get gzipped

[] 

[·      ]It saves the precious network band-width.

[·      ]It reduces the load-time. As a result, the web form which consists of the Syncfusion controls, will get loaded more faster on the client browser.

[·      ]It also reduces the network traffic.

 

[]{#related-topics}

