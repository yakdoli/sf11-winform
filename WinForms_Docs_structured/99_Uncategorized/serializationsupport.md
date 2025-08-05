---
title: serializationsupport.md
original_path: WinForms_Docs/99_Uncategorized/serializationsupport.md
created_at: 2025-08-05
---








  









### Serialization Support {#serialization-support style="tab-stops: 0pt"}

Essential GridControl supports Serialization. The whole grid can be serialized and deserialized at runtime.

**[]** 

Use Case Scenarios

Serialization can be implemented for the applications which need to save its data and structure after the application is closed. Serialization supports to save the structure and data of the GridControl to an XML file and it can be loaded at any time.

[] 

Adding Serialization to an Application

The following sample application explains the implementation of the Serialization support to GirdControl.

[] 

1.   Create an application

      Create a Silverlight application and add the GridControl to it.

[] 

2.   Call the Serialization support methods

**[      ]**In the application, create three buttons. The first button to call the **Serialize()** method, the second button to make changes to the Grid and the third button is to call the **Deserialize()** method. The following code snippet explains the implementation of Serialization.

[] 

+-------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                        |
|                                                                                                                         |
| **[]**                                                                              |
|                                                                                                                         |
| **[// To Serialize the GridControl.]**                              |
|                                                                                                                         |
| [this][.grid.Model.Serialize();]   |
|                                                                                                                         |
| []                                                                                  |
|                                                                                                                         |
| **[// To Deserialize the GridControl.]**                            |
|                                                                                                                         |
| [this][.grid.Model.Deserialize();] |
|                                                                                                                         |
| []                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------+

 

3.   Run the application

Run the application. Click the Serialize button which opens as **SaveAs** dialog to serialize the initial load; it creates an XML file. Click the second button **ModifyGridStyle** to make some changes in the GridControl. Now click the **Deserialize** button which opens an Open dialog box to restore the old settings of the GridControl.

[] 

[] 

Supported Properties for Serialization

The following Properties are Serialized in the GridControl.

[] 

[·      ]RowCount

[·      ]ColCount

[·      ]ActivateCurrentCellBehavior

[·      ]AllowSelection

[·      ]AllowSelectionOnShiftTab

[·      ]ColumnSizer

[·      ]CurrentCellBorder

[·      ]CurrentCellBorderWidth

[·      ]DataObjectConsumerOptions

[·      ]DrawSelectionOptions

[·      ]ExcelLikeCurrentCell

[·      ]ExcelLikeSelectionFrame

[·      ]HighlightSelectionBorder

[·      ]HighlightSelectionBorderWidth

[·      ]ListBoxModeAllowUIElementClick

[·      ]ListBoxSelectionMode

[·      ]MaxLength

[·      ]ScrollFrozen

[·      ]ShowCurrentCell

[·      ]WrapCell

[·      ]WrapCellBehavior

[] 

Methods

Table 16: Serialization Support Table

  Method                  Description                                                                                                                            Parameters       Type      Return Type
  ----------------------- -------------------------------------------------------------------------------------------------------------------------------------- ---------------- --------- -------------
  Serialize()             A virtual method called to Serialize the GridControl. It stores the settings in an xml file named as specified in its parameter.       NA               public    void
  Deserialize()           A virtual method called to Deserialize the GridControl. It restores the settings in an xml file named as specified in its parameter.   NA               public    void
  SerializeToStream()     Serialize the Grid to Stream.                                                                                                          Stream stream    public    void
  SerializeAsString()     Serialize the Grid  as String.                                                                                                         NA               public    string 
  DeserializeFromStream   Deserialize from the given TextReader.                                                                                                 Stream stream    public    void
  DeserializeFromString   Deserialize from the given String content.                                                                                             string content   public    void

[] 

Sample Link

Refer to the samples in the shipped Sample Browser.

Go to Essential Studio WPF Sample Browser [à] Grid [à] Serialization [à]GridControl Serialization Demo

[] 

 

[]{#related-topics}

