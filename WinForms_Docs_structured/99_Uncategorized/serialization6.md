---
title: serialization6.md
original_path: WinForms_Docs/99_Uncategorized/serialization6.md
created_at: 2025-08-05
---








  









## Serialization {#serialization style="tab-stops: 0pt"}

[]{#p101}Serialization is the process of saving and retrieving the Essential Diagram file. Essential Diagram WPF supports saving the diagram page as an XAML file. The page and all its properties get saved. On loading, the page gets loaded in the current view with all its nodes and connections. This load and save feature allows you to save their diagram page for future use. You can continue working on their page by loading the appropriate XAML file.

[] 

Table 84: Methods Table

+--------------+------------------+-------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Name         | Parameters       | Return Type | Description                                                                     | Reference Links                                                                                            |
+--------------+------------------+-------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Save()       | Null             | Void        | Displays the Save Dialogue Box to save the DiagramPage into XAML file.          |  |
|              |                  |             |                                                                                 |                                                                                                            |
|              |                  |             |                                                                                 |                                                                                                            |
+--------------+------------------+-------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Save(string) | String           | Void        | Saves the DiagramPage into  XAML file whose file name is specified.             |  |
|              |                  |             |                                                                                 |                                                                                                            |
|              |                  |             |                                                                                 |                                                                                                            |
+--------------+------------------+-------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Save(Stream) | System.IO.Stream | Void        | Saves the DiagramPage into memory stream.                                       |  |
|              |                  |             |                                                                                 |                                                                                                            |
|              |                  |             |                                                                                 |                                                                                                            |
+--------------+------------------+-------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Load()       | Null             | Void        | Displays the Load Dialogue Box to load the DiagramPage from selected XAML file. |  |
|              |                  |             |                                                                                 |                                                                                                            |
|              |                  |             |                                                                                 |                                                                                                            |
+--------------+------------------+-------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Load(string) | String           | Void        | Loads the DiagramPage from the file name mentioned.                             |  |
|              |                  |             |                                                                                 |                                                                                                            |
|              |                  |             |                                                                                 |                                                                                                            |
+--------------+------------------+-------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Load(Stream) | System.IO.Stream | Void        | Loads the DiagramPage from the memory stream.                                   |  |
|              |                  |             |                                                                                 |                                                                                                            |
|              |                  |             |                                                                                 |                                                                                                            |
+--------------+------------------+-------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

[] 

 This process is explained in the following topic:

More:







