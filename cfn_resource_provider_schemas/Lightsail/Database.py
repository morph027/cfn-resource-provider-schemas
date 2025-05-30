SCHEMA = {
  "typeName" : "AWS::Lightsail::Database",
  "description" : "Resource Type definition for AWS::Lightsail::Database",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lightsail.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key" ],
      "additionalProperties" : False
    },
    "RelationalDatabaseParameter" : {
      "description" : "Describes the parameters of the database.",
      "type" : "object",
      "properties" : {
        "AllowedValues" : {
          "type" : "string",
          "description" : "Specifies the valid range of values for the parameter."
        },
        "ApplyMethod" : {
          "type" : "string",
          "description" : "Indicates when parameter updates are applied. Can be immediate or pending-reboot."
        },
        "ApplyType" : {
          "type" : "string",
          "description" : "Specifies the engine-specific parameter type."
        },
        "DataType" : {
          "type" : "string",
          "description" : "Specifies the valid data type for the parameter."
        },
        "Description" : {
          "type" : "string",
          "description" : "Provides a description of the parameter."
        },
        "IsModifiable" : {
          "type" : "boolean",
          "description" : "A Boolean value indicating whether the parameter can be modified."
        },
        "ParameterName" : {
          "type" : "string",
          "description" : "Specifies the name of the parameter."
        },
        "ParameterValue" : {
          "type" : "string",
          "description" : "Specifies the value of the parameter."
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "RelationalDatabaseName" : {
      "description" : "The name to use for your new Lightsail database resource.",
      "type" : "string",
      "pattern" : "\\w[\\w\\-]*\\w",
      "minLength" : 2,
      "maxLength" : 255
    },
    "DatabaseArn" : {
      "type" : "string"
    },
    "AvailabilityZone" : {
      "description" : "The Availability Zone in which to create your new database. Use the us-east-2a case-sensitive format.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "RelationalDatabaseBlueprintId" : {
      "description" : "The blueprint ID for your new database. A blueprint describes the major engine version of a database.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "RelationalDatabaseBundleId" : {
      "description" : "The bundle ID for your new database. A bundle describes the performance specifications for your database.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "MasterDatabaseName" : {
      "description" : "The name of the database to create when the Lightsail database resource is created. For MySQL, if this parameter isn't specified, no database is created in the database resource. For PostgreSQL, if this parameter isn't specified, a database named postgres is created in the database resource.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "MasterUsername" : {
      "description" : "The name for the master user.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 63
    },
    "MasterUserPassword" : {
      "description" : "The password for the master user. The password can include any printable ASCII character except \"/\", \"\"\", or \"@\". It cannot contain spaces.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 63
    },
    "PreferredBackupWindow" : {
      "description" : "The daily time range during which automated backups are created for your new database if automated backups are enabled.",
      "type" : "string"
    },
    "PreferredMaintenanceWindow" : {
      "description" : "The weekly time range during which system maintenance can occur on your new database.",
      "type" : "string"
    },
    "PubliclyAccessible" : {
      "description" : "Specifies the accessibility options for your new database. A value of True specifies a database that is available to resources outside of your Lightsail account. A value of False specifies a database that is available only to your Lightsail resources in the same region as your database.",
      "type" : "boolean"
    },
    "CaCertificateIdentifier" : {
      "description" : "Indicates the certificate that needs to be associated with the database.",
      "type" : "string"
    },
    "BackupRetention" : {
      "description" : "When True, enables automated backup retention for your database. Updates are applied during the next maintenance window because this can result in an outage.",
      "type" : "boolean"
    },
    "RotateMasterUserPassword" : {
      "description" : "When True, the master user password is changed to a new strong password generated by Lightsail. Use the get relational database master user password operation to get the new password.",
      "type" : "boolean"
    },
    "RelationalDatabaseParameters" : {
      "description" : "Update one or more parameters of the relational database.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/RelationalDatabaseParameter"
      }
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "RelationalDatabaseName", "RelationalDatabaseBlueprintId", "RelationalDatabaseBundleId", "MasterDatabaseName", "MasterUsername" ],
  "readOnlyProperties" : [ "/properties/DatabaseArn" ],
  "writeOnlyProperties" : [ "/properties/MasterUserPassword", "/properties/RelationalDatabaseParameters", "/properties/RotateMasterUserPassword" ],
  "primaryIdentifier" : [ "/properties/RelationalDatabaseName" ],
  "createOnlyProperties" : [ "/properties/RelationalDatabaseName", "/properties/AvailabilityZone", "/properties/RelationalDatabaseBlueprintId", "/properties/RelationalDatabaseBundleId", "/properties/MasterDatabaseName", "/properties/MasterUsername" ],
  "propertyTransform" : {
    "/properties/PreferredMaintenanceWindow" : "$lowercase(PreferredMaintenanceWindow)"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:CreateRelationalDatabase", "lightsail:GetRelationalDatabase", "lightsail:GetRelationalDatabases", "lightsail:GetRegions", "lightsail:TagResource", "lightsail:UntagResource", "lightsail:UpdateRelationalDatabase", "lightsail:UpdateRelationalDatabaseParameters" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetRelationalDatabase", "lightsail:GetRelationalDatabases" ]
    },
    "update" : {
      "permissions" : [ "lightsail:GetRelationalDatabase", "lightsail:GetRelationalDatabases", "lightsail:TagResource", "lightsail:UntagResource", "lightsail:UpdateRelationalDatabase", "lightsail:UpdateRelationalDatabaseParameters" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:DeleteRelationalDatabase", "lightsail:GetRelationalDatabase", "lightsail:GetRelationalDatabases" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetRelationalDatabases" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "lightsail:TagResource", "lightsail:UntagResource" ]
  }
}