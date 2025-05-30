SCHEMA = {
  "typeName" : "AWS::IdentityStore::Group",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-identitystore",
  "description" : "Resource Type definition for AWS::IdentityStore::Group",
  "properties" : {
    "Description" : {
      "description" : "A string containing the description of the group.",
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 1,
      "pattern" : "^[\\p{L}\\p{M}\\p{S}\\p{N}\\p{P}\\t\\n\\r  　]+$"
    },
    "DisplayName" : {
      "description" : "A string containing the name of the group. This value is commonly displayed when the group is referenced.",
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 1,
      "pattern" : "^[\\p{L}\\p{M}\\p{S}\\p{N}\\p{P}\\t\\n\\r  ]+$"
    },
    "GroupId" : {
      "description" : "The unique identifier for a group in the identity store.",
      "type" : "string",
      "maxLength" : 47,
      "minLength" : 1,
      "pattern" : "^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$"
    },
    "IdentityStoreId" : {
      "description" : "The globally unique identifier for the identity store.",
      "type" : "string",
      "maxLength" : 36,
      "minLength" : 1,
      "pattern" : "^d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "IdentityStoreId", "DisplayName" ],
  "readOnlyProperties" : [ "/properties/GroupId" ],
  "createOnlyProperties" : [ "/properties/IdentityStoreId" ],
  "primaryIdentifier" : [ "/properties/GroupId", "/properties/IdentityStoreId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "identitystore:CreateGroup", "identitystore:DescribeGroup" ]
    },
    "read" : {
      "permissions" : [ "identitystore:DescribeGroup" ]
    },
    "update" : {
      "permissions" : [ "identitystore:DescribeGroup", "identitystore:UpdateGroup" ]
    },
    "delete" : {
      "permissions" : [ "identitystore:DescribeGroup", "identitystore:DeleteGroup" ]
    },
    "list" : {
      "permissions" : [ "identitystore:ListGroups" ],
      "handlerSchema" : {
        "properties" : {
          "IdentityStoreId" : {
            "$ref" : "resource-schema.json#/properties/IdentityStoreId"
          }
        },
        "required" : [ "IdentityStoreId" ]
      }
    }
  },
  "additionalProperties" : False
}