SCHEMA = {
  "typeName" : "AWS::Transfer::Profile",
  "description" : "Resource Type definition for AWS::Transfer::Profile",
  "definitions" : {
    "Tag" : {
      "description" : "Creates a key-value pair for a specific resource.",
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "description" : "The name assigned to the tag that you create.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "type" : "string",
          "description" : "Contains one or more values that you assigned to the key name you create.",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "CertificateId" : {
      "description" : "A unique identifier for the certificate.",
      "type" : "string",
      "pattern" : "^cert-([0-9a-f]{17})$",
      "minLength" : 22,
      "maxLength" : 22
    }
  },
  "properties" : {
    "As2Id" : {
      "description" : "AS2 identifier agreed with a trading partner.",
      "type" : "string",
      "pattern" : "^[\\u0020-\\u007E\\s]*$",
      "minLength" : 1,
      "maxLength" : 128
    },
    "ProfileType" : {
      "description" : "Enum specifying whether the profile is local or associated with a trading partner.",
      "type" : "string",
      "enum" : [ "LOCAL", "PARTNER" ]
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "maxItems" : 50,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "CertificateIds" : {
      "description" : "List of the certificate IDs associated with this profile to be used for encryption and signing of AS2 messages.",
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/CertificateId"
      }
    },
    "Arn" : {
      "description" : "Specifies the unique Amazon Resource Name (ARN) for the profile.",
      "type" : "string",
      "pattern" : "arn:.*",
      "minLength" : 20,
      "maxLength" : 1600
    },
    "ProfileId" : {
      "description" : "A unique identifier for the profile",
      "type" : "string",
      "pattern" : "^p-([0-9a-f]{17})$",
      "minLength" : 19,
      "maxLength" : 19
    }
  },
  "additionalProperties" : False,
  "required" : [ "As2Id", "ProfileType" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/ProfileId" ],
  "primaryIdentifier" : [ "/properties/ProfileId" ],
  "createOnlyProperties" : [ "/properties/ProfileType" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "transfer:ListTagsForResource", "transfer:UnTagResource", "transfer:TagResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "transfer:CreateProfile", "transfer:TagResource" ]
    },
    "read" : {
      "permissions" : [ "transfer:DescribeProfile" ]
    },
    "update" : {
      "permissions" : [ "transfer:UpdateProfile", "transfer:UnTagResource", "transfer:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "transfer:DeleteProfile" ]
    },
    "list" : {
      "permissions" : [ "transfer:ListProfiles" ]
    }
  }
}