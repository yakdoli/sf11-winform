---
title: databinding46.md
original_path: WinForms_Docs/03_Data_Binding/databinding46.md
created_at: 2025-08-05
---


{#d2h_url_template} {#d2h_package_url style="WIDTH: 0px; DISPLAY: none; HEIGHT: 0px"}



#### Databinding {#databinding style="tab-stops: 0pt"}

This feature allows you to bind the data source to the listbox control.

Properties

 

+-------------+---------------------------------+----------------------+----------------------------------------------------------------------------------------------------+-------------+
| Name        | Description                     | Type of the property | Value it accepts                                                                                   | Dependency  |
+-------------+---------------------------------+----------------------+----------------------------------------------------------------------------------------------------+-------------+
| ActionMode  | Used to specify the Action mode | enum                 | [ActionMode].Server,                                                       | NA          |
|             |                                 |                      |                                                                                                    |             |
|             |                                 |                      | [ActionMode].Json,                                                         |             |
|             |                                 |                      |                                                                                                    |             |
|             |                                 |                      | [ActionMode].[WebService] |             |
|             |                                 |                      |                                                                                                    |             |
|             |                                 |                      |                                                                                                    |             |
+-------------+---------------------------------+----------------------+----------------------------------------------------------------------------------------------------+-------------+

 

Methods

  -------------------- ------------------------------ -------------------------------- ----------------------------- -----------------
  Name of the method   Parameters of the method       Return type                      Descriptions                  Reference links
  BindDataSource       Action\<ListBoxItemBuilder\>   ListBoxItemBuilderBuilder\<T\>   Used to bind the datasource    NA
  -------------------- ------------------------------ -------------------------------- ----------------------------- -----------------

 

More:







