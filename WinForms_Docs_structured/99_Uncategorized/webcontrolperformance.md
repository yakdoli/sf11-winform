---
title: webcontrolperformance.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\webcontrolperformance.md
created_at: 2025-07-03
---








  









## Web Control Performance {#web-control-performance style="tab-stops: 0pt"}

 

Syncfusion Essential studio makes use of the class named ScriptResourceAttribute which is used to define a resource in an assembly to be used from a client script file.

 

Then the resource files which are all used in the Syncfusion controls are gzipped and served over the network. The following screen shot shows this.

 

{border="0"}

Figure 36: Web Control Performance

[] 

In order to achieve this, you need to set the following attributes in the project\'s web.config file.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<][configuration system.web.extensions][/\>\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ][. . .\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|       ][\<][scripting][\>\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ][            ][\<][ScriptResourceHandler][ ][enableCompression][=\"][true][\" ][enableCaching][=\"][true\"][ ][/\>\ |
| ][      ][\<][/][scripting][\>\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ][. . .\                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ][\</][system.web.extensions][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

As the resource files get gzipped

 

[·      ]It saves the precious network band-width.

[·      ]It reduces the load-time. As a result, the web form, which consists of the Syncfusion controls, will get loaded faster on the client browser.

[·      ]It also reduces the network traffic.

 

[]{#related-topics}

