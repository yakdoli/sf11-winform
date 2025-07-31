---
title: serialization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\serialization.md
created_at: 2025-07-03
---








  









## Serialization {#serialization style="tab-stops: 0pt"}

 

[]{#p101}Serialization is the process of saving and retrieving the Essential Diagram file. Essential Diagram Silverlight supports saving the diagram page as an XAML file. The page and all its properties get saved. On loading, the page gets loaded in the current view with all its nodes and connections. This load and save feature allows the user to save their diagram page for future use. The users can continue working on their page by loading the appropriate XAML file.

[] 

Methods[:]

[] 

+--------------+------------------+-------------+------------------------------------------------------------------------------------+-------------------+
| Name         | Parameters       | Return Type | Description                                                                        | Reference Links   |
+==============+==================+=============+====================================================================================+===================+
| Save()       | Null             | Void        | Displays the Save Dialogue Box to save the DiagramPage into xaml file              | Save Diagram Page |
|              |                  |             |                                                                                    |                   |
|              |                  |             |                                                                                    |                   |
+--------------+------------------+-------------+------------------------------------------------------------------------------------+-------------------+
| Save(string) | String           | Void        | Saves the DiagramPage into  xaml file whose file name is specified.                | Save Diagram Page |
|              |                  |             |                                                                                    |                   |
|              |                  |             |                                                                                    |                   |
+--------------+------------------+-------------+------------------------------------------------------------------------------------+-------------------+
| Save(Stream) | System.IO.Stream | Void        | Saves the DiagramPage into memory stream                                           | Save Diagram Page |
|              |                  |             |                                                                                    |                   |
|              |                  |             |                                                                                    |                   |
+--------------+------------------+-------------+------------------------------------------------------------------------------------+-------------------+
| Load()       | Null             | Void        | Displays the Load Dialogue Box to load the DiagramPage from the selected xaml file | Load Diagram Page |
|              |                  |             |                                                                                    |                   |
|              |                  |             |                                                                                    |                   |
+--------------+------------------+-------------+------------------------------------------------------------------------------------+-------------------+
| Load(string) | String           | Void        | Loads the DiagramPage from the file name mentioned.                                | Load Diagram Page |
|              |                  |             |                                                                                    |                   |
|              |                  |             |                                                                                    |                   |
+--------------+------------------+-------------+------------------------------------------------------------------------------------+-------------------+
| Load()       | System.IO.Stream | Void        | Loads the DiagramPage from the memory stream                                       | Load Diagram Page |
|              |                  |             |                                                                                    |                   |
|              |                  |             |                                                                                    |                   |
+--------------+------------------+-------------+------------------------------------------------------------------------------------+-------------------+

[] 

 This process is explained in the following topic:

More:







