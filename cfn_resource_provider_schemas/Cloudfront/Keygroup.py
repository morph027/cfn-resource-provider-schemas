SCHEMA = {
  "additionalProperties" : False,
  "definitions" : {
    "KeyGroupConfig" : {
      "additionalProperties" : False,
      "properties" : {
        "Comment" : {
          "type" : "string",
          "description" : "A comment to describe the key group. The comment cannot be longer than 128 characters."
        },
        "Items" : {
          "items" : {
            "type" : "string"
          },
          "type" : "array",
          "uniqueItems" : False,
          "description" : "A list of the identifiers of the public keys in the key group."
        },
        "Name" : {
          "type" : "string",
          "description" : "A name to identify the key group."
        }
      },
      "required" : [ "Name", "Items" ],
      "type" : "object",
      "description" : "A key group configuration.\n A key group contains a list of public keys that you can use with [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)."
    }
  },
  "description" : "A key group.\n A key group contains a list of public keys that you can use with [CloudFront signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html).",
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudfront:CreateKeyGroup" ]
    },
    "delete" : {
      "permissions" : [ "cloudfront:DeleteKeyGroup", "cloudfront:GetKeyGroup" ]
    },
    "list" : {
      "permissions" : [ "cloudfront:ListKeyGroups" ]
    },
    "read" : {
      "permissions" : [ "cloudfront:GetKeyGroup" ]
    },
    "update" : {
      "permissions" : [ "cloudfront:UpdateKeyGroup", "cloudfront:GetKeyGroup" ]
    }
  },
  "primaryIdentifier" : [ "/properties/Id" ],
  "properties" : {
    "Id" : {
      "type" : "string",
      "description" : ""
    },
    "KeyGroupConfig" : {
      "$ref" : "#/definitions/KeyGroupConfig",
      "description" : "The key group configuration."
    },
    "LastModifiedTime" : {
      "type" : "string",
      "description" : ""
    }
  },
  "readOnlyProperties" : [ "/properties/Id", "/properties/LastModifiedTime" ],
  "required" : [ "KeyGroupConfig" ],
  "tagging" : {
    "cloudFormationSystemTags" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "taggable" : False
  },
  "typeName" : "AWS::CloudFront::KeyGroup"
}