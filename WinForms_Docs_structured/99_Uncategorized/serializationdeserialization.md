---
title: serializationdeserialization.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\serializationdeserialization.md
created_at: 2025-07-03
---








  









## Serialization/Deserialization {#serializationdeserialization style="tab-stops: 0pt"}

 

Using this feature, you can save the current state of **PivotGrid** as an XML file format and restore the same at any time.

The following properties of **PivotGrid** control can be serialized.

 


  ---------------------------- ----------------------------------------------
  Property Name                Type
  AllowResizeColumns           bool
  AllowResizeRows              bool
  AllowSelection               bool
  AutoSizeColumnCount          int
  AutoSizeOption               GridAutoSizeOption
  DeferLayoutUpdate            bool
  Filters                      ObservableCollection\<FilterExpression\>
  FreezeHeaders                bool
  IsDynamicData                bool
  PivotCalculations            ObservableCollection\<PivotComputationInfo\>
  PivotColumns                 ObservableCollection\<PivotItem\>
  PivotFields                  ObservableCollection\<PivotItem\>
  PivotRows                    ObservableCollection\<PivotItem\>
  ShowCalculationsAsColumns    bool
  ShowGrandTotals              bool
  ShowGroupingBar              bool
  GroupingBar.AllowFiltering   bool
  GroupingBar.AllowSorting     bool
  ---------------------------- ----------------------------------------------


 

On Serialization, the expand and the collapse state of PivotGrid cells are maintained. So while de-serializing, the item source specified for the Grid should be as same as that when used in Serialization. This can be ignored by setting **IgnoreExpandCollapseOnSerialization** property of PivotGrid control to False.

 

Use Case Scenarios

Serialization can be implemented for applications which need to save its data and structure after the application is closed. Serialization supports to save the structure and data of **PivotGridControl** to an XML file and it can be loaded at any time.

 

Adding Serialization/Deserialization

 

Serialization/Deserialization can be achieved using the following code snippet,

 

+--------------------------------------------------------------------------------------------------------------------------------------------------+
| [\[C#\]]                                                                                                     |
|                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                  |
| [///][ Serialize the PivotGrid into XML file format.]       |
|                                                                                                                                                  |
| [this][.pivotGrid1.Serialize();]                            |
|                                                                                                                                                  |
| []                                                                                                           |
|                                                                                                                                                  |
| [///][ De serialize the PivotGrid from the saved XML file.] |
|                                                                                                                                                  |
| [this][.pivotGrid1.Deserialize();]                          |
|                                                                                                                                                  |
| []                                                                                           |
+--------------------------------------------------------------------------------------------------------------------------------------------------+

 

+----------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                     |
|                                                                                                                      |
| [\' Serialize the PivotGrid into XML file format.]                               |
|                                                                                                                      |
| [Me][.pivotGrid1.Serialize()]   |
|                                                                                                                      |
| []                                                                               |
|                                                                                                                      |
| [\' De serialize the PivotGrid from the saved XML file.]                         |
|                                                                                                                      |
| [Me][.pivotGrid1.Deserialize()] |
|                                                                                                                      |
| **[]**                                                                           |
+----------------------------------------------------------------------------------------------------------------------+

 

Methods

  --------------- ------------------------------------------------------------------------------- ------------ ------ -------------
  Method          Description                                                                     Parameters   Type   Return Type
  Serialize()     Serializes the PivotGrid into XML file format using the save file dialog        \-           void   void
  Deserialize()   Deserializes the PivotGrid from the saved XML file using the open file dialog   \-           void   void
  --------------- ------------------------------------------------------------------------------- ------------ ------ -------------

 

{border="0"}

Figure 19: Serialized XML file

 

Sample Link

To access Serialization Demo sample:

1.   Open the Syncfusion Dashboard.

2.   Click Business Intelligence.

3.   Click the **Silverlight** drop-down list, and select **Explore Samples**.

4.   Navigate to Syncfusion.PivotAnalysis.Silverlight.Samples -\> Syncfusion.PivotAnalysis.Silverlight.Samples -\> Samples -\> SerializationDemo.

 

[]{#related-topics}

