---
title: readingaprojectfile.md
original_path: WinForms_Docs/99_Uncategorized/readingaprojectfile.md
created_at: 2025-08-05
---








  









### Reading a project file {#reading-a-project-file style="tab-stops: 0pt"}

**Read** method of the **ProjectReader** class is used to read the project files. The Read method has two overloads namely:

[·      ]Read(string filename) -- opens the file specified by the given file name.

[·      ]Read(Stream stream) -- opens the file specified by the Stream.

**Read** method returns a **Project** object, which can then be used to retrieve or manipulate project information.

The following code illustrates the use of the **Read** method:

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
|                                                                                                                                                                                                        |
| [// Assigning the Project object returned by the Read method]                                                                                        |
|                                                                                                                                                                                                        |
| [Project][ P = [ProjectReader].Open([\"SimpleProject.xml\"]);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                       |
|                                                                                                                                                                                                        |
| **[]**                                                                                                                                                             |
|                                                                                                                                                                                                        |
| [\' Assigning the Project object returned by the Read method]                                                                                        |
|                                                                                                                                                                                                        |
| [Dim][ P [As] Project = ProjectReader.Open([\"SimpleProject.xml\"])] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

[]{#related-topics}

