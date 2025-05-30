SCHEMA = {
  "typeName" : "AWS::Glue::SchemaVersion",
  "description" : "This resource represents an individual schema version of a schema defined in Glue Schema Registry.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-glue.git",
  "definitions" : {
    "Schema" : {
      "description" : "Identifier for the schema where the schema version will be created.",
      "type" : "object",
      "properties" : {
        "SchemaArn" : {
          "description" : "Amazon Resource Name for the Schema. This attribute can be used to uniquely represent the Schema.",
          "type" : "string",
          "pattern" : "arn:(aws|aws-us-gov|aws-cn):glue:.*"
        },
        "SchemaName" : {
          "description" : "Name of the schema. This parameter requires RegistryName to be provided.",
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 255
        },
        "RegistryName" : {
          "description" : "Name of the registry to identify where the Schema is located.",
          "type" : "string",
          "maxLength" : 255,
          "minLength" : 1
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Schema" : {
      "$ref" : "#/definitions/Schema"
    },
    "SchemaDefinition" : {
      "type" : "string",
      "description" : "Complete definition of the schema in plain-text.",
      "minLength" : 1,
      "maxLength" : 170000
    },
    "VersionId" : {
      "type" : "string",
      "description" : "Represents the version ID associated with the schema version.",
      "pattern" : "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
    }
  },
  "required" : [ "Schema", "SchemaDefinition" ],
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/VersionId" ],
  "createOnlyProperties" : [ "/properties/Schema", "/properties/SchemaDefinition" ],
  "primaryIdentifier" : [ "/properties/VersionId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "glue:RegisterSchemaVersion", "glue:GetSchemaVersion", "glue:GetSchemaByDefinition" ]
    },
    "read" : {
      "permissions" : [ "glue:GetSchemaVersion" ]
    },
    "delete" : {
      "permissions" : [ "glue:DeleteSchemaVersions", "glue:GetSchemaVersion" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "Schema" : {
            "$ref" : "resource-schema.json#/properties/Schema"
          }
        },
        "required" : [ "Schema" ]
      },
      "permissions" : [ "glue:ListSchemaVersions" ]
    }
  }
}