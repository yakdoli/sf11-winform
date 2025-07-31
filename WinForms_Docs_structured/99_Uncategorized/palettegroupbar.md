---
title: palettegroupbar.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\palettegroupbar.md
created_at: 2025-07-03
---








  









### PaletteGroupBar[] {#palettegroupbar style="tab-stops: 0pt"}

[] 

The PaletteGroupBar control provides support to drag symbols onto a diagram. It is based on the Syncfusion Essential Tools GroupBar control. Each symbol palette loaded in the PaletteGroupBar occupies a panel that can be selected by a bar button that is labeled with the name of the symbol palette. The symbols in the palette are shown as icons that can be dragged and dropped onto the diagram. This control enables you to add symbols to a palette, and save or load the palette whenever necessary. It provides a way to classify and maintain symbols.

           

Drag the PaletteGroupBar from the toolbox onto the web page. This will open the Diagram Wizard window.

[] 

{border="0"}

[] 

Figure 14: Diagram Wizard

[] 

This window provides you options to use documents and applications in a palette file. Following are the options provided:

[] 

1.   Documents-Allows you to load diagram and palette files

 

a.   Load EDD File-Allows you to load diagram file to the diagram control.

b.   Load EDP File-Allows you to load a Palette file to PaletteGroupView.

 

[] 

2.   Applications-Allows you to design diagram, custom symbols and shapes.[]

a.   Start Diagram Builder-Allows you to launch Diagram Builder application and design diagrams.

[b.   ]Start Symbol Builder-Allows you to launch Symbol Builder application and design custom shapes and symbols.[]

[] 

Symbol builder is a powerful application for creating different symbol palettes. Symbol Builder enables you to create palettes and save them as \*.edp files. If you do not want to start the diagram wizard after dragging the PaletteGroupBar onto the web page every time, select **Show on startup** option displayed in the diagram wizard.

3.   Click Ok, and then click Cancel, to view the PaletteGroupBar on your web page.

4.   Click on the PaletteGroupBar to view the PaletteGroupBar properties.

The following are the properties of the PaletteGroupBar control.

[] 


+-----------------------------------+-------------------------------------------------------------------------------------------+
|                                   |                                                                                           |
|                                   |                                                                                           |
| Property                          | Description                                                                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| BackColor                         | Gets or sets the background color of the component.                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| BorderColor                       | Gets or sets the color of the border around the control                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| BorderStyle                       | Gets or sets the Border style for the PaletteGroupBar. It includes the following options. |
|                                   |                                                                                           |
|                                   | [·      ]FixedSingle                                         |
|                                   |                                                                                           |
|                                   | [·      ]Fixed3D                                             |
|                                   |                                                                                           |
|                                   | [·      ]None                                                |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| CssClass                          | Specifies the Css class name applied to the control.                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| NodesLayout                       | Gets or sets the Symbols Layout.                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| CollapsedDuration                 | Gets or sets the duration of animation collapse in milliseconds.                          |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| CollapseSlideType                 | Specifies the type of slide effect to use during animation collapse.                      |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| CollapseTransition                | Specifies the visual effect to use during animation collapse.                             |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| ExpandDuration                    | Gets or sets the duration of animation expand in milliseconds.                            |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| ExpandSlideType                   | Specifies the type of slide effect to use during animation expand.                        |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| ExpandTransition                  | Specifies the visual effect to use during animation expand.                               |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| HTTPHandlerName                   | Specifies the name of the HTTP Handler which draws images at run time.                    |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| ImageFilesPath                    | Specifies the folder path where the control image resources are stored.                   |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| ScriptFilesPath                   | Specifies the folder path where the control script resources are stored.                  |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| SelectedItemColor                 | Specifies the color of the selected item.                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------------+
| SelectedItemTextColor             | Specifies the text color of the selected item.                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------+


[] 

The following are the important events of the PaletteGroupBar control.

 


