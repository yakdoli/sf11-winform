---
title: intellisensesupport.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\intellisensesupport.md
created_at: 2025-07-03
---








  









### IntelliSense Support {#intellisense-support style="tab-stops: 0pt"}

Essential Edit for WPF provides Visual Studio like **IntelliSense** support. With **IntelliSense** support users can quickly choose the possible words while typing text in the control.

[] 

**IntelliSense** support in Edit WPF facilitates the users to select possible words while typing text in the **EditControl**

[] 

When users type the text in the **EditControl**, it displays a list of possible words in a popup. Users can navigate, using **Up** and **Down** arrow keys or mouse and Scrollbar, to appropriate items. Select an item from the list to append to the text in the **EditControl.**

[] 

Important Features

[·      ]**IntelliSense** in Edit WPF works in two modes namely **Auto** or **Custom**.

[o  ]**Auto mode**---This automatically generates the list of items to be displayed from the pre-built assemblies specified in **AssemblyReferences** property. This mode of operation is currently support for **C#** and **Visual Basic** language respectively.

[o  ]**Custom mode**---This enables the users to provide the list of items to be displayed in the **IntelliSense**.

[·      ]Exclusive properties in **EditControl** enable the users to customize the look and feel of the **IntelliSense** popup and its items.

This provides the facility to modify the characters on which the selected item to be appended to the text similar to that of **Visual Studio IntelliSense** settings. It also provides options to enable or disable appending text when space bar is pressed.

[] 

Customization of IntelliSense Modes

**IntelliSense** in Edit WPF works in two modes: **Auto** and **Custom.**  **IntelliSense** modes can be switched by using **IntelliSenseMode** property in **EditControl** class. It is an enum of the type of **IntelliSenseMode**. By default, **IntelliSenseMode** property is set to **Auto**.

[] 

Auto Mode

In Auto mode, **EditControl** generates the **IntelliSense** list box items similar to **Visual Studio** based on the current language configurations **(Lexem).** **IntelliSense** also displays **Types**, **Properties**, **Events** and **Methods** from pre-built assemblies specified using **AssemblyReferences** property of **EditControl** class.

[] 


{border="0"}Note: Auto IntelliSense mode is currently supported for C# and Visual Basic languages and will be extended to other markup languages supported by EditControl in forthcoming releases.


[] 

Adding EditControl to the application

Add **EditControl** to the application and set its **IntelliSenseMode** to **Auto**, by using the following code.

[] 

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<!\--Adding EditControl to application and setting its IntelliSenseMode to Auto\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [\<][syncfusion][:][EditContro**l**][ Background][=\"White\"][ Name][=\"EditControl1\"][ IntelliSenseMode][=\"Auto\"/\>] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

**[]** 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                           |
| [            [ObservableCollection]\<[Uri]\> uriList = [new] [ObservableCollection]\<[Uri]\>();] |
|                                                                                                                                                                                                                                                           |
| [            uriList.Add([new] [Uri]([@\"C:\\Assemblies\\Syncfusion.Chart.WPF\"]));]                                                             |
|                                                                                                                                                                                                                                                           |
| [            EditControl1.AssemblyReferences = uriList;]                                                                                                                                                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: Having an INotifyCollectionChanged implemented collection as AssemblyReferences will update the IntelliSense items automatically when an assembly reference is added at runtime.


[] 

{border="0"}

Figure 45: IntelliSense Displaying Types From Pre-built Assembly Based on the Namespaces Included

**[]** 

**[]** 

Custom Mode

**IntelliSense** support in Edit WPF enables users to bind collections of their business object as an **ItemsSource** of **IntelliSenseListBox**. It also provides the flexibility to change the **ItemTemplate** of the **IntelliSenseListBox** to suite their business object or requirements.

[] 

This ensures that their business object is implemented from **IIntelliSenseItem** interface to make their business object compatible with the **IntelliSenseListBox**. **EditControl** has exclusive properties implemented to enable the users bind custom collections and apply custom **ItemTemplates**.

[] 

[·      ]**IntelliSenseMode**---Set **IntelliSense**Mode property to **Custom** to apply a custom **ItemsSource** to **IntelliSense.**

[·      ]**IntelliSenseCustomItemsSource**---**IEnumerable** type of property to bind custom **ItemsSource** to **IntelliSense** **ListBox**.

[·      ]**IntelliSenseItemTemplate**---**DataTemplate** type of property to apply custom **ItemTemplate** to **IntelliSense ListBox**.

 

Creating DataTemplate in the ResourceDictionary

Create DataTemplate in the **ResourceDictionary** to apply it as **IntellisenseItemTemplate** property of **EditControl,** by using the following code.

[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [\<!\--Resources\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        ][\<][DataTemplate][ x][:][Key][=\"CustomIntelliSenseItemTemplate\"\>]                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            ][\<][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                ][\<][Grid.ColumnDefinitions][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                    ][\<][ColumnDefinition][ Width][=\"Auto\"/\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                    ][\<][ColumnDefinition][ Width][=\"\*\"/\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                ][\</][Grid.ColumnDefinitions][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                ][\<][Image][ Source][=\"{][Binding][ Icon][}\"][ MaxHeight][=\"16\"][ MaxWidth][=\"16\"][ Margin][=\"3\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [                ][\<][TextBlock][ Text][=\"{][Binding][ Text][}\"][ Grid.Column][=\"1\"][ Margin][=\"3\"/\>]                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [            ][\</][Grid][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [        ][\</][DataTemplate][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

Apply **IntellisenseMode** and **IntellisenseItemTemplate** properties, by using the following code.

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [\<!\--Adding EditControl to application and setting its IntelliSenseMode to Custom\--\>]                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [\<][syncfusion][:][EditControl][ Background][=\"White\"][ Name][=\"EditControl1\"][ ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [IntelliSenseMode][=\"Custom\"][ ]                                                                                                                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [                               [ IntelliSens**e**ItemTemplate][=\"{][StaticResource][ ]]                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [CustomIntelliSenseItemTemplate][}\"/\>]                                                                                                                                                                                                                                                                                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Creating a Custom Business Object

**[]** 

Create a custom business object implemented using **IIntellisenseItem** interface, by using the following code**.**

**[]** 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                          |
|                                                                                                                                                                                                         |
| **[Business Object]**                                                                                                                                 |
|                                                                                                                                                                                                         |
| **[]**                                                                                                                                                |
|                                                                                                                                                                                                         |
| [  [///][ ][\<summary\>]]                                                                           |
|                                                                                                                                                                                                         |
| [    [///][ Business object implemented from IIntelliSenseItem interface in ]]                                           |
|                                                                                                                                                                                                         |
| [    [///][ Syncfusion.Windows.Edit namespace]]                                                                          |
|                                                                                                                                                                                                         |
| [    [///][ ][\</summary\>]]                                                                        |
|                                                                                                                                                                                                         |
| [    [public] [class] [CustomIntelliSenseItem] : [IIntelliSens**e**Item]] |
|                                                                                                                                                                                                         |
| [    {]                                                                                                                                                             |
|                                                                                                                                                                                                         |
| [        #region][ IIntelliSenseItem Members]                                                                      |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [        [///][ ][\<summary\>]]                                                                     |
|                                                                                                                                                                                                         |
| [        [///][ Gets or set a value indicating Icon to be displayed in the IntelliSenseListBox]]                         |
|                                                                                                                                                                                                         |
| [        [///][ ][\</summary\>]]                                                                    |
|                                                                                                                                                                                                         |
| [        [public] [ImageSource] Icon]                                                                                  |
|                                                                                                                                                                                                         |
| [        {]                                                                                                                                                         |
|                                                                                                                                                                                                         |
| [            [get];]                                                                                                                           |
|                                                                                                                                                                                                         |
| [            [set];]                                                                                                                           |
|                                                                                                                                                                                                         |
| [        }]                                                                                                                                                         |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [        [///][ ][\<summary\>]]                                                                     |
|                                                                                                                                                                                                         |
| [        [///][ Gets or set a value indicating Text to be displayed in the IntelliSenseListBox]]                         |
|                                                                                                                                                                                                         |
| [        [///][ ][\</summary\>]]                                                                    |
|                                                                                                                                                                                                         |
| [        [public] [string] Text]                                                                                          |
|                                                                                                                                                                                                         |
| [        {]                                                                                                                                                         |
|                                                                                                                                                                                                         |
| [            [get];]                                                                                                                           |
|                                                                                                                                                                                                         |
| [            [set];]                                                                                                                           |
|                                                                                                                                                                                                         |
| [        }]                                                                                                                                                         |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [        [///][ ][\<summary\>]]                                                                     |
|                                                                                                                                                                                                         |
| [        [///][ Gets or set a collection of sub-items to be displayed]]                                                  |
|                                                                                                                                                                                                         |
| [        [///][ ][\</summary\>]]                                                                    |
|                                                                                                                                                                                                         |
| [        [public] [IEnumerable]\<[IIntelliSenseItem]\> NestedItems]                            |
|                                                                                                                                                                                                         |
| [        {]                                                                                                                                                         |
|                                                                                                                                                                                                         |
| [            [get];]                                                                                                                           |
|                                                                                                                                                                                                         |
| [            [set];]                                                                                                                           |
|                                                                                                                                                                                                         |
| [        }]                                                                                                                                                         |
|                                                                                                                                                                                                         |
| []                                                                                                                                                                  |
|                                                                                                                                                                                                         |
| [        #endregion]                                                                                                                                   |
|                                                                                                                                                                                                         |
| [    }]                                                                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

Create a Custom Collection of the Business Object

**[]** 


Now, create a Custom Collection of the Business Object and set as Custom ItemsSource using IntellisenseCustomItemsSource property, by using the following code.


[] 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Window1.xaml.cs]**                                                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                           |
|                                                                                                                                                                                                                                                                                                                                |
| [// Initializing custom business object collection ]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [            [ObservableCollection]\<[CustomIntelliSenseItem]\> customItems = [new]]                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                |
| [ [ObservableCollection]\<[CustomIntelliSenseItem]\>();]                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                |
| [            customItems.Add([new] [CustomIntelliSenseItem]()]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [                Text = [\"Syncfusion\"],]                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [                Icon = [new] [BitmapImage]([new] [Uri]([\"/CustomIntelliSenseDemo;component/Resources/syncfusion.png\"], [UriKind].Relative))]  |
|                                                                                                                                                                                                                                                                                                                                |
| [            });]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [            customItems.Add([new] [CustomIntelliSenseItem]()]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [                Text = [\"Silverlight\"],]                                                                                                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                |
| [                Icon = [new] [BitmapImage]([new] [Uri]([\"/CustomIntelliSenseDemo;component/Resources/silverlight.png\"], [UriKind].Relative))] |
|                                                                                                                                                                                                                                                                                                                                |
| [            });]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| [            customItems.Add([new] [CustomIntelliSenseItem]()]                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [            {]                                                                                                                                                                                                                                                                            |
|                                                                                                                                                                                                                                                                                                                                |
| [                Text = [\"WPF\"],]                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                |
| [                Icon = [new] [BitmapImage]([new] [Uri]([\"/CustomIntelliSenseDemo;component/Resources/wpf.png\"], [UriKind].Relative))]         |
|                                                                                                                                                                                                                                                                                                                                |
| [            });]                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                |
| []                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                |
| [            [// Applying custom business object collection as IntelliSenseCustomItemsSource]]                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                |
| [            EditControl1.IntelliSenseCustomItemsSource = customItems;]                                                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**[]** 

When the code runs, the following output displays**.**

**[]** 

**[]** 

**[{border="0"}][]**

Figure 46: IntelliSense displaying business object from custom collection

**[]** 

**[]** 

Customizing IntelliSense List Box Style

**EditControl** enables the users to customize the look and feel of the **IntelliSense** **listbox** by applying custom style to the **IntelliSense** **listbox**. **IntelliSenseBoxStyle** property of **EditControl** class can be used to apply custom style for **IntelliSense listbox.**

[] 

Customize the IntelliSense List Box Style, by using the following code.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<!\--Resources\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\<][Style][ x][:][Key][=\"ListBoxItemStyle\"][ TargetType][=\"ListBoxItem\"\>]                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][Setter][ Property][=\"syncfusion:SkinStorage.VisualStyle\"][ Value][=\"Default\"/\>]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][Setter][ Property][=\"Background\"][ Value][=\"AliceBlue\"/\>]                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][Setter][ Property][=\"FontSize\"][ Value][=\"11\"/\>]                                                                                                                                                                                                                                                                                                                                                                                   |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][Setter][ Property][=\"FocusVisualStyle\"][ Value][=\"{][x][:][Null][}\" /\>]                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\</][Style][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\<][Style][ x][:][Key][=\"ListBoxStyle\"][ TargetType][=\"ListBox\"\>]                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][Setter][ Property][=\"syncfusion:SkinStorage.VisualStyle\"][ Value][=\"Default\"/\>]                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][Setter][ Property][=\"Background\"][ Value][=\"White\"/\>]                                                                                                                                                                                                                                                                                                                                                                              |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [                ][\<][Setter][ Property][=\"ItemContainerStyle\"][ Value][=\"{][StaticResource][ ListBoxItemStyle][}\"/\>]                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [            ][\</][Style][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [\<][syncfusion][:]**[EditControl]**[ Grid.Row][=\"2\"][ Name][=\"editCSharp\"][ **IntelliSense**BoxStyle][=\"{][StaticResource][ ListBoxStyle][}\"/\>] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

{border="0"}

Figure 47: Before Applying IntelliSenseBoxStyle

***[\
\
]***

{border="0"}

Figure 48: After Applying IntelliSenseBoxStyle, Background color of ListBox is Changed to AliceBlue

**[]** 

Applying Multi-level IntelliSense Items in Custom Mode

As mentioned in earlier topics, **EditControl** supports applying custom collection of business objects as **IntelliSense,** when the business objects are implemented using **IIntelliSenseItem interface.** This **IIntelliSenseItem interface** has a **NestedItems** property which can be used to display sub items in **IntelliSense**. **EditControl** has a property under **CurrentLanguage** a **DrillDownChar** property of the type **char** to specify on which character press, the sub-items to be displayed in **IntelliSense**.  The default value of **DrillDownChar** is **"."** (Periods) and when users press **"."**(Periods) key **EditControl** will automatically get the collection from **NestedItems** property and displays it in the **EditControl**

**[]** 

Create **Custom** **IntelliSense** for tables and its fields for **SQL** language, by using the following code.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[XAML\]]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<!\--Resources\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        ][\<][DataTemplate][ x][:][Key][=\"CustomIntelliSenseItemTemplate\"\>]                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                ][\<][TextBlock][ Text][=\"{][Binding][ Text][}\"][ Margin][=\"3\"/\>]                                                                                                                                        |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [        ][\</][DataTemplate][\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **[]**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<!\--Adding EditControl to application and setting its IntelliSenseMode to Auto\--\>]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [\<][syncfusion][:][EditControl][ Background][=\"White\"][ Name][=\"EditControl1\"][ DocumentLanguage][=\"SQL\"][ [ IntelliSenseMode][=\"Custom\"] ] |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [                               [ IntelliSenseItemTemplate][=\"{][StaticResource][ CustomIntelliSenseItemTemplate][}\"/\>]]                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

[] 

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                      |
|                                                                                                                                                                                                     |
| **[]**                                                                                                                                            |
|                                                                                                                                                                                                     |
| **[Business Object]**                                                                                                                             |
|                                                                                                                                                                                                     |
| **[]**                                                                                                                                            |
|                                                                                                                                                                                                     |
| [  [///][ ][\<summary\>]]                                                                       |
|                                                                                                                                                                                                     |
| [    [///][ Business object implemented from IIntelliSenseItem interface in ]]                                       |
|                                                                                                                                                                                                     |
| [    [///][ Syncfusion.Windows.Edit namespace]]                                                                      |
|                                                                                                                                                                                                     |
| [    [///][ ][\</summary\>]]                                                                    |
|                                                                                                                                                                                                     |
| [    [public] [class] [CustomIntelliSenseItem] : [IIntelliSenseItem]] |
|                                                                                                                                                                                                     |
| [    {]                                                                                                                                                         |
|                                                                                                                                                                                                     |
| [        #region][ IIntelliSenseItem Members]                                                                  |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [        [///][ ][\<summary\>]]                                                                 |
|                                                                                                                                                                                                     |
| [        [///][ Gets or set a value indicating Icon to be displayed in the IntelliSenseListBox]]                     |
|                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                |
|                                                                                                                                                                                                     |
| [        [public] [ImageSource] Icon]                                                                              |
|                                                                                                                                                                                                     |
| [        {]                                                                                                                                                     |
|                                                                                                                                                                                                     |
| [            [get];]                                                                                                                       |
|                                                                                                                                                                                                     |
| [            [set];]                                                                                                                       |
|                                                                                                                                                                                                     |
| [        }]                                                                                                                                                     |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [        [///][ ][\<summary\>]]                                                                 |
|                                                                                                                                                                                                     |
| [        [///][ Gets or set a value indicating Text to be displayed in the IntelliSenseListBox]]                     |
|                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                |
|                                                                                                                                                                                                     |
| [        [public] [string] Text]                                                                                      |
|                                                                                                                                                                                                     |
| [        {]                                                                                                                                                     |
|                                                                                                                                                                                                     |
| [            [get];]                                                                                                                       |
|                                                                                                                                                                                                     |
| [            [set];]                                                                                                                       |
|                                                                                                                                                                                                     |
| [        }]                                                                                                                                                     |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [        [///][ ][\<summary\>]]                                                                 |
|                                                                                                                                                                                                     |
| [        [///][ Gets or set a collection of sub-items to be displayed]]                                              |
|                                                                                                                                                                                                     |
| [        [///][ ][\</summary\>]]                                                                |
|                                                                                                                                                                                                     |
| [        [public] [IEnumerable]\<[IIntelliSenseItem]\> NestedItems]                        |
|                                                                                                                                                                                                     |
| [        {]                                                                                                                                                     |
|                                                                                                                                                                                                     |
| [            [get];]                                                                                                                       |
|                                                                                                                                                                                                     |
| [            [set];]                                                                                                                       |
|                                                                                                                                                                                                     |
| [        }]                                                                                                                                                     |
|                                                                                                                                                                                                     |
| []                                                                                                                                                              |
|                                                                                                                                                                                                     |
| [        #endregion]                                                                                                                               |
|                                                                                                                                                                                                     |
| [    }]                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

**[]** 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[Window1.xaml.cs]**                                                                                                                                         |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                            |
|                                                                                                                                                                                                                 |
| [ObservableCollection][\<[CustomIntelliSenseItem]\> customItems = [new] ]  |
|                                                                                                                                                                                                                 |
| [ObservableCollection][\<[CustomIntelliSenseItem]\>();]                                         |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [            [//Intializing sub-items for products]]                                                                                                  |
|                                                                                                                                                                                                                 |
| [            [ObservableCollection]\<[CustomIntelliSenseItem]\> productsSubItem = [new]]               |
|                                                                                                                                                                                                                 |
| [ [ObservableCollection]\<[CustomIntelliSenseItem]\>();]                                                                    |
|                                                                                                                                                                                                                 |
| [            productsSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"ID\"] });]               |
|                                                                                                                                                                                                                 |
| [            productsSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"Name\"] });]             |
|                                                                                                                                                                                                                 |
| [            productsSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"Manufacturer\"] });]     |
|                                                                                                                                                                                                                 |
| [            productsSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"Price\"] });]            |
|                                                                                                                                                                                                                 |
| [            productsSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"OrderQuantity\"] });]    |
|                                                                                                                                                                                                                 |
| [            productsSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"Units\"] });]            |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [            [//Intializing sub-items for employee]]                                                                                                  |
|                                                                                                                                                                                                                 |
| [            [ObservableCollection]\<[CustomIntelliSenseItem]\> employeeSubItem = [new] ]              |
|                                                                                                                                                                                                                 |
| [ObservableCollection][\<[CustomIntelliSenseItem]\>();]                                         |
|                                                                                                                                                                                                                 |
| [            employeeSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"ID\"] });]               |
|                                                                                                                                                                                                                 |
| [            employeeSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"Name\"] });]             |
|                                                                                                                                                                                                                 |
| [            employeeSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"DOB\"] });]              |
|                                                                                                                                                                                                                 |
| [            employeeSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"City\"] });]             |
|                                                                                                                                                                                                                 |
| [            employeeSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"ContactNumber\"] });]    |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [            [//Intializing sub-items for customer]]                                                                                                  |
|                                                                                                                                                                                                                 |
| [            [ObservableCollection]\<[CustomIntelliSenseItem]\> customerSubItem = [new]]               |
|                                                                                                                                                                                                                 |
| [ [ObservableCollection]\<[CustomIntelliSenseItem]\>();]                                                                    |
|                                                                                                                                                                                                                 |
| [            customerSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"ID\"] });]               |
|                                                                                                                                                                                                                 |
| [            customerSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"Name\"] });]             |
|                                                                                                                                                                                                                 |
| [            customerSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"City\"] });]             |
|                                                                                                                                                                                                                 |
| [            customerSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"State\"] });]            |
|                                                                                                                                                                                                                 |
| [            customerSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"Country\"] });]          |
|                                                                                                                                                                                                                 |
| [            customerSubItem.Add([new] [CustomIntelliSenseItem]() { Text = [\"ContactNumber\"] });]    |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [            [//adding items to main collection]]                                                                                                     |
|                                                                                                                                                                                                                 |
| [            customItems.Add([new] [CustomIntelliSenseItem]() { Text = [\"Products\"], NestedItems = ] |
|                                                                                                                                                                                                                 |
| [productsSubItem });]                                                                                                                                                       |
|                                                                                                                                                                                                                 |
| [            customItems.Add([new] [CustomIntelliSenseItem]() { Text = [\"Employee\"], NestedItems = ] |
|                                                                                                                                                                                                                 |
| [employeeSubItem });]                                                                                                                                                       |
|                                                                                                                                                                                                                 |
| [            customItems.Add([new] [CustomIntelliSenseItem]() { Text = [\"Customer\"], NestedItems = ] |
|                                                                                                                                                                                                                 |
| [customerSubItem });]                                                                                                                                                       |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
|                                                                                                                                                                                                                 |
| [            [// Applying custom business object collection as IntelliSenseCustomItemsSource]]                                                        |
|                                                                                                                                                                                                                 |
| [            EditControl1.IntelliSenseCustomItemsSource = customItems;]                                                                                                     |
|                                                                                                                                                                                                                 |
| []                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[            ]

The following image illustrates IntelliSense displaying first-level of items from custom collection

[] 

[] 

[] 

{border="0"}

Figure 49: First-Level of Items from Custom Collection

*[]* 

The following image illustrates IntelliSense displaying sub-items from selected item

[] 

{border="0"}

Figure 50: Sub-Items from Selected Item

[] 

Following classes in **EditControl** will be helpful to perform various operations related to **IntelliSense**.

[] 

Table 13: Edit Control Properties related to IntelliSense


  ------------------------------- ---------------------------------------------------------------------------------------------- ------------------ -------------------------------------------------------------------------
  Name of Property                Description                                                                                    Type of Property   Value It Accepts
  EnableIntelliSense              Gets or sets a value indicating if IntelliSense Support has to be enabled or disabled.         Bool               True / false
  IntelliSenseMode                Gets or sets a value representing IntelliSense' mode of operations.                            IntelliSenseMode   IntellisenseMode.Auto / IntellisenseMode.Custom
  IntelliSenseCustomItemsSource   To specify the custom collection of business objects to be displayed in custom IntelliSense.   IEnumerable        Any collection of with items implemented using   IIntellisenseItem     
  IntelliSenseBoxStyle            IntelliSense.                                                                                  Style              Style object
  IntelliSenseItemTemplate        IntelliSense.                                                                                  DataTemplate       DataTemplate object
  ------------------------------- ---------------------------------------------------------------------------------------------- ------------------ -------------------------------------------------------------------------


[] 

[] 

[] 

Following classes in **LanguageBase** will be helpful to perform various operations related to **IntelliSense** specific to supported and custom languages. These properties can be modified in custom language classes inherited from **LanguageBase** or **ProceduralLanguageBase** or **MarkupLanguageBase** class. It can also be modified using **CurrentLanguage** property of **EditControl** class.

[] 

Table 14: LanguageBase Properties


  ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------
  Name of the Property                Description                                                                                                                                                                                               Type of the Property
  DrillDownChar                       The character specified is used to drill down to **nested items.** When the user presses the corresponding key, **IntelliSense** drills down and displays the sub-items in the **IntelliSense**.          Char
  IntelliSenseCommitCharacters        Specifies the characters when used, the **IntelliSense** should append the selected **IntelliSense** item to **EditControl's** text.                                                                      String
  CommitsIntelliSenseItemOnSpaceBar   Specifies if the selected **IntelliSense** item to be appended to the **EditControl's** text when a space bar is pressed.                                                                                 Bool
  SupportsIntelliSense                To allow or restrict **IntelliSense** auto mode in custom languages.                                                                                                                                      Bool
  ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------


[] 

[] 

**[]** 

Events

Table 15: LanguageBase  Methods


  ------------------------ ------------------------------------------------------------------------------ ----------------------------- ------------------------------------------------------------------------------------------------
  Event                    Usage                                                                          Handler Type                  Handle
  IntelliSenseBoxOpening   This event gets triggered before the **IntelliSense** popup is displayed.      IntelliSenseBoxEventHandler   Set **IsCancel** property in the **EventArgs** to cancel displaying of **IntelliSense** popup.
  IntelliSenseDrillDown    This event gets triggered when a **DrillDownChar** specified is encountered.   IntelliSenseBoxEventHandler   Set **IsCancel** property in the **EventArgs** to cancel displaying of **IntelliSense** popup.
  ------------------------ ------------------------------------------------------------------------------ ----------------------------- ------------------------------------------------------------------------------------------------


[] 

[] 

[] 

 IntelliSenseBoxEventArgs contains following arguments.

[] 

Table 16: IntelliSenseBoxEventArgsArgument


  ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  Argument      Usage
  Assemblies    Contains the list of assemblies included as **AssemblyReferences.**
  Cancel        A **bool** argument can be used to cancel the event.
  CursorIndex   Contains current cursor index where the event is triggered.
  ItemsSource   Contains the **ItemsSource** to be applied to the **IntelliSense,** it can also be changed if there are any custom **filterations** or to be done in the event.
  LineIndex     Contains current line index where the event is triggered (0 based values).
  ------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------


[] 

[] 

[]{#p40} 

[]{#related-topics}

