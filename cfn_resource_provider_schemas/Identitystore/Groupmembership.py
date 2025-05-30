SCHEMA = {
  "typeName" : "AWS::IdentityStore::GroupMembership",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-identitystore",
  "description" : "Resource Type Definition for AWS:IdentityStore::GroupMembership",
  "definitions" : {
    "MemberId" : {
      "description" : "An object containing the identifier of a group member.",
      "type" : "object",
      "title" : "UserId",
      "properties" : {
        "UserId" : {
          "description" : "The identifier for a user in the identity store.",
          "type" : "string",
          "maxLength" : 47,
          "minLength" : 1,
          "pattern" : "^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$"
        }
      },
      "required" : [ "UserId" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
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
    },
    "MemberId" : {
      "description" : "An object containing the identifier of a group member.",
      "$ref" : "#/definitions/MemberId"
    },
    "MembershipId" : {
      "description" : "The identifier for a GroupMembership in the identity store.",
      "type" : "string",
      "maxLength" : 47,
      "minLength" : 1,
      "pattern" : "^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$"
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "IdentityStoreId", "GroupId", "MemberId" ],
  "readOnlyProperties" : [ "/properties/MembershipId" ],
  "createOnlyProperties" : [ "/properties/IdentityStoreId", "/properties/GroupId", "/properties/MemberId" ],
  "primaryIdentifier" : [ "/properties/MembershipId", "/properties/IdentityStoreId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "identitystore:CreateGroupMembership", "identitystore:DescribeGroupMembership" ]
    },
    "read" : {
      "permissions" : [ "identitystore:DescribeGroupMembership" ]
    },
    "delete" : {
      "permissions" : [ "identitystore:DeleteGroupMembership", "identitystore:DescribeGroupMembership" ]
    },
    "list" : {
      "permissions" : [ "identitystore:ListGroupMemberships" ],
      "handlerSchema" : {
        "properties" : {
          "IdentityStoreId" : {
            "$ref" : "resource-schema.json#/properties/IdentityStoreId"
          },
          "GroupId" : {
            "$ref" : "resource-schema.json#/properties/GroupId"
          }
        },
        "required" : [ "IdentityStoreId", "GroupId" ]
      }
    }
  },
  "additionalProperties" : False
}