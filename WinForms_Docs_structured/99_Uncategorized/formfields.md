---
title: formfields.md
original_path: WinForms_Docs/99_Uncategorized/formfields.md
created_at: 2025-08-05
---








  









### Form Fields {#form-fields style="tab-stops: 0pt"}

 

An interactive form is a collection of fields for gathering information interactively from the user. A PDF document may contain any number of fields appearing on any combination of pages, all of which makes up a single global interactive form spanning the entire document. Arbitrary subsets of these fields can be imported or exported from the document.

 

You can change the form\'s properties, add new fields or remove existing fields. Also you can flatten the loaded field by using the Flatten property.

 

This section covers the following:

 

[·      ]Form Fields Creation

[·      ]Editing Form Fields

 

Form Fields Creation

 

The following classes are used to create Form Fields.

 


  ------------------------- -----------------------------------------------------------------
  Class                     Description
  PdfButtonField            Creates Button (Submit Button and Reset button can be created).
  PdfCheckBoxField          Creates Check Box.
  PdfComboBoxField          Creates Combo Box.
  PdfListFieldItem          Creates list items from Combo Box and List Box.
  PdfListBoxField           Creates List Box.
  PdfTextBoxField           Creates Text Box.
  PdfRadioButtonListField   Creates Radio button list.
  PdfRadioButtonListItem    Creates Radio button list item.
  ------------------------- -----------------------------------------------------------------


[] 

Button field

 

A button field represents an interactive control on the screen that the user can manipulate using the mouse. PdfButtonField class is used to create Buttons fields.

 

The most important feature of PDF form is the ability to send entered data to a server. To perform this action you should create an action of SubmitAction type, and specify a valid data processing script URL. The action must be assigned to a MouseUp action of the submit button.

 

{border="0"} ResetAction is used to restore the default values of the fields or simply clear them.

 

The following code example illustrates how to create a button field.

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [// Creating a Button ]                                                                                                                                                                           |
|                                                                                                                                                                                                                                                     |
| [PdfButtonField][ button = [new] [PdfButtonField](page, [\"Click\"]);]                        |
|                                                                                                                                                                                                                                                     |
| [button.Bounds = [new] [RectangleF](0, 420, 90, 20);]                                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [button.Text = [\"Click\"];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                     |
| [loadedDoc.Form.Fields.Add(button);]                                                                                                                                                                            |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [// Creating Submit action button]                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [PdfSubmitAction][ submitAction = [new] [PdfSubmitAction]([\"http://stevex.net/dump.php\"]);] |
|                                                                                                                                                                                                                                                     |
| [submitAction.DataFormat = [SubmitDataFormat].Html;]                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                     |
| [//Create submit button to transfer the values in the form]                                                                                                                                       |
|                                                                                                                                                                                                                                                     |
| [PdfButtonField][ submitButton = [new] [PdfButtonField](page, [\"submitButton\"]);]           |
|                                                                                                                                                                                                                                                     |
| [submitButton.Bounds = [new] [RectangleF](100, 420, 90, 20);]                                                                                                         |
|                                                                                                                                                                                                                                                     |
| [submitButton.Font = font;]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                     |
| [submitButton.Text = [\"Submit\"];]                                                                                                                                                      |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [// Assigning the submit action]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| [submitButton.Actions.MouseUp = submitAction;]                                                                                                                                                                  |
|                                                                                                                                                                                                                                                     |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                     |
| [// Adding the Field            ]                                                                                                                                                                 |
|                                                                                                                                                                                                                                                     |
| [loadedDoc.Form.Fields.Add(submitButton);]                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\' Creating a Button ]                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                           |
| [Dim][ button [As] PdfButtonField = [New] PdfButtonField(page, [\"Click\"])]                        |
|                                                                                                                                                                                                                                                           |
| [button.Bounds = [New] RectangleF(0, 420, 90, 20)]                                                                                                                                               |
|                                                                                                                                                                                                                                                           |
| [button.Text = [\"Click\"]]                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [loadedDoc.Form.Fields.Add(button)]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\' Creating Submit action button]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [Dim][ submitAction [As] PdfSubmitAction = [New] PdfSubmitAction([\"http://stevex.net/dump.php\"])] |
|                                                                                                                                                                                                                                                           |
| [submitAction.DataFormat = SubmitDataFormat.Html]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\'Create submit button to transfer the values in the form]                                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| [Dim][ submitButton [As] PdfButtonField = [New] PdfButtonField(page, [\"submitButton\"])]           |
|                                                                                                                                                                                                                                                           |
| [submitButton.Bounds = [New] RectangleF(100, 420, 90, 20)]                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [submitButton.Font = font]                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| [submitButton.Text = [\"Submit\"]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [\' Assigning the submit action]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [submitButton.Actions.MouseUp = submitAction]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [\' Adding the Field            ]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                           |
| [loadedDoc.Form.Fields.Add(submitButton)        ]                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Essential PDF enables to add a Print Button to the form. Clicking the print button, initializes a print dialog. The following code example illustrates this.

 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                        |
|                                                                                                                                                                                                       |
| []                                                                                                                                                                |
|                                                                                                                                                                                                       |
| [// Create a print button]                                                                                                                          |
|                                                                                                                                                                                                       |
| [PdfButtonField][ print = [new] PdfButtonField(page, [\"print\"]);] |
|                                                                                                                                                                                                       |
| [print.Bounds = [new] [RectangleF](200, 25, 90, 15);]                                                                |
|                                                                                                                                                                                                       |
| [print.Text = [\"Print\"];]                                                                                                               |
|                                                                                                                                                                                                       |
| [print.AddPrintAction();]                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [\'Create a print button]                                                                                                                                                       |
|                                                                                                                                                                                                                                   |
| [Dim][ print [As] PdfButtonField = [New] PdfButtonField(page, [\"print\"])] |
|                                                                                                                                                                                                                                   |
| [print.Bounds = [New] RectangleF(200, 25, 90, 15)]                                                                                                                       |
|                                                                                                                                                                                                                                   |
| [print.Text = [\"Print\"]]                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [print.AddPrintAction()]                                                                                                                                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Check Box Field

 

A check box field represents one or more check boxes that toggle between two states, ON and OFF. The check box state is manipulated by the user using the mouse or keyboard[. ]

 

**PdfCheckBoxField** class is used to create a check box in PDF forms. You can customize the check box style by using properties such as **BorderStyle**, **HighlightMode**, **BorderWidth** and so on.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                            |
|                                                                                                                                                                                                                                   |
| [//Create a check box]                                                                                                                                                          |
|                                                                                                                                                                                                                                   |
| [PdfCheckBoxField][ checkBox = [new] [PdfCheckBoxField](page, [\".NET\"]);] |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [//Set properties]                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [checkBox.Bounds = [new] [RectangleF](100, 290, 20, 20);]                                                                                           |
|                                                                                                                                                                                                                                   |
| [checkBox.HighlightMode = [PdfHighlightMode].Push;]                                                                                                                      |
|                                                                                                                                                                                                                                   |
| [checkBox.BorderStyle = [PdfBorderStyle].Beveled;]                                                                                                                       |
|                                                                                                                                                                                                                                   |
| []                                                                                                                                                                              |
|                                                                                                                                                                                                                                   |
| [//Set the value for the check box]                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [checkBox.Checked = [true];]                                                                                                                                             |
|                                                                                                                                                                                                                                   |
| [g.DrawString([\".NET\"], font, brush, [new] [RectangleF](150, 290, 180, 20));]                                              |
|                                                                                                                                                                                                                                   |
| [loadedDoc.Form.Fields.Add(checkBox);]                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                      |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                         |
| [\'Create a check box]                                                                                                                                                                |
|                                                                                                                                                                                                                                         |
| [Dim][ checkBox [As] PdfCheckBoxField = [New] PdfCheckBoxField(page, [\".NET\"])] |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [\'Set properties]                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [checkBox.Bounds = [New] RectangleF(100, 290, 20, 20)]                                                                                                                         |
|                                                                                                                                                                                                                                         |
| [checkBox.HighlightMode = PdfHighlightMode.Push]                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [checkBox.BorderStyle = PdfBorderStyle.Beveled]                                                                                                                                                     |
|                                                                                                                                                                                                                                         |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [\'Set the value for the check box]                                                                                                                                                   |
|                                                                                                                                                                                                                                         |
| [checkBox.Checked = [True]]                                                                                                                                                    |
|                                                                                                                                                                                                                                         |
| [g.DrawString([\".NET\"],font,brush,[New] RectangleF(150,290,180,20))]                                                                                  |
|                                                                                                                                                                                                                                         |
| [loadedDoc.Form.Fields.Add(checkBox)]                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

PdfComboBox Field

 

A combo box represents a drop-down list, optionally accompanied by an editable text box in which the user can type a value other than the predefined choices. PdfComboBoxField class is used to create a combo box field in PDF forms. You can add list of items to the combo box by using the PdfListFieldItem class.

 

   The following code example illustrates this.

 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [//Create a combo box]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [PdfComboBoxField][ positionComboBox = [new] [PdfComboBoxField](page, [\"positionComboBox\"]);]                    |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [//Set properties]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [positionComboBox.Bounds = [new] [RectangleF](100, 115, 200, 20);]                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| [positionComboBox.Font = font;]                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [// Setting the combobox as editable]                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [positionComboBox.Editable = [true];            ]                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                 |
| [//Add combobox to document]                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                 |
| [loadedDoc.Form.Fields.Add(positionComboBox);]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [//Create the field item to be added in the combobox]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                 |
| [PdfListFieldItem][ item1 = [new] [PdfListFieldItem]([\"Developer\"], [\"Developer\"]);]   |
|                                                                                                                                                                                                                                                                                 |
| [PdfListFieldItem][ item2 = [new] [PdfListFieldItem]([\"Accountant\"], [\"Accountant\"]);] |
|                                                                                                                                                                                                                                                                                 |
| []                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                 |
| [//Add the items in combo box.]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                 |
| [positionComboBox.Items.Add(item1);]                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                 |
| [positionComboBox.Items.Add(item2);  ]                                                                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [\'Create a combo box]                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [Dim][ positionComboBox [As] PdfComboBoxField = [New] PdfComboBoxField(page, [\"positionComboBox\"])]                   |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [\'Set properties]                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [positionComboBox.Bounds = [New] RectangleF(100, 115, 200, 20)]                                                                                                                                                      |
|                                                                                                                                                                                                                                                                               |
| [positionComboBox.Font = font]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [\' Setting the combobox as editable]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [positionComboBox.Editable = [True]            ]                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                               |
| [\'Add combobox to document]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [loadedDoc.Form.Fields.Add(positionComboBox)]                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [\'Create the field item to be added in the combobox]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [Dim][ item1 [As] PdfListFieldItem = [New] PdfListFieldItem([\"Developer\"], [\"Developer\"])]   |
|                                                                                                                                                                                                                                                                               |
| [Dim][ item2 [As] PdfListFieldItem = [New] PdfListFieldItem([\"Accountant\"], [\"Accountant\"])] |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [\'Add the items in combobox.]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [positionComboBox.Items.Add(item1)]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| [positionComboBox.Items.Add(item2)]                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

PdfListBoxField

 

A scrollable List Box contains several text items, one or more of which may be selected as the field value. **PdfListBoxField** is used to create the ListBox field in PDF forms.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                         |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [//Create list box]                                                                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [PdfListBoxField][ listBox = [new] [PdfListBoxField](page, [\"list1\"]);] |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                   |
|                                                                                                                                                                                                                                        |
| [//Set the properties.]                                                                                                                                                              |
|                                                                                                                                                                                                                                        |
| [listBox.Bounds = [new] [RectangleF](100, 350, 100, 50);]                                                                                             |
|                                                                                                                                                                                                                                        |
| [listBox.HighlightMode = [PdfHighlightMode].Outline;]                                                                                                                      |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [//Add the items to the list box]                                                                                                                                                    |
|                                                                                                                                                                                                                                        |
| [listBox.Items.Add([new] [PdfListFieldItem]([\"English\"], [\"English\"]));]                          |
|                                                                                                                                                                                                                                        |
| [listBox.Items.Add([new] [PdfListFieldItem]([\"French\"], [\"French\"]));]                            |
|                                                                                                                                                                                                                                        |
| [listBox.Items.Add([new] [PdfListFieldItem]([\"German\"], [\"German\"]));]                            |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [//Select the item]                                                                                                                                                                  |
|                                                                                                                                                                                                                                        |
| [listBox.SelectedIndex = 2;]                                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| []                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                        |
| [//Set the multiselect option]                                                                                                                                                       |
|                                                                                                                                                                                                                                        |
| [listBox.MultiSelect = [true];]                                                                                                                                               |
|                                                                                                                                                                                                                                        |
| [loadedDoc.Form.Fields.Add(listBox);]                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [\'Create list box]                                                                                                                                                                 |
|                                                                                                                                                                                                                                       |
| [Dim][ listBox [As] PdfListBoxField = [New] PdfListBoxField(page, [\"list1\"])] |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                  |
|                                                                                                                                                                                                                                       |
| [\'Set the properties.]                                                                                                                                                             |
|                                                                                                                                                                                                                                       |
| [listBox.Bounds = [New] RectangleF(100, 350, 100, 50)]                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [listBox.HighlightMode = PdfHighlightMode.Outline]                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [\'Add the items to the list box]                                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [listBox.Items.Add([New] PdfListFieldItem([\"English\"],[\"English\"]))]                                                       |
|                                                                                                                                                                                                                                       |
| [listBox.Items.Add([New] PdfListFieldItem([\"French\"],[\"French\"]))]                                                         |
|                                                                                                                                                                                                                                       |
| [listBox.Items.Add([New] PdfListFieldItem([\"German\"],[\"German\"]))]                                                         |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [\'Select the item]                                                                                                                                                                 |
|                                                                                                                                                                                                                                       |
| [listBox.SelectedIndex = 2]                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [\'Set the multiselect option]                                                                                                                                                      |
|                                                                                                                                                                                                                                       |
| [listBox.MultiSelect = [True]]                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [loadedDoc.Form.Fields.Add(listBox)]                                                                                                                                                              |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}Note: You can create multiple options from the ListBox by setting the MultiSelect option to True.


[] 

TextBox field

[] 

A text field is a box or space in which the user can enter text through the keyboard. The text can be restricted to a single line or permitted to span multiple lines, depending on the setting of the Multiline flag. **PdfTextBoxField** class is used to create a textbox field in PDF forms. This class also provides support to create password and multilined text boxes.

 

  The following code example illustrates this.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [//Create a text box]                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                            |
| [PdfTextBoxField][ firstNameTextBox = [new] [PdfTextBoxField](page, [\"firstNameTextBox\"]);] |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [//Set properties]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [firstNameTextBox.Bounds = [new] [RectangleF](100, 20, 200, 20);]                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [firstNameTextBox.Font = font;]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                            |
| [firstNameTextBox.Password = [true];]                                                                                                                                                             |
|                                                                                                                                                                                                                                                            |
| [firstNameTextBox.Multiline = [true];]                                                                                                                                                            |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                            |
| [//Add the text box in document]                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| [loadedDoc.Form.Fields.Add(firstNameTextBox);]                                                                                                                                                                         |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\'Create a text box]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [Dim][ firstNameTextBox [As] PdfTextBoxField = [New] PdfTextBoxField(page, [\"firstNameTextBox\"])] |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                           |
| [\'Set properties]                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [firstNameTextBox.Bounds = [New] RectangleF(100, 20, 200, 20)]                                                                                                                                   |
|                                                                                                                                                                                                                                                           |
| [firstNameTextBox.Font = font]                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [firstNameTextBox.Password = [True]]                                                                                                                                                             |
|                                                                                                                                                                                                                                                           |
| [firstNameTextBox.Multiline = [True]]                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                           |
| [\'Add the text box in document]                                                                                                                                                                        |
|                                                                                                                                                                                                                                                           |
| [loadedDoc.Form.Fields.Add(firstNameTextBox)]                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Radio Button field

 

Radio button fields contain a set of related buttons that can each be set to ON or OFF. Typically, at most, one radio button in a set can be ON at any given time, and selecting any one of the buttons automatically de-selects all the others.[ ]PdfRadioButtonListField class is used to create a radio button in the PDF Forms. You can create the radio button list items by using the PdfRadioButtonListItem class.

 

The following code example illustrates how to create radio buttons.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [ //Create a Radio button]                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| [PdfRadioButtonListField][ employeesRadioList = [new] [PdfRadioButtonListField](page, [\"employeesRadioList\"]);            ] |
|                                                                                                                                                                                                                                                                                            |
| [loadedDoc.Form.Fields.Add(employeesRadioList);]                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [            ]                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                            |
| [ [//Create radio button items ]]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                            |
| [PdfRadioButtonListItem][ radioItem1 = [new] [PdfRadioButtonListItem]([\"1-9\"]);]                                            |
|                                                                                                                                                                                                                                                                                            |
| [radioItem1.Bounds = [new] [RectangleF](100, 140, 20, 20);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| [g.DrawString([\"1-9\"], font, brush, [new] [RectangleF](150, 145, 180, 20));]                                                                                                    |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [PdfRadioButtonListItem][ radioItem2 = [new] [PdfRadioButtonListItem]([\"10-49\"]);]                                          |
|                                                                                                                                                                                                                                                                                            |
| [radioItem2.Bounds = [new] [RectangleF](100, 170, 20, 20);]                                                                                                                                               |
|                                                                                                                                                                                                                                                                                            |
| [g.DrawString([\"10-49\"], font, brush, [new] [RectangleF](150, 175, 180, 20));           ]                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                            |
| [ [//add the items to radio button group]]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                            |
| [employeesRadioList.Items.Add(radioItem1);]                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                            |
| [employeesRadioList.Items.Add(radioItem2);            ]                                                                                                                                                                                                |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [\'Create a Radio button]                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                               |
| [Dim][ employeesRadioList [As] PdfRadioButtonListField = [New] PdfRadioButtonListField(page, [\"employeesRadioList\"])] |
|                                                                                                                                                                                                                                                                               |
| [loadedDoc.Form.Fields.Add(employeesRadioList)]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [\'Create radio button items ]                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                               |
| [Dim][ radioItem1 [As] PdfRadioButtonListItem = [New] PdfRadioButtonListItem([\"1-9\"])]                                |
|                                                                                                                                                                                                                                                                               |
| [radioItem1.Bounds = [New] RectangleF(100, 140, 20, 20)]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [g.DrawString([\"1-9\"],font,brush,[New] RectangleF(150,145,180,20))]                                                                                                                         |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [Dim][ radioItem2 [As] PdfRadioButtonListItem = [New] PdfRadioButtonListItem([\"10-49\"])]                              |
|                                                                                                                                                                                                                                                                               |
| [radioItem2.Bounds = [New] RectangleF(100, 170, 20, 20)]                                                                                                                                                             |
|                                                                                                                                                                                                                                                                               |
| [g.DrawString([\"10-49\"],font,brush,[New] RectangleF(150,175,180,20))]                                                                                                                       |
|                                                                                                                                                                                                                                                                               |
| []                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                               |
| [\'add the items to radio button group]                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                               |
| [employeesRadioList.Items.Add(radioItem1)]                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                               |
| [employeesRadioList.Items.Add(radioItem2)        ]                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Signature fields

**[]** 

A signature field is a form field that contains a [digital signature][. ]**PdfSignatureField** class is used to create signature fields in PDF forms. **PdfSignature** class enables to sign the signature field with the given certificate.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                      |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| [PdfSignatureField][ field = [new] [PdfSignatureField](page, [\"Signature\"]);] |
|                                                                                                                                                                                                                                       |
| [field.Bounds = [new] [RectangleF](0, 0, 90, 20);]                                                                                                      |
|                                                                                                                                                                                                                                       |
| [field.BackColor = [new] [PdfColor]([Color].Red);]                                                                                 |
|                                                                                                                                                                                                                                       |
| [field.BorderColor = [new] [PdfColor]([Color].Red);]                                                                               |
|                                                                                                                                                                                                                                       |
| [field.Signature = [new] PdfSignature();]                                                                                                                                    |
|                                                                                                                                                                                                                                       |
| [field.Signature.Certificate = certificate;]                                                                                                                                                      |
|                                                                                                                                                                                                                                       |
| [field.Signature.Reason = [\"Reason\"];]                                                                                                                                   |
|                                                                                                                                                                                                                                       |
| [document.Form.Fields.Add(field);]                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                    |
|                                                                                                                                                                                                                         |
| **[]**                                                                                                                                                                              |
|                                                                                                                                                                                                                         |
| [Dim][ field [As] [New] PdfSignatureField(page, [\"Signature\"])] |
|                                                                                                                                                                                                                         |
| [field.Bounds = [New] RectangleF(0, 0, 90, 20)]                                                                                                                |
|                                                                                                                                                                                                                         |
| [field.BackColor = [New] PdfColor(Color.Red)]                                                                                                                  |
|                                                                                                                                                                                                                         |
| [field.BorderColor = [New] PdfColor(Color.Red)]                                                                                                                |
|                                                                                                                                                                                                                         |
| [field.Signature = [New] PdfSignature()]                                                                                                                       |
|                                                                                                                                                                                                                         |
| [field.Signature.Certificate = certificate]                                                                                                                                         |
|                                                                                                                                                                                                                         |
| [field.Signature.Reason = [\"Reason\"]]                                                                                                                      |
|                                                                                                                                                                                                                         |
| [document.Form.Fields.Add(field)]                                                                                                                                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 


{border="0"}Note: For more details on public members, see class reference documentation for pdf.


**[]** 

Editing Form Fields

[] 

**PdfLoadedForm** class contains collection of loaded fields, represented by the **PdfLoadedFormFieldCollection** class, and inherited from the **PdfFieldCollection** class. The base class for each loaded field is represented by the **PdfLoadedField** class and inherited from the **PdfField** class.

 

The following loaded fields are supported in the library:

 

[·      ]Button fields

[o  ]Push button field, represented by **PdfLoadedButtonField** class

[o  ]Check Box field, represented by **PdfLoadedCheckBoxField** class

[o  ]Radio button field, represented by **PdfLoadedRadioButtonListField** class

[·      ]Text fields

[o  ]Text field, represented by **PdfLoadedTextBoxField** class

[·      ]Choice fields

[o  ]List Box field, represented by **PdfLoadedListBoxField** class

[o  ]Combo Box field, represented by **PdfLoadedComboBoxField** class

[·      ]Signature fields

[o  ]Signature field, represented by **PdfLoadedSignatureField** class

 

You can access each field by using its index or field name. The following code example illustrates this.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                      |
| []                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                      |
| [PdfLoadedTextBoxField][ field = form.Fields\[[\"fieldname\"]\] [as] [PdfLoadedTextBoxField];] |
|                                                                                                                                                                                                                                                      |
| [PdfLoadedTextBoxField][ ldField = form.Fields\[ 0 \] [as] [PdfLoadedTextBoxField]; ]                                 |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                            |
| []                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                            |
| [Dim][ field [As] PdfLoadedTextBoxField = form.Fields\[[\"fieldname\"]\] [as] PdfLoadedTextBoxField] |
|                                                                                                                                                                                                                                                            |
| [Dim][ field [As] PdfLoadedTextBoxField =  form.Fields( 0 ) [as] PdfLoadedTextBoxField ]                                    |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

Essential PDF enables you to retrieve the bounds and value of the field, change the field location and size, and modify its value. Also you can get or set another available property.

 

The following code example illustrates how to change the bounds and value of the field.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                       |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                 |
|                                                                                                                                                                                                                      |
| [PdfLoadedDocument][ ldDoc = [new] [PdfLoadedDocument](filename); ]                   |
|                                                                                                                                                                                                                      |
| [PdfLoadedForm][ form = ldDoc.Form; ]                                                                                           |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [PdfLoadedTextBoxField][ ldField = form.Fields\[ 0 \] [as] [PdfLoadedTextBoxField]; ] |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [RectangleF][ newBounds = [new] [RectangleF]( 100, 100, 50, 50 ); ]                   |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [ldField.Bounds = newBounds; ]                                                                                                                                                   |
|                                                                                                                                                                                                                      |
| [ldField.SpellCheck = [true]; ]                                                                                                                             |
|                                                                                                                                                                                                                      |
| [ldField.Text = [\"New text of the field.\"]; ]                                                                                                           |
|                                                                                                                                                                                                                      |
| [ldField.Password = [false]; ]                                                                                                                              |
|                                                                                                                                                                                                                      |
| []                                                                                                                                                                               |
|                                                                                                                                                                                                                      |
| [ldDoc.Save( newFileName ); ]                                                                                                                                                    |
|                                                                                                                                                                                                                      |
| [ldDoc.Close(); ]                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                        |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                      |
|                                                                                                                                                                                                                           |
| [Dim][ ldDoc [As] PdfLoadedDocument = [New] PdfLoadedDocument(filename)]                   |
|                                                                                                                                                                                                                           |
| [Dim][ form [As] PdfLoadedForm = ldDoc.Form]                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [Dim][ ldField [As] PdfLoadedTextBoxField =  form.Fields( 0 ) [as] PdfLoadedTextBoxField ] |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [Dim][ NewBounds [As] RectangleF = [New] RectangleF(100, 100, 50, 50)]                     |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [ldField.Bounds = NewBounds ]                                                                                                                                                         |
|                                                                                                                                                                                                                           |
| [ldField.SpellCheck = [True] ]                                                                                                                                   |
|                                                                                                                                                                                                                           |
| [ldField.Text = [\"New text of the field.\"] ]                                                                                                                 |
|                                                                                                                                                                                                                           |
| [ldField.Password = [False] ]                                                                                                                                    |
|                                                                                                                                                                                                                           |
| []                                                                                                                                                                                    |
|                                                                                                                                                                                                                           |
| [ldDoc.Save(NewFileName) ]                                                                                                                                                            |
|                                                                                                                                                                                                                           |
| [ldDoc.Close()]                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

