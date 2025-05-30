SCHEMA = {
  "typeName" : "AWS::Lightsail::Bucket",
  "description" : "Resource Type definition for AWS::Lightsail::Bucket",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lightsail.git",
  "definitions" : {
    "Tag" : {
      "description" : "A key-value pair to associate with a resource.",
      "type" : "object",
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
      "required" : [ "Key" ],
      "additionalProperties" : False
    },
    "AccessRules" : {
      "description" : "An object that sets the public accessibility of objects in the specified bucket.",
      "type" : "object",
      "properties" : {
        "GetObject" : {
          "type" : "string",
          "description" : "Specifies the anonymous access to all objects in a bucket."
        },
        "AllowPublicOverrides" : {
          "type" : "boolean",
          "description" : "A Boolean value that indicates whether the access control list (ACL) permissions that are applied to individual objects override the getObject option that is currently specified."
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "BucketName" : {
      "description" : "The name for the bucket.",
      "type" : "string",
      "pattern" : "^[a-z0-9][a-z0-9-]{1,52}[a-z0-9]$",
      "minLength" : 3,
      "maxLength" : 54
    },
    "BundleId" : {
      "description" : "The ID of the bundle to use for the bucket.",
      "type" : "string"
    },
    "BucketArn" : {
      "type" : "string"
    },
    "ObjectVersioning" : {
      "description" : "Specifies whether to enable or disable versioning of objects in the bucket.",
      "type" : "boolean"
    },
    "AccessRules" : {
      "$ref" : "#/definitions/AccessRules"
    },
    "ResourcesReceivingAccess" : {
      "description" : "The names of the Lightsail resources for which to set bucket access.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "ReadOnlyAccessAccounts" : {
      "description" : "An array of strings to specify the AWS account IDs that can access the bucket.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "type" : "string"
      }
    },
    "Tags" : {
      "description" : "An array of key-value pairs to apply to this resource.",
      "type" : "array",
      "uniqueItems" : True,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Url" : {
      "description" : "The URL of the bucket.",
      "type" : "string"
    },
    "AbleToUpdateBundle" : {
      "description" : "Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.",
      "type" : "boolean"
    }
  },
  "additionalProperties" : False,
  "required" : [ "BucketName", "BundleId" ],
  "readOnlyProperties" : [ "/properties/BucketArn", "/properties/Url", "/properties/AbleToUpdateBundle" ],
  "primaryIdentifier" : [ "/properties/BucketName" ],
  "createOnlyProperties" : [ "/properties/BucketName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "lightsail:CreateBucket", "lightsail:GetBuckets", "lightsail:GetInstance", "lightsail:UpdateBucket", "lightsail:UpdateBucketBundle", "lightsail:SetResourceAccessForBucket", "lightsail:TagResource", "lightsail:UntagResource" ]
    },
    "read" : {
      "permissions" : [ "lightsail:GetBuckets" ]
    },
    "delete" : {
      "permissions" : [ "lightsail:DeleteBucket", "lightsail:GetBuckets" ]
    },
    "list" : {
      "permissions" : [ "lightsail:GetBuckets" ]
    },
    "update" : {
      "permissions" : [ "lightsail:GetBuckets", "lightsail:GetInstance", "lightsail:UpdateBucket", "lightsail:UpdateBucketBundle", "lightsail:SetResourceAccessForBucket", "lightsail:TagResource", "lightsail:UntagResource" ],
      "timeoutInMinutes" : 2160
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "lightsail:TagResource", "lightsail:UntagResource" ]
  }
}