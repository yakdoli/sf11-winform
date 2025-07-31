---
title: serialization7.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\serialization7.md
created_at: 2025-07-03
---








  









## Serialization {#serialization style="tab-stops: 0pt"}

Serialization is the process of saving and retrieving Essential Diagram (for MVC and SL) which supports saving the diagram page as an XML file. The page and all its properties get saved in the process.\
On loading, the page gets loaded in the current view with all its nodes and connections. The users can continue working on their page while loading the appropriate XML file.

Use Case Scenario

This load and save feature allows the user to save their diagram page for future use.

 

Limitations of using the Save and Load feature for diagrams from Silverlight

This feature doesn't have any significant limitations in MVC, but there are a few that show up when you try to save and load diagrams from Silverlight, as given below:

1.   Content other than shapes (images, buttons etc.) from Silverlight will not be supported in the diagram page in MVC. This means content that you save or load from SL will not work in MVC diagram, unless they are shapes.

2.   The stretch option for SL is not supported in diagram MVC. This means that if you had formatted you shapes in SL, and loaded or saved the shape to diagram MVC, the changes will be discarded and only the original shape will be usable.

3.   In order to use custom shapes and save, or load them in diagram from SL, you will have to use the path name of the required custom shape. In case you retrieve the path name using the namespace attributes, the shape will not be loaded, or saved.

 

Where do I find the installed samples?

[To view the samples:]

1.   [Open the Essential Diagram sample browser from the Dashboard. (Refer to the Samples and Locations section).]

2.   [Go to the **Getting Started** tab, and click **Serialization**.]

 

Methods

+-------------------+-----------------------------------------------------------------------+-------------------------------------------------+-------------+--------------+
| Method            | Description                                                           | Parameters                                      | Type        | Return Type  |
+-------------------+-----------------------------------------------------------------------+-------------------------------------------------+-------------+--------------+
| Save              | Saves the diagram page into an XML file whose file name is specified. | String file name                                | Server Side | ActionResult |
+-------------------+-----------------------------------------------------------------------+-------------------------------------------------+-------------+--------------+
| Save              | Saves the diagram page into memory stream.                            | [System.IO.Stream stream] | Server Side | ActionResult |
|                   |                                                                       |                                                 |             |              |
|                   | This method is not applicable for diagrams in Silverlight.            |                                                 |             |              |
+-------------------+-----------------------------------------------------------------------+-------------------------------------------------+-------------+--------------+
| Load              | Loads the diagram page from the file name mentioned.                  | String file name                                | Server Side | Void         |
+-------------------+-----------------------------------------------------------------------+-------------------------------------------------+-------------+--------------+
| Load              | Loads the diagram page from the memory stream.                        | [System.IO.Stream stream] | Server Side | void         |
|                   |                                                                       |                                                 |             |              |
|                   | This method is not applicable for diagrams in SL.                     |                                                 |             |              |
+-------------------+-----------------------------------------------------------------------+-------------------------------------------------+-------------+--------------+
| LoadCommonDiagram | Loads the Silverlight diagram page from the file name mentioned.      | String file name                                | Server Side | Void         |
+===================+=======================================================================+=================================================+=============+==============+

 

More:





