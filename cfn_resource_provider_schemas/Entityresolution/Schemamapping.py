SCHEMA = {
  "typeName" : "AWS::EntityResolution::SchemaMapping",
  "description" : "SchemaMapping defined in AWS Entity Resolution service",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-entity-resolution.git",
  "definitions" : {
    "EntityName" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z_0-9-]*$",
      "minLength" : 0,
      "maxLength" : 255
    },
    "Description" : {
      "type" : "string",
      "minLength" : 0,
      "maxLength" : 255
    },
    "AttributeName" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z_0-9- \\t]*$",
      "minLength" : 0,
      "maxLength" : 255
    },
    "SchemaAttributeType" : {
      "type" : "string",
      "enum" : [ "NAME", "NAME_FIRST", "NAME_MIDDLE", "NAME_LAST", "ADDRESS", "ADDRESS_STREET1", "ADDRESS_STREET2", "ADDRESS_STREET3", "ADDRESS_CITY", "ADDRESS_STATE", "ADDRESS_COUNTRY", "ADDRESS_POSTALCODE", "PHONE", "PHONE_NUMBER", "PHONE_COUNTRYCODE", "EMAIL_ADDRESS", "UNIQUE_ID", "DATE", "STRING", "PROVIDER_ID" ]
    },
    "MappedInputFields" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/SchemaInputAttribute"
      },
      "minItems" : 2,
      "maxItems" : 35,
      "insertionOrder" : False
    },
    "Hashed" : {
      "type" : "boolean"
    },
    "SchemaInputAttribute" : {
      "type" : "object",
      "properties" : {
        "FieldName" : {
          "$ref" : "#/definitions/AttributeName"
        },
        "Type" : {
          "$ref" : "#/definitions/SchemaAttributeType"
        },
        "SubType" : {
          "type" : "string",
          "description" : "The subtype of the Attribute. Would be required only when type is PROVIDER_ID"
        },
        "GroupName" : {
          "$ref" : "#/definitions/AttributeName"
        },
        "MatchKey" : {
          "$ref" : "#/definitions/AttributeName"
        },
        "Hashed" : {
          "$ref" : "#/definitions/Hashed"
        }
      },
      "required" : [ "FieldName", "Type" ],
      "additionalProperties" : False
    },
    "SchemaMappingArn" : {
      "description" : "The SchemaMapping arn associated with the Schema",
      "type" : "string",
      "pattern" : "^arn:(aws|aws-us-gov|aws-cn):entityresolution:.*:[0-9]+:(schemamapping/.*)$"
    },
    "CreatedAt" : {
      "description" : "The time of this SchemaMapping got created",
      "type" : "string"
    },
    "UpdatedAt" : {
      "description" : "The time of this SchemaMapping got last updated at",
      "type" : "string"
    },
    "HasWorkflows" : {
      "description" : "The boolean value that indicates whether or not a SchemaMapping has MatchingWorkflows that are associated with",
      "type" : "boolean"
    },
    "Tag" : {
      "description" : "A key-value pair to associate with a resource",
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
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "SchemaName" : {
      "description" : "The name of the SchemaMapping",
      "$ref" : "#/definitions/EntityName"
    },
    "Description" : {
      "description" : "The description of the SchemaMapping",
      "$ref" : "#/definitions/Description"
    },
    "MappedInputFields" : {
      "description" : "The SchemaMapping attributes input",
      "$ref" : "#/definitions/MappedInputFields"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "minItems" : 0,
      "maxItems" : 200,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "SchemaArn" : {
      "$ref" : "#/definitions/SchemaMappingArn"
    },
    "CreatedAt" : {
      "$ref" : "#/definitions/CreatedAt"
    },
    "UpdatedAt" : {
      "$ref" : "#/definitions/UpdatedAt"
    },
    "HasWorkflows" : {
      "$ref" : "#/definitions/HasWorkflows"
    }
  },
  "createOnlyProperties" : [ "/properties/SchemaName" ],
  "readOnlyProperties" : [ "/properties/SchemaArn", "/properties/CreatedAt", "/properties/UpdatedAt", "/properties/HasWorkflows" ],
  "primaryIdentifier" : [ "/properties/SchemaName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "entityresolution:TagResource", "entityresolution:UntagResource", "entityresolution:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "entityresolution:CreateSchemaMapping", "entityresolution:GetSchemaMapping", "entityresolution:TagResource" ]
    },
    "read" : {
      "permissions" : [ "entityresolution:GetSchemaMapping", "entityresolution:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "entityresolution:DeleteSchemaMapping", "entityresolution:GetSchemaMapping" ]
    },
    "update" : {
      "permissions" : [ "entityresolution:GetSchemaMapping", "entityresolution:UpdateSchemaMapping", "entityresolution:ListTagsForResource", "entityresolution:TagResource", "entityresolution:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "entityresolution:ListSchemaMappings" ]
    }
  },
  "required" : [ "SchemaName", "MappedInputFields" ],
  "additionalProperties" : False
}