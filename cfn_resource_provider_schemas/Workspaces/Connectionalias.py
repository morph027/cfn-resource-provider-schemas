SCHEMA = {
  "typeName" : "AWS::WorkSpaces::ConnectionAlias",
  "description" : "Resource Type definition for AWS::WorkSpaces::ConnectionAlias",
  "definitions" : {
    "ConnectionAliasAssociation" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AssociationStatus" : {
          "type" : "string",
          "enum" : [ "NOT_ASSOCIATED", "PENDING_ASSOCIATION", "ASSOCIATED_WITH_OWNER_ACCOUNT", "ASSOCIATED_WITH_SHARED_ACCOUNT", "PENDING_DISASSOCIATION" ]
        },
        "AssociatedAccountId" : {
          "type" : "string"
        },
        "ResourceId" : {
          "type" : "string",
          "pattern" : ".+",
          "minLength" : 1,
          "maxLength" : 1000
        },
        "ConnectionIdentifier" : {
          "type" : "string",
          "maxLength" : 20,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z0-9]+$"
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "Associations" : {
      "type" : "array",
      "maxLength" : 25,
      "minLength" : 1,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/ConnectionAliasAssociation"
      }
    },
    "AliasId" : {
      "type" : "string",
      "pattern" : "^wsca-[0-9a-z]{8,63}$",
      "maxLength" : 68,
      "minLength" : 13
    },
    "ConnectionString" : {
      "type" : "string",
      "pattern" : "^[.0-9a-zA-Z\\-]{1,255}$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "ConnectionAliasState" : {
      "type" : "string",
      "enum" : [ "CREATING", "CREATED", "DELETING" ]
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "ConnectionString" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "workspaces:CreateTags", "workspaces:DescribeTags" ]
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/AliasId" ],
  "createOnlyProperties" : [ "/properties/ConnectionString", "/properties/Tags" ],
  "readOnlyProperties" : [ "/properties/ConnectionAliasState", "/properties/AliasId", "/properties/Associations" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "workspaces:CreateConnectionAlias", "workspaces:CreateTags", "workspaces:DescribeConnectionAliases", "workspaces:DescribeTags" ]
    },
    "read" : {
      "permissions" : [ "workspaces:DescribeConnectionAliases", "workspaces:DescribeTags" ]
    },
    "delete" : {
      "permissions" : [ "workspaces:DeleteConnectionAlias", "workspaces:DeleteTags", "workspaces:DescribeTags", "workspaces:DescribeConnectionAliases" ]
    }
  }
}