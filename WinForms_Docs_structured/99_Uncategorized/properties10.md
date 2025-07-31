---
title: properties10.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\properties10.md
created_at: 2025-07-03
---








  









### Properties {#properties style="tab-stops: 0pt"}

The following table illustrates the properties of the Toggle-Button control.

 

+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| Name          | Description                                                           | Type of the property | Data Type      | Value it accepts                                                    | Dependency  |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| ContentType   | Specifies the field that provides the content of the button.          | Server side          | ContentTypes   | [ContentTypes].TextOnly                     | NA          |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ContentTypes].ImageOnly                    |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ContentTypes].TextAndImage                 |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| ImagePosition | Specifies the field that provides the position of the button's image. | Server side          | ImagePositions | [ImagePositions].Left                       | ContentType |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Right                      |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Top                        |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [ImagePositions].Bottom                     |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| Skin          | Specifies the field that provides the appearance of the button.       | Server side          | Enum           | [Skins.Almond]                              | NA          |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Blend]                               |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Blueberry]                           |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Marble]                              |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Midnight]                            |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Monochrome]                          |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Office2007Black]                     |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Office2007Blue]                      |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Office2007Silver]                    |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Olive]                               |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Sandune]                             |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Turquoise]                           |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.Vista]                               |             |
|               |                                                                       |                      |                |                                                                     |             |
|               |                                                                       |                      |                | [Skins.VS2010]                              |             |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| Height        | Defines the height of the button.                                     | Server side          | Unit           | [Unit.]Pixel(100)[] | NA          |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| Width         | Defines the width of the button.                                      | Server side          | Unit           | [Unit.]Pixel(100)[] | NA          |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+
| IsChecked     | Defines the checked state of the button.                              | Server side          | Bool           | [True/false]                                | NA          |
+---------------+-----------------------------------------------------------------------+----------------------+----------------+---------------------------------------------------------------------+-------------+

 

[]{#related-topics}

