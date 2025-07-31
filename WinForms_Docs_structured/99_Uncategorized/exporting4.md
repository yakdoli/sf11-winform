---
title: exporting4.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\exporting4.md
created_at: 2025-07-03
---






#### Exporting {#exporting style="tab-stops: 0pt"}

 

Essential LinearGauge has built-in support for exporting the gauge control into various image formats like jpeg, bmp, gif and so on.

 

Essential LinearGauge can be exported in both server and client side.

The following table lists the file formats a LinearGauge can be exported to:

 

 


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


**[]** 

More:







