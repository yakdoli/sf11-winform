---
title: howtopluginanexternalconfigurationdileintotheeditcontrol.md
original_path: WinForms_Docs/99_Uncategorized/howtopluginanexternalconfigurationdileintotheeditcontrol.md
created_at: 2025-08-05
---








  









## How To Plug-in an External Configuration Dile Into the Edit Control {#how-to-plug-in-an-external-configuration-dile-into-the-edit-control style="tab-stops: 0pt"}

[] 

The Edit Control supports the creation and plug-in of custom configuration files into the Edit Control for syntax coloring. The configuration file has to be in XML format, and as per the directions in the [Configuration Settings] section. The following code snippet illustrates how to plug-in an external configuration file.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                       |
|                                                                                                                                                                                      |
| []                                                                                                                                 |
|                                                                                                                                                                                      |
| [// Plug-In an external configuration file.]                                                                                       |
|                                                                                                                                                                                      |
| [this][.editControl1.Configurator.Open([\" Configuration_File.xml \"]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                |
|                                                                                                                                                                                   |
| []                                                                                                                              |
|                                                                                                                                                                                   |
| [\' Plug-In an external configuration file.]                                                                                    |
|                                                                                                                                                                                   |
| [Me][.editControl1.Configurator.Open([\" Configuration_File.xml \"])] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p197} 

[]{#related-topics}

