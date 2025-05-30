SCHEMA = {
  "typeName" : "AWS::RAM::Permission",
  "description" : "Resource type definition for AWS::RAM::Permission",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-ram",
  "additionalProperties" : False,
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "Name" : {
      "description" : "The name of the permission.",
      "type" : "string"
    },
    "Version" : {
      "description" : "Version of the permission.",
      "type" : "string"
    },
    "IsResourceTypeDefault" : {
      "description" : "Set to True to use this as the default permission.",
      "type" : "boolean"
    },
    "PermissionType" : {
      "type" : "string"
    },
    "ResourceType" : {
      "description" : "The resource type this permission can be used with.",
      "type" : "string"
    },
    "PolicyTemplate" : {
      "description" : "Policy template for the permission.",
      "type" : "object"
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
  "required" : [ "Name", "ResourceType", "PolicyTemplate" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Version", "/properties/IsResourceTypeDefault", "/properties/PermissionType" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/ResourceType", "/properties/PolicyTemplate" ],
  "definitions" : {
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
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
      "required" : [ "Key", "Value" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "ram:TagResource", "ram:UntagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "ram:CreatePermission", "ram:TagResource" ]
    },
    "read" : {
      "permissions" : [ "ram:GetPermission" ]
    },
    "update" : {
      "permissions" : [ "ram:CreatePermissionVersion", "ram:DeletePermissionVersion", "ram:SetDefaultPermissionVersion", "ram:GetPermission", "ram:ReplacePermissionAssociations", "ram:ListReplacePermissionAssociationsWork", "ram:ListPermissionVersions", "ram:UntagResource", "ram:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "ram:DeletePermissionVersion", "ram:DeletePermission" ]
    },
    "list" : {
      "permissions" : [ "ram:ListPermissions", "ram:ListPermissionVersions" ]
    }
  }
}