---
title: automaticfields.md
original_path: WinForms_Docs/99_Uncategorized/automaticfields.md
created_at: 2025-08-05
---






##### Automatic Fields {#automatic-fields style="tab-stops: 0pt"}

[] 

Automatic Fields are special objects that display information calculated automatically, just before the document is saved.

 

The following are the fields displayed:

[] 

[·      ]Page number

[·      ]Count of pages

[·      ]Author of the document

[·      ]Creation and current date

[·      ]Other document information

[] 


{border="0"}Note: These fields are not always evaluated at the moment of constructing the document.


 

To display the correct value of the field, you should specify some important properties, which are listed below.

 

[·      ]**Font**-Used to display the value of the field. Exception is thrown, if this property is not set.

[·      ]**Brush**-Used to print the value of the field. Exception is thrown, if this property is not set.

[·      ]**Bounds**-Specifies the bounds of the field

 

You can also use the **Location** and **Size** properties to define the bounds of the field.

 

[·      ]**Location**: Represents the location of the field. Default point is (0, 0).

[·      ]**Size**: Represents the size of the field. If it is not set, the size of the field is automatically calculated to display the value.

[] 


{border="0"}Note: It is not necessary to set the Bounds and Size with Location at the same time. Size and Bounds.Size have the same values.


[] 

Numeric fields have an additional **NumberingStyle** property. There are five possible numbering styles supported by the automatic fields. They are as follows.

**[]** 

[·      ]Arabic (1, 2, 3, 4, \...)

[·      ]Upper Roman (I, II, III, IV, \...)

[·      ]Roman (i, ii, iii, iv, \...)

[·      ]Upper Latin (A, B, C, D, \..., Z, AA, AB, \...)

[·      ]Latin (a, b, c, d, \..., z, aa, ab, \...)

[] 

Brief descriptions on the various numbering fields are given below.

[] 

[·      ]**PdfPageNumberField** - Specifies the number of the page on which the field has been drawn

[·      ]**PdfPageCountField** - Specifies the total number of pages in the document

[·      ]**PdfSectionPageNumberField** - Specifies the number of pages within a section

[·      ]**PdfSectionPageCountField** - Specifies the number of sections in a document

[·      ]**PdfSectionNumberField** - Specifies the number of sections within a document

[·      ]**PdfCreationDateField** - Specifies the creation date of the document

 

The value is taken from the **DocumentInformation.CreationDate** property.

 

[·      ]**PdfDateTimeField** - Specifies the current date and time

[·      ]**PdfDestinationPageNumberField** - Specifies the number of the specified destination page

[·      ]**PdfCompositeField** - Specifies the value of the field that is composed of any number of other automatic fields

[] 

