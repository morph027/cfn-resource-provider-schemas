SCHEMA = {
  "typeName" : "AWS::Athena::PreparedStatement",
  "description" : "Resource schema for AWS::Athena::PreparedStatement",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-athena.git",
  "properties" : {
    "StatementName" : {
      "description" : "The name of the prepared statement.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256
    },
    "WorkGroup" : {
      "description" : "The name of the workgroup to which the prepared statement belongs.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Description" : {
      "description" : "The description of the prepared statement.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "QueryStatement" : {
      "description" : "The query string for the prepared statement.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 262144
    }
  },
  "required" : [ "StatementName", "WorkGroup", "QueryStatement" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "athena:CreatePreparedStatement", "athena:GetPreparedStatement" ]
    },
    "read" : {
      "permissions" : [ "athena:GetPreparedStatement" ]
    },
    "update" : {
      "permissions" : [ "athena:UpdatePreparedStatement" ]
    },
    "delete" : {
      "permissions" : [ "athena:DeletePreparedStatement", "athena:GetPreparedStatement" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "WorkGroup" : {
            "$ref" : "resource-schema.json#/properties/WorkGroup"
          }
        },
        "required" : [ "WorkGroup" ]
      },
      "permissions" : [ "athena:ListPreparedStatements" ]
    }
  },
  "primaryIdentifier" : [ "/properties/StatementName", "/properties/WorkGroup" ],
  "createOnlyProperties" : [ "/properties/StatementName", "/properties/WorkGroup" ],
  "additionalProperties" : False,
  "taggable" : False
}