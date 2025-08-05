---
title: xpstopdf.md
original_path: WinForms_Docs/99_Uncategorized/xpstopdf.md
created_at: 2025-08-05
---








  









### XPS to PDF {#xps-to-pdf style="tab-stops: 0pt"}

An XPS (XML Paper Specification) document, standardized by Ecma International, can be now converted to PDF.

The XPS document format consists of XML structured markup that defines the layout of a document and the visual appearance of each page, along with rendering rules for distributing, archiving, rendering, processing, and printing the documents. Similar to PDF, XPS is also a fixed-layout document format which helps to preserve document fidelity and to achieve device-independent document appearance.

 

XPS documents can be converted to PDF using the **Convert** method of the **XPSToPdfConverter** class.

{border="0"}***Note: You need to add the Syncfusion.XPS namespace to work with the XPSToPdfConverter class.***

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]][]**                                                |
|                                                                                                                                                                                                               |
| [public][ [PdfDocument] Convert([byte\[\]] file);]                          |
|                                                                                                                                                                                                               |
| [public][ [PdfDocument] Convert([string] fileName);]                        |
|                                                                                                                                                                                                               |
| [public][ [PdfDocument] Convert([Stream] file);][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]][]** |
|                                                                                                                                                                    |
| [public][ PdfDocument Convert([byte\[\]] file)]          |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [public][ PdfDocument Convert([String] fileName)]        |
|                                                                                                                                                                    |
| []                                                                                                                             |
|                                                                                                                                                                    |
| [public][ PdfDocument Convert([Stream] file)]            |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

An XPS document can be converted to PDF using the following code snippet:

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                     |
| [// Create converter class.]                                                                                                                      |
|                                                                                                                                                                                                     |
| [XPSToPdfConverter][ converter = [new] [XPSToPdfConverter]();] |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [// Convert the XPS to PDF]                                                                                                                       |
|                                                                                                                                                                                                     |
| [PdfDocument][ document = converter.Convert(fileName);]                                                     |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [// Save and close the document]                                                                                                                  |
|                                                                                                                                                                                                     |
| [document.Save([\"Sample.pdf\"]);]                                                                                                      |
|                                                                                                                                                                                                     |
| [document.Close([true]);]                                                                                                                  |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                            |
|                                                                                                                                                                                 |
| [\' Create converter class.][]                                                            |
|                                                                                                                                                                                 |
| [Dim][ converter [As] [New] XPSToPdfConverter()] |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [\' Convert the XPS to PDF][]                                                             |
|                                                                                                                                                                                 |
| [Dim][ document [As] PdfDocument = converter.Convert(fileName)]       |
|                                                                                                                                                                                 |
| []                                                                                                                                          |
|                                                                                                                                                                                 |
| [\' Save and close the document][]                                                        |
|                                                                                                                                                                                 |
| [document.Save([\"Sample.pdf\"])]                                                                                   |
|                                                                                                                                                                                 |
| [document.Close([True])]                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Supported Elements


  ---------------------------- ----------------
  Element                      Convert to PDF
  ArcSegment                   Yes
  Canvas                       Yes
  DocumentOutline              No
  DocumentReference            No
  FigureStructure              No
  FixedPageResources           Yes
  Glyphs                       Yes
  Gradient                     Yes
  ImageBrush                   Yes
  Intent                       Yes
  LinkTarget                   Yes
  ListItemStructure            Yes
  ListStructure                Yes
  MatrixTransform              Yes
  NamedElement                 No
  OutlineEntry                 No
  PageContent                  Yes
  PageContentLinkTargets       No
  ParagraphStructure           No
  Path                         Yes
  PolyBezierSegment            Yes
  PolyLineSegment              Yes
  PolyQuadraticBezierSegment   Yes
  ResourceDictionary           Yes
  SectionStructure             No
  SignBy                       No
  SignatureDefinition          No
  SignatureDefinitions         No
  SigningLocation              No
  SolidColorBrush              Yes
  SpotLocation                 No
  Story                        No
  TableStructure               No
  VisualBrush                  No
  ---------------------------- ----------------


 

[]{#related-topics}

