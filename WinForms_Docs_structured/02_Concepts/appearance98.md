---
title: appearance98.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\02_Concepts\appearance98.md
created_at: 2025-07-03
---






#### Appearance {#appearance style="tab-stops: 0pt"}

[The GalleryView control supports fourteen built-in themes which enhance the look and feel of the control.]

 

Properties

+-------------+--------------------------------------+------------------+--------------------------------------------------+-------------+
| Name        | Description                          | Type of property | Value it accepts                                 | Dependency  |
+-------------+--------------------------------------+------------------+--------------------------------------------------+-------------+
| AutoFormat  | Used to define the syncfusion themes | enum             | [Skins].Office2007Blue   | NA          |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Office2007Silver |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Office2007Black  |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Vista            |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Almond           |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Blueberry        |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Blend            |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Olive            |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Turquoise        |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Monochrome       |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Sandune          |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].VS2010           |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Marble           |             |
|             |                                      |                  |                                                  |             |
|             |                                      |                  | [Skins].Midnight         |             |
+-------------+--------------------------------------+------------------+--------------------------------------------------+-------------+

 

Using Builder

1.   In the **view**, invoke the **GalleryView** helper with the control ID as an argument.**[]**

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                              |
| [  ]                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                              |
| [\<%][=][Html.Syncfusion().GalleryView([\"gallery1\"]).AutoFormat(Skins.Vista)[%\>]] |
|                                                                                                                                                                                                                                                                                                                              |
| **[]**                                                                                                                                                                                                                                                                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[Razor\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [  ]                                                                                                                                                                               |
|                                                                                                                                                                                                                                     |
| [@][{]                                                                                    |
|                                                                                                                                                                                                                                     |
| [ Html.Syncfusion().GalleryView([\"gallery1\"]).AutoFormat(Skins.Vista).Render();][}] |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

2.   Build and run the application.

 

Using Model

1.   In the controller, create an instance of **GalleryViewModel**.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Controller]**                                                                                                                             |
|                                                                                                                                                                                  |
| [public][ [ActionResult] Index()]                                   |
|                                                                                                                                                                                  |
| [        {]                                                                                                                                  |
|                                                                                                                                                                                  |
| [            [//Create an instance of GalleryViewModel.]]                                                              |
|                                                                                                                                                                                  |
| [            [GalleryViewModel] myModel = [new] [GalleryViewModel] ();] |
|                                                                                                                                                                                  |
| [            myModel.AutoFormat = Skins.Vista;]                                                                                              |
|                                                                                                                                                                                  |
| **[            ]**[]                                                                                     |
|                                                                                                                                                                                  |
| [            [//Pass the instance through view data to the view.]]                                                     |
|                                                                                                                                                                                  |
| [            ViewData\[[\"myGalleryView\"]\] = myModel;]                                                             |
|                                                                                                                                                                                  |
| [            [return] View();]                                                                                          |
|                                                                                                                                                                                  |
| [        }]                                                                                                                                  |
|                                                                                                                                                                                  |
| []                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

2.   In the **view**, invoke the **GalleryView** helper with the view data key as the control ID.**

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                     |
| [\<%][=][Html.Syncfusion().GalleryView ([\"myGalleryView\"])[%\>]] |
|                                                                                                                                                                                                                                                                     |
| **[]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                     |
| **[\[Razor\]]**                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                     |
| [       [@]][{]                                                                                                                |
|                                                                                                                                                                                                                                                                     |
| [ Html.Syncfusion().GalleryView ([\"myGalleryView\").Render();]][}]                                                                |
|                                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[{border="0"}]

[{border="0"}]

Fourteen built-in skins of the GalleryView control:

**[]** 

{border="0"}  

Figure 123: Gallery View---Almond Skin    

{border="0"}

Figure 124: Gallery View---Blend Skin

{border="0"}

Figure 125: Gallery View---BlueBerry Skin

{border="0"}

Figure 126: Gallery View---Marble Skin

{border="0"}

Figure 127: Gallery View---MidNight Skin

{border="0"}

Figure 128: Gallery View---Monochrome Skin

{border="0"}

Figure 129: Gallery View---Office2007Black Skin

  {border="0"}

Figure 6: Gallery View---Office2007Blue Skin

 {border="0"}

Figure 130: Gallery View---Office2007Silver Skin

{border="0"}

Figure 131: Gallery View---Olive Skin

{border="0"}

Figure 132: Gallery View---Sandune Skin

{border="0"}

Figure 133: Gallery View---Turqoise Skin

{border="0"}

Figure 134: Gallery View---Vista Skin

{border="0"}

Figure 135: Gallery View---VS2010 Skin

 

[]{#related-topics}

