---
title: "])\]] |
original_path: c:/workspace/sf11-winform/WinForms_Docs\03_Data_Binding\bindingbusinessobjectstotemplatemarkers.md
created_at: 2025-07-03
---






##### Binding Business Objects to Template Markers {#binding-business-objects-to-template-markers style="tab-stops: 0pt"}

[] 

The Marker Syntax with business objects is shown below:

[] 

{border="0"}[]

Figure 97

[] 

[The following code snippet illustrates the binding of data from a business object, to a marker.]

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                      |
|                                                                                                                                                                       |
|  [//Definition of the business objects]                                                                |
|                                                                                                                                                                       |
| [class][ [Sales]]              |
|                                                                                                                                                                       |
| [    {]                                                                                                              |
|                                                                                                                                                                       |
| [        [private] [string] m_salesPerson;]                                |
|                                                                                                                                                                       |
| [        [private] [int] m_sold;]                                          |
|                                                                                                                                                                       |
| []                                                                                                                   |
|                                                                                                                                                                       |
| [        [public] [string] SalesPerson]                                    |
|                                                                                                                                                                       |
| [        {]                                                                                                          |
|                                                                                                                                                                       |
| [            [get]]                                                                             |
|                                                                                                                                                                       |
| [            {]                                                                                                      |
|                                                                                                                                                                       |
| [                [return] m_salesPerson;]                                                       |
|                                                                                                                                                                       |
| [            }]                                                                                                      |
|                                                                                                                                                                       |
| [            [set]]                                                                             |
|                                                                                                                                                                       |
| [            {]                                                                                                      |
|                                                                                                                                                                       |
| [                m_salesPerson = [value];]                                                      |
|                                                                                                                                                                       |
| [            }]                                                                                                      |
|                                                                                                                                                                       |
| [        }]                                                                                                          |
|                                                                                                                                                                       |
| []                                                                                                                   |
|                                                                                                                                                                       |
| [        [public] [int] Sold]                                              |
|                                                                                                                                                                       |
| [        {]                                                                                                          |
|                                                                                                                                                                       |
| [            [get]]                                                                             |
|                                                                                                                                                                       |
| [            {]                                                                                                      |
|                                                                                                                                                                       |
| [                [return] m_sold ;]                                                             |
|                                                                                                                                                                       |
| [            }]                                                                                                      |
|                                                                                                                                                                       |
| [            [set]]                                                                             |
|                                                                                                                                                                       |
| [            {]                                                                                                      |
|                                                                                                                                                                       |
| [                m_sold = [value];]                                                             |
|                                                                                                                                                                       |
| [            }]                                                                                                      |
|                                                                                                                                                                       |
| []                                                                                                                   |
|                                                                                                                                                                       |
| [        }]                                                                                                          |
|                                                                                                                                                                       |
| [        [public] Customer([string] name,[int] sold)] |
|                                                                                                                                                                       |
| [        {]                                                                                                          |
|                                                                                                                                                                       |
| [            [this].m_salesPerson = name;]                                                      |
|                                                                                                                                                                       |
| [            [this].m_sold = sold;]                                                             |
|                                                                                                                                                                       |
| [        }]                                                                                                          |
|                                                                                                                                                                       |
| [    }]                                                                                                              |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
| [// Creating Template Marker Processor]                                                                             |
|                                                                                                                                                                       |
| [// Northwind Customers Table]                                                                                      |
|                                                                                                                                                                       |
| [ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();]                                                   |
|                                                                                                                                                                       |
| [marker.AddVariable([\"Sales\"], arrSalesPerson);]                                           |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
|                                                                                                                                                                       |
| [// Processing the markers in the template]                                                                         |
|                                                                                                                                                                       |
| [marker.ApplyMarkers();]                                                                                                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Template Marker representing the HeaderName and NumberFormat

**[]** 

[The following code example illustrates the binding of data from a business object to a marker, with the NumberFormat and HeaderName arguments.]

[] 

{border="0"}

Figure 98

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                             |
|  [//Definition of the business objects with the marker argument][]          |
|                                                                                                                                                                                             |
| [    [class] [Sales]]                                                                         |
|                                                                                                                                                                                             |
| [    {]                                                                                                                                    |
|                                                                                                                                                                                             |
| [        [private] [string] m_salesPerson;]                                                      |
|                                                                                                                                                                                             |
| [        [private] [int] m_sold;]                                                                |
|                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                             |
| [        [public] [string] SalesPerson]                                                          |
|                                                                                                                                                                                             |
| [        {]                                                                                                                                |
|                                                                                                                                                                                             |
| [            [get]]                                                                                                   |
|                                                                                                                                                                                             |
| [            {]                                                                                                                            |
|                                                                                                                                                                                             |
| [                [return] m_salesPerson;]                                                                             |
|                                                                                                                                                                                             |
| [            }]                                                                                                                            |
|                                                                                                                                                                                             |
| [            [set]]                                                                                                   |
|                                                                                                                                                                                             |
| [            {]                                                                                                                            |
|                                                                                                                                                                                             |
| [                m_salesPerson = [value];]                                                                            |
|                                                                                                                                                                                             |
| [            }]                                                                                                                            |
|                                                                                                                                                                                             |
| [        }]                                                                                                                                |
|                                                                                                                                                                                             |
| [        \[[TemplateMarkerAttributes]([\"Sold\"],[\"\$#,###\"])\]] |
|                                                                                                                                                                                             |
| [        [public] [int] Sold]                                                                    |
|                                                                                                                                                                                             |
| [        {]                                                                                                                                |
|                                                                                                                                                                                             |
| [            [get]]                                                                                                   |
|                                                                                                                                                                                             |
| [            {]                                                                                                                            |
|                                                                                                                                                                                             |
| [                [return] m_sold ;]                                                                                   |
|                                                                                                                                                                                             |
| [            }]                                                                                                                            |
|                                                                                                                                                                                             |
| [            [set]]                                                                                                   |
|                                                                                                                                                                                             |
| [            {]                                                                                                                            |
|                                                                                                                                                                                             |
| [                m_sold = [value];]                                                                                   |
|                                                                                                                                                                                             |
| [            }]                                                                                                                            |
|                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                             |
| [        }]                                                                                                                                |
|                                                                                                                                                                                             |
| [        [public] Sales()]                                                                                            |
|                                                                                                                                                                                             |
| [        {]                                                                                                                                |
|                                                                                                                                                                                             |
| [        }]                                                                                                                                |
|                                                                                                                                                                                             |
| [        [public] Sales([string] name,[int] sold)]                          |
|                                                                                                                                                                                             |
| [        {]                                                                                                                                |
|                                                                                                                                                                                             |
| [            [this].m_salesPerson = name;]                                                                            |
|                                                                                                                                                                                             |
| [            [this].m_sold = sold;]                                                                                   |
|                                                                                                                                                                                             |
| [        }]                                                                                                                                |
|                                                                                                                                                                                             |
| [    }]                                                                                                                                    |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
| [// Creating the Template Marker Processor]                                                                                               |
|                                                                                                                                                                                             |
| [// Northwind Customers Table]                                                                                                            |
|                                                                                                                                                                                             |
| [ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();]                                                                         |
|                                                                                                                                                                                             |
| [marker.AddVariable([\"Sales\"], arrSalesPerson);]                                                                 |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
| [// Processing the markers in the template]                                                                                               |
|                                                                                                                                                                                             |
| [marker.ApplyMarkers();]                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output:

{border="0"}

Figure 99

 

Template Marker with the Class name

The following is the Marker syntax with the Class Name:

{border="0"}

Figure 100[]

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                                            |
|                                                                                                                                                                                             |
|  [//Definition of the business objects with the marker argument][]          |
|                                                                                                                                                                                             |
| [    [class] [Sales]]                                                                         |
|                                                                                                                                                                                             |
| [    {]                                                                                                                                    |
|                                                                                                                                                                                             |
| [        [private] [string] m_salesPerson;]                                                      |
|                                                                                                                                                                                             |
| [        [private] [int] m_sold;]                                                                |
|                                                                                                                                                                                             |
| [        \[[TemplateMarkerAttributes]([\"Sales Person Name\"])\]]                          |
|                                                                                                                                                                                             |
| [        [public] [string] SalesPerson]                                                          |
|                                                                                                                                                                                             |
| [        {]                                                                                                                                |
|                                                                                                                                                                                             |
| [            [get]]                                                                                                   |
|                                                                                                                                                                                             |
| [            {]                                                                                                                            |
|                                                                                                                                                                                             |
| [                [return] m_salesPerson;]                                                                             |
|                                                                                                                                                                                             |
| [            }]                                                                                                                            |
|                                                                                                                                                                                             |
| [            [set]]                                                                                                   |
|                                                                                                                                                                                             |
| [            {]                                                                                                                            |
|                                                                                                                                                                                             |
| [                m_salesPerson = [value];]                                                                            |
|                                                                                                                                                                                             |
| [            }]                                                                                                                            |
|                                                                                                                                                                                             |
| [        }]                                                                                                                                |
|                                                                                                                                                                                             |
| [        \[[TemplateMarkerAttributes]([\"Sold\"],[\"\$#,###\"])\]] |
|                                                                                                                                                                                             |
| [        [public] [int] Sold]                                                                    |
|                                                                                                                                                                                             |
| [        {]                                                                                                                                |
|                                                                                                                                                                                             |
| [            [get]]                                                                                                   |
|                                                                                                                                                                                             |
| [            {]                                                                                                                            |
|                                                                                                                                                                                             |
| [                [return] m_sold ;]                                                                                   |
|                                                                                                                                                                                             |
| [            }]                                                                                                                            |
|                                                                                                                                                                                             |
| [            [set]]                                                                                                   |
|                                                                                                                                                                                             |
| [            {]                                                                                                                            |
|                                                                                                                                                                                             |
| [                m_sold = [value];]                                                                                   |
|                                                                                                                                                                                             |
| [            }]                                                                                                                            |
|                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                             |
| [        }]                                                                                                                                |
|                                                                                                                                                                                             |
| [        [public] Sales()]                                                                                            |
|                                                                                                                                                                                             |
| [        {]                                                                                                                                |
|                                                                                                                                                                                             |
| [        }]                                                                                                                                |
|                                                                                                                                                                                             |
| [        [public] Sales([string] name,[int] sold)]                          |
|                                                                                                                                                                                             |
| [        {]                                                                                                                                |
|                                                                                                                                                                                             |
| [            [this].m_salesPerson = name;]                                                                            |
|                                                                                                                                                                                             |
| [            [this].m_sold = sold;]                                                                                   |
|                                                                                                                                                                                             |
| [        }]                                                                                                                                |
|                                                                                                                                                                                             |
| [    }]                                                                                                                                    |
|                                                                                                                                                                                             |
| []                                                                                                                                         |
|                                                                                                                                                                                             |
| [// Creating Template Marker Processor]                                                                                                   |
|                                                                                                                                                                                             |
| [// Northwind Customers Table]                                                                                                            |
|                                                                                                                                                                                             |
| [ITemplateMarkersProcessor marker = workbook.CreateTemplateMarkersProcessor();]                                                                         |
|                                                                                                                                                                                             |
| [marker.AddVariable([\"Sales\"], arrSalesPerson);]                                                                 |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
|                                                                                                                                                                                             |
| [// Processing the markers in the template]                                                                                               |
|                                                                                                                                                                                             |
| [marker.ApplyMarkers();]                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

Output

{border="0"}

Figure 101

 

[]{#related-topics}

