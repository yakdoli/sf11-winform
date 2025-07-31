---
title: othersettings.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\othersettings.md
created_at: 2025-07-03
---






##### Other Settings {#other-settings style="MARGIN-LEFT: 18pt; tab-stops: 18.0pt"}

[] 

TabControlAdv now supports animation on tab pages. Animated image in GIF can be inserted in a tab page. The format supports up to 8 bits per pixel with a palette of up to 256 distinct colors chosen from the 24-bit RGB color space. Both 3D and 2D formats are supported.

                  Users can insert graphics or logos with solid areas of color, small animations, low-resolution film clips etc. to make the tab page more interactive and lively. The size of the image can also be adjusted.

[] 

There are two major properties which come into picture:

[·      ]Image

[·      ]Image size

[] 

{border="0"}

Figure 1045: Image Settings

[] 

The following table lists the properties of the GIF image:

[] 


  ----------- ------------------------------------------------------------------------------------------- ------------------
   Property   Description                                                                                 Type of Property
  Image       Allows the user to insert the required image using the location where the image is saved.   Image
  ImageSize   Allows the users to modify the size of the image.                                           Size
  ----------- ------------------------------------------------------------------------------------------- ------------------


[                       ]

[] 

[] 

Inserting GIF Image

**[]** 

The code should be in the following format:

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                               |
|                                                                                                                                                                                                              |
| **[]**                                                                                                                                                     |
|                                                                                                                                                                                                              |
| [this][.tabPageAdv.Image = [Image.FromFile(imagepath)];]                                           |
|                                                                                                                                                                                                              |
| [this][.tabPageAdv.ImageSize = [new] System.Drawing.[Size](height,width);] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

The following code illustrates insertion of the required GIF image.

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| **[]**                                                                                                                                              |
|                                                                                                                                                                                                       |
| [this][.tabPageAdv.Image = [Image.FromFile("sample.gif")];]                                 |
|                                                                                                                                                                                                       |
| [this][.tabPageAdv.ImageSize = [new] System.Drawing.[Size](16,16);] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 


{border="0"}Note: Only when the ImageIndex property is -1, Image from the Image property will be displayed or else Image from ImageList will be displayed.


[] 

Run the code. The required image is displayed.

 

 

 

[]{#related-topics}

