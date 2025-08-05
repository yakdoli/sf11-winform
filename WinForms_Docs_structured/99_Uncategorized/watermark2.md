---
title: watermark2.md
original_path: WinForms_Docs/99_Uncategorized/watermark2.md
created_at: 2025-08-05
---






#### Watermark {#watermark style="tab-stops: 0pt"}

 

**Watermark** class represents printed watermark in the Word document.

 

To insert a watermark into the Word document, open the **Format** menu, point to **Background**, and then click **Printed Watermark**. There are two types of watermarks.

 

[·      ]Picture Watermark

[·      ]Text Watermark

 

The type of watermark is defined by using the **Type** property. This property returns the object of type, WatermarkType. It includes the following options.

 

[·      ]**NoWatermark**: document does not have watermark

[·      ]**PictureWatermark**: document has picture watermark

[·      ]**TextWatermark**: document has text watermark

 

You can create a Picture Watermark or Text Watermark, but you cannot create an object of the Watermark class.

 

Watermark is a paragraph item. It is found in the first paragraph of the header / footer subdocument. DocIO Watermark is accessible through the **WordDocument.Watermark** property.

 

**Class Hierarchy**

 

ParagraphItem

            \|

            Watermark

 

**Public Properties**

 


  ------------ ----------------------------------
  **Name**     **Description**
  EntityType   Gets the type of the entity.  
  Type         Gets or sets the watermark type.
  ------------ ----------------------------------


 

**Picture Watermark**

 

**PictureWatermark** class represents the picture watermark in the Word document.

 

{border="0"}

Figure 29: Selecting Picture Watermark in Printed Watermark Dialog Box

 

**Picture** property defines the picture to be used as the watermark. **Scaling** property defines the watermark scaling (in percents). **Washout** property defines whether the washout effect is to be applied to the watermark. Default value for **Washout** property is set to **True**.

 

**Class Hierarchy**

 

ParagraphItem

            \|

            Watermark

                        \|

                                 PictureWatermark

 

**Public Constructors**

 


  ------------------------------------------------ -------------------------------------------------------------
  Name                                             Description
  PictureWatermark.PictureWatermark()              Initializes a new instance of the PictureWatermark class.  
  PictureWatermark.PictureWatermark(Image, bool)   Initializes a new instance of the PictureWatermark class.
  ------------------------------------------------ -------------------------------------------------------------


 

Public Properties

 


  ------------ --------------------------------------------------------
  Name         Description
  EntityType   Gets the type of the entity.  
  Picture      Gets or sets picture for Picture watermark.  
  Scaling      Gets or sets picture scaling in percents.  
  Washout      Gets or sets Washout property for Picture watermark.  
  ------------ --------------------------------------------------------


 

