SCHEMA = {
  "typeName" : "AWS::Deadline::Farm",
  "description" : "Definition of AWS::Deadline::Farm Resource Type",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 127
        },
        "Value" : {
          "type" : "string",
          "description" : "The value for the tag. You can specify a value that is 1 to 255 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "minLength" : 1,
          "maxLength" : 255
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Description" : {
      "type" : "string",
      "default" : "",
      "maxLength" : 100,
      "minLength" : 0
    },
    "DisplayName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1
    },
    "FarmId" : {
      "type" : "string",
      "pattern" : "^farm-[0-9a-f]{32}$"
    },
    "KmsKeyArn" : {
      "type" : "string",
      "pattern" : "^arn:aws[-a-z]*:kms:.*:key/.*"
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:(aws[a-zA-Z-]*):deadline:[a-z0-9-]+:[0-9]+:farm/farm-[0-9a-z]{32}$"
    },
    "Tags" : {
      "type" : "array",
      "maxItems" : 50,
      "description" : "An array of key-value pairs to apply to this resource.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "insertionOrder" : False,
      "uniqueItems" : True
    }
  },
  "required" : [ "DisplayName" ],
  "readOnlyProperties" : [ "/properties/FarmId", "/properties/Arn" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "deadline:TagResource", "deadline:UntagResource", "deadline:ListTagsForResource" ]
  },
  "createOnlyProperties" : [ "/properties/KmsKeyArn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:CreateFarm", "deadline:GetFarm", "deadline:TagResource", "deadline:ListTagsForResource", "identitystore:ListGroupMembershipsForMember", "kms:Encrypt", "kms:Decrypt", "kms:CreateGrant", "kms:GenerateDataKey" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetFarm", "deadline:ListTagsForResource", "identitystore:ListGroupMembershipsForMember", "kms:Encrypt", "kms:Decrypt", "kms:CreateGrant", "kms:GenerateDataKey" ]
    },
    "update" : {
      "permissions" : [ "deadline:UpdateFarm", "deadline:GetFarm", "deadline:TagResource", "deadline:UntagResource", "deadline:ListTagsForResource", "identitystore:ListGroupMembershipsForMember", "kms:Encrypt", "kms:Decrypt", "kms:CreateGrant", "kms:GenerateDataKey" ]
    },
    "delete" : {
      "permissions" : [ "deadline:DeleteFarm", "deadline:GetFarm", "identitystore:ListGroupMembershipsForMember", "kms:Encrypt", "kms:Decrypt", "kms:CreateGrant", "kms:GenerateDataKey" ]
    },
    "list" : {
      "permissions" : [ "deadline:ListFarms", "identitystore:ListGroupMembershipsForMember" ]
    }
  },
  "additionalProperties" : False
}