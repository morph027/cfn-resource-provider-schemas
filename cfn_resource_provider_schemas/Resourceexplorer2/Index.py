SCHEMA = {
  "typeName" : "AWS::ResourceExplorer2::Index",
  "description" : "Definition of AWS::ResourceExplorer2::Index Resource Type",
  "definitions" : {
    "IndexType" : {
      "type" : "string",
      "enum" : [ "LOCAL", "AGGREGATOR" ]
    },
    "TagMap" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string"
        }
      },
      "additionalProperties" : False
    },
    "IndexState" : {
      "type" : "string",
      "enum" : [ "ACTIVE", "CREATING", "DELETING", "DELETED", "UPDATING" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "Tags" : {
      "$ref" : "#/definitions/TagMap"
    },
    "Type" : {
      "$ref" : "#/definitions/IndexType"
    },
    "IndexState" : {
      "$ref" : "#/definitions/IndexState"
    }
  },
  "required" : [ "Type" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/IndexState" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "resource-explorer-2:CreateIndex", "resource-explorer-2:GetIndex", "resource-explorer-2:TagResource", "resource-explorer-2:UpdateIndexType", "resource-explorer-2:DeleteIndex", "iam:CreateServiceLinkedRole" ]
    },
    "update" : {
      "permissions" : [ "resource-explorer-2:GetIndex", "resource-explorer-2:UpdateIndexType", "resource-explorer-2:TagResource", "resource-explorer-2:UntagResource", "resource-explorer-2:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "resource-explorer-2:DeleteIndex", "resource-explorer-2:GetIndex", "resource-explorer-2:UntagResource" ]
    },
    "list" : {
      "permissions" : [ "resource-explorer-2:ListIndexes" ]
    },
    "read" : {
      "permissions" : [ "resource-explorer-2:GetIndex" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "cloudFormationSystemTags" : False,
    "tagUpdatable" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "resource-explorer-2:ListTagsForResource", "resource-explorer-2:TagResource", "resource-explorer-2:UntagResource" ]
  },
  "additionalProperties" : False
}