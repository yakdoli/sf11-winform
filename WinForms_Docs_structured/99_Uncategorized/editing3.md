---
title: editing3.md
original_path: WinForms_Docs/99_Uncategorized/editing3.md
created_at: 2025-08-05
---








  









## Editing {#editing style="tab-stops: 0pt"}

Essential Diagram offers add, edit, and delete operations for node and line details in a diagram page. This can be achieved by specifying the mapper for save actions in the diagram.[]

 

Use Case Scenarios

This feature enables the user to add, update, and delete the data from the diagram page.[]

 

Properties

  ----------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------- -------------------------------------------------------------------------------
  **Property**                                                                        **Description**                                                                                                                                                       **Type**                                                                        **Data Type**
  [[SaveMapper]]{.apple-style-span}[]   [[Gets the function name to save the diagram with added, updated, and deleted nodes and lines.]]{.apple-style-span}[]   [[Server]]{.apple-style-span}[]   [[String]]{.apple-style-span}[]
  ----------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------- -------------------------------------------------------------------------------

 

 

Methods

  **[Method ]**[]   **[Description ]**[]   **[Parameters ]**[]   **[Type ]**[]   **[Return Type ]**[]
  --------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------
  addNode[]                                                                   Add a node in a diagram.[]                                                       Name, text, shape, width, height[]                                              Client[]                                                                  NA[]
  addLine                                                                                             Add a line in a diagram.                                                                                 Name, text, type, linewidth, and line color                                                             Client                                                                                            NA
  save                                                                                                Save the diagram with added, edited, and deleted nodes collection.                                       NA                                                                                                      Client                                                                                            NA

[] 

Sample Link

[To view the samples:]

1.   [Open the Essential Diagram sample browser form the Dashboard. (Refer to the ]**[Samples and Locations]**[ section).]

2.   [Go to the **Editing** tab, and click **CRUD Demo**.]

More:





