SCHEMA = {
  "typeName" : "AWS::LakeFormation::DataCellsFilter",
  "description" : "A resource schema representing a Lake Formation Data Cells Filter.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "CatalogIdString" : {
      "description" : "A string representing the Catalog Id.",
      "type" : "string",
      "minLength" : 12,
      "maxLength" : 12
    },
    "NameString" : {
      "description" : "A string representing a resource's name.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "RowFilter" : {
      "description" : "An object representing the Data Cells Filter's Row Filter. Either a Filter Expression or a Wildcard is required.",
      "type" : "object",
      "properties" : {
        "FilterExpression" : {
          "description" : "A PartiQL predicate.",
          "type" : "string"
        },
        "AllRowsWildcard" : {
          "description" : "An empty object representing a row wildcard.",
          "type" : "object",
          "additionalProperties" : False
        }
      },
      "additionalProperties" : False
    },
    "ColumnNames" : {
      "description" : "A list of column names.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/NameString"
      }
    },
    "ColumnWildcard" : {
      "description" : "An object representing the Data Cells Filter's Columns. Either Column Names or a Wildcard is required.",
      "type" : "object",
      "properties" : {
        "ExcludedColumnNames" : {
          "description" : "A list of column names to be excluded from the Data Cells Filter.",
          "$ref" : "#/definitions/ColumnNames"
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "TableCatalogId" : {
      "description" : "The Catalog Id of the Table on which to create a Data Cells Filter.",
      "$ref" : "#/definitions/CatalogIdString"
    },
    "DatabaseName" : {
      "description" : "The name of the Database that the Table resides in.",
      "$ref" : "#/definitions/NameString"
    },
    "TableName" : {
      "description" : "The name of the Table to create a Data Cells Filter for.",
      "$ref" : "#/definitions/NameString"
    },
    "Name" : {
      "description" : "The desired name of the Data Cells Filter.",
      "$ref" : "#/definitions/NameString"
    },
    "RowFilter" : {
      "description" : "An object representing the Data Cells Filter's Row Filter. Either a Filter Expression or a Wildcard is required",
      "$ref" : "#/definitions/RowFilter"
    },
    "ColumnNames" : {
      "description" : "A list of columns to be included in this Data Cells Filter.",
      "$ref" : "#/definitions/ColumnNames"
    },
    "ColumnWildcard" : {
      "description" : "An object representing the Data Cells Filter's Columns. Either Column Names or a Wildcard is required",
      "$ref" : "#/definitions/ColumnWildcard"
    }
  },
  "additionalProperties" : False,
  "required" : [ "TableCatalogId", "DatabaseName", "TableName", "Name" ],
  "createOnlyProperties" : [ "/properties/TableCatalogId", "/properties/DatabaseName", "/properties/TableName", "/properties/Name", "/properties/RowFilter", "/properties/ColumnNames", "/properties/ColumnWildcard" ],
  "replacementStrategy" : "delete_then_create",
  "tagging" : {
    "taggable" : False
  },
  "primaryIdentifier" : [ "/properties/TableCatalogId", "/properties/DatabaseName", "/properties/TableName", "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lakeformation:CreateDataCellsFilter", "glue:GetTable" ]
    },
    "delete" : {
      "permissions" : [ "lakeformation:DeleteDataCellsFilter" ]
    },
    "read" : {
      "permissions" : [ "lakeformation:ListDataCellsFilter" ]
    },
    "list" : {
      "permissions" : [ "lakeformation:ListDataCellsFilter" ]
    }
  }
}