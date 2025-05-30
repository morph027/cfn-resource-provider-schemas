SCHEMA = {
  "typeName" : "AWS::Glue::Table",
  "description" : "Resource Type definition for AWS::Glue::Table",
  "additionalProperties" : False,
  "properties" : {
    "DatabaseName" : {
      "type" : "string"
    },
    "TableInput" : {
      "$ref" : "#/definitions/TableInput"
    },
    "OpenTableFormatInput" : {
      "$ref" : "#/definitions/OpenTableFormatInput"
    },
    "Id" : {
      "type" : "string"
    },
    "CatalogId" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "TableIdentifier" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "DatabaseName" : {
          "type" : "string"
        },
        "Region" : {
          "type" : "string"
        },
        "CatalogId" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "Order" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Column" : {
          "type" : "string"
        },
        "SortOrder" : {
          "type" : "integer"
        }
      },
      "required" : [ "Column", "SortOrder" ]
    },
    "SchemaReference" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SchemaId" : {
          "$ref" : "#/definitions/SchemaId"
        },
        "SchemaVersionId" : {
          "type" : "string"
        },
        "SchemaVersionNumber" : {
          "type" : "integer"
        }
      }
    },
    "TableInput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Owner" : {
          "type" : "string"
        },
        "ViewOriginalText" : {
          "type" : "string"
        },
        "Description" : {
          "type" : "string"
        },
        "TableType" : {
          "type" : "string"
        },
        "Parameters" : {
          "type" : "object"
        },
        "ViewExpandedText" : {
          "type" : "string"
        },
        "StorageDescriptor" : {
          "$ref" : "#/definitions/StorageDescriptor"
        },
        "TargetTable" : {
          "$ref" : "#/definitions/TableIdentifier"
        },
        "PartitionKeys" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/Column"
          }
        },
        "Retention" : {
          "type" : "integer"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "MetadataOperation" : {
      "type" : "object",
      "additionalProperties" : False
    },
    "OpenTableFormatInput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "IcebergInput" : {
          "$ref" : "#/definitions/IcebergInput"
        }
      }
    },
    "SkewedInfo" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SkewedColumnValues" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "SkewedColumnValueLocationMaps" : {
          "type" : "object"
        },
        "SkewedColumnNames" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        }
      }
    },
    "Column" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Comment" : {
          "type" : "string"
        },
        "Type" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      },
      "required" : [ "Name" ]
    },
    "StorageDescriptor" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "StoredAsSubDirectories" : {
          "type" : "boolean"
        },
        "Parameters" : {
          "type" : "object"
        },
        "BucketColumns" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "NumberOfBuckets" : {
          "type" : "integer"
        },
        "OutputFormat" : {
          "type" : "string"
        },
        "Columns" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/Column"
          }
        },
        "SerdeInfo" : {
          "$ref" : "#/definitions/SerdeInfo"
        },
        "SortColumns" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/Order"
          }
        },
        "Compressed" : {
          "type" : "boolean"
        },
        "SchemaReference" : {
          "$ref" : "#/definitions/SchemaReference"
        },
        "SkewedInfo" : {
          "$ref" : "#/definitions/SkewedInfo"
        },
        "InputFormat" : {
          "type" : "string"
        },
        "Location" : {
          "type" : "string"
        }
      }
    },
    "SchemaId" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "RegistryName" : {
          "type" : "string"
        },
        "SchemaName" : {
          "type" : "string"
        },
        "SchemaArn" : {
          "type" : "string"
        }
      }
    },
    "IcebergInput" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MetadataOperation" : {
          "$ref" : "#/definitions/MetadataOperation"
        },
        "Version" : {
          "type" : "string"
        }
      }
    },
    "SerdeInfo" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Parameters" : {
          "type" : "object"
        },
        "SerializationLibrary" : {
          "type" : "string"
        },
        "Name" : {
          "type" : "string"
        }
      }
    }
  },
  "required" : [ "TableInput", "DatabaseName", "CatalogId" ],
  "createOnlyProperties" : [ "/properties/DatabaseName", "/properties/CatalogId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}