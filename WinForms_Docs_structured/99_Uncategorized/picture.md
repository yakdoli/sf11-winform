---
title: picture.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\picture.md
created_at: 2025-07-03
---






##### Picture {#picture style="tab-stops: 0pt"}

 

WPicture class represents a picture in the Word document.

 

A picture is a shape. Positioning properties of WPicture class are almost the same as the other shapes.

 

A picture is positioned by using the VerticalPosition and HorizontalPosition properties. Measure unit is Point. Relative positioning is defined by using the HorizontalAlignment and VerticalAlignment properties.

 

HorizontalAlignment property returns the object of the ShapeHorizontalAlignment type. The following are the variants for the HorizontalAlignment property.

 

[·      ]None

[·      ]Left

[·      ]Center

[·      ]Right

[·      ]Inside

[·      ]Outside

 

VerticalAlignment property returns the object of the ShapeVerticalAlignment type. The following are the variants for the VerticalAlignment property.

 

[·      ]Bottom

[·      ]Center

[·      ]Inline

[·      ]Inside

[·      ]None

[·      ]Outside

[·      ]Top

 

**HorizontalOrigin** and **VerticalOrigin** properties define the reference origin, which is used for relative positioning of a picture.

 

HorizontalOrigin property returns the value of the HorizontalOrigin type. The following are the variants for the HorizontalOrigin property.

 

[·      ]Margin

[·      ]Page

[·      ]Column

[·      ]Character

 

VerticalOrigin property returns value of VerticalOrigin type. The following are the variants for the VerticalOrigin property.

 

[·      ]Margin

[·      ]Page

[·      ]Paragraph

[·      ]Line

 

You can set the width and height of the picture by using the **Width** and **Height** properties, and the **HeightScale** and **WidthScale** properties to get or set picture scaling.

 

The **LoadImage** function is used to set an image by loading the System.Drawing.Image object, or image bytes array. Also, you can use the **AppendPicture** function of the WParagraph class to append a picture to a paragraph.

 

Class Hierarchy

 

ParagraphItem

                \|

            WPicture

 

Public Constructor

 


  ----------------------------------- ------------------------------
  Name                                Description
  WPicture.WPicture (IWordDocument)   Gets the type of the entity.
  ----------------------------------- ------------------------------


 

**Public Properties**

 


  --------------------- -----------------------------------------------------------
  Name                  Description
  EntityType            Gets the type of the entity.
  Height                Gets or sets picture height.
  HeightScale           Gets or sets picture height scale factor in percent.
  HorizontalAlignment   Gets or sets picture horizontal alignment.
  HorizontalOrigin      Gets sets horizontal origin of the picture.  
  HorizontalPosition    Gets sets absolute vertical position of the picture.  
  Image                 Gets internal System.Drawing.Image object.  
  ImageBytes            Gets image byte array.  
  IsBelowText           Gets or sets whether picture is below image.  
  Size                  Gets or sets size of the picture object.  
  TextWrappingStyle     Gets or sets text wrapping style of the picture.  
  TextWrappingType      Gets or sets text wrapping type of the picture.  
  VerticalAlignment     Gets or sets picture vertical alignment.  
  VerticalOrigin        Gets or sets absolute horizontal position of the picture.
  VerticalPosition      Gets or sets text wrapping style of the picture.  
  Width                 Gets or sets picture width (in points).  .  
  WidthScale            Gets or sets picture width scale factor in percent.  
  --------------------- -----------------------------------------------------------


 

Public Methods

 


  ------------ ----------------------------------
  Name         Description
  AddCaption   Add Caption for current Picture.
  LoadImage    Loads image.
  ------------ ----------------------------------


 

The following screen shot illustrates the various layout formats available in MS Word.

 

{border="0"}

Figure 62: Layout Formats in MS Word

 

The following code illustrates how to use the **WPicture** class.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                               |
| [IWordDocument][ doc = [new] [WordDocument]();]                                                |
|                                                                                                                                                                                                                               |
| [IWSection][ section = doc.AddSection();]                                                                                                |
|                                                                                                                                                                                                                               |
| [IWParagraph][ paragraph = section.AddParagraph();]                                                                                      |
|                                                                                                                                                                                                                               |
| [paragraph.AppendText([\"First image\"]);]                                                                                                                         |
|                                                                                                                                                                                                                               |
| [IWPicture][ picture = paragraph.AppendPicture([new] [Bitmap](ImagesPath + DEF_IMAGE1_NAME));] |
|                                                                                                                                                                                                                               |
| [picture.HeightScale = 50f;]                                                                                                                                                              |
|                                                                                                                                                                                                                               |
| [picture.WidthScale = 50f;]                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [paragraph = section.AddParagraph();]                                                                                                                                                     |
|                                                                                                                                                                                                                               |
| [paragraph.AppendText([\"Second image\"]);]                                                                                                                        |
|                                                                                                                                                                                                                               |
| [picture = paragraph.AppendPicture([new] [Bitmap](ImagesPath + DEF_IMAGE2_NAME));]                                                              |
|                                                                                                                                                                                                                               |
| [picture.HeightScale = 50f;]                                                                                                                                                              |
|                                                                                                                                                                                                                               |
| [picture.WidthScale = 50f;]                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| []                                                                                                                                                                                        |
|                                                                                                                                                                                                                               |
| [section.HeadersFooters.OddHeader.Paragraphs.Add(paragraph);]                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [Dim][ doc [As] IWordDocument = [New] WordDocument()]                                                |
|                                                                                                                                                                                                                                     |
| [Dim][ section [As] IWSection = doc.AddSection()]                                                                         |
|                                                                                                                                                                                                                                     |
| [Dim][ paragraph [As] IWParagraph = section.AddParagraph()]                                                               |
|                                                                                                                                                                                                                                     |
| [paragraph.AppendText([\"First image\"])]                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [Dim][ picture [As] IWPicture = paragraph.AppendPicture([New] Bitmap(ImagesPath + DEF_IMAGE1_NAME))] |
|                                                                                                                                                                                                                                     |
| [picture.HeightScale = 50f]                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [picture.WidthScale = 50f]                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [paragraph = section.AddParagraph()]                                                                                                                                                            |
|                                                                                                                                                                                                                                     |
| [paragraph.AppendText([\"Second image\"])]                                                                                                                               |
|                                                                                                                                                                                                                                     |
| [picture = paragraph.AppendPicture([New] Bitmap(ImagesPath + DEF_IMAGE2_NAME))]                                                                                            |
|                                                                                                                                                                                                                                     |
| [picture.HeightScale = 50f]                                                                                                                                                                     |
|                                                                                                                                                                                                                                     |
| [picture.WidthScale = 50f]                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [section.HeadersFooters.OddHeader.Paragraphs.Add(paragraph)]                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

