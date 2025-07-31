---
title: performance10.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\performance10.md
created_at: 2025-07-03
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}





  






   


## Performance {#performance style="tab-stops: 0pt"}

 

The Syncfusion Essential studio makes use of class named ScriptResourceAttribute which can be used to define a resource in an assembly to be used from a client script file.

 

Then the resource files which are all used in the Syncfusion controls will be zipped and served over the network. The following screen shot shows this:

 

{border="0"}

Figure 1

 

In order to achieve this, you will need to set the following attributes in the project\'s web.config file:

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<] [configuration system.web.extensions] [/\>\                                                                                                                                                                                                                                                                                                                |
| ]. . .\                                                                                                                                                                                                                                                                                                                                                                                                            |
|           [\<][scripting][\>\                                                                                                                                                                                                                                                                                                                                   |
| ]                   [\<][ScriptResourceHandler][enableCompression]=[\"true\"][enableCaching]=[\"true\"][/\>\ |
| ]          [\<]/[scripting][\>\                                                                                                                                                                                                                                                                                |
| ]. . .\                                                                                                                                                                                                                                                                                                                                                                                                            |
| [\</][system.web.extensions][\>]                                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

As the resource files gets zipped,

[·      ]It saves the precious network band-width

[·      ]It reduces the load-time. As a result, the webform which consists of the Syncfusion controls will get loaded faster on the client's browser

[·      ]It also reduces the network traffic

 

More:





