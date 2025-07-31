---
title: exporting5.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exporting5.md
created_at: 2025-07-03
---






#### Exporting {#exporting style="tab-stops: 0pt"}

 

Essential Digital Gauge has built-in support for exporting the gauge control into various image formats like jpeg, bmp, gif etc.

Essential Digital Gauge can be exported in both server and client side.

The following table lists the file formats a Digital Gauge can be exported to:

 

 


  ---------------- -----------
  File Extension   File Type
  .bmp             BMP
  .jpg             JPEG
  .jpeg            JPEG
  .gif             GIF
  .tiff            TIFF
  .Wmf             WMF
  .Png             PNG
  .emf             EMF
  ---------------- -----------


[] 

 


+-------------+-----------------------+-----------------------------+--------------------------------------------------+--------------------------------------------------+
| Property    | Description           | Property Type               | Value It Accepts                                 | Any other dependencies/Sub properties associated |
+-------------+-----------------------+-----------------------------+--------------------------------------------------+--------------------------------------------------+
| GaugeExport | Sets the Export Type. | [enum] | [GaugeExport].ServerSide | NA                                               |
|             |                       |                             |                                                  |                                                  |
|             |                       |                             |                                                  |                                                  |
|             |                       |                             |                                                  |                                                  |
|             |                       |                             | [GaugeExport].ClientSide |                                                  |
|             |                       |                             |                                                  |                                                  |
|             |                       |                             |                                                  |                                                  |
|             |                       |                             |                                                  |                                                  |
|             |                       |                             | [GaugeExport].None       |                                                  |
+-------------+-----------------------+-----------------------------+--------------------------------------------------+--------------------------------------------------+


**[]** 

 


+--------------------+---------------------------------------------------------+--------------------------------------------------------+------------------------------------------------------------------------------------+
| Name               | Parameters                                              | Return Type                                            | Description[]                                                |
+--------------------+---------------------------------------------------------+--------------------------------------------------------+------------------------------------------------------------------------------------+
| GenerateGaugeImage | [(Gauge_Obj,FileName,FileFormat)] | [None][] | [Used to generate the Gauge image in client or server side.] |
|                    |                                                         |                                                        |                                                                                    |
|                    |                                                         |                                                        |                                                                                    |
+--------------------+---------------------------------------------------------+--------------------------------------------------------+------------------------------------------------------------------------------------+


[] 

More:







