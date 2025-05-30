SCHEMA = {
  "typeName" : "AWS::Route53Profiles::Profile",
  "description" : "Resource Type definition for AWS::Route53Profiles::Profile",
  "additionalProperties" : False,
  "properties" : {
    "Name" : {
      "type" : "string",
      "description" : "The name of the profile.",
      "minLength" : 1,
      "maxLength" : 64
    },
    "ClientToken" : {
      "type" : "string",
      "description" : "The id of the creator request",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Tags" : {
      "type" : "array",
      "description" : "An array of key-value pairs to apply to this resource.",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Arn" : {
      "type" : "string",
      "description" : "The Amazon Resource Name (ARN) of the resolver profile."
    },
    "Id" : {
      "type" : "string",
      "description" : "The ID of the profile."
    }
  },
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
      "required" : [ "Value", "Key" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "route53profiles:TagResource", "route53profiles:UntagResource" ]
  },
  "required" : [ "Name" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Id", "/properties/ClientToken" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "route53profiles:CreateProfile", "route53profiles:GetProfile", "route53profiles:TagResource", "route53profiles:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "route53profiles:GetProfile", "route53profiles:TagResource", "route53profiles:UntagResource", "route53profiles:ListTagsForResource" ]
    },
    "read" : {
      "permissions" : [ "route53profiles:GetProfile", "route53profiles:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "route53profiles:DeleteProfile", "route53profiles:GetProfile", "route53profiles:UntagResource", "route53profiles:ListTagsForResource" ]
    },
    "list" : {
      "permissions" : [ "route53profiles:ListProfiles", "route53profiles:ListTagsForResource" ]
    }
  }
}