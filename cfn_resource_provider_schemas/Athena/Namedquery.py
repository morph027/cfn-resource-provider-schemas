SCHEMA = {
  "typeName" : "AWS::Athena::NamedQuery",
  "description" : "Resource schema for AWS::Athena::NamedQuery",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-athena.git",
  "properties" : {
    "Name" : {
      "description" : "The query name.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "Database" : {
      "description" : "The database to which the query belongs.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 255
    },
    "Description" : {
      "description" : "The query description.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 1024
    },
    "QueryString" : {
      "description" : "The contents of the query with all query statements.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 262144
    },
    "WorkGroup" : {
      "description" : "The name of the workgroup that contains the named query.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "NamedQueryId" : {
      "description" : "The unique ID of the query.",
      "type" : "string"
    }
  },
  "required" : [ "Database", "QueryString" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "athena:CreateNamedQuery" ]
    },
    "read" : {
      "permissions" : [ "athena:GetNamedQuery" ]
    },
    "list" : {
      "permissions" : [ "athena:ListNamedQueries" ]
    },
    "delete" : {
      "permissions" : [ "athena:DeleteNamedQuery" ]
    }
  },
  "readOnlyProperties" : [ "/properties/NamedQueryId" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Database", "/properties/Description", "/properties/QueryString", "/properties/WorkGroup" ],
  "primaryIdentifier" : [ "/properties/NamedQueryId" ],
  "additionalProperties" : False,
  "taggable" : False
}