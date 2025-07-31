---
title: addingdicomtoanapplication.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\addingdicomtoanapplication.md
created_at: 2025-07-03
---








  









### Adding DICOM to an Application {#adding-dicom-to-an-application style="tab-stops: 0pt"}

The following sets of code snippets illustrate the conversion to DICOM Format.

[] 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                     |
|                                                                                                                                                                                                                                      |
| [   [//Initailizing the DICOM Image object.]]                                                                                                                              |
|                                                                                                                                                                                                                                      |
| [     [DICOMImage] dcmImage = [new] [DICOMImage](([string])[this].textBox1.Tag);] |
|                                                                                                                                                                                                                                      |
| [   [//Saving the DICOM image.]]                                                                                                                                           |
|                                                                                                                                                                                                                                      |
| [     dcmImage.Save([\"Sample.dcm\"]);]                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                         |
| [   [\'Initailizing the DICOM Image object.]]                                                                                                                                                 |
|                                                                                                                                                                                                                                                         |
| [    [Dim] dcmImage [As] [New] DICOMImage([DirectCast]([Me].textBox1.Tag, [String]))] |
|                                                                                                                                                                                                                                                         |
| [   [\'Saving the DICOM image.]]                                                                                                                                                              |
|                                                                                                                                                                                                                                                         |
| [   dcmImage.Save([\"Sample.dcm\"])]**[]**                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[] 

[] 

[] 

[] 

[] 

[] 

[] 

[] 

[] 

[] 

 

 

[]{#related-topics}

