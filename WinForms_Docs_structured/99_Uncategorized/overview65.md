---
title: overview65.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\overview65.md
created_at: 2025-07-03
---








  









### Overview {#overview style="tab-stops: 0pt"}

 

AcroForms are the PDF files that contain form fields. Data can be entered into these fields by the end-user or the author of the form. Internally, AcroForms are annotations or fields applied to a PDF document. While loading an existing document, the AcroForm is also loaded if available.

 

Creating Form

 

The loaded form is represented by the **PdfLoadedForm** class. It is accessed by using the **Form** property of the **PdfLoadedDocument** class. If the document does not contain an AcroForm, you can create it by using the **CreateForm** method of the PdfLoadedDocument class.

 

The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [// Loading Existing Document]                                                                                                                                          |
|                                                                                                                                                                                                                           |
| [PdfLoadedDocument][ loadedDoc = [new] [PdfLoadedDocument](filename);]                     |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [// Creates a form            ]                                                                                                                                         |
|                                                                                                                                                                                                                           |
| [loadedDoc.CreateForm();]                                                                                                                                                             |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [// Adding a new Page]                                                                                                                                                  |
|                                                                                                                                                                                                                           |
| [PdfPageBase][ page = loadedDoc.Pages.Add();]                                                                                        |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [// Creating a new Field]                                                                                                                                               |
|                                                                                                                                                                                                                           |
| [PdfButtonField][ bt = [new] [PdfButtonField](page, [\"Submit\"]);] |
|                                                                                                                                                                                                                           |
| [bt.Bounds = [new] [RectangleF](0, 0, 100, 100);]                                                                                           |
|                                                                                                                                                                                                                           |
| [bt.Text = [\"Submit\"];]                                                                                                                                      |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [// Adding the Field]                                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [loadedDoc.Form.Fields.Add(bt);]                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                              |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\' Loading Existing Document]                                                                                                                            |
|                                                                                                                                                                                                             |
| [Dim][ loadedDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(filename)] |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\' Creates a form            ]                                                                                                                           |
|                                                                                                                                                                                                             |
| [loadedDoc.CreateForm()]                                                                                                                                                |
|                                                                                                                                                                                                             |
| []                                                                                                                                                        |
|                                                                                                                                                                                                             |
| [\' Adding a new Page]                                                                                                                                    |
|                                                                                                                                                                                                             |
| [Dim][ page [As] PdfPageBase = loadedDoc.Pages.Add()]                                             |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\' Creating a new Field]                                                                                                                                 |
|                                                                                                                                                                                                             |
| [Dim][ bt [As] PdfButtonField = [New] PdfButtonField(page, \"SumBit\")]      |
|                                                                                                                                                                                                             |
| [bt.Bounds = [New] RectangleF(0, 0, 100, 100)]                                                                                                     |
|                                                                                                                                                                                                             |
| [bt.Text = \"Submit\"]                                                                                                                                                  |
|                                                                                                                                                                                                             |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                             |
| [\' Adding the Field]                                                                                                                                     |
|                                                                                                                                                                                                             |
| [loadedDoc.Form.Fields.Add(bt)]                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Accessing Form**

 

**PdfLoadedForm** class contains the collection of loaded fields represented by the **PdfLoadedFormFieldCollection** class, and inherited from the **PdfFieldCollection** class. The base class for each loaded field is represented by the **PdfLoadedField** class, and inherited from the **PdfField** class.

 

You can change the form\'s properties, add new fields or remove the existing fields.

 

The following code example illustrates how to use a loaded form.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                                     |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](filename);]                                   |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [PdfLoadedForm][ form = ldDoc.Form;]                                                                                                           |
|                                                                                                                                                                                                                                     |
| [PdfPage][ page = ldDoc.Pages.Add() [as] [PdfPage];]                                                 |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [PdfTextBoxField][ textField = [new] [PdfTextBoxField](page, [\"textBox\"]);] |
|                                                                                                                                                                                                                                     |
| [textField.Bounds = [new] [RectangleF](0, 0, 100, 100);]                                                                                              |
|                                                                                                                                                                                                                                     |
| [textField.Text = [\"New text field\"];]                                                                                                                                 |
|                                                                                                                                                                                                                                     |
| [form.Fields.Add(textField);]                                                                                                                                                                   |
|                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                              |
|                                                                                                                                                                                                                                     |
| [ldDoc.Save(newFileName);]                                                                                                                                                                      |
|                                                                                                                                                                                                                                     |
| [ldDoc.Close();]                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                   |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                             |
|                                                                                                                                                                                                                  |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(filename)]          |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ form [As] PdfLoadedForm = ldDoc.Form]                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ page [As] PdfPage = TryCast(ldDoc.Pages.Add(), PdfPage)]                                        |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [Dim][ textField [As] PdfTextBoxField = [New] PdfTextBoxField(page, \"textBox\")] |
|                                                                                                                                                                                                                  |
| [textField.Bounds = [New] RectangleF(0, 0, 100, 100)]                                                                                                   |
|                                                                                                                                                                                                                  |
| [textField.Text = \"New text field\"]                                                                                                                                        |
|                                                                                                                                                                                                                  |
| [form.Fields.Add(textField)]                                                                                                                                                 |
|                                                                                                                                                                                                                  |
| []                                                                                                                                                                           |
|                                                                                                                                                                                                                  |
| [ldDoc.Save(newFileName)]                                                                                                                                                    |
|                                                                                                                                                                                                                  |
| [ldDoc.Close()]                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Flattening

[] 

[The library enables to flatten the loaded field by using the Flatten property of the PdfLoadedField class. A particular field or the whole form can be flattened using this class. The following code snippet illustrates this.]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| []                                                                                                                                                    |
|                                                                                                                                                                                                         |
| [//For Whole form flattening]                                                                                                                         |
|                                                                                                                                                                                                         |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](filename);] |
|                                                                                                                                                                                                         |
| [PdfLoadedForm][ form = ldDoc.Form;]                                                                            |
|                                                                                                                                                                                                         |
| [form.Flatten = [true];]                                                                                                                       |
|                                                                                                                                                                                                         |
| [ldDoc.Save(newFileName);]                                                                                                                                          |
|                                                                                                                                                                                                         |
| [ldDoc.Close(); ]                                                                                                                                                   |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [//Flattening the first field]                                                                                                                        |
|                                                                                                                                                                                                         |
| [form.Fields\[0\].Flatten = [true];]                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                  |
|                                                                                                                                                                                     |
| []                                                                                                                                |
|                                                                                                                                                                                     |
| [\'For Whole form flattening]                                                                                                     |
|                                                                                                                                                                                     |
| [Dim][ ldDoc [As] [New] PdfLoadedDocument(filename)] |
|                                                                                                                                                                                     |
| [Dim][ form [As] PdfLoadedForm = ldDoc.Form]                              |
|                                                                                                                                                                                     |
| [form.Flatten = [True]]                                                                                                    |
|                                                                                                                                                                                     |
| [ldDoc.Save(newFileName)]                                                                                                                       |
|                                                                                                                                                                                     |
| [ldDoc.Close()]                                                                                                                                 |
|                                                                                                                                                                                     |
| []                                                                                                                                              |
|                                                                                                                                                                                     |
| [\'Flattening the first field]                                                                                                    |
|                                                                                                                                                                                     |
| [form.Fields(0).Flatten = [True]]                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Disable AutoFormat

This property allows you to disable the formatting applied to form fields.  Formats can be disabled for either selected fields or for the complete form.

 

Use Case Scenarios

This property helps when filling fields in different cultures. For example, a currency text field might get a number as an input in different formats, based on the culture in use. If it is preset with a culture that may affect other culture inputs, this property will help to remove it and set the input text with the new formatting.

 

Adding Disable AutoFormat to an Application

Adding the Disable AutoFormat feature to the application is described in the following code snippets:

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| [// Disable format for the selected field]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [PdfLoadedTextBoxField][ field = loadedDocument.Form.Fields\[[\"Price\"]\] [as] [PdfLoadedTextBoxField];] |
|                                                                                                                                                                                                                                                                        |
| [field.Text = [\"\$1,000.23\"];]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| [field.DisableAutoFormat = [true];]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                        |
| [// Disable format for all fields in the form]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                        |
| [loadedDocument.Form.DisableAutoFormat = [true];]                                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                      |
| [\' Disable format for the selected field]                                                                                                                                                         |
|                                                                                                                                                                                                                                                      |
| [Dim][ field [As] PdfLoadedTextBoxField = TryCast(loadedDocument.Form.Fields([\"Price\"]), PdfLoadedTextBoxField)] |
|                                                                                                                                                                                                                                                      |
| [field.Text = [\"\$1,000.23\"]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                      |
| [field.DisableAutoFormat = [True]]                                                                                                                                                          |
|                                                                                                                                                                                                                                                      |
| [\' Disable format for all fields in the form][]                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [loadedDocument.Form.DisableAutoFormat = [True]]                                                                                                                                            |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: XFA Form is currently supported with the following limitations:


[·      ]User rights will not be preserved

[·      ]Only XFA static forms are supported

[] 

Modifying loaded form actions

 

Essential PDF provides support for modifying the various actions of the loaded forms. The following code example illustrates this.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                |
| [//Load the Document.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                |
| [PdfLoadedDocument][ ldoc1 = [new] [PdfLoadedDocument]([\"Form_Action.pdf\"]);]          |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [//Create a PdfLodedForm.]                                                                                                                                                                   |
|                                                                                                                                                                                                                                                |
| [PdfLoadedForm][ form = ldoc1.Form;]                                                                                                                      |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [PdfJavaScriptAction javaAction1 = [new] PdfJavaScriptAction([\"app.alert(\\\"You are looking at Java script action of PDF (PdfLoadedCheckBoxField)\\\")\"]);] |
|                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                |
| [(form.Fields\[[\".NET\"]\] [as] [PdfLoadedCheckBoxField]).LostFocus = javaAction1;]                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[][VB.NET[\]]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [\'Load the Document.]                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                          |
| [Dim][ ldoc1 [As] [New] PdfLoadedDocument([\"Form_Action.pdf\"])]                                                                                  |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [\'Create a PdfLodedForm.]                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                          |
| [Dim][ form [As] PdfLoadedForm = ldoc1.Form]                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [Dim][ javaAction1 [As] [New] PdfJavaScriptAction([\"app.alert(\"\"You are looking at Java script action of PDF (PdfLoadedCheckBoxField)\"\")\"])] |
|                                                                                                                                                                                                                                                                                                          |
| []                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                          |
| [TryCast][(form.Fields([\".NET\"]), PdfLoadedCheckBoxField).LostFocus = javaAction1]                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 

[]{#related-topics}

