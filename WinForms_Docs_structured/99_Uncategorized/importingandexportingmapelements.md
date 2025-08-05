---
title: importingandexportingmapelements.md
original_path: WinForms_Docs/99_Uncategorized/importingandexportingmapelements.md
created_at: 2025-08-05
---








  









## Importing and Exporting Map Elements {#importing-and-exporting-map-elements style="tab-stops: 0pt"}

Map Elements---Symbols, Labels, Shapes and Paths can be saved in a XML and Image file. Only the XML file can be imported and if changes are needed it can be done and the Map Elements can be exported.

 

Property


  ------------------------ ----------------------------------------------------------- ------------ ----------- -----------------
  Property                 Description                                                 Type         Data Type   Reference links
  **EnableImageCapture**   Enables to save the portion of the map in an image format   Dependency   Boolean     NA
  ------------------------ ----------------------------------------------------------- ------------ ----------- -----------------


 

Methods


  ---------- ------------------------------------------------------------------------ ----------------- ------------- -----------------
  Methods    Description                                                              Parameters        Return Type   Reference links
  **Save**   Save the Map Elements in a XML and Image format with save file dialog.   NA                NA            NA
  **Save**   Save as per the Parameter Filename                                       String Filename   NA            NA
  **Load**   Loads the Map Elements from a XML file with Open file dialog.            NA                NA            NA
  **Load**   Loads the Map Elements from the given XML file                           String FileName   NA            NA
  ---------- ------------------------------------------------------------------------ ----------------- ------------- -----------------


 

Saving through the Save dialog box

Save the Map Elements in a XML and Image format. When calling the Save method, a save file dialog will be open. In that dialog we can specify the file name and format (Xml / Image) of the map. Then the map will be saved with given file format with the given name. For image file the following formats are supported:

[·      ]Tiff

[·      ]Gif

[·      ]Jpg

[·      ]Bmp

[·      ]Png

 

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                 |
| [this][.Map.Save();][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

 

Save through the File name

Save as per the Parameter Filename. When you call the Save method with the filename as a parameter as shown in the code snippet, the map will be saved in the appropriate file name. Format will be determined based on the extension of the file name. For example if we give file name as "Maps.xml" then the map will be saved as xml file.  If we give the file name as "Maps.tiff" then the map will be saved as tiff image file. For image file the following formats are supported:

[·      ]Tiff

[·      ]Gif

[·      ]Jpg

[·      ]Bmp

[·      ]Png

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                              |
| [this][.Map.Save("D:\\Map.xml");][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

{border="0"}

Figure 18: Save Dailog Box**[]**

 

Loading through the Open dialog box

Loads the Map Elements from a XML file. When calling the Load method without any parameter in it, an open file dialog box will be opened. The open dialog shows the list of Xml file which will be available in the current directory. We can choose the Xml file which is saved already by the Map control.

+-------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                |
|                                                                                                                                                 |
| [this][.Map.Load();][] |
+-------------------------------------------------------------------------------------------------------------------------------------------------+

 

Loads through the File name

Loads the Map Elements from the given XML file.  For example if the location is given as "D:\\Maps.xml" then the map will be loaded to the given location. Xml file will only be desterilized. Image files cannot be desterilized.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                             |
|                                                                                                                                                              |
| [this][.Map.Load("D:\\Map.xml");][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

{border="0"}

Figure 19: Load**[]**

Saving the Portion of Map as Image

To save the portion of the map as an image, set the EnableMouseCapture Property as true for the  Map Control  as shown in the following code snippet and select the portion from the map.

 

+-------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                          |
|                                                                                                                                           |
| [  mapControl.EnableImageCapture = [true]][] |
+-------------------------------------------------------------------------------------------------------------------------------------------+

{border="0"}

Figure 20: Save as Image

 

[]{#related-topics}