PdfCreationDateField and PdfDateTimeField have the **DateFormatString** property, which defines the formatting string for the value of the field. This property uses the same formatting rules and specifiers as DateTime type of .NET. For detailed information on formatting specifiers, see [[http://msdn2.microsoft.com/en-us/library/73ctwf33(VS.80).aspx]{.UGHyperlink}](http://msdn2.microsoft.com/en-us/library/73ctwf33(VS.80).aspx).

[] 

You can draw the Automatic Fields on the **PdfTemplate** and set them as the document template or manually draw them on the necessary pages. The values of the fields will be automatically populated on each copy of the template.

[] 

The following code example illustrates how to display page numbers.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [PdfDocument][ document = [new] [PdfDocument]();]                                                |
|                                                                                                                                                                                                                                 |
| [PdfPage][ page = document.Pages.Add();]                                                                                                   |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [PdfFont][ font = [new] [PdfStandardFont]([PdfFontFamily].Helvetica, 12f);] |
|                                                                                                                                                                                                                                 |
| [PdfBrush][ brush = [PdfBrushes].Black;]                                                                              |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [PdfPageNumberField][ pageNumber = [new] [PdfPageNumberField](font, brush);]                     |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [for][ ([int] i = 0; i \< 50; i++)]                                                                                   |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [page = document.Pages.Add();]                                                                                                                                                              |
|                                                                                                                                                                                                                                 |
| [pageNumber.Draw(page.Graphics);]                                                                                                                                                           |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                              |
|                                                                                                                                                                                                                   |
| [Dim][ document [As] PdfDocument = [New] PdfDocument()]                            |
|                                                                                                                                                                                                                   |
| [Dim][ page [As] PdfPage = document.Pages.Add()]                                                        |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [Dim][ font [As] PdfFont = [New] PdfStandardFont(PdfFontFamily.Helvetica, 12.0F)]  |
|                                                                                                                                                                                                                   |
| [Dim][ brush [As] PdfBrush = PdfBrushes.Black]                                                          |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [Dim][ pageNumber [As] PdfPageNumberField = [New] PdfPageNumberField(font, brush)] |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [For][ i [As] [Integer] = 0 [To] 49]                          |
|                                                                                                                                                                                                                   |
| [  page = document.Pages.Add()]                                                                                                                                               |
|                                                                                                                                                                                                                   |
| [  pageNumber.Draw(page.Graphics)]                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [Next][ i]                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following code example illustrates how to use a composite field.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                                 |
| [PdfDocument][ document = [new] [PdfDocument]();]                                                |
|                                                                                                                                                                                                                                 |
| [PdfPage][ page = document.Pages.Add();]                                                                                                   |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [PdfFont][ font = [new] [PdfStandardFont]([PdfFontFamily].Helvetica, 12f);] |
|                                                                                                                                                                                                                                 |
| [PdfBrush][ brush = [PdfBrushes].Black;]                                                                              |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [PdfCompositeField][ compositeField = [new] [PdfCompositeField](font, brush);]                   |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [for][ ([int] i = 0; i \< 50; i++)]                                                                                   |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [PdfPage][ page = document.Pages.Add();]                                                                                                   |
|                                                                                                                                                                                                                                 |
| [compositeField.Draw(page.Graphics);]                                                                                                                                                       |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                   |
| **[]**                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [Dim][ document [As] PdfDocument = [New] PdfDocument()]                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [Dim][ page [As] PdfPage = document.Pages.Add()]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [Dim][ font [As] PdfFont = [New] PdfStandardFont(PdfFontFamily.Helvetica, 12.0F)]                                                                                  |
|                                                                                                                                                                                                                                                                                                   |
| [Dim][ brush [As] PdfBrush = PdfBrushes.Black]                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [Dim][ [compositeField] [As] [PdfCompositeField] = [New] [PdfCompositeField](font, brush)] |
|                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                   |
| [For][ i [As] [Integer] = 0 [To] 49]                                                                                                          |
|                                                                                                                                                                                                                                                                                                   |
| [Dim][ page [As] PdfPage = document.Pages.Add()]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                   |
| [  [compositeField].Draw(page.Graphics)]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                   |
| [Next][ i]                                                                                                                                                                                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

When an automatic field is used as a component of the composite field, it is not necessary to specify its Font, Brush and Bounds properties. Just call its constructor without parameters.

[] 


{border="0"}Note: You must specify the preceding properties for the composite field.


[] 

The following code example illustrates how to use automatic fields in templates.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                  |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [PdfDocument][ document = [new] [PdfDocument]();]                                                |
|                                                                                                                                                                                                                                 |
| [PdfPage][ page = document.Pages.Add();]                                                                                                   |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [PdfFont][ font = [new] [PdfStandardFont]([PdfFontFamily].Helvetica, 12f);] |
|                                                                                                                                                                                                                                 |
| [PdfBrush][ brush = [PdfBrushes].Black;]                                                                              |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [PdfTemplate][ template = [new] [PdfTemplate](15, 15);]                                          |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [PdfDateTimeField][ dateField = [new] [PdfDateTimeField](font, brush);]                          |
|                                                                                                                                                                                                                                 |
| [dateField.DateFormatString = [\"dd\'/\'MMMM\'/\'yyyy\"];]                                                                                                           |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [dateField.Draw(template.Graphics);]                                                                                                                                                        |
|                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                          |
|                                                                                                                                                                                                                                 |
| [for][ ([int] i = 0; i \< 50; i++)]                                                                                   |
|                                                                                                                                                                                                                                 |
| [{]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                 |
| [PdfPage][ page = document.Pages.Add();]                                                                                                   |
|                                                                                                                                                                                                                                 |
| [page.Graphics.DrawPdfTemplate(template, [new] [Point](50, 50));]                                                                                 |
|                                                                                                                                                                                                                                 |
| [}]                                                                                                                                                                                         |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                               |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [Dim][ document [As] PdfDocument = [New] PdfDocument()]                           |
|                                                                                                                                                                                                                  |
| [Dim][ page [As] PdfPage = document.Pages.Add()]                                                       |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ font [As] PdfFont = [New] PdfStandardFont(PdfFontFamily.Helvetica, 12.0F)] |
|                                                                                                                                                                                                                  |
| [Dim][ brush [As] PdfBrush = PdfBrushes.Black]                                                         |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ template [As] PdfTemplate = [New] PdfTemplate(15, 15)]                     |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ dateField [As] PdfDateTimeField = [New] PdfDateTimeField(font, brush)]     |
|                                                                                                                                                                                                                  |
| [Dim][ dateField.DateFormatString = [\"dd\'/\'MMMM\'/\'yyyy\"]]                                      |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                  |
| [dateField.Draw(template.Graphics)]                                                                                                                                          |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [For][ i [As] [Integer] = 0 [To] 49]                         |
|                                                                                                                                                                                                                  |
| [Dim][ page [As] PdfPage = document.Pages.Add()]                                                       |
|                                                                                                                                                                                                                  |
| [page.Graphics.DrawPdfTemplate(template, [New] Point(50, 50))]                                                                                          |
|                                                                                                                                                                                                                  |
| [Next][ i]                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

 

[]{#related-topics}