+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
|                                   |                                                                                                              |
|                                   |                                                                                                              |
| Event                             | Description                                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| CallbackRefresh                   | Server-side event that is fired with the client-side args, after calling client object Refresh(sArg) method. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+
| NodeSelectChanged Event           | Triggered after a node is clicked.                                                                           |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------+


[] 

HTTP Handler for PaletteGroupBar

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[ASPX\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [\<][add][ [verb][=\"\*\"] [path][=\"PaletteImgRequest.ashx\"] [type][=\"Syncfusion.Web.UI.WebControls.Diagram.ThumbNodeRenderHandler,       Syncfusion.Diagram.Web, Version=X.X.X.X, Culture=neutral, PublicKeyToken=3d67ed1f87d44c89\"/\>]] |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


{border="0"}[Note:][ ]X.X.X.X in the above code corresponds to the correct version number of the Essential Studio version that you are currently using.


[] 

The following code example illustrates how to set the properties for the PaletteGroupBar.

[] 

+-------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                  |
|                                                                                                                   |
| []                                                                            |
|                                                                                                                   |
| [PaletteGroupBar1.BackColor = Color.Cornsilk;]                                |
|                                                                                                                   |
| [PaletteGroupBar1.BorderColor = Color.Navy;]                                  |
|                                                                                                                   |
| [PaletteGroupBar1.BorderStyle = [BorderStyle].Solid;] |
|                                                                                                                   |
| [PaletteGroupBar1.SelectedItemColor = Color.Salmon;]                          |
+-------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

[] 

Figure 15: PaletteGroupBar

**[]** 

Loading Files

**[]** 

1.   To display a diagram in the PaletteGroupBar, click the **Load EDD File** button, select required \*.edd file and run the application. The diagram is displayed.

2.   To display a palette file in the PaletteGroupView, click the **Load EDP File** button, select the required \*.edp file and run the application. The palette file is displayed.

[] 

***[]*** 

***[]*** 


 

{border="0"}Note: While loading older versions of palette files, the OldToNewDeserializationBinder class is used by the control. The class helps achieve compatibility between the versions using its BindToType method which performs binding of serialized object to a type. The following example illustrates a scenario where the old types in the older palette files are bound to the new types in the current palette files-Line Node type has been bound to Line type.


[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                              |
|                                                                                                                                                                                                                                       |
| [sealed][ [class] [OldToNewDeserializationBinder] : SerializationBinder]                            |
|                                                                                                                                                                                                                                       |
| [{]                                                                                                                                                                                               |
|                                                                                                                                                                                                                                       |
| [    [public] [override] [Type] BindToType([string] assemblyName, [string] typeName)] |
|                                                                                                                                                                                                                                       |
| [    {]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                       |
| [        [Type] typeToDeserialize;]                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [        [// For each assemblyName/typeName that you want to deserialize to]]                                                                                               |
|                                                                                                                                                                                                                                       |
| [        [// a different type, set typeToDeserialize to the desired type.]]                                                                                                 |
|                                                                                                                                                                                                                                       |
| [        [if] (typeName.IndexOf([\"LineNode\"]) != -1)]                                                                                              |
|                                                                                                                                                                                                                                       |
| [        {]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| [            [// types binding to ensure loading previous versions]]                                                                                                        |
|                                                                                                                                                                                                                                       |
| [            typeName = typeName.Replace([\"LineNode\"], [\"Line\"]);]                                                                            |
|                                                                                                                                                                                                                                       |
| [        }]                                                                                                                                                                                       |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [        [// The following line of code returns the type.]]                                                                                                                 |
|                                                                                                                                                                                                                                       |
| [        typeToDeserialize = [Type].GetType([String].Format([\"{0}, {1}\"], typeName, assemblyName));]                    |
|                                                                                                                                                                                                                                       |
| []                                                                                                                                                                                                |
|                                                                                                                                                                                                                                       |
| [        [return] typeToDeserialize;]                                                                                                                                        |
|                                                                                                                                                                                                                                       |
| [    }]                                                                                                                                                                                           |
|                                                                                                                                                                                                                                       |
| [}]                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

