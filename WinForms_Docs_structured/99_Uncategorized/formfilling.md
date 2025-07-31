---
title: formfilling.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\formfilling.md
created_at: 2025-07-03
---








  









### Form Filling {#form-filling style="tab-stops: 0pt"}

 

Essential PDF provides support to fill AcroForm fields. You can fill the form field value either by using its field name or field index.

 

The following code example illustrates how to fill various loaded fields by using Essential PDF.

 

**Filling the Text Box Field**

 

The following code illustrates how to fill the Text Box Field.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                    |
|                                                                                                                                                                                                                   |
| []                                                                                                                                                                            |
|                                                                                                                                                                                                                   |
| [PdfLoadedTextBoxField][ ldField = form.Fields\[0\] [as] [PdfLoadedTextBoxField];] |
|                                                                                                                                                                                                                   |
| [RectangleF][ newBounds = [new] [RectangleF](100, 100, 50, 50);]                   |
|                                                                                                                                                                                                                   |
| [ldField.Bounds = newBounds;]                                                                                                                                                 |
|                                                                                                                                                                                                                   |
| [ldField.SpellCheck = [true];]                                                                                                                           |
|                                                                                                                                                                                                                   |
| [ldField.Text = [\"New text of the field.\"];]                                                                                                         |
|                                                                                                                                                                                                                   |
| [ldField.Password = [false];]                                                                                                                            |
|                                                                                                                                                                                                                   |
| [ldField.BorderStyle = [PdfBorderStyle].Dashed;]                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [Dim][ ldField [As] PdfLoadedTextBoxField = form.Fields( 0 ) [as] PdfLoadedTextBoxField ] |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [Dim][ NewBounds [As] RectangleF = [New] RectangleF(100, 100, 50, 50)]                    |
|                                                                                                                                                                                                                          |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [ldField.Bounds = NewBounds ]                                                                                                                                                        |
|                                                                                                                                                                                                                          |
| [ldField.SpellCheck = [True] ]                                                                                                                                  |
|                                                                                                                                                                                                                          |
| [ldField.Text = [\"New text of the field.\"] ]                                                                                                                |
|                                                                                                                                                                                                                          |
| [ldField.Password = [False] ]                                                                                                                                   |
|                                                                                                                                                                                                                          |
| [ldField.BorderStyle = PdfBorderStyle.Dashed]                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

**Formatting the text box**

 

The following table lists some of the properties of the TextBoxField.

 


+-----------------------------------+-----------------------------------------------------------------------------------------+
| TextBoxField Property             | Description                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BackColor                         | Gets or sets the back color of the field.                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderColor                       | Gets or sets the border color for the field.                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| BorderStyle                       | Gets or sets the border style for the field.                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| Border                            | Gets or sets the width of the field border.                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ForeColor                         | Gets or sets the fore color for the field.                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| HighlightMode                     | Gets or sets the highlight mode of the field. It includes the following options.        |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | *Invert*                                                                                |
|                                   |                                                                                         |
|                                   | *Outline*                                                                               |
|                                   |                                                                                         |
|                                   | *Push*                                                                                  |
|                                   |                                                                                         |
|                                   | *NoHighlighting*                                                                        |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| TextAlignment                     | Gets or sets the alignment of the text in the field. It includes the following options. |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   |                                                                                         |
|                                   | *Center*                                                                                |
|                                   |                                                                                         |
|                                   | *Left*                                                                                  |
|                                   |                                                                                         |
|                                   | *Right*                                                                                 |
|                                   |                                                                                         |
|                                   | *Justify*                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------+


[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [PdfLoadedTextBoxField][ txt = frm.Fields\[i\] [as] [PdfLoadedTextBoxField];]          |
|                                                                                                                                                                                                                       |
| [txt.BorderColor = [Color].SteelBlue;]                                                                                                                       |
|                                                                                                                                                                                                                       |
| [txt.BorderStyle = [PdfBorderStyle].Solid;]                                                                                                                  |
|                                                                                                                                                                                                                       |
| [txt.BorderWidth = 1;]                                                                                                                                                            |
|                                                                                                                                                                                                                       |
| [txt.BackColor = [new] [PdfColor]([Color].AliceBlue );]                                                            |
|                                                                                                                                                                                                                       |
| [txt.ForeColor = [new] [PdfColor]([Color].Navy );]                                                                 |
|                                                                                                                                                                                                                       |
| [txt.HighlightMode = [PdfHighlightMode].Invert;]                                                                                                             |
|                                                                                                                                                                                                                       |
| [txt.TextAlignment = [PdfTextAlignment].Right;]                                                                                                              |
|                                                                                                                                                                                                                       |
| [Font][ f = [new] [Font]([\"Arial\"], 18f);]                    |
|                                                                                                                                                                                                                       |
| [PdfTrueTypeFont][ txtfnt = [new] [PdfTrueTypeFont](f, [false]);] |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [txt.Font = txtfnt;]                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                      |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [Dim][ txt [As] PdfLoadedTextBoxField = [TryCast](frm.Fields(i), PdfLoadedTextBoxField)] |
|                                                                                                                                                                                                                         |
| [txt.BorderColor = Color.SteelBlue]                                                                                                                                                 |
|                                                                                                                                                                                                                         |
| [txt.BorderStyle = PdfBorderStyle.Solid]                                                                                                                              |
|                                                                                                                                                                                                                         |
| [txt.BorderWidth = 1]                                                                                                                                                               |
|                                                                                                                                                                                                                         |
| [txt.BackColor = [New] PdfColor(Color.AliceBlue)]                                                                                                              |
|                                                                                                                                                                                                                         |
| [txt.ForeColor = [New] PdfColor(Color.Navy)]                                                                                                                   |
|                                                                                                                                                                                                                         |
| [txt.HighlightMode = PdfHighlightMode.Invert]                                                                                                                                       |
|                                                                                                                                                                                                                         |
| [txt.TextAlignment = PdfTextAlignment.Right]                                                                                                                                        |
|                                                                                                                                                                                                                         |
| [Dim][ f [As] [New] Font([\"Arial\"], 18.0F)]                     |
|                                                                                                                                                                                                                         |
| [Dim][ txtfnt [As] [New] PdfTrueTypeFont(f, [False])]               |
|                                                                                                                                                                                                                         |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                         |
| [txt.Font = txtfnt]                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 62: BorderColor = \"SteelBlue\"; BorderStyle = \"Solid\"; BorderWidth = \"1\"; BackColor = \"AliceBlue\"; ForeColor = \"Navy\"

[] 

Filling the Combo Box Field

 

The following code illustrates how to fill the ComboBox Field.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                              |
| []                                                                                                                                                       |
|                                                                                                                                                                                              |
| [//fill combo box]                                                                                                                         |
|                                                                                                                                                                                              |
| [PdfLoadedComboBoxField][ combo = ([PdfLoadedComboBoxField])doc.Form.Fields\[1\];] |
|                                                                                                                                                                                              |
| [combo.SelectedIndex = 3;]                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                             |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [\'fill combo box]                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| [Dim][ combo [As] PdfLoadedComboBoxField = [CType](doc.Form.Fields(1), PdfLoadedComboBoxField)] |
|                                                                                                                                                                                                                                |
| [combo.SelectedIndex = 3]                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Filling the Radio Button Field

 

The following code illustrates how to fill the Radio Button Field.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                             |
|                                                                                                                                                                                                            |
| []                                                                                                                                                                     |
|                                                                                                                                                                                                            |
| [//Fill radio button]                                                                                                                                    |
|                                                                                                                                                                                                            |
| [PdfLoadedRadioButtonListField][ radio = ([PdfLoadedRadioButtonListField])doc.Form.Fields\[2\];] |
|                                                                                                                                                                                                            |
| [radio.SelectedIndex = 1;]                                                                                                                                             |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                              |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                              |
| [\'Fill radio button]                                                                                                                                                                      |
|                                                                                                                                                                                                                                              |
| [Dim][ radio [As] PdfLoadedRadioButtonListField = [CType](doc.Form.Fields(2), PdfLoadedRadioButtonListField)] |
|                                                                                                                                                                                                                                              |
| [radio.SelectedIndex = 1]                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Filling the List Box Field

 

The following code illustrates how to fill the List Box Field.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                            |
|                                                                                                                                                                                           |
| []                                                                                                                                                    |
|                                                                                                                                                                                           |
| [//fill list box]                                                                                                                       |
|                                                                                                                                                                                           |
| [PdfLoadedListBoxField][ list = ([PdfLoadedListBoxField])doc.Form.Fields\[3\];] |
|                                                                                                                                                                                           |
| [list.SelectedIndex = 2;]                                                                                                                             |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'fill list box]                                                                                                                                                         |
|                                                                                                                                                                                                                             |
| [Dim][ list [As] PdfLoadedListBoxField = [CType](doc.Form.Fields(3), PdfLoadedListBoxField)] |
|                                                                                                                                                                                                                             |
| [list.SelectedIndex = 2]                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Filling the Check Box Field

 

The following code illustrates how to fill the Check Box Field.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                                |
|                                                                                                                                                                                                                       |
| [//Fill check box]                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [PdfLoadedCheckBoxField][ loadField = form.Fields\[4\] [as] [PdfLoadedCheckBoxField];] |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [//Check the first item in the checkbox group]                                                                                                                      |
|                                                                                                                                                                                                                       |
| [loadField.Items\[0\].Checked = [true];]                                                                                                                     |
|                                                                                                                                                                                                                       |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                                       |
| [//check the checkbox if it is not grouped.]                                                                                                                        |
|                                                                                                                                                                                                                       |
| [loadField.Checked = [true];]                                                                                                                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                          |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                                      |
|                                                                                                                                                                                                                             |
| [\'Fill check box]                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [Dim][ loadField [As] PdfLoadedCheckBoxField =  form.Fields(4) [as] PdfLoadedCheckBoxField ] |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [\'Check the first item in the checkbox group]                                                                                                                            |
|                                                                                                                                                                                                                             |
| [loadField.Items(0).Checked = [True]]                                                                                                                              |
|                                                                                                                                                                                                                             |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                                             |
| [\'check the checkbox if it is not grouped.]                                                                                                                              |
|                                                                                                                                                                                                                             |
| [loadField.Checked = [True]]                                                                                                                                       |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Filling the Signature Field

 

The following code illustrates how to fill the Signature Field.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                       |
|                                                                                                                                                                                                      |
| []                                                                                                                                                               |
|                                                                                                                                                                                                      |
| [PdfLoadedSignatureField ][sigField = ldoc.Form.Fields\[0\] as [PdfLoadedSignatureField];] |
|                                                                                                                                                                                                      |
| [sigField.Signature = new [PdfSignature]();]                                                                                                |
|                                                                                                                                                                                                      |
| [sigField.Signature.Certificate = certificate;]                                                                                                                  |
|                                                                                                                                                                                                      |
| [sigField.Signature.Reason = \"Reason\";]                                                                                                                        |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                |
| [Dim][ [sigField As ][PdfLoadedSignatureField][ = TryCast(ldoc.Form.Fields(0), ][PdfLoadedSignatureField][)]] |
|                                                                                                                                                                                                                                                                                                                                                |
| [sigField.Signature = New PdfSignature()]                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                |
| [sigField.Signature.Certificate = certificate]                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                |
| [sigField.Signature.Reason = \"Reason\"]                                                                                                                                                                                                                                     |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

You can also enumerate the fields and fill them. The following code example illustrates how to enumerate the text fields.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                               |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [PdfLoadedForm][ form = doc.Form;]                                                        |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [PdfLoadedFormFieldCollection][ fields = form.Fields;]                                    |
|                                                                                                                                                                                |
| []                                                                                                                                         |
|                                                                                                                                                                                |
| [for][ ( i = 0; i \< doc.Form.Fields.Count; i++)]                                         |
|                                                                                                                                                                                |
| [ {]                                                                                                                                       |
|                                                                                                                                                                                |
| [       [if] (doc.Form.Fields\[i\] [is] [PdfLoadedTextBoxField])]           |
|                                                                                                                                                                                |
| [       {]                                                                                                                                 |
|                                                                                                                                                                                |
| [              [PdfLoadedTextBoxField] textBox = ([PdfLoadedTextBoxField])doc.Form.Fields\[i\];] |
|                                                                                                                                                                                |
| [              textBox.Text = [\"Text\"];]                                                                          |
|                                                                                                                                                                                |
| [        }]                                                                                                                                |
|                                                                                                                                                                                |
| [ }]                                                                                                                                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                           |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [Dim][ form [As] PdfLoadedForm = doc.Form]                                                                           |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [Dim][ fields [As] PdfLoadedFormFieldCollection = form.Fields]                                                       |
|                                                                                                                                                                                                                                |
| []                                                                                                                                                                                         |
|                                                                                                                                                                                                                                |
| [For][ i = 0 [To]  doc.Form.Fields.Count- 1  [Step]  i + 1]                                     |
|                                                                                                                                                                                                                                |
| [       [If] [TypeOf] doc.Form.Fields(i) [Is] PdfLoadedTextBoxField [Then]]                            |
|                                                                                                                                                                                                                                |
| [Dim][ textBox [As] PdfLoadedTextBoxField = [CType](doc.Form.Fields(i), PdfLoadedTextBoxField)] |
|                                                                                                                                                                                                                                |
| [               textBox.Text = [\"Text\"]]                                                                                                                          |
|                                                                                                                                                                                                                                |
| [       [End] [If]]                                                                                                                              |
|                                                                                                                                                                                                                                |
| [Next]                                                                                                                                                                        |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

 Form Fields

 

TryGetField:

 

Loaded field from the PdfLoadedFormFieldCollection provides TryGetField method to obtain the form fields. It is used to get the field value from the given field name. It specifies whether the particular field is loaded or not by returning the boolean value.

 

Syntax:

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                   |
|                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                  |
| [public][ [bool] TryGetField([string] fieldName,[out] PdfLoadedField field)] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                |
| [Public][ [Function] TryGetField(fieldName [As] [String], [ByRef] field [As] PdfLoadedField) [As] [Boolean]][] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Example:

 

[The following code example illustrates how to get the form field with the given field name. ]

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                    |
| [// Load the document.]                                                                                                                                                                          |
|                                                                                                                                                                                                                                                    |
| [PdfLoadedDocument][ doc = [new] [PdfLoadedDocument]([@\"..\\..\\Data\\Form.pdf\"]);] |
|                                                                                                                                                                                                                                                    |
| [// Load the form from the loaded document.]                                                                                                                                                     |
|                                                                                                                                                                                                                                                    |
| [PdfLoadedForm][ form = doc.Form;]                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [// Load the form field collections from the form.]                                                                                                                                              |
|                                                                                                                                                                                                                                                    |
| [PdfLoadedFormFieldCollection][ field = [new] [PdfLoadedFormFieldCollection](form);]                          |
|                                                                                                                                                                                                                                                    |
| [PdfLoadedField][ m_field = [null];]                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [string][ fieldValue = [string].Empty;]                                                                                                  |
|                                                                                                                                                                                                                                                    |
| [// TryGetField Method.]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                    |
| [if][ (field.TryGetField([\"f1-1\"], [out] m_field))]                                                            |
|                                                                                                                                                                                                                                                    |
| [{]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                    |
| [    (m_field [as] [PdfLoadedTextBoxField]).Text = [\"1\"];]                                                                              |
|                                                                                                                                                                                                                                                    |
| [}]                                                                                                                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                            |
|                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                               |
| [\' Load the document.]                                                                                                                                                     |
|                                                                                                                                                                                                                               |
| [Dim][ doc [As] [New] PdfLoadedDocument([\"..\\..\\Data\\Form.pdf\"])] |
|                                                                                                                                                                                                                               |
| [\' Load the form from the loaded document.]                                                                                                                                |
|                                                                                                                                                                                                                               |
| [Dim][ form [As] PdfLoadedForm = doc.Form]                                                                          |
|                                                                                                                                                                                                                               |
| [\' Load the form field collections from the form.][]                                                                                   |
|                                                                                                                                                                                                                               |
| [Dim][ field [As] [New] PdfLoadedFormFieldCollection(Form)]                                    |
|                                                                                                                                                                                                                               |
| [Dim][ m_field [As] PdfLoadedField = [Nothing]]                                                |
|                                                                                                                                                                                                                               |
| [Dim][ fieldValue [As] [String] = [String].Empty]                         |
|                                                                                                                                                                                                                               |
| [\' TryGetField Method.]                                                                                                                                                    |
|                                                                                                                                                                                                                               |
| [If][ field.TryGetField([\"f1-1\"], m_field) [Then]]                                        |
|                                                                                                                                                                                                                               |
| [  TryCast][(m_field, PdfLoadedTextBoxField).Text = [\"1\"]]                                                     |
|                                                                                                                                                                                                                               |
| [End][ [If]]                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

TryGetValue:

 

Loaded field from the PdfLoadedFormFieldCollection provides TryGetValue method to obtain the field values. It is used to get the field value from the given field name. It specifies whether the particular field returns true or false value.

 

Example - For a check box field, it returns a value whether it is checked or not.

 

**Syntax:**

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                        |
| **[]**                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                        |
| [public][ [bool] TryGetValue ([string] fieldName, [out] [string] fieldValue)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                          |
| [Public][ [Function] TryGetValue(fieldName [As] [String], [ByRef] fieldValue [As] [string]) [As] [Boolean]] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Example:

 

The following code example illustrates how to get the form field with the given field name.

 

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                             |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                            |
| [// Load the document.]                                                                                                                                                                  |
|                                                                                                                                                                                                                                            |
| [PdfLoadedDocument][ doc = [new] [PdfLoadedDocument]([@\"Form.pdf\"]);]       |
|                                                                                                                                                                                                                                            |
| [// Load the form from the loaded document.]                                                                                                                                             |
|                                                                                                                                                                                                                                            |
| [PdfLoadedForm][ form = doc.Form;]                                                                                                                 |
|                                                                                                                                                                                                                                            |
| [// Load the form field collections from the form.]                                                                                                                                      |
|                                                                                                                                                                                                                                            |
| [PdfLoadedFormFieldCollection][ field = [new] [PdfLoadedFormFieldCollection](form);]                  |
|                                                                                                                                                                                                                                            |
| [PdfLoadedField][ m_field = [null];]                                                                                          |
|                                                                                                                                                                                                                                            |
| [string][ fieldValue = [string].Empty;]                                                                                          |
|                                                                                                                                                                                                                                            |
| [// TryGetValue Method.]                                                                                                                                                                 |
|                                                                                                                                                                                                                                            |
| [if][ (field.TryGetValue([\"f1-2\"], [out] fieldValue) && fieldValue == [\"\"])] |
|                                                                                                                                                                                                                                            |
| [{]                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                            |
| [    (form.Fields\[[\"f1-2\"]\] [as] [PdfLoadedTextBoxField]).Text = [\"2\"];]                            |
|                                                                                                                                                                                                                                            |
| [}]                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                      |
| **[]**                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                      |
| [\' Load the document.]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                      |
| [Dim][ doc [As] [New] PdfLoadedDocument([\"Form.pdf\"])]                                                      |
|                                                                                                                                                                                                                                                                      |
| [\' Load the form from the loaded document.]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [Dim][ form [As] PdfLoadedForm = doc.Form]                                                                                                                 |
|                                                                                                                                                                                                                                                                      |
| [\' Load the form field collections from the form.][]                                                                                                                          |
|                                                                                                                                                                                                                                                                      |
| [Dim][ field [As] [New] PdfLoadedFormFieldCollection(Form)]                                                                           |
|                                                                                                                                                                                                                                                                      |
| [Dim][ m_field [As] PdfLoadedField = [Nothing]]                                                                                       |
|                                                                                                                                                                                                                                                                      |
| [Dim][ fieldValue [As] [String] = [String].Empty]                                                                |
|                                                                                                                                                                                                                                                                      |
| [\' TryGetValue Method.]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                      |
| [If][ field.TryGetValue([\"f1-2\"], fieldValue) [AndAlso] fieldValue = [\"\"] [Then]] |
|                                                                                                                                                                                                                                                                      |
| [  [TryCast](form.Fields([\"f1-2\"]), PdfLoadedTextBoxField).Text = [\"2\"]]                                                                                |
|                                                                                                                                                                                                                                                                      |
| [End][ [If]]                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p100} 

[]{#related-topics}

