---
title: creatingasimpleproject.md
original_path: WinForms_Docs/99_Uncategorized/creatingasimpleproject.md
created_at: 2025-08-05
---








  









### Creating a simple project {#creating-a-simple-project style="tab-stops: 0pt"}

**Project** is the main class of Essential ProjIO. We can only create project files in XML format. The following lines of code create a simple project.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                      |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
| [// Creating an instance of Project]                                                                                                                |
|                                                                                                                                                                                                       |
| [Project][ project = [new] [Project]();[]] |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [// Saving the project - Creates an empty project]                                                                                                  |
|                                                                                                                                                                                                       |
| [project.Save([\"Empty Project.xml\"]);]                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                              |
|                                                                                                                                                                               |
| **[]**                                                                                                                                    |
|                                                                                                                                                                               |
| [\' Creating an instance of Project]                                                                                        |
|                                                                                                                                                                               |
| [Dim][ project [As] Project = [New] Project()] |
|                                                                                                                                                                               |
| []                                                                                                                                        |
|                                                                                                                                                                               |
| [\' Saving the Project - Creates an empty project]                                                                          |
|                                                                                                                                                                               |
| [project.Save([\"Empty Project.xml\"])]                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

The XML project file can be viewed in Microsoft Project using the option **File -- Open** and then selecting the XML format (\*.xml) option from the file types. Select '**Project Information**' option from the **Projects menu** and the options will look as follows:

 

{border="0"}

Figure 6: Project Information for Empty Project

 

[]{#related-topics}

