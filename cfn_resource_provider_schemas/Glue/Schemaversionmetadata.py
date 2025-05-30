SCHEMA = {
  "typeName" : "AWS::Glue::SchemaVersionMetadata",
  "description" : "This resource adds Key-Value metadata to a Schema version of Glue Schema Registry.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-glue.git",
  "properties" : {
    "SchemaVersionId" : {
      "type" : "string",
      "description" : "Represents the version ID associated with the schema version.",
      "pattern" : "[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"
    },
    "Key" : {
      "type" : "string",
      "description" : "Metadata key",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Value" : {
      "type" : "string",
      "description" : "Metadata value",
      "minLength" : 1,
      "maxLength" : 256
    }
  },
  "required" : [ "SchemaVersionId", "Key", "Value" ],
  "additionalProperties" : False,
  "createOnlyProperties" : [ "/properties/SchemaVersionId", "/properties/Key", "/properties/Value" ],
  "primaryIdentifier" : [ "/properties/SchemaVersionId", "/properties/Key", "/properties/Value" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "glue:putSchemaVersionMetadata" ]
    },
    "read" : {
      "permissions" : [ "glue:querySchemaVersionMetadata" ]
    },
    "delete" : {
      "permissions" : [ "glue:removeSchemaVersionMetadata" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "SchemaVersionId" : {
            "$ref" : "resource-schema.json#/properties/SchemaVersionId"
          }
        },
        "required" : [ "SchemaVersionId" ]
      },
      "permissions" : [ "glue:querySchemaVersionMetadata" ]
    }
  }
}