The following example illustrates how to use the PictureWatermark class.                       

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                 |
|                                                                                                                                                                                                |
| []                                                                                                                                                                       |
|                                                                                                                                                                                                |
| [IWordDocument][ doc = [new] [WordDocument]();]                 |
|                                                                                                                                                                                                |
| [doc.EnsureMinimal();]                                                                                                                                     |
|                                                                                                                                                                                                |
| [PictureWatermark][ picWatermark = [new] [PictureWatermark]();] |
|                                                                                                                                                                                                |
| [picWatermark.Scaling = 120f;]                                                                                                                             |
|                                                                                                                                                                                                |
| [picWatermark.Washout = [true];]                                                                                                      |
|                                                                                                                                                                                                |
| [doc.Watermark = picWatermark;]                                                                                                                            |
|                                                                                                                                                                                                |
| [picWatermark.Picture = [Image].FromFile(ImagesPath + [\"Water lilies.jpg\"]);]                                |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                   |
|                                                                                                                                                                                                      |
| []                                                                                                                                                                             |
|                                                                                                                                                                                                      |
| [Dim][ doc [As] IWordDocument = [New] WordDocument()]                 |
|                                                                                                                                                                                                      |
| [doc.EnsureMinimal()]                                                                                                                                            |
|                                                                                                                                                                                                      |
| [Dim][ picWatermark [As] PictureWatermark = [New] PictureWatermark()] |
|                                                                                                                                                                                                      |
| [picWatermark.Scaling = 120f]                                                                                                                                    |
|                                                                                                                                                                                                      |
| [picWatermark.Washout = [True]]                                                                                                             |
|                                                                                                                                                                                                      |
| [doc.Watermark = picWatermark]                                                                                                                                   |
|                                                                                                                                                                                                      |
| [picWatermark.Picture = Image.FromFile(ImagesPath & [\"Water lilies.jpg\"])]                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Text Watermark**

 

**TextWatermark** class represents the text watermark in the Word document. The following screen shot illustrates the Text Watermark settings.

 

{border="0"}

Figure 30: Selecting Text Watermark in Printed Watermark Dialog Box

 

**Text** property defines the text of the Text Watermark. **FontName** property defines the name of the text font. Default font name is **Times New Roman**. **Size** property defines the font size. Default font size is **36**. **Color** property defines the color of the text (font). Default font color is **Color.Gray**. **Semitransparent** property defines whether the text watermark is semi-transparent. Default value for this property is set to **True**.

 

**Layout** property defines the layout for the watermark.

 

[·      ]**Diagonal**: diagonal watermark layout

[·      ]**Horizontal**: horizontal watermark layout

 

Layout property returns the value of the **WatermarkLayout** type. Default layout is **Diagonal**.

 

**Class Hierarchy**

 

ParagraphItem

            \|

            Watermark

                        \|

                                TextWatermark

 

**Public Properties**

 


  -------------------------------------------------------------------- --------------------------------------------------------
  Name                                                                 Description
  TextWatermark.TextWatermark ()                                       Initializes a new instance of the TextWatermark class.
  TextWatermark.TextWatermark (string)                                 Initializes a new instance of the TextWatermark class.
  TextWatermark.TextWatermark (string, string, int, WatermarkLayout)   Initializes a new instance of the TextWatermark class.
  -------------------------------------------------------------------- --------------------------------------------------------


 

Public Properties

 


  ----------------- -----------------------------------------------------------
  Name              Description
  Color             Gets or sets text watermark color.  
  EntityType        Gets the type of the entity.  
  FontName          Gets or sets watermark text\'s font name.  
  Layout            Gets or sets layout for Text watermark.  
  Semitransparent   Gets or sets semitransparent property for Text watermark.
  Size              Gets or sets the text watermark size (in points).
  Text              Gets or sets watermark text.
  ----------------- -----------------------------------------------------------


 

The following example illustrates how to use the TextWatermark class.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                                  |
|                                                                                                                                                                                           |
| [IWordDocument][ doc = [new] [WordDocument]();]            |
|                                                                                                                                                                                           |
| [doc.EnsureMinimal();]                                                                                                                                |
|                                                                                                                                                                                           |
| [TextWatermark][ textWatermark = [new] [TextWatermark]();] |
|                                                                                                                                                                                           |
| [doc.Watermark = textWatermark;]                                                                                                                      |
|                                                                                                                                                                                           |
| [textWatermark.Size = 96;]                                                                                                                            |
|                                                                                                                                                                                           |
| [textWatermark.Layout = [WatermarkLayout].Horizontal;]                                                                           |
|                                                                                                                                                                                           |
| [textWatermark.Semitransparent = [false];]                                                                                       |
|                                                                                                                                                                                           |
| [textWatermark.Color = [Color].Black;]                                                                                           |
|                                                                                                                                                                                           |
| [textWatermark.Text = [\"TextWatermark\"]; ]                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                              |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
|                                                                                                                                                                                                 |
| [Dim][ doc [As] IWordDocument = [New] WordDocument()]            |
|                                                                                                                                                                                                 |
| [doc.EnsureMinimal()]                                                                                                                                       |
|                                                                                                                                                                                                 |
| [Dim][ textWatermark [As] TextWatermark = [New] TextWatermark()] |
|                                                                                                                                                                                                 |
| [doc.Watermark = textWatermark]                                                                                                                             |
|                                                                                                                                                                                                 |
| [textWatermark.Size = 96]                                                                                                                                   |
|                                                                                                                                                                                                 |
| [textWatermark.Layout = WatermarkLayout.Horizontal]                                                                                                         |
|                                                                                                                                                                                                 |
| [textWatermark.Semitransparent = [False]]                                                                                              |
|                                                                                                                                                                                                 |
| [textWatermark.Color = Color.Black]                                                                                                                         |
|                                                                                                                                                                                                 |
| [textWatermark.Text = [\"TextWatermark\"]]                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#related-topics}

