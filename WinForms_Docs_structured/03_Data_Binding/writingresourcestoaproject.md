---
title: writingresourcestoaproject.md
original_path: WinForms_Docs/03_Data_Binding/writingresourcestoaproject.md
created_at: 2025-08-05
---








  









### Writing Resources to a Project {#writing-resources-to-a-project style="tab-stops: 0pt"}

**Resources** property exposed by **Project** class represents the list of all the **Resource** objects in a project. This property can be used to update resources in a project.

The following code shows how to write resources to a project.

 

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
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [// Calculating Resource IDs and UIDs]                                                                                         |
|                                                                                                                                                                                  |
| [project.CalculateResourceIDs();]                                                                                                            |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
|                                                                                                                                                                                  |
| [// Saving the project]                                                                                                        |
|                                                                                                                                                                                  |
| [project.Save([\"Project With Resources.xml\"]);]                                                                    |
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
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [\' Calculating Resource IDs and UIDs]                                                                                                              |
|                                                                                                                                                                                                       |
| [project.CalculateResourceIDs()]                                                                                                                                  |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [\' Saving the project]                                                                                                                             |
|                                                                                                                                                                                                       |
| [project.Save([@\"D:\\Project With Resources.xml\"])]                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

