SCHEMA = {
  "typeName" : "AWS::IoT::RoleAlias",
  "description" : "Use the AWS::IoT::RoleAlias resource to declare an AWS IoT RoleAlias.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.",
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "RoleAlias" : {
      "type" : "string",
      "pattern" : "[\\w=,@-]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "RoleAliasArn" : {
      "type" : "string",
      "pattern" : "[\\w=,@-]+",
      "minLength" : 1,
      "maxLength" : 128
    },
    "RoleArn" : {
      "type" : "string",
      "pattern" : "arn:(aws[a-zA-Z-]*)?:iam::\\d{12}:role/?[a-zA-Z_0-9+=,.@\\-_/]+",
      "minLength" : 20,
      "maxLength" : 2048
    },
    "CredentialDurationSeconds" : {
      "type" : "integer",
      "minimum" : 900,
      "maximum" : 43200,
      "default" : 3600
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iot:ListTagsForResource", "iot:TagResource", "iot:UntagResource" ]
  },
  "additionalProperties" : False,
  "required" : [ "RoleArn" ],
  "readOnlyProperties" : [ "/properties/RoleAliasArn" ],
  "createOnlyProperties" : [ "/properties/RoleAlias" ],
  "primaryIdentifier" : [ "/properties/RoleAlias" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iam:GetRole", "iam:PassRole", "iot:CreateRoleAlias", "iot:DescribeRoleAlias", "iot:TagResource", "iot:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "iam:GetRole", "iam:PassRole", "iot:DescribeRoleAlias", "iot:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iam:GetRole", "iam:PassRole", "iot:UpdateRoleAlias", "iot:DescribeRoleAlias", "iot:TagResource", "iot:UntagResource", "iot:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "iot:DeleteRoleAlias", "iot:DescribeRoleAlias" ]
    },
    "list" : {
      "permissions" : [ "iot:ListRoleAliases" ]
    }
  }
}