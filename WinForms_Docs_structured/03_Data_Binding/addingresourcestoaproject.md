---
title: addingresourcestoaproject.md
original_path: WinForms_Docs/03_Data_Binding/addingresourcestoaproject.md
created_at: 2025-08-05
---








  









### Adding Resources to a Project {#adding-resources-to-a-project style="tab-stops: 0pt"}

**Resources** property exposed by **Project** class represents the list of all the **Resource** objects in a project. This property can be used to add resources.

The following code snippet illustrates adding resources to a project.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                  |
| **[]**                                                                                                                                       |
|                                                                                                                                                                                  |
| [// Creating an instance of the Project]                                                                                       |
|                                                                                                                                                                                  |
| [Project][ project = [new] [Project]();]    |
|                                                                                                                                                                                  |
| []                                                                                                                             |
|                                                                                                                                                                                  |
| [// Creating resource]                                                                                                         |
|                                                                                                                                                                                  |
| [Resource][ resource = [new] [Resource]();] |
|                                                                                                                                                                                  |
| [resource.Name = [\"Resource1\"];]                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [// Adding resource to project]                                                                                                |
|                                                                                                                                                                                  |
| [project.Resources.Add(resource);]                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                      |
|                                                                                                                                                                                                       |
| [\' Creating an instance of the Project]                                                                                                            |
|                                                                                                                                                                                                       |
| [Dim][ project [As] Project = [New] Project()[]] |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                                            |
|                                                                                                                                                                                                       |
| [\' Creating resource]                                                                                                                              |
|                                                                                                                                                                                                       |
| [Dim][ resource [As] Resource = [New] Resource()]                      |
|                                                                                                                                                                                                       |
| [resource.Name = [\"Resource1\"]]                                                                                                         |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [\' Adding resource to Project][]                                                                               |
|                                                                                                                                                                                                       |
| [project.Resources.Add(resource)]                                                                                                                                 |
|                                                                                                                                                                                                       |
|                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

