---
title: connectordeletion.md
original_path: WinForms_Docs/99_Uncategorized/connectordeletion.md
created_at: 2025-08-05
---








  









### Connector Deletion {#connector-deletion style="tab-stops: 0pt"}

This feature allows you to delete a [single] connector from the diagram page in Essential Diagram for MVC without deleting the nodes attached to it.

 

Appearance and Structure

The following figures illustrate the appearance, structure, and function of the connector deletion feature and its settings:

{border="0"}

Figure 76: Selection of a Connector for Deletion

 

{border="0"}

 

Figure 77: Connectors after Deletion of the Selected Connector


 


Where do I find the installed samples?

[To view the samples:]

1.   [Open the Essential Diagram sample browser from the dashboard. (Refer to the ]**[Samples and Locations]**[ section).]

2.   [Go to the **Getting Started** tab, and click **Flat Diagram**.]

 

Properties

+-------------+-----------------------------------------------------------------------+---------------------+----------------------+--------------+
| Property    | Description                                                           | Type of Property    | Value it Accepts     | Dependencies |
+-------------+-----------------------------------------------------------------------+---------------------+----------------------+--------------+
| AllowDelete | Gets or sets a value indicating whether the connector can be deleted. | Dependency property | Boolean (true/false) | No           |
|             |                                                                       |                     |                      |              |
|             | The default value is set to true.                                     |                     |                      |              |
|             |                                                                       |                     |                      |              |
|             |                                                                       |                     |                      |              |
+-------------+-----------------------------------------------------------------------+---------------------+----------------------+--------------+

 

Enabling Connector Deletion in Essential Diagram for MVC

This section guides you through the process of enabling connector deletion in an MVC application. You can implement this feature in either one of the following two ways:

[·      ]Using Builder

[·      ]Through the properties model

 

More:







