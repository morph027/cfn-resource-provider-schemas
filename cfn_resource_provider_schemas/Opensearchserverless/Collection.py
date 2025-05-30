SCHEMA = {
  "typeName" : "AWS::OpenSearchServerless::Collection",
  "description" : "Amazon OpenSearchServerless collection resource",
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags"
  },
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "description" : "A key-value pair metadata associated with resource",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "The key in the key-value pair"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0,
          "description" : "The value in the key-value pair"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "CollectionType" : {
      "type" : "string",
      "description" : "The possible types for the collection",
      "enum" : [ "SEARCH", "TIMESERIES", "VECTORSEARCH" ]
    },
    "StandbyReplicas" : {
      "type" : "string",
      "description" : "The possible standby replicas for the collection",
      "enum" : [ "ENABLED", "DISABLED" ]
    }
  },
  "properties" : {
    "Description" : {
      "type" : "string",
      "maxLength" : 1000,
      "description" : "The description of the collection"
    },
    "Id" : {
      "type" : "string",
      "maxLength" : 40,
      "minLength" : 3,
      "description" : "The identifier of the collection"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 32,
      "minLength" : 3,
      "pattern" : "^[a-z][a-z0-9-]{2,31}$",
      "description" : "The name of the collection.\n\nThe name must meet the following criteria:\nUnique to your account and AWS Region\nStarts with a lowercase letter\nContains only lowercase letters a-z, the numbers 0-9 and the hyphen (-)\nContains between 3 and 32 characters\n"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 50,
      "minItems" : 0,
      "insertionOrder" : False,
      "description" : "List of tags to be added to the resource"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the collection.",
      "type" : "string"
    },
    "CollectionEndpoint" : {
      "description" : "The endpoint for the collection.",
      "type" : "string"
    },
    "DashboardEndpoint" : {
      "description" : "The OpenSearch Dashboards endpoint for the collection.",
      "type" : "string"
    },
    "Type" : {
      "$ref" : "#/definitions/CollectionType"
    },
    "StandbyReplicas" : {
      "$ref" : "#/definitions/StandbyReplicas"
    }
  },
  "required" : [ "Name" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn", "/properties/CollectionEndpoint", "/properties/DashboardEndpoint" ],
  "writeOnlyProperties" : [ "/properties/Tags" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Tags", "/properties/Type" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/Name" ], [ "/properties/Arn" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "aoss:CreateCollection", "aoss:BatchGetCollection", "iam:CreateServiceLinkedRole" ]
    },
    "delete" : {
      "permissions" : [ "aoss:DeleteCollection", "aoss:BatchGetCollection" ]
    },
    "list" : {
      "permissions" : [ "aoss:ListCollections" ]
    },
    "read" : {
      "permissions" : [ "aoss:BatchGetCollection" ]
    },
    "update" : {
      "permissions" : [ "aoss:UpdateCollection", "aoss:BatchGetCollection" ]
    }
  },
  "additionalProperties" : False
